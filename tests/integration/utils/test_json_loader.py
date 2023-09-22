
import unittest
import utils

class TestChunkRead(unittest.TestCase):
    def setUp(self):
        self.RAW_FILE = "datasets/eval_travel_times_formatted.json"
    def test_chunk_read(self):
        with open(self.RAW_FILE, 'r') as f_obj:
            for chunk in utils.chunk_read(f_obj, 'RouteID', 1):
                print('new line:', chunk)
                break