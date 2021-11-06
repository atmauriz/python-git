import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pythongit-atmauriz",
    version="0.0.3",
    author="Maurizio Bussi",
    author_email="maurizio.bussi.mb@gmail.com",
    description="PythonGit package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atmauriz/python-git",
    project_urls={
        "Bug Tracker": "https://github.com/atmauriz/python-git/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
)
