import json


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
        vertex_list = []

        with open(json_file) as f:
            data = json.load(f)
        
        with open(f"txt-files/{text_file}.txt", "w") as f:


            

            for i in data['data']['nodes']['_data']:
                for j in data['data']['nodes']['_data'][i]:
                    if j == "label":
                        vertex_list.append(data['data']['nodes']['_data'][i][j])

            

            f.write(str(len(vertex_list)) + "\n")

            for i in data['data']['edges']['_data']:
                for j in data['data']['edges']['_data'][i]:
                    if j == "from":
                        print(vertex_list[data['data']['edges']['_data'][i][j]-1])
                        f.write(vertex_list[data['data']['edges']['_data'][i][j]-1] + " ")
                    if j == "to":
                        print(vertex_list[data['data']['edges']['_data'][i][j]-1])
                        f.write(vertex_list[data['data']['edges']['_data'][i][j]-1] + " ")
                    if j == "label":
                        print(data['data']['edges']['_data'][i][j])
                        f.write(data['data']['edges']['_data'][i][j] + " ")
                f.write("\n")
                    
