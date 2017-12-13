#Kruskal’s Algorithm
def find(C, u):
    #输出该节点的根
    #案例中，到了边14时，查找1获得3，再查找3获得6，最后才知道1的跟是6,4一步得出4的跟是6。在这个期间，就把1的跟转换为6
    #案例中，到了边32时(25和13通过23连接了，但2指向5,1指向3指向6，并没有1指向3指向2，这个路径)
    #       由于32边才通过逐级查找，判断出2跟5的跟是6
    if C[u] != u:      #判断这个点是不是根，如果不是向顶点查找(由于做了路径压缩处理，查找很快)
        C[u] = find(C, C[u])                    
    return C[u]
 
def union(C, R, u, v):
    #将其视为平衡树，等级小的指向等级大的，如果两者等级一样，则前者指像后者。最后后者等级加1
    u, v = find(C, u), find(C, v)
    #这句if,else是由等级来判断是否需要转换跟
    if R[u] > R[v]:                             
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:                            #等级加1
        R[v] += 1
 
def kruskal(G):
    E = [(G[u][v],u,v) for u in G for v in G[u]] #生成的E是(边的权，边的起点，边的终点)的列表
    T = set()
    C, R = {u:u for u in G}, {u:0 for u in G}   
    # 定义的c是通过路径压缩后，点的对应的最终顶节点，也就是树的根，
    #R定义的是点的等级
    for _, u, v in sorted(E): #由于使用sorted所以排序先按权排序再按起点排序，所以这样生成的树中都是数字小的充当子节点，大的充当节点（但是在整颗树中并不是这样的）
        print("(",u,v,")")
        print("C", C)
        print("R", R)
        print("u,v", u, v)
        print("C[u],u",C[u],u)
        print("C[v],v",C[v],v)
        if find(C, u) != find(C, v):
            #如果两个段点的根不同，就代表没有构成回路
            print("录入u,v",u,v)
            T.add((u, v))
            union(C, R, u, v)
        print("------")
    return T



G = {
    1: {2:6, 3:1, 4:5},
    2: {1:6, 3:5, 5:3},
    3: {1:1, 2:5, 4:5, 5:6, 6:4},
    4: {1:5, 3:5, 6:2},
    5: {2:3, 3:6, 6:6},
    6: {3:4, 4:2, 5:6},
    }


print (list(kruskal(G))) 