"""
project: Graph Theory 
Operation: BFS, DFS Algorithm
Language: Python 
Author: Moinul Islam
""" 
from queue import Queue 
class Graph:
    def __init__(self,num_node,directed= False) -> None:
        self.num_node = num_node
        self.directed = directed
        self.adj_matrix = [[0 for col in range(num_node)]for row in range(num_node)]
        self.adj_list = {node:set() for node in range(num_node)}
    def add_node_to_matrix(self,node1,node2):
        self.adj_matrix[node1][node2] = 1 
        if not self.directed:
            self.adj_matrix[node2][node1] = 1
    def add_node_to_list(self,node1,node2):
        self.adj_list[node1].add(node2)
        if not self.directed:
            self.adj_list[node2].add(node1)
    def bfs_traversal(self,startNode):
        queue = Queue()
        visited = set()
        queue.put(startNode)
        visited.add(startNode)
        while not queue.empty():
            curr_node = queue.get()
            print(curr_node,end=" ")
            for child in self.adj_list[curr_node]:
                if child not in visited:
                    queue.put(child)
                    visited.add(child)
                    
    visited = set()
    def dfs_traversal(self,startNode):
        if startNode not  in self.visited:
            print(startNode,end=" ")
            self.visited.add(startNode)
        for child in self.adj_list[startNode]:
            self.dfs_traversal(child)
    
g= Graph(5,True)
g.add_node_to_list(0,1)
g.add_node_to_list(0,2)
g.add_node_to_list(1,2)
g.add_node_to_list(1,4)
g.add_node_to_list(2,3)
g.add_node_to_list(2,4)
g.add_node_to_matrix(0,1)
g.add_node_to_matrix(0,2)
g.add_node_to_matrix(1,2)
g.add_node_to_matrix(1,4)
g.add_node_to_matrix(2,3)
g.add_node_to_matrix(3,4)
while True:
    print("="*10+"GRAPH THEORY"+"="*10)
    print("1.Show Adjacency Matrix\n2.Show Adjacency List\n3.RUN BFS\n4.RUN DFS")
    choose = int(input("Enter your choice: "))
    if choose == 1:
        print(f"Adjacency Matrix: {g.adj_matrix}")
    elif choose == 2:
        print(f"Adjacency List: {g.adj_list}")
    elif choose == 3:
        print(f"BFS TRAVERSAL: {g.bfs_traversal(0)}")
    elif choose == 4:
        print(f"DFS TRAVERSAL: {g.dfs_traversal(0)}")
    else:
        break
    
                    
                    