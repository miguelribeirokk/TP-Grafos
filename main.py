from weighted_graph import *

with open("teste.txt", "r") as f:
    v_number = int(f.readline())
    graph = GraphWeighted(v_number)
    for line in f:
        a, b, w = line.split()
        graph.add_edge(int(a), int(b), float(w))

print("\nGraph\n"
      f"{graph.get_graph()}"
      "\nOrder\n"
      f"Order of the graph: {graph.get_order()}\n"
      "\nSize\n"
      f"Size of the graph: {graph.size()}\n"
      "\nNeighbours\n"
      f"Neighbors of 5: {graph.get_neighbours(5)}\n"
      f"Neighbors of 1: {graph.get_neighbours(1)}\n"
      f"Neighbors of 2: {graph.get_neighbours(2)}\n"
      f"Neighbors of 3: {graph.get_neighbours(3)}\n"
      "\nDegrees\n"
      f"Degree of 5: {graph.degree_of_vertex(5)}\n"
      f"Degree of 1: {graph.degree_of_vertex(1)}\n"
      f"Degree of 2: {graph.degree_of_vertex(2)}\n"
      f"Degree of 3: {graph.degree_of_vertex(3)}\n"
      "\nDegrees sequence\n"
      f"Degree sequence: {graph.degree_sequence()}\n"
      "\nEccentricities\n"
      f"Eccentricity of 1: {graph.eccentricity(1)}\n"
      f"Eccentricity of 2: {graph.eccentricity(2)}\n"
      f"Eccentricity of 3: {graph.eccentricity(3)}\n"
      f"\nRadius\n"
      f"Radius of the graph: {graph.center()}\n"
      f"\nCenter\n"
      f"Center of the graph: {graph.center()}\n"
      f"\nDFS traversal\n"
      f"DFS traversal: {graph.dfs(1)}\n"
      f"Not in DFS traversal: {graph.dfs_not_visited()}\n"
      f"\nMinimum path\n"
      f"Minimum path between 1 and 2: {graph.bellman_ford(1)}\n"
      "\nCloseness centralities\n"
      f"Closeness centrality of 1: {graph.closeness_centrality(1)}\n"
      f"Closeness centrality of 2: {graph.closeness_centrality(2)}\n"
      f"Closeness centrality of 3: {graph.closeness_centrality(3)}\n"
      f"\nJSON\n"
      f"JSON: {generate_json_file_from_text_file('teste.txt', 'matt.json')}\n")
