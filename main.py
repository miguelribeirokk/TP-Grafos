import os

from functions.converter import *
from functions.weighted_graph import *

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
    try:
        v_number = int(f.readline())
        graph = GraphWeighted(v_number)
        for line in f:
            a, b, w = line.split()
            graph.add_edge(int(a), int(b), float(w))
    except:
        print("File not formatted correctly!")

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

print("Degree sequence")
print(f"Degree sequence: {graph.degree_sequence()}")

print("\nDFS of a graph")
print(f"DFS traversal: {graph.dfs(first)}")

print("\nNot visited in DFS")
print(f"Not visited in DFS: {graph.dfs_not_visited()}")

if graph.bellman_ford(first) == 0:
    print("Negative cycle detected!")
else:
    print("\nEccentricities")
    for v in sequence:
        print(f"Eccentricity of {v}: {graph.eccentricity(v)}")

    print("\nRadius")
    print(f"Radius of the graph: {graph.radius()}")

    print("\nCenter")
    print(f"Center of the graph: {graph.center()}")

    print("\nDiameter")
    print(f"Diameter of the graph: {graph.diameter()}")

    print("\nDistances")
    for v in sequence:
        print(f"Distance from {first} to {v}: {graph.bellman_ford(first)[v]}")

    print("\nMinimum path")
    for v in sequence:
        print(f"Minimum path between {first} and {v}: {graph.minimum_path(first, v)}")

    print("\nCloseness centralities")
    for v in sequence:
        print(f"Closeness centrality of {v}: {graph.closeness_centrality(v)}")

print("\n\nJson to text?")
print("1. Yes")
print("2. No")
if int(input("Option: ")) == 1:
    print("Type the directory of the .json file: ")
    json_file = input()
    print("Type the name of the .txt file: ")
    text_file = input()
    json_to_text(json_file, text_file)
    print("Done!")

print("\n\nText to json?")
print("1. Yes")
print("2. No")
if int(input("Option: ")) == 1:
    print("Type the directory of the .txt file: ")
    text_file = input()
    print("Type the name of the .json file: ")
    json_file = input()
    text_to_json(text_file, json_file)
    print("Done!")

print("Ty for using my program!")
