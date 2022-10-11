class Edge:
    # Constructor, Time O(1) Space O(1)
    def __init__(self, v, w):
        self.connected_vertex = v
        self.weight = w

    # Time O(1) Space O(1)
    def __str__(self):
        return "(" + str(self.connected_vertex) + "," + str(self.weight) + ")"


class GraphWeighted:
    # Constructor, Time O(1) Space O(1)
    def __init__(self, v_number):
        self.v_number = v_number
        self.adj = {}

    # Add edges including adding nodes, Time O(1) Space O(1)
    def add_edge(self, a, b, w):
        if a not in self.adj:
            self.adj[a] = []
        if b not in self.adj:
            self.adj[b] = []
        edge1 = Edge(b, w)
        self.adj[a].append(edge1)
        edge2 = Edge(a, w)
        self.adj[b].append(edge2)

    # Find the edge between two nodes, Time O(n) Space O(1), n is number of neighbors
    def find_edge_by_vertex(self, a, b):
        ne = self.adj.get(a)
        for edge in ne:
            if edge.connected_vertex == b:
                return edge
        return None

    # Remove direct connection between a and b, Time O(1) Space O(1)
    def remove_edge(self, a, b):
        ne1 = self.adj[a]
        ne2 = self.adj[b]
        if ne1 is None or ne2 is None:
            return
        edge1 = self.find_edge_by_vertex(a, b)
        ne1.remove(edge1)
        edge2 = self.find_edge_by_vertex(b, a)
        ne2.remove(edge2)

    # Remove a node including all its edges,
    # Time O(v) Space O(1), V is number of vertices in graph
    def remove_node(self, a):
        ne1 = self.adj[a]
        for edge in ne1:
            edge1 = self.find_edge_by_vertex(edge.connected_vertex, a)
            self.adj[edge.connected_vertex].remove(edge1)

        self.adj.pop(a)

    # Check whether there is node by its key, Time O(1) Space O(1)
    def has_node(self, key):
        return key in self.adj.keys()

    # Check whether there is direct connection between two nodes, Time O(n), Space O(1)
    def has_edge(self, a, b):
        edge1 = self.find_edge_by_vertex(a, b)
        edge2 = self.find_edge_by_vertex(b, a)
        return edge1 is not None and edge2 is not None

    # Check there is path from src and dest
    # DFS, Time O(V+E), Space O(V)
    def has_path_dfs(self, src, dest):
        visited = {}
        return self.dfs_helper(src, dest, visited)

    # DFS helper, Time O(V+E), Space O(V)
    def dfs_helper(self, v, dest, visited):
        if v == dest:
            return True
        visited[v] = True
        for edge in self.adj[v]:
            u = edge.connected_vertex
            if u not in visited:
                return self.dfs_helper(u, dest, visited)
        return False

    # Check there is path from src and dest
    # BFS, Time O(V+E), Space O(V)
    def has_path_bfs(self, src, dest):
        visited = {}
        q = []
        visited[src] = True
        q.append(src)
        while q:
            v = q.pop(0)
            if v == dest:
                return True
            for edge in self.adj[v]:
                u = edge.connected_vertex
                if u not in visited:
                    q.append(u)
                    visited[u] = True
        return False

    def numbers_of_edges(self):
        count = 0
        for k, v in self.adj.items():
            count += len(v)
        return count // 2

    def get_order(self):
        return self.v_number

    def get_neighbors(self, v):
        list = []
        for edge in self.adj[v]:
            list.append(edge.connected_vertex)
        return list

    def degree_of_node(self, v):
        return len(self.adj[v])

    def degree_sequence(self):
        seq = []
        for k, v in self.adj.items():
            seq.append(len(v))
        return seq

    
        #using weighted
  
   



        #use weight to find the highest distance between nodes
    '''def get_highest_distance_between_nodes(self, v, src):
        visited = {}
        return self.highest_distance_between_nodes_helper(v, src, visited)

    def highest_distance_between_nodes_helper(self, v, src, visited):
        visited[src] = True
        highest = 0
        for edge in self.adj[src]:
            u = edge.connected_vertex
            if u not in visited:
                highest = max(highest, edge.weight + self.highest_distance_between_nodes_helper(v, u, visited))
        return highest'''






    # Print graph as hashmap, Time O(V+E), Space O(1)
    def print_graph(self):
        for k, v in self.adj.items():
            print(str(k) + "-", end="")
            for edge in v:
                print(edge, end="")
            print()

    # Traversal starting from src, DFS, Time O(V+E), Space O(V)
    def dfs_traversal(self, src):
        visited = {}
        self.helper(src, visited)
        print()

    # DFS helper, Time O(V+E), Space O(V)
    def helper(self, v, visited):
        visited[v] = True
        print(str(v) + " ", end="")
        for edge in self.adj[v]:
            u = edge.connected_vertex
            if u not in visited:
                self.helper(u, visited)

    # Traversal starting from src, BFS, Time O(V+E), Space O(V)
    def bfs_traversal(self, src):
        q = []
        visited = {}
        q.append(src)
        visited[src] = True
        while len(q) > 0:
            v = q.pop(0)
            print(str(v) + " ", end="")
            for edge in self.adj[v]:
                u = edge.connected_vertex
                if u not in visited:
                    q.append(u)
                    visited[u] = True
        print()
