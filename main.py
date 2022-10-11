from weighted_graph import *

graph = GraphWeighted(5)

graph.add_edge(1, 2, 1.2)
graph.add_edge(2, 5, 2.3)
graph.add_edge(3, 5, 8.4)
graph.add_edge(3, 4, 0.3)
graph.add_edge(4, 5, 4.6)
graph.add_edge(1, 5, 0.1)

# print("undirected graph:")
# graph.print_graph()
#
# print("dfs:")
# graph.dfs_traversal(1)
#
# print("bfs:")
# graph.bfs_traversal(1)
#
# print("Order: " + str(graph.get_order()))
#
# print("Number of vertices: " + str(graph.numbers_of_edges()))
#
# print("Neighbors of 5: " + str(graph.get_neighbors(5)))
#
# print("Degree of 5: " + str(graph.degree_of_node(5)))
#
# print("Degree sequence: " + str(graph.degree_sequence()))
#
# print("Graph center: " + str(graph.graph_center()))

# print("Shortest distance between 1 and 2: " + str(graph.dijkstra(1)))

print("Eccentricity of 3: " + str(graph.eccentricity(3)))

print("Eccentricity of 1: " + str(graph.eccentricity(1)))

print("Eccentricity of 2: " + str(graph.eccentricity(2)))

print("Eccentricity of 4: " + str(graph.eccentricity(4)))

# print("Closeness Centrality 3: " + str(graph.closeness_centrality(3)))

# print("has node 3:" + str(graph.has_node(3)))
# print("has node 5:" + str(graph.has_node(5)))
# print("has edge 3,2: " + str(graph.has_edge(3, 2)))
# print("has edge 3,1: " + str(graph.has_edge(3, 1)))
# print("has path 2,3 (DFS): " + str(graph.has_path_dfs(2, 3)))
# print("has path 2,5 (DFS): " + str(graph.has_path_dfs(2, 5)))
# print("has path 2,3 (BFS): " + str(graph.has_path_bfs(2, 3)))
# print("has path 2,5 (BFS): " + str(graph.has_path_bfs(2, 5)))
#
# graph.remove_edge(3, 4)
# print("after remove edge:")
# graph.print_graph()
# graph.add_edge(3, 4, 20)
# print("after add back edge:")
# graph.print_graph()
#
# graph.remove_node(1)
# print("after remove node:")
# graph.print_graph()
# print()
