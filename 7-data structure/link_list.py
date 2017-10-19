
class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            return self.getitem(key)

    def __setitem__(self, key, value):

        if self.is_empty():
            print( 'linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)

    #写入列表
    def initlist(self,data):
        #定义第一个元素的开头和指针
        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            #定义指针
            p.next = node
            #定义下一个数
            p = p.next

    #获取列表的函数，如果没输入y时，则默认读取到最后面，如果没输入x,y则输出全部数据，且x不能大于等于y
    def getlist(self,x=0,y=-1):
        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head
        length = self.getlength()
        if y == -1:
            y = length
        if y > length or x >= y:
            print('error')
            return

        while p.next!=0 and j <x:
            p = p.next
            j+=1
        p_first = str(p.data)
        while p.next!=0 and j <y:
            p = p.next
            p_first += ','+str(p.data) 
            j+=1
        return p_first


    def getlength(self):
        #循环读取数据，读取一次记录+1
        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next
        return length

    def is_empty(self):
        #判断是否有列表存在
        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):
        #清除链表
        self.head = 0


    def append(self,item):
        #在列表最后面添加一个数据
        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getitem(self,index):
        #获取指定位置的数据
        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print ('target is not exist!')

    def insert(self,index,item):
        #向指定位置插入数据
        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p


    def delete(self,index):
        #删除指定位置数据
        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return

        p = self.head
        post  = self.head

        if index ==0:
            q = p.next
            self.head = q

        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            post.next = p.next


    def index(self,value):
        #查找元素是否在里面
        if self.is_empty():
            print ('Linklist is empty.')
            return

        p = self.head
        while p.next!=0 and p.next:
            if value == p.data:
                return True
            p = p.next

        return False

l = LinkList()
l.initlist([1,2,3,4,5])
print(l.getlist())
print (l.getitem(4))
l.append(6)
print(l.getlist())

l.insert(4,40)
print(l.getlist())

l.delete(5)
print(l.getlist())
print(l.index(9))
print(l.getlist())

