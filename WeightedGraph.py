
class Edge : 
	#Constructor, Time O(1) Space O(1)
	def __init__(self, v, w) :
		self.connectedVetex = v 
		self.weight = w

    #Time O(1) Space O(1)
	def __str__(self):
		return "(" + str(self.connectedVetex) + "," + str(self.weight) + ")"
	
class GraphWeighted :
    #Constructor, Time O(1) Space O(1)
    def __init__(self, directed) :
        self.adj = {}
        self.directed = directed #true or false 
	
	#Add edges including adding nodes, Time O(1) Space O(1)
    def addEdge(self, a, b, w) :    
        if a not in self.adj:
            self.adj[a] = []
        if b not in self.adj:
            self.adj[b] = []   	
        edge1 = Edge(b, w)	
        self.adj[a].append(edge1)
        if (self.directed == False) :
            edge2 = Edge(a, w)
            self.adj[b].append(edge2)	

	#Find the edge between two nodes, Time O(n) Space O(1), n is number of neighbors 
    def findEdgeByVetex(self, a,  b) :
        ne = self.adj.get(a)
        for edge in ne:
            if edge.connectedVetex == b :
                return edge
        return None
    
    #Remove direct connection between a and b, Time O(1) Space O(1)
    def removeEdge(self, a, b) :
        ne1 = self.adj[a]
        ne2 = self.adj[b] 
        if ne1 == None or ne2 == None :
            return
        edge1 = self.findEdgeByVetex(a, b)
        ne1.remove(edge1)
        if (self.directed == False) :
            edge2 = self.findEdgeByVetex(b, a)
            ne2.remove(edge2)
        
    #Remove a node including all its edges, 
	#Time O(v) Space O(1), V is number of vertics in graph
    def removeNode(self, a) :       
        if self.directed == False:  #undirected
            ne1 = self.adj[a]
            for edge in ne1 :
                edge1 = self.findEdgeByVetex(edge.connectedVetex, a) 
                self.adj[edge.connectedVetex].remove(edge1)
        else : #directed
            for k, v in self.adj.items(): 
                edge2 = self.findEdgeByVetex(k, a)
                if edge2 is not None:
                    self.adj[k].remove(edge2);	
        self.adj.pop(a)
			
	#Check whether there is node by its key, Time O(1) Space O(1)
    def hasNode(self, key) :
        return key in self.adj.keys()
	
	#Check whether there is direct connection between two nodes, Time O(n), Space O(1)
    def hasEdge(self, a, b):
        edge1 = self.findEdgeByVetex(a, b)
        if self.directed : #directed
            return edge1 is not None
        else : #undirected or bi-directed
            edge2 = self.findEdgeByVetex(b, a)
            return edge1 is not None and edge2 is not None
		
    # Check there is path from src and dest
	# DFS, Time O(V+E), Space O(V)
    def hasPathDfs(self, src, dest) : 
        visited = {}
        return self.dfsHelper(src, dest, visited)
	
	#DFS helper, Time O(V+E), Space O(V) 
    def dfsHelper(self, v, dest, visited) :
        if v == dest:
            return True
        visited[v] = True
        for edge in self.adj[v] :
            u = edge.connectedVetex
            if u not in visited:
                return self.dfsHelper(u, dest, visited)
        return False

	#Check there is path from src and dest
	#BFS, Time O(V+E), Space O(V)
    def hasPathBfs(self, src, dest) : 
        visited = {} 
        q = [] 
        visited[src] = True
        q.append(src) 
        while q : 
            v = q.pop(0); 
            if v == dest: 
                return True 
            for edge in self.adj[v] :  
                u = edge.connectedVetex              
                if u not in visited:  
                    q.append(u)
                    visited[u] = True	    	        
        return False 

	# Print graph as hashmap, Time O(V+E), Space O(1)
    def printGraph(self) :
        for k, v in self.adj.items():
            print(str(k) + "-", end ="")
            for edge in v:
                print(edge, end="")
            print()
		
	#Traversal starting from src, DFS, Time O(V+E), Space O(V)
    def dfsTraversal(self, src) : 
        visited = {}
        self.helper(src, visited)
        print()
	
	#DFS helper, Time O(V+E), Space O(V) 
    def helper(self, v, visited) :
        visited[v] = True
        print(str(v) +" ",end="")
        for edge in self.adj[v] :
            u = edge.connectedVetex
            if u not in visited:               
                self.helper(u, visited)
    
    # Traversal starting from src, BFS, Time O(V+E), Space O(V)
    def bfsTraversal(self, src) : 
        q = [] 
        visited = {} 
        q.append(src) 
        visited[src] = True 
        while (len(q) > 0) : 
            v = q.pop(0) 
            print(str(v) + " ",end="");        
            for edge in self.adj[v] :   
                u = edge.connectedVetex
                if u not in visited:
                    q.append(u); 
                    visited[u] = True
        print()

