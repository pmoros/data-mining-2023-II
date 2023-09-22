import json

def get_all_ids(json_file):
    ids = []

    with open(json_file, 'r') as file:
        json_data = json.load(file)

        for id in json_data.keys():
            ids.append(id)

    return ids

def load_data(json_file, ids_to_load):
    data = []

    with open(json_file, 'r') as file:
        for line in file:
            record = json.loads(line)
            for id_to_load in ids_to_load:
                if id_to_load in record:
                    data.append(record[id_to_load])

def chunk_ids(ids, chunk_size):
    """Split a list of IDs into smaller chunks."""
    for i in range(0, len(ids), chunk_size):
        yield ids[i:i + chunk_size]                