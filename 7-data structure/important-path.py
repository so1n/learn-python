class Pro:  
    def __init__(self,pro_id,require_time,previous,pro_list):  
        self.pro_id = pro_id  
        self.require_time = require_time  
        self.previous = previous  
        #self.status = False  
        pro_list.append(self)  
  
    # def Test(self):  
    #   for item in self.previous:  
    #       if pro_list[item].status == False:  
    #           return False  
    #   return True  
    def ShowSelf(self):  
        print (self.id,self.require_time,self.previous)#self.status,  
    # def Pro_Finish(self):  
    #   self.status = True  
    def run(self):  
        total = 0  
        tmp = []  
        if self.pro_id == 0:  
            return 0  
        a = len(self.previous)  
        for x in range(a):  
            tmp.append(pro_list[self.previous[x]].run() + self.require_time)  
        print (tmp) 
        total = max(tmp)  
        print (total)  
        return total  
  
  
  
  
pro_list = []  
pro_0 = Pro(0, 0, [0], pro_list)  
# pro_0.status = True  
  
#init the pro_list  
pro_1 = Pro(1, 4, [0], pro_list)  
pro_2 = Pro(2, 3, [1], pro_list)  
pro_3 = Pro(3, 2, [1], pro_list)  
pro_4 = Pro(4, 5, [2], pro_list)  
pro_5 = Pro(5, 3, [3,4,8], pro_list)  
pro_6 = Pro(6, 1, [4], pro_list)  
pro_7 = Pro(7, 3, [5,6], pro_list)  
pro_8 = Pro(8, 5, [1], pro_list)  
pro_9 = Pro(9, 4, [7], pro_list)  
  
  
  
total_time = pro_9.run()    #此处为总项目，也可以是单个项目  
print ("Total_time:",total_time ) 
  