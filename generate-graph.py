import random


def generate_graph(n, p):
    """
    Generates a graph with n vertices and p probability.
    """
    with open(f"txt-files/graph-{n}-{p}.txt", "w") as f:
        f.write(str(n) + "\n")
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < p:
                    f.write(str(i) + " " + str(j) + " " + str(random.randint(1, 100)) + "\n")


if __name__ == "__main__":
    print("Generating graph...")
    print("Number of vertexes: ", end="")
    n = int(input())
    print("Probability: ", end="")
    p = float(input())
    for i in range(100):
        generate_graph(n, p)
    print("Done!")
