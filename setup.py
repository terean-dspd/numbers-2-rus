import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="num2rus",
    version="0.0.8.2",
    author="DennisKot",
    author_email="DennisKot@google.com",
    description="A small package to convert float numbers to russian string",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/terean-dspd/numbers-2-rus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
