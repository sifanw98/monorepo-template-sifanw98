import unittest
import jsonapi

class TestJSONAPI(unittest.TestCase):

    def test_complex_encoder(self):
        complex_number = 3 + 4j
        encoded = jsonapi.dumps(complex_number)
        expected_encoded = '{"__extended_json_type__": "complex", "values": [3.0, 4.0]}'
        self.assertEqual(encoded, expected_encoded)

    def test_complex_decoder(self):
        json_string = '[3.0, 4.0]'
        decoded = jsonapi.loads(json_string)
        self.assertEqual(decoded, [3.0, 4.0])

    def test_dumps_and_loads(self):
        complex_number = 5 + 6j
        encoded = jsonapi.dumps(complex_number)
        decoded = jsonapi.loads(encoded)
        self.assertEqual(decoded, 5 + 6j)

    def test_range_encoder(self):
        r = range(0, 10, 2)
        encoded = jsonapi.dumps(r)
        expected_encoded = '{"__extended_json_type__": "range", "values": [0, 10, 2]}'
        self.assertEqual(encoded, expected_encoded)

    def test_range_decoder(self):
        json_string = '{"__extended_json_type__": "range", "values": [0, 10, 2]}'
        decoded = jsonapi.loads(json_string)
        self.assertEqual(decoded, range(0, 10 , 2))

    def test_dumps_and_loads_range(self):
        r = range(1, 10)
        encoded = jsonapi.dumps(r)
        decoded = jsonapi.loads(encoded)
        self.assertEqual(decoded, range(1, 10))