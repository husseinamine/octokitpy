import requests
import json

class Octokit:
    """this object represents the github api as a python object"""

    def __init__(self, token):
        self.headers = {"Authorization": "token %s" % token}
        self.base_url = "https://api.github.com"
    
    def request(self, url, options):
        method, path = url.split(" ")
        result = requests.request(method, "%s%s" % (options.get("base_url") or self.base_url, path), headers={**self.headers, **(options.get("headers") or {})}, json=options.get("body"), params=options.get("query"))
        
        try:
            response = json.loads(result.text)
        except ValueError:
            return result.text

        return response
