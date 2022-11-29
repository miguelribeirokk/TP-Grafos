class Edge:
    """
    A class used to represent an edge.

    ...

    Attributes
    ----------
    connected_vertex : int
        an integer that represents a vertex.
    weight : float
        the weight of the edge.

    Methods
    -------
     __str__(self)
        Returns a string representation of the edge.
    """

    def __init__(self, v, w):
        """
        Parameters
        ----------
        v : int
            an integer that represents a vertex.
        w : float
            the weight of the edge.
        """

        self.connected_vertex = v
        self.weight = w

    def __str__(self):
        """
        Returns a string representation of the edge.
        """

        return "(" + str(self.connected_vertex) + "," + str(self.weight) + ")"


class GraphWeighted:
    """
    A class used to represent an undirected graph backed by an adjacency list.

    ...

    Attributes
    ----------
    v_number : int
        an integer that represents the number of vertices.
    adj : 
        a dictionary that represents the adjacency list of the graph.

    Methods
    -------
    get_vertex_sequence(self)
        Returns a sequence of vertex.

    get_first_vertex(self)
        Returns the first vertex of the graph.

    add_edge(self, a, b, w)
        Adds a new edge to the graph.

    get_order(self)
        Returns the order of the graph.

    size(self)
        Returns the size of the graph.

    get_neighbours(self, v)
        Returns the neighbours of a vertex.

    degree_of_vertex(self, v)
        Returns the degree of a vertex.

    degree_sequence(self)
        Returns the degree sequence of the graph.

    eccentricity(self, v)
        Returns the eccentricity of a vertex.

    bellman_ford(self, vertex)
        Returns the distances of all vertices from a vertex using bellman ford algorithm.

    radius(self)
        Returns the radius of the graph.

    diameter(self)
        Returns the diameter of the graph.

    center(self)
        Returns the center of the graph.

    dfs(self, v)
        Returns the dfs of the graph.

    dfs_util(self, v, visited)
        Helper function for dfs.

    dfs_not_visited(self)
        Returns vertices that were not visited by the dfs.

    closeness_centrality(self, v)
        Returns the closeness centrality of a vertex.

    minimum_path(self, v, w)
        Returns the minimum path between two vertices.
    """

    def __init__(self, v_number):
        """
        Parameters
        ----------
        v_number : int
            an integer that represents the number of vertices.
        """

        self.v_number = v_number
        self.adj = {}

    def get_vertex_sequence(self):
        """
        Returns a sequence of vertex.

        Returns
        -------
        a sequence of vertex.
        """

        return self.adj.keys()

    def get_first_vertex(self):
        """
        Returns the first vertex of the graph.

        Returns
        -------
        first vertex of the graph.
        """

        for k, v in self.adj.items():
            return k

    def add_edge(self, a, b, w):
        """
        Adds a new edge to the graph.

        Parameters
        ----------
        a : int
            first vertex.
        b : int
            second vertex.
        w : float
            weight of the edge.
        """

        if a not in self.adj:
            self.adj[a] = []
        if b not in self.adj:
            self.adj[b] = []
        edge1 = Edge(b, w)
        self.adj[a].append(edge1)
        edge2 = Edge(a, w)
        self.adj[b].append(edge2)

    def get_order(self):
        """
        Returns the order of the graph.

        Returns
        -------
        order of the graph.
        """

        return self.v_number

    def size(self):
        """
        Returns the size of the graph.

        Returns
        -------
        size of the graph.
        """

        size = 0
        for k, v in self.adj.items():
            size += len(v)
        return size // 2

    def get_neighbours(self, v):
        """
        Returns the neighbours of a vertex.

        Parameters
        ----------
        v : int
            a vertex.

        Returns
        -------
        list of neighbours.
        """

        edges = []
        for edge in self.adj[v]:
            edges.append(edge.connected_vertex)
        return edges

    def degree_of_vertex(self, v):
        """
        Returns the degree of a vertex.

        Parameters
        ----------
        v : int
            a vertex.

        Returns
        -------
        degree of the vertex.
        """

        return len(self.adj[v])

    def degree_sequence(self):
        """
        Returns the degree sequence of the graph.

        Returns
        -------
        list of degrees.
        """

        degree = []
        for k, v in self.adj.items():
            degree.append(len(v))

        degree.sort(reverse=True)
        return degree

    def eccentricity(self, v):
        """
        Returns the eccentricity of a vertex using bellman ford algorithm.

        Parameters
        ----------
        v : int
            a vertex.

        Returns
        -------
        eccentricity of the vertex.
        """

        distances = self.bellman_ford(v)

        max_distance = 0
        for k, v in distances.items():
            if v > max_distance:
                max_distance = v
        return max_distance

    def bellman_ford(self, vertex):
        """
        Returns the distances of all vertices from a vertex using bellman ford algorithm.

        Parameters
        ----------
        vertex : int
            a vertex.

        Returns
        -------
        dictionary of distances.
        """

        distances = {}
        for k, v in self.adj.items():
            distances[k] = float("inf")
        distances[vertex] = 0
        for i in range(self.v_number - 1):
            for k, v in self.adj.items():
                for edge in v:
                    if distances[k] + edge.weight < distances[edge.connected_vertex]:
                        distances[edge.connected_vertex] = distances[k] + edge.weight
        for k, v in self.adj.items():
            for edge in v:
                if distances[k] + edge.weight < distances[edge.connected_vertex]:
                    return 0
        return distances

    def radius(self):
        """
        Returns the radius of the graph.

        Returns
        -------
        radius of the graph.
        """

        radius = float("inf")
        for k, v in self.adj.items():
            eccentricity = self.eccentricity(k)
            if eccentricity < radius:
                radius = eccentricity
        return radius

    def diameter(self):
        """
        Returns the diameter of the graph.

        Returns
        -------
        diameter of the graph.
        """

        maximum = 0
        for k, v in self.adj.items():
            e = self.eccentricity(k)
            if e > maximum:
                maximum = e
        return maximum

    def center(self):
        """
        Returns the center of the graph.

        Returns
        -------
        center of the graph.
        """

        center = []
        r = self.radius()
        for k, v in self.adj.items():
            if self.eccentricity(k) == r:
                center.append(k)
        return center

    def dfs(self, v):
        """
        Returns the dfs of the graph.

        Parameters
        ----------
        v : int
            a vertex.

        Returns
        -------
        list of vertices in dfs order.
        """

        visited = {}
        sequence = []
        self.dfs_util(v, visited, sequence)
        return sequence

    def dfs_util(self, v, visited, sequence):
        """
        Helper function for dfs.

        Parameters
        ----------
        v : int
            a vertex.
        visited : dict
            dictionary of visited vertices.
        sequence : list
            list of vertices in dfs order.

        Returns
        -------
        list of vertices in dfs order.
        """

        visited[v] = True
        sequence.append(v)
        for edge in self.adj[v]:
            if edge.connected_vertex not in visited:
                self.dfs_util(edge.connected_vertex, visited, sequence)

    def dfs_not_visited(self):
        """
        Returns vertices that were not visited by the dfs.

        Returns
        -------
        list of vertices that were not visited by the dfs.
        """

        not_visited = []
        for k, v in self.adj.items():
            if k not in self.dfs(self.get_first_vertex()):
                not_visited.append(k)
        return not_visited

    def minimum_path(self, a, b):
        """
        Returns the minimum path between two vertices using dijkstra algorithm.

        Parameters
        ----------
        a : int
            first vertex.
        b : int
            second vertex.

        Returns
        -------
        list of vertices in the minimum path.
        """

        distances = self.bellman_ford(a)
        path = [b]
        # se não tiver caminho entre os dois vertices, retorna 0
        if distances[b] == float("inf"):
            return 0
        while b != a:
            for edge in self.adj[b]:
                if distances[b] - edge.weight == distances[edge.connected_vertex]:
                    path.append(edge.connected_vertex)
                    b = edge.connected_vertex
                    break
        path.reverse()

        ''''
        while b != a:
            for edge in self.adj[b]:
                if distances[edge.connected_vertex] + edge.weight == distances[b]:
                    b = edge.connected_vertex
                    path.append(b)
                    break
        path.reverse()
        '''
        return path

    def closeness_centrality(self, v):
        """
        Returns the closeness centrality of a vertex.

        Parameters
        ----------
        v : int
            a vertex.

        Returns
        -------
        closeness centrality of the vertex.
        """

        dist = self.bellman_ford(v)
        sum_bf = 0
        for k, v in dist.items():
            sum_bf += v
        if sum_bf == 0:
            return 0
        return (self.v_number - 1) / sum_bf

    '''
    TP02 - Questão 1
    '''

    def has_cycle(self):
        """
        Returns if the graph has a cycle.

        Returns
        -------
        True if the graph has a cycle, False otherwise.
        """

        for k, v in self.adj.items():
            if self.has_cycle_util(k, k, {}):
                return True
        return False

    def has_cycle_util(self, v, parent, visited):
        """
        Helper function for has_cycle.

        Parameters
        ----------
        v : int
            a vertex.
        parent : int
            parent of the vertex.
        visited : dict
            dictionary of visited vertices.

        Returns
        -------
        True if the graph has a cycle, False otherwise.
        """

        visited[v] = True
        for edge in self.adj[v]:
            if edge.connected_vertex not in visited:
                if self.has_cycle_util(edge.connected_vertex, v, visited):
                    return True
            elif edge.connected_vertex != parent:
                return True
        return False

    '''
    TP02 - Questão 3
    '''

    def vertex_list(self):
        """
        Returns a list of vertices.

        Returns
        -------
        list of vertices.
        """

        return list(self.adj.keys())

    def minimum_vertex_cover_heuristic(self):
        """
        Returns the minimum vertex cover of the graph using a heuristic.

        Returns
        -------
        the minimum vertex cover of the graph.
        """

        cover = []
        nC = 0

        V = self.vertex_list()

        V.sort(key=lambda x: len(self.adj[x]), reverse=True)

        M = []
        for k, v in self.adj.items():
            for edge in v:
                M.append((k, edge.connected_vertex))

        while len(M) != 0:

            k = V[0]

            V.remove(k)
            cover.append(k)

            neighborsofK = []
            for edge in self.adj[k]:
                neighborsofK.append(edge.connected_vertex)

            for v in neighborsofK:
                for a in M:
                    if (k, v) in M:
                        M.remove((k, v))
                    if (v, k) in M:
                        M.remove((v, k))
            nC += 1
        return cover

    """"
    TP02 - Questão 4
    """

    # Max matching using Edmonds's Blossom Algorithm
    def maximum_matching(self):
        """
        Returns the maximum matching of the graph.

        Returns
        -------
        the maximum matching of the graph.
        """

        # Initialize the matching M as empty
        M = []

        # While there exists an augmenting path P
        while self.augmenting_path(M) is not None:
            # Augment M along P
            P = self.augmenting_path(M)
            for i in range(0, len(P) - 1, 2):
                M.append((P[i], P[i + 1]))
        return M

    def augmenting_path(self, M):
        """
        Returns an augmenting path of the graph.

        Parameters
        ----------
        M : list
            the matching.

        Returns
        -------
        an augmenting path of the graph.
        """

        # Initialize the set of visited vertices as empty
        visited = []

        # Initialize the queue Q with all free vertices
        Q = []
        for v in self.vertex_list():
            if self.is_free(v, M):
                Q.append(v)

        # Initialize the tree T as empty
        T = {}

        # While Q is not empty
        while len(Q) != 0:
            # Dequeue a vertex v from Q
            v = Q.pop(len(Q) - 1)

            # For each edge (v, w) in E
            for edge in self.adj[v]:
                w = edge.connected_vertex
                # If w is free
                if self.is_free(w, M):
                    # Return the alternating path P from v to w
                    return self.alternating_path(v, w, T)
                # Else if w is not visited
                elif w not in visited:
                    # Mark w as visited
                    visited.append(w)

                    # Add w to Q
                    Q.append(w)

                    # Add (v, w) to T
                    T[w] = v

                    # Add (w, v) to T
                    T[v] = w

        # Return null
        return None

    def is_free(self, v, M):
        """
        Returns if the vertex is free.

        Parameters
        ----------
        v : int
            a vertex.
        M : list
            the matching.

        Returns
        -------
        True if the vertex is free, False otherwise.
        """

        for e in M:
            if v in e:
                return False
        return True

    def alternating_path(self, v, w, T):
        """
        Returns an alternating path of the graph.

        Parameters
        ----------
        v : int
            a vertex.
        w : int
            a vertex.
        T : dict
            the tree.

        Returns
        -------
        an alternating path of the graph.
        """

        P = [v, w]
        while v in T:
            P.insert(0, T[v])
            v = T[v]
            P.insert(1, v)
        return P
