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

    # # Find the edge between two nodes, Time O(n) Space O(1), n is number of neighbors
    # def find_edge_by_vertex(self, a, b):
    #     ne = self.adj.get(a)
    #     for edge in ne:
    #         if edge.connected_vertex == b:
    #             return edge
    #     return None
    #
    # # Remove direct connection between a and b, Time O(1) Space O(1)
    # def remove_edge(self, a, b):
    #     ne1 = self.adj[a]
    #     ne2 = self.adj[b]
    #     if ne1 is None or ne2 is None:
    #         return
    #     edge1 = self.find_edge_by_vertex(a, b)
    #     ne1.remove(edge1)
    #     edge2 = self.find_edge_by_vertex(b, a)
    #     ne2.remove(edge2)
    #
    # # Remove a node including all its edges,
    # # Time O(v) Space O(1), V is number of vertices in graph
    # def remove_node(self, a):
    #     ne1 = self.adj[a]
    #     for edge in ne1:
    #         edge1 = self.find_edge_by_vertex(edge.connected_vertex, a)
    #         self.adj[edge.connected_vertex].remove(edge1)
    #
    #     self.adj.pop(a)

    # Get order of a weighted non-directional graph
    # Time O(1), Space O(1)
    def get_order(self):
        return self.v_number

    # Size of a weighted non-directional graph
    # Time O(V+E), Space O(V)
    def size(self):
        return len(self.adj)

    # Neighbours of a weighted non-directional graph
    # Time O(1), Space O(1)
    def get_neighbours(self, v):
        edges = []
        for edge in self.adj[v]:
            edges.append(edge.connected_vertex)
        return edges

    # Degree of a vertex of a weighted non-directional graph
    # Time O(1), Space O(1)
    def degree_of_vertex(self, v):
        return len(self.adj[v])

    # Degree sequence of a weighted non-directional graph
    # Time O(V+E), Space O(V)
    def degree_sequence(self):
        degree = []
        for k, v in self.adj.items():
            degree.append(len(v))
        return degree

    # Get eccentricity of a vertex of a weighted non-directional graph using dijkstra algorithm
    # Time O(V*V*E), Space O(V)
    def eccentricity(self, src):
        max = 0
        for k, v in self.adj.items():
            d = self.dijkstra(src, k)
            if d > max:
                max = d
        return max

    # Dijkstra algorithm to find shortest path from src to dest
    # Time O(V*V*E), Space O(V)
    def dijkstra(self, src, dest):
        visited = {}
        distance = {}
        for k, v in self.adj.items():
            distance[k] = float("inf")
        distance[src] = 0
        for k, v in self.adj.items():
            u = self.min_distance(distance, visited)
            visited[u] = True
            for edge in self.adj[u]:
                if edge.connected_vertex not in visited:
                    d = distance[u] + edge.weight
                    if d < distance[edge.connected_vertex]:
                        distance[edge.connected_vertex] = d
        return distance[dest]

    # Find the vertex with minimum distance
    # Time O(V), Space O(1)
    def min_distance(self, distance, visited):
        min = float("inf")
        min_index = None
        for k, v in distance.items():
            if k not in visited and v < min:
                min = v
                min_index = k
        return min_index

    # Radius of a weighted non-directional graph
    # Time O(V*V*E), Space O(V)
    def radius(self):
        min = self.v_number
        for k, v in self.adj.items():
            e = self.eccentricity(k)
            if e < min:
                min = e
        return min

    # Diameter of a weighted non-directional graph
    # Time O(V*V*E), Space O(V)
    def diameter(self):
        max = 0
        for k, v in self.adj.items():
            e = self.eccentricity(k)
            if e > max:
                max = e
        return max

    # Center of a weighted non-directional graph
    # Time O(V*V*E), Space O(V)
    def center(self):
        ecc = {}
        for k, v in self.adj.items():
            ecc[k] = self.eccentricity(k)
        min = self.v_number
        for k, v in ecc.items():
            if v < min:
                min = v
                min_index = k
        return min_index

    # Get sequence of vertex of dfs traversal
    # Time O(V+E), Space O(V)
    def dfs(self, v):
        visited = {}
        sequence = []
        self.dfs_util(v, visited, sequence)
        return sequence

    # Util function for dfs
    # Time O(V+E), Space O(V)
    def dfs_util(self, v, visited, sequence):
        visited[v] = True
        sequence.append(v)
        for edge in self.adj[v]:
            if edge.connected_vertex not in visited:
                self.dfs_util(edge.connected_vertex, visited, sequence)

    # Get sequence of vertex not visited by dfs traversal
    # Time O(V+E), Space O(V)
    def dfs_not_visited(self):
        visited = {}
        sequence = []
        for k, v in self.adj.items():
            if k in visited:
                self.dfs_util(k, visited, sequence)
        return sequence

    # Closeness centrality of a weighted non-directional graph using dijkstra algorithm
    # Time O(V*V*E), Space O(V)
    def closeness_centrality(self, vertex):
        sum = 0
        for k, v in self.adj.items():
            d = self.dijkstra(vertex, k)
            sum += d
        return sum / (self.v_number - 1)

    # Get weighted non-directional graph
    # Time O(1), Space O(1)
    def get_graph(self):
        return self.adj

    # Generate JSON file based on the weighted non-directional graph
    # Time O(V+E), Space O(V)
    def generate_json(self):
        json = {}
        for k, v in self.adj.items():
            json[k] = []
            for edge in v:
                json[k].append(edge.connected_vertex)
        return json
