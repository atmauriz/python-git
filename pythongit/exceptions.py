"""
Custom Exceptions
"""


class GitDirectoryNotFound(FileNotFoundError):

    def __init__(self, *args: object) -> None:
        super().__init__("Git Directory not found in the current directory")
