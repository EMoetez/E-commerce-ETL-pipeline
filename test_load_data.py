import unittest
from unittest.mock import patch, MagicMock
import load_data

class TestLoadData(unittest.TestCase):

    @patch('load_data.mysql.connector.connect')
    def test_load_customer_data(self, mock_connect):
        # Mock the database connection and cursor
        mock_db = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_db
        mock_db.cursor.return_value = mock_cursor

        # Mock the data returned by the cursor
        mock_cursor.fetchall.return_value = [
            {'CustomerID': 1, 'Email': 'test1@example.com'},
            {'CustomerID': 2, 'Email': 'test2@example.com'}
        ]

        # Ensure the cursor's execute method does not raise an error
        mock_cursor.execute.return_value = None

        customers = load_data.load_customer_data()
        self.assertEqual(len(customers), 2)
        self.assertEqual(customers[0]['Email'], 'test1@example.com')

    @patch('load_data.mysql.connector.connect')
    def test_load_event_data(self, mock_connect):
        # Mock the database connection and cursor
        mock_db = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_db
        mock_db.cursor.return_value = mock_cursor

        # Mock the data returned by the cursor
        mock_cursor.fetchall.side_effect = [
            [{'EventID': 1, 'CustomerID': 1, 'ContentID': 1, 'Quantity': 2, 'EventDate': '2020-04-01'}],
            [{'ContentID': 1, 'Price': 10.0}]
        ]

        # Ensure the cursor's execute method does not raise an error
        mock_cursor.execute.return_value = None

        events = load_data.load_event_data()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]['Price'], 10.0)

if __name__ == '__main__':
    unittest.main()