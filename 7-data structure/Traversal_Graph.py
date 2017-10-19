class Graph(object):

    def __init__(self,*args,**kwargs):
        self.node_neighbors = {}

    def add_nodes(self,nodelist):
        #批量添加节点
        for node in nodelist:
            self.add_node(node)

    def add_node(self,node):
        #添加节点
        if not node in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self,edge):
        #定义节点的邻接点(双向的)
        u,v = edge
        if(v not in self.node_neighbors[u]) and ( u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)

            if(u!=v):
                self.node_neighbors[v].append(u)

    def nodes(self):
        #返回节点
        return self.node_neighbors.keys()

    def depth_first_search(self,root=None):
        #深度遍历
        visited = {}
        order = [] #记录遍历好的节点
        def dfs(node):
            visited[node] = True #代表该节点标记为读取过了
            order.append(node) #记录
            for n in self.node_neighbors[node]:
                if not n in visited:
                    dfs(n) #取出第一个节点，利用回调，遍历该节点的第一个邻节点


        if root:
            dfs(root)

        #如果定义了开始节点，此步骤就是最后循环一遍，把未遍历的点再遍历一次
        #如果没定义节点，此步骤就是记录要遍历的点
        for node in self.nodes():
            if not node in visited:
                dfs(node)

        print (order)

        return order

    def breadth_first_search(self,root=None):
        #广度遍历
        visited = {}
        queue = [] #记录要遍历的节点
        order = [] #记录遍历好的节点
        def bfs():
            while len(queue)> 0:
                node  = queue.pop(0) #取出顶点
                visited[node] = True #代表该节点标记为读取过了
                for n in self.node_neighbors[node]: #self.node_neighbors[node]为读取对应key的value也就是读取节点对应的邻节点
                    if (not n in visited) and (not n in queue):
                        #not n in self.visited判断这个节点是否读取过，not n in queue用来对节点对应的邻节点去重
                        queue.append(n) #添加要遍历的节点
                        order.append(n) #记录遍历好的节点

        if root:
            queue.append(root)
            order.append(root)
            bfs()

        #如果定义了开始节点，此步骤就是最后循环一遍，把未遍历的点再遍历一次
        #如果没定义节点，此步骤就是记录要遍历的点
        for node in self.nodes():
            if not node in visited:
                queue.append(node)
                order.append(node)
                bfs()
        print (order)

        return order


if __name__ == '__main__':
    g = Graph()
g.add_nodes([i+1 for i in range(8)])
g.add_edge((1, 2))
g.add_edge((1, 3))
g.add_edge((2, 4))
g.add_edge((2, 5))
g.add_edge((4, 8))
g.add_edge((5, 8))
g.add_edge((3, 6))
g.add_edge((3, 7))
g.add_edge((6, 7))
print ("nodes:", g.nodes())

order = g.breadth_first_search(1)
order = g.depth_first_search(1)