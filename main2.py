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
    except FileNotFoundError:
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
    "\nHas cycle?\n"
    f"Has cycle?: {graph.has_cycle()}\n"
)

graph.minimum_spanning_tree(file)
print("Minimum Spanning Tree\n"
      f"File name: {file.removesuffix('.txt')}MST.txt\n")

print("Minimum Vertex Cover\n"
      f"Final result: {graph.minimum_vertex_cover_heuristic()}, with {len(graph.minimum_vertex_cover_heuristic())} vertices\n")

print(f"Maximum matching\n"
      f"Final result: {graph.maximum_matching()} \n")
