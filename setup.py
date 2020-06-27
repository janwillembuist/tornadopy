import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tornadopy-janwillembuist",
    version="1.0",
    author="J.W. Buist",
    description="Tornado plot in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/janwillembuist/tornadopy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)