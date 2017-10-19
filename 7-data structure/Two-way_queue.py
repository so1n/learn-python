class Queue():  
    def __init__(self,size): 
        #定义队列长度，还有未出队第一数据的位置，入队数据位置 
        self.size=size  
        self.front=-1  
        self.rear=-1  
        self.next = -1
        self.queue=[] 

    def __len__(self):
        if self.isempty():  
            raise BaseException("queue is empty") 
        return len(self.queue)

    def enqueue(self,ele):  #入队操作  
        if self.isfull():  
            raise BaseException("queue is full")  
        elif self.rear <= 0:  
            self.queue.append(ele)
            self.next=self.next+1  
            self.rear=0
        else:
            self.queue.append(ele)
            self.queue[self.next].rear = self.next   
            self.rear=0
        print('add',ele,'at',self.rear) 


    def dequeue(self):      
        #出队操作，切片取数据是O(1)，如果要使用remove复杂度为O(k)  
        if self.isempty():  
            raise BaseException("queue is empty")   
        else:  
            self.front=self.front+1   
            #self.queueremove(self.queue[self.front])  remove需要遍历，不符O(1)
            return self.queue[self.front]
            #del self.queue[self.front]      不知道del的实现原理。。。


    def isfull(self):  
        return self.next-self.front==self.size

    def isempty(self):  
        return self.front==self.rear==-1 

    def get_queue(self):
        #根据第一数据位置指标来返回队列list，该list为自己定义
        if self.isempty():  
            raise BaseException("queue is empty")   
        get_queue_list = []
        my_front = self.front
        i = 0
        while my_front != self.next:
            my_front += 1
            get_queue_list.append(self.queue[my_front])
        while i != self.front:
            i += 1
            get_queue_list.append(self.queue[i])
        return get_queue_list
      
q=Queue(10) 
for i in range(10):
    q.enqueue(i)
print (q.isempty()) 
print('-----')
print (q.dequeue())
print (q.get_queue())
print(len(q))
print('-----')
print (q.dequeue())
print (q.get_queue())
print(len(q))
print('-----')
print (q.dequeue())
print (q.get_queue())
print(len(q))
print('-----')
print (q.dequeue())
print (q.get_queue())
print(len(q))