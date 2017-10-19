class Stack(object):  
    def __init__(self,size=10):  
        self.size=size  
        self.stack=[] 
        self.top=-1 

    def __len__(self):
        if self.isempty():  
            raise exception("stack is empty") 
        #利用len模拟len()的方法。
        return len(self.stack)

    def push(self,ele):        
        #入栈之前检查栈是否已满  
        if self.isfull():  
            raise exception("out of range");  
        else:  
            self.stack.append(ele) 
            self.top=self.top+1  

    def pop(self):             
        # 出栈之前检查栈是否为空  
        if self.isempty():  
            raise exception("stack is empty") 
        else:  
            self.top=self.top-1  
            return self.stack.pop()  
      
    def isfull(self):  
        return self.top+1==self.size 

    def isempty(self):  
        return self.top==-1

    def get_Stack(self):
        #返回栈
        if self.isempty():  
            raise exception("stack is empty") 
        return self.stack

s = Stack()
for i in range(6):
    s.push(i)
print(s.get_Stack())
print(s.pop())
print(s.get_Stack())
print(len(s))