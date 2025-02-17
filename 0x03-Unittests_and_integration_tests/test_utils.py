#!/usr/bin/env python3
import unittest
import requests
from parameterized import parameterized
from unittest.mock import Mock, patch, MagicMock
get_json = __import__('utils').get_json
access_nested_map = __import__('utils').access_nested_map
memoize = __import__("utils").memoize
"""
a unittest for utils.access_nested_map
"""


class TestAccessNestedMap(unittest.TestCase):
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, result):
        self.assertEqual(access_nested_map(nested_map, path), result)
    
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")), 
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), str(path[-1]))



class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42
            @memoize
            def a_property(self):
                return self.a_method()
            
        test_instance = TestClass()

        with patch.object(test_instance, "a_method", return_value = 42) as mock_method:
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, result2)
            mock_method.assert_called_once()

if __name__ == "__main__":
        unittest.main()
        
