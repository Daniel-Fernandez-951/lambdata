"""lambdata-collection of datascience functions"""

import setuptools

REQUIRED  = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lambdata-rgiuffre90",
    version="0.0.1",
    author="rgiuffre90",
    description="collection of DS functions",
    long_description=LONG_DESCRIPTION,
    long_description_content="text/markdown",
    url="https://github.com/rgiuffre90/lambdata.git",
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)
