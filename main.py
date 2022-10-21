from msilib import sequence
import os
from functions.weighted_graph import *
from functions.converter import *




while True:
    try:
        file = input("Type the directory of the .txt file: ")
        if os.path.isfile(file):
            break
        else:
            print("File not found!")
    except:
        print("File not found!")

    
with open(file) as f:
    v_number = int(f.readline())
    graph = GraphWeighted(v_number)
    for line in f:
        a, b, w = line.split()
        graph.add_edge(int(a), int(b), float(w))


sequence = graph.get_vertex_sequence()
first = graph.get_first_vertex()

print(
      "\nOrder\n"
      f"Order of the graph: {graph.get_order()}\n"
      "\nSize\n"
      f"Size of the graph: {graph.size()}\n"
)

print("Neighbours")
for v in sequence:
    print(f"Neighbours of {v}: {graph.get_neighbours(v)}")

print("\nDegrees")
for v in sequence:
    print(f"Degree of {v}: {graph.degree_of_vertex(v)}")

print("\nEccentricities")
for v in sequence:
    print(f"Eccentricity of {v}: {graph.eccentricity(v)}")

print("\nRadius")
print(f"Radius of the graph: {graph.radius()}")

print("\nCenter")
print(f"Center of the graph: {graph.center()}")

print("\nDiameter")
print(f"Diameter of the graph: {graph.diameter()}")



print("\nDFS of a graph")
print(f"DFS traversal: {graph.dfs(first)}")

print("\nNot visited in DFS")
print(f"Not visited in DFS: {graph.dfs_not_visited()}")

print("\nDistances")
for v in sequence:
    print(f"Distance from {first} to {v}: {graph.bellman_ford(first)[v]}")

print("\nMinimum path")
for v in sequence:
    print(f"Minimum path between {first} and {v}: {graph.minimum_path(first, v)}")

print("\nCloseness centralities")
for v in sequence:
    print(f"Closeness centrality of {v}: {graph.closeness_centrality(v)}")

while True:
    try:
        file_json = input("\nType the directory of the .json file: ")
        if os.path.isfile(file):
            break
        else:
            print("File not found!")
    except:
        print("File not found!")

file_txt = input("\nType the name of the .txt file to converts:")


json_to_text(file_json, file_txt)








        
        



    
    

    
