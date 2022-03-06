#!/usr/bin/env python3
"""
Tests for utils
"""

from unittest import TestCase, mock
from parameterized import parameterized
from utils import requests, get_json, access_nested_map, memoize


class TestAccessNestedMap(TestCase):
    """ Test cases for utils.test_access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, values, path, expected):
        """
        Testing return
        """
        r = access_nested_map(values, path)
        self.assertEqual(r, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, values, path, expected):
        """
        Testing errors
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(values, path)
            self.assertEqual(expected, str(e.exception))


class TestGetJson(TestCase):
    """
    Test class for utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test utils.get_json
        """

        mock_obj = mock.Mock()
        mock_obj.json.return_value = test_payload

        with mock.patch('requests.get', return_value=mock_obj) as n:
            r = get_json(test_url)
            mock_obj.json.assert_called_once()
            self.assertEqual(r, test_payload)


class TestMemoize(TestCase):
    """
    Test class for utils.memoize
    """

    def test_memoize(self):
        """
        Test utils.memoize
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_obj:
            """ test a_method """
            t_c1 = TestClass()
            t_c1.a_property()
            t_c1.a_property()
            mock_obj.assert_called_once()
