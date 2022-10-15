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

    # Eccentricity of a vertex of a weighted undirected graph using bellman ford algorithm
    # Time O(V*E), Space O(V)
    def eccentricity(self, v):
        dist = self.bellman_ford(v)
        max = 0
        for k, v in dist.items():
            if v > max:
                max = v
        return max

    # Bellman ford algorithm of a weighted undirected graph that detects negative cycles
    # Time O(V*E), Space O(V)
    def bellman_ford(self, vertex):
        dist = {}
        for k, v in self.adj.items():
            dist[k] = self.v_number
        dist[vertex] = 0
        for i in range(self.v_number - 1):
            for k, v in self.adj.items():
                for edge in v:
                    if dist[k] + edge.weight < dist[edge.connected_vertex]:
                        dist[edge.connected_vertex] = dist[k] + edge.weight
        for k, v in self.adj.items():
            for edge in v:
                if dist[k] + edge.weight < dist[edge.connected_vertex]:
                    return dict()
        return dist

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

    # Closeness centrality of a weighted undirected graph
    # Time O(V*V*E), Space O(V)
    def closeness_centrality(self, v):
        dist = self.bellman_ford(v)
        sum = 0
        for k, v in dist.items():
            sum += v
        if sum == 0:
            return 0
        return (self.v_number - 1) / sum

    # Get weighted non-directional graph
    # Time O(1), Space O(1)
    def get_graph(self):
        return self.adj


# Read a json and generate a text file where the first line is the number of vertex and the following lines are the two vertex and the weight without using json library
# Time O(V+E), Space O(V)
def generate_text_file_from_json_file(json_file, text_file):
    with open(json_file, 'r') as f:
        data = f.read()
    with open(text_file, 'w') as f:
        f.write(str(data.count("weight")) + "\n")
        for i in range(len(data)):
            if data[i] == "w":
                f.write(data[i - 1] + " " + data[i + 2] + " " + data[i + 8] + "\n")


# Generate json file following the JSON format file
# Time O(V+E), Space O(V)
def generate_json_file_from_text_file(text_file, json_file):
    with open(text_file, 'r') as f:
        data = f.read()
    with open(json_file, 'w') as f:
        f.write("{\n")
        f.write("  \"graph\": {\n")
        f.write("    \"nodes\": [\n")
        for i in range(int(data[0])):
            f.write("      {\n")
            f.write("        \"id\": \"" + str(i) + "\",\n")
            f.write("        \"label\": \"" + str(i) + "\"\n")
            if i == int(data[0]) - 1:
                f.write("      }\n")
            else:
                f.write("      },\n")
        f.write("    ],\n")
        f.write("    \"edges\": [\n")
        for i in range(int(data[0])):
            f.write("      {\n")
            f.write("        \"source\": \"" + str(i) + "\",\n")
            f.write("        \"target\": \"" + str(i) + "\",\n")
            f.write("        \"label\": \"" + str(i) + "\"\n")
            if i == int(data[0]) - 1:
                f.write("      }\n")
            else:
                f.write("      },\n")
        f.write("    ]\n")
        f.write("  }\n")
        f.write("}\n")
