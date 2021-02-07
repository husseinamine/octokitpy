# Welcome To Octokit.py 
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/B0B71YU9Y)

# Setup and Install

```sh
git clone github.com/husseinraed/octokit.py
cd octokit.py
python setup.py install
```

# Authorization

```py
from octokit import Octokit

octokit = Octokit("api_key")
```

# Body, Query and Headers Options

```py
from octokit import Octokit

octokit = Octokit("api_key")

# Body Example | change username
octokit.request("PATCH /user", {
    "body": {
        "name": "new_username"
    }
})

# Query Example | get the latest user that signed up to github
print(octokit.request("GET /users", {
    "query": {
        "per_page": 1
    }
}))

# Headers Example | get all your gist and recieve its content in base64 format
print(octokit.request("GET /gists", {
    "headers": {
        "accept": "application/vnd.github.v3.base64"
    }
}))
```

-----------------------------------------------------
# Note
as you see the api is really simple and to use it u just have to know how to use the [github rest api](https://docs.github.com/rest/reference)
