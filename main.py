if __name__ == "__main__":
    CHUNK_SIZE = 100    
    json_file = "datasets/eval_travel_times_formatted.json"
    
    all_ids = get_all_ids(json_file)