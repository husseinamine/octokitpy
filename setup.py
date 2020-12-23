import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="octokit",
    version="0.0.dev1",
    author="Hussein Amine",
    author_email="me@husseinraed.cf",
    description="a github api wrapper inspired by octokit-js",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/memesterhub/octokit.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)