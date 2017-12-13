def prim( graph, vertex_num ):  
      
    INF      = 1 << 10  
    visit    = [False] * vertex_num   #检测是否遍历过
    dist     = [INF] * vertex_num     #该集合是用于记录且判断权的最小值（需要与visit一起判断）
    #利用dist可以做到，假如到了某个点，哪个点已经没有可以遍历的点了，就可以回到之前记录的点的没记录粿点的最小权
    my_list = []

    for i in range( vertex_num ):  
          
        minDist = INF + 1  
        nextIndex = -1  
          
        for j in range( vertex_num ):  
            #查找第i个点与未遍历的点的最小权值的对应点
            if dist[j] < minDist and not visit[j]:  
                    minDist = dist[j]  
                    nextIndex = j

        for j,n in enumerate(graph[nextIndex]):
            #查找该点的前驱
            if minDist == INF:
                a = 0
            elif n == minDist:
                a = j+1

        #记录改点(poin_list的第一个为前驱，第二个为点)
        poin_list = [a,nextIndex+1]
        my_list.append(poin_list)   
        visit[nextIndex] = True  
          
        for j in range( vertex_num ):
            #为所查找的点附上与之对应点的权
            if dist[j] > graph[nextIndex][j] and not visit[j]:  
                dist[j] = graph[nextIndex][j]

    return my_list
  
_ = 1 << 10  
#<<的解释https://zhidao.baidu.com/question/583597339.html
#所以_是1024，代表无穷大

graph=[
    [0,6,1,5,_,_],
    [6,0,5,_,3,_],
    [1,5,0,5,6,4],
    [5,_,5,0,_,2],
    [_,3,6,_,0,6],
    [_,_,4,2,6,0],
]  
  
print(prim( graph, 6 ))  