#
#    Test case 1, Undirected graph
#    1-- 3
#    | \ |
#    2   4 
#
g = GraphWeighted(False)
g.addEdge(1, 2, 26)
g.addEdge(1, 3, 13)  
g.addEdge(1, 4, 28)   
g.addEdge(3, 4, 19)
print("undirected graph:")
g.printGraph()
print("dfs:")
g.dfsTraversal(1)
print("bfs:")
g.bfsTraversal(1)

print("has node 3:" + str(g.hasNode(3)))
print("has node 5:" + str(g.hasNode(5)))
print("has edge 3,2: " + str(g.hasEdge(3,2)))
print("has edge 3,1: " + str(g.hasEdge(3,1)))		
print("has path 2,3 (DFS): " + str(g.hasPathDfs(2, 3)))
print("has path 2,5 (DFS): " + str(g.hasPathDfs(2, 5)))
print("has path 2,3 (BFS): " + str(g.hasPathBfs(2, 3)))
print("has path 2,5 (BFS): " + str(g.hasPathBfs(2, 5)))

g.removeEdge(3, 4)
print("after remove edge:")
g.printGraph()
g.addEdge(3, 4, 20); #add back
print("after add back edge:")
g.printGraph()

g.removeNode(1)
print("after remove node:")
g.printGraph()
print()
        

#     directed graph
#     2\     /  5 <
#       >  <    ^  \
#        1      |   6
#       >  <    |  /
#     4 / <-- \ 3<
   
g1 = GraphWeighted(True) 
g1.addEdge(6, 5, 26)
g1.addEdge(6, 3, 13)  
g1.addEdge(3, 5, 28)   
g1.addEdge(5, 1, 19)
g1.addEdge(3, 1, 35)  
g1.addEdge(3, 4, 27)  
g1.addEdge(4, 1, 11)  
g1.addEdge(2, 1, 38)  
print("directed graph:")
g1.printGraph()
print("dfs:")
g1.dfsTraversal(3)
print("bfs:")
g1.bfsTraversal(3)

print("has node 3:" + str(g1.hasNode(3)))
print("has node 5:" + str(g1.hasNode(5)))
print("has edge 6,5: "+ str(g1.hasEdge(6,5)))
print("has edge 4,2: "+ str(g1.hasEdge(4,2)))
print("has path 6,1 (DFS): " + str(g1.hasPathDfs(6, 1)))
print("has path 2,3 (DFS): " + str(g1.hasPathDfs(2, 3)))
print("has path 6,1 (BFS): " + str(g1.hasPathBfs(6, 1)))
print("has path 2,3 (BFS): " + str(g1.hasPathBfs(2, 3)))

g1.removeEdge(6, 5)
print("after remove edge:")
g1.printGraph()
g.addEdge(6, 5, 3); #add back

g1.removeNode(5)
print("after remove node:")
g1.printGraph()