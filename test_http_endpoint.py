from vorpal import BaseHttpEndpoint

def test_http_endpoint():
    """
    Test that the BaseHttpEndpoint class can make a GET to a base url
    """
    github_api_endpoint = BaseHttpEndpoint("https://api.github.com")
    response_body = github_api_endpoint.GET('/').json()
    assert response_body["current_user_url"] == "https://api.github.com/user"
