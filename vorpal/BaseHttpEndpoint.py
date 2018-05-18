"""
Module containing base class for HTTP endpoints.
"""

import requests

class BaseHttpEndpoint:
    """
    Base class for HTTP endpoints.
    Http endpoints should subclass this.
    Base methods return request objects from 'requests' library.
    Requests libary docs: http://docs.python-requests.org/en/master/
    """

    def __init__(self, base_url):
        """
        Initializes the BaseHttpEndpoint class.
        :param base_url: base url for the endpoint as str (e.g. 'https://wwwi3logix.com')
        """
        # If the provided base_url ends with '/', snip that off
        self.base_url = base_url if base_url[-1] != '/' else base_url[:-1]

    def GET(self, relative_path='/', query_params={}, **kwargs):
        """
        Send GET request to endpoint
        :param relative_path: (optional) path to endpoint relative to base_url (e.g. '/users')
        :param query_params: (optional) query parameters in key:value dict
        :param **kwargs: (optional) additional keyword args to pass to requests.get
        :return: response object from 'requests' library
        """
        return requests.get(self.base_url + relative_path, params=query_params, **kwargs)
    
    def POST(self, relative_path='/', data = {}, is_json=True, **kwargs):
        """
        Send POST request to endpoint
        :param relative_path: (optional) path to endpoint relative to base_url (e.g. '/users')
        :param data: (optional) request data as dict
        :param is_json: (optional) sends data as JSON if true, else as form data
        :param **kwargs: (optional) additional keyword args to pass to requests.post
        :return: response object from 'requests' library
        """
        # If not is_json, we assume data is from a form
        if is_json:
            return requests.post(self.base_url + relative_path, json=data, **kwargs)
        else:
            return requests.post(self.base_url + relative_path, data=data, **kwargs)
    
    def PUT(self, relative_path='/', data = {}, is_json=True, **kwargs):
        """
        Send PUT request to endpoint
        :param relative_path: (optional) path to endpoint relative to base_url (e.g. '/users')
        :param data: (optional) request data as dict
        :param is_json: (optional) sends data as JSON if true, else as form data
        :param **kwargs: (optional) additional keyword args to pass to requests.put
        :return: response object from 'requests' library
        """
        # If not is_json, we assume data is from a form
        if is_json:
            return requests.put(self.base_url + relative_path, json=data, **kwargs)
        else:
            return requests.put(self.base_url + relative_path, data=data, **kwargs)
    
    def PATCH(self, relative_path='/', data = {}, is_json=True, **kwargs):
        """
        Send PATCH request to endpoint
        :param relative_path: (optional) path to endpoint relative to base_url (e.g. '/users')
        :param data: (optional) request data as dict
        :param is_json: (optional) sends data as JSON if true, else as form data
        :param **kwargs: (optional) additional keyword args to pass to requests.put
        :return: response object from 'requests' library
        """
        # If not is_json, we assume data is from a form
        if is_json:
            return requests.patch(self.base_url + relative_path, json=data, **kwargs)
        else:
            return requests.patch(self.base_url + relative_path, data=data, **kwargs)

    def DELETE(self, relative_path='/', **kwargs):
        """
        Send DELETE request to endpoint
        :param relative_path: (optional) path to endpoint relative to base_url (e.g. '/users')
        :param **kwargs: (optional) additional keyword args to pass to requests.delete
        :return: response object from 'requests' library
        """
        return requests.delete(self.base_url + relative_path, **kwargs)
