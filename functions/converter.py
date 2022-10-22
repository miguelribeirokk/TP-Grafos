import json


def vertex_list(text_file):
    """
    Returns a list with the vertices of a graph.

    Parameters
    ----------
    text_file : str
        text file.
    """

    vertexlist = []

    file = open(text_file, "r")
    lines = file.readlines()[1:]

    for line in lines:
        first = line.split()[0]
        second = line.split()[1]
        if first not in vertexlist:
            vertexlist.append(first)
        if second not in vertexlist:
            vertexlist.append(second)
    file.close()
    return vertexlist


def json_to_text(json_file, text_file):
    """
    Converts a json file to a text file.

    Parameters
    ----------
    json_file : str
        json file.
    text_file : str
        text file.
    """
    vertexlist = []

    with open(json_file) as f:
        data = json.load(f)

    with open(f"txt-files/{text_file}.txt", "w") as f:

        for i in data['data']['nodes']['_data']:
            for j in data['data']['nodes']['_data'][i]:
                if j == "label":
                    vertexlist.append(data['data']['nodes']['_data'][i][j])

        f.write(str(len(vertexlist)) + "\n")

        for i in data['data']['edges']['_data']:
            for j in data['data']['edges']['_data'][i]:
                if j == "from":
                    print(vertexlist[data['data']['edges']['_data'][i][j] - 1])
                    f.write(vertexlist[data['data']['edges']['_data'][i][j] - 1] + " ")
                if j == "to":
                    print(vertexlist[data['data']['edges']['_data'][i][j] - 1])
                    f.write(vertexlist[data['data']['edges']['_data'][i][j] - 1] + " ")
                if j == "label":
                    f.write(data['data']['edges']['_data'][i][j] + " ")
            f.write("\n")


def text_to_json(text_file, json_file):
    """
    Converts a text file to a json file.

    Parameters
    ----------
    text_file : str
        text file.
    json_file : str
        json file.
    """

    text_file = str(text_file)
    vlist = vertex_list(text_file)

    with open(text_file, "r") as f:
        lines = f.readlines()[1:]
        with open(f"json-files/{json_file}.json", "w") as f:
            f.write("{\n")
            f.write('"data": {\n')
            f.write('"nodes": {\n')
            f.write('"_data": {\n')
            for i in range(len(vlist)):
                f.write(f'"{i + 1}": {{\n')
                f.write(f'"id": {i + 1},\n')
                f.write(f'"label": "{vlist[i]}"\n')
                if i == len(vlist) - 1:
                    f.write("}\n")
                else:
                    f.write("},\n")
            f.write("}\n")
            f.write("},\n")
            f.write('"edges": {\n')
            f.write('"_data": {\n')
            for i in range(len(lines)):
                f.write(f'"{i + 1}": {{\n')
                f.write(f'"from": {vlist.index(lines[i].split()[0]) + 1},\n')
                f.write(f'"to": {vlist.index(lines[i].split()[1]) + 1},\n')
                f.write(f'"label": "{lines[i].split()[2]}",\n')
                f.write(f'"id": {i + 1},\n')
                f.write(f'"color": {{\n')
                f.write("}\n")
                if i == len(lines) - 1:
                    f.write("}\n")
                else:
                    f.write("},\n")

            f.write("}\n")
            f.write("}\n")
            f.write("},\n")

            f.write('"ponderado": true,\n')
            f.write('"ordenado": false\n')

            f.write("}\n")
