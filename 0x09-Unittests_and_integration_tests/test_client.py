#!/usr/bin/env python3
"""
Test for client
"""

from unittest import TestCase, mock
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import requests


class TestGithubOrgClient(TestCase):
    """
    Test for client.GithubOrgClient
    """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, name, payload, fn_get):
        """ test case for client.org """
        goc = GithubOrgClient(name)
        fn_get.return_value = payload

        self.assertEqual(payload, goc.org)
        fn_get.assert_called_once()

    def test_public_repos_url(self):
        """
        test for client._public_repos_url
        """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_obj:
            mock_obj.return_value = {"url": 'http://google.com'}

            r = GithubOrgClient(mock_obj.return_value)._public_repos_url

            self.assertEqual(r, mock_obj.return_value)
            mock_obj.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license, expected):
        """
        test for client._has_licence
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)

    @patch('client.get_json')
    def test_public_repos(self, mock1):
        """
        test for client._public_repos
        """
        a = {"name": "a", "license": {"key": "k"}}
        b = {"name": "b", "license": {"key": "l"}}
        c = {"name": "c"}
        method = 'client.GithubOrgClient._public_repos_url'
        mock1.return_value = [a, b, c]
        with patch(method, PropertyMock(return_value="www.k.com")) as m2:
            goc = GithubOrgClient("my_goc")
            self.assertEqual(goc.public_repos(), ['a', 'b', 'c'])
            self.assertEqual(goc.public_repos("k"), ['a'])
            self.assertEqual(goc.public_repos("c"), [])
            self.assertEqual(goc.public_repos(17), [])
            mock1.assert_called_once_with("www.k.com")
            m2.assert_called_once_with()
