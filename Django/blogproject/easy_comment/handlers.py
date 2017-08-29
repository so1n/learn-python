from django.db.models.signals import post_save
from .models import Comment, Like
from notifications.signals import notify
from django.conf import settings
from django.apps import apps
from django.template.loader import render_to_string
from django.core.mail import send_mail

def get_recipient():
    admins = [i[0] for i in settings.ADMINS]
    app_model = settings.AUTH_USER_MODEL.split('.')
    User_model = apps.get_model(*app_model)
    recipient = User_model.objects.filter(username__in=admins)
    return recipient

ADMINS = get_recipient()
SEND_NOTIFICATION_EMAIL = getattr(settings, 'SEND_NOTIFICATION_EMAIL', False)

def email_handler(*args):
    for user in args:
        try:
            if not (hasattr(user, 'onlinestatus') and user.onlinestatus.is_online()):
                context = {'receiver':user.username,
                           'unsend_count':user.notifications.filter(unread=True, emailed=False).count(),
                           'notice_list':user.notifications.filter(unread=True, emailed=False),
                           'unread_link':'http://www.aaron-zhao.com/notifications/unread/'}
                msg_plain = render_to_string("notifications/email/email.txt", context=context)
                send_mail("来自[AA的博客] 您有未读的评论通知",
                          msg_plain,
                          'support@aaron-zhao.com',
                          recipient_list=[user.email])
                user.notifications.unsent().update(emailed=True)
        except Exception as e:
            print("Error in easy_comment.handlers.py.email_handler: %s" % e)

def comment_handler(sender, instance, created, **kwargs):
    if created:
        recipient = ADMINS.exclude(id=instance.user.id)
        if not instance.parent is None:
            recipient = recipient.exclude(id=instance.parent.user.id)
            if recipient.count() > 0:
                notify.send(instance.user, recipient=recipient,
                            verb='回复了 %s' % instance.parent.user_name,
                            action_object=instance,
                            target=instance.post,
                            description=instance.content)
                if SEND_NOTIFICATION_EMAIL:
                    email_handler(*recipient)
            if not instance.user_name == instance.parent.user_name:
                notify.send(instance.user, recipient=instance.parent.user, verb='@了你',
                            action_object=instance,
                            target=instance.post,
                            description=instance.content)
                if SEND_NOTIFICATION_EMAIL:
                    email_handler(instance.parent.user)
        else:
            if recipient.count() > 0:
                notify.send(instance.user, recipient=recipient, verb='发表了评论',
                            action_object=instance,
                            target=instance.post,
                            description=instance.content)
                if SEND_NOTIFICATION_EMAIL:
                    email_handler(*recipient)

post_save.connect(comment_handler, sender=Comment)

def like_handler(sender, instance, created, **kwargs):
    if created:
        recipient = ADMINS.exclude(id=instance.user.id).exclude(id=instance.comment.user.id)
        verb = '的评论' if instance.comment.parent is None else '的回复'
        action = '赞了' if instance.status else '踩了'
        if recipient.count() > 0:
            notify.send(instance.user, recipient=recipient,
                        verb=action+instance.comment.user_name+verb,
                        action_object=instance.comment,
                        target=instance.comment.post,
                        description=instance.comment.content)
        if (not instance.user.username == instance.comment.user_name) and instance.status:
            notify.send(instance.user, recipient=instance.comment.user,
                        verb='赞了你'+verb,
                        action_object=instance.comment,
                        target=instance.comment.post,
                        description=instance.comment.content)

post_save.connect(like_handler, sender=Like)