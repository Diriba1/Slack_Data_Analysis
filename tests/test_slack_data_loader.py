# tests/test_slack_data_loader.py

import unittest
from SlackDataLoader import slack_data

class TestSlackDataLoader(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            'original_column': [1, 2, 3],
            'other_column': ['A', 'B', 'C']
        }

        self.loader = SlackDataLoader(self.sample_data)
        self.df = self.loader.load_data()

    def test_load_data_columns(self):
        expected_columns = ['original_column', 'other_column']
        self.assertCountEqual(expected_columns, self.df.columns)

    def test_process_data_columns(self):
        processed_df = self.loader.process_data(self.df)
        expected_columns = ['original_column', 'other_column', 'processed_column']
        self.assertCountEqual(expected_columns, processed_df.columns)

if __name__ == '__main__':
    unittest.main()
