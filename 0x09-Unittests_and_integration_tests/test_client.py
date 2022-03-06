#!/usr/bin/env python3
"""
Module for client_utils.py
0x09. Unittests and Integration Tests
Holberton Web Stack programming Spec ― Back-end
"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """ Defines the TestAccessNestedMap Class """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Tests that GithubOrgClient.org returns the correct value
        """
        test = GithubOrgClient(org_name)
        test.org()
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """
        Test that the result of `GithubOrgClient._public_repos_url`
        is the expected one based on the mocked payload.

        @property
        def _public_repos_url(self) -> str:
            return self.org["repos_url"]
        """
        # You can't do relative imports from the file you execute since
        # GithubOrgClient is not a part of a package:
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
            mock.return_value = payload
            test = GithubOrgClient("google")
            self.assertEqual(test._public_repos_url,
                             mock.return_value["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ unit-test GithubOrgClient.public_repos """
        mock_get_json.return_value = [
                                {"name": "tracing-framework"},
                                {"name": "episodes.dart"}
                            ]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            mock.return_value = "https://api.github.com/orgs/google/repos"
            test = GithubOrgClient("google")
            public_repos = test.public_repos()
            self.assertEqual(['tracing-framework', 'episodes.dart'],
                             public_repos)
            mock_get_json.assert_called_once()
            mock_get_json.assert_called_once_with(mock.return_value)
            mock.assert_called_once()
