"""
Exceptions dedicated module
"""


class GitDirectoryNotFound(FileNotFoundError):
    """
    GitDirectory error in case the working directory does not contain any '.git' directory.
    In case no directory you won't be able to process this python module
    """

    def __init__(self, *args: object) -> None:
        super().__init__("Git Directory not found in the current directory")
