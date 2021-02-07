from octokit import Octokit

octokit = Octokit("api_key")


octokit.request("POST /user/repos", {
    "body": {
        "name": "repo_name"
    }
}) # create repository

# replace owner with the repository owner name and repo with the repository name for example /repos/husseinraed/octokit.py

octokit.request("GET /repos/owner/repo") # get repository

octokit.request("PATCH /repos/owner/repo", {
    "body": {
        "name": "updated_name"
    }
}) # update repository

octokit.request("DELETE /repos/owner/repo") # delete repository
