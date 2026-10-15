import unittest
from signal_processing_recommender import data_loader

class TestDataLoader(unittest.TestCase):

    def test_load_file(self):
        path = 'path/to/file.txt'
        with open(path, 'w') as f:
            f.write('Hello, World!')
        self.assertEqual(data_loader._load_file(path), b'Hello, World!')
        os.remove(path)

    def test_load_json_file(self):
        path = 'path/to/data.json'
        with open(path, 'w') as f:
            json.dump([{'key': 'value'}], f)
        self.assertEqual(data_loader._load_json_file(path), [{'key': 'value'}])
        os.remove(path)

    def test_load_waveform_data_numpy(self):
        path = 'path/to/data.npy'
        with open(path, 'w') as f:
            f.write('Hello, World!')
        self.assertEqual(data_loader._load_waveform_data(path, 'numpy'), b'Hello, World!')
        os.remove(path)

    def test_load_waveform_data_pandas(self):
        path = 'path/to/data.csv'
        with open(path, 'w') as f:
            f.write('1\n2\n3')
        self.assertEqual(data_loader._load_waveform_data(path, 'pandas'), [1.0, 2.0, 3.0], 3)
        os.remove(path)

    def test_load_audio_data(self):
        path = 'path/to/audio.npy'
        with open(path, 'w') as f:
            f.write('Hello, World!')
        self.assertEqual(data_loader.load_audio_data(path), b'Hello, World!')
        os.remove(path)

    def test_load_sensor_data(self):
        path = 'path/to/sensor.npy'
        with open(path, 'w') as f:
            f.write('Hello, World!')
        self.assertEqual(data_loader.load_sensor_data(path), b'Hello, World!')
        os.remove(path)

if __name__ == '__main__':
    unittest.main()
