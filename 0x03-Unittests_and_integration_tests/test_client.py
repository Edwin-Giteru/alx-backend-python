#!/usr/bin/env python3
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient 
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json):
        """Test the org method of GithubOrgClient"""
        mock_org_response = {"repos_url": f"https://api.github.com/orgs/{org_name}/repos"}
        mock_get_json.return_value = mock_org_response
        client = GithubOrgClient(org_name)
        result = client.org()
        self.assertEqual(result, mock_org_response)
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

    @patch.object(GithubOrgClient, 'org', return_value={"repos_url": "https://api.github.com/orgs/google/repos"})
    def test_public_repos_url(self, mock_org):
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")
        mock_org.assert_called_once()
   
    @patch("utils.get_json")
    @patch.object(GithubOrgClient, "_public_repos_url", return_value="https://api.github.com/orgs/google/repos")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        client = GithubOrgClient("google")
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        result = client.public_repos()
        self.assertEqual(result, ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")



if __name__ == '__main__':
    unittest.main()
