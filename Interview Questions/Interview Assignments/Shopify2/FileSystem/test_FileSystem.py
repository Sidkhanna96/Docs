import pytest
from FileSystem import FileSystem

def test_should_be_able_make_directories():
    fileSystemInstance = FileSystem()

    fileSystemInstance.mkdir("/a/b/c")

    assert fileSystemInstance.directories == {"a": {"b": {"c": {}}}}

def test_should_be_able_to_add_content_to_file():
    fileSystemInstance = FileSystem()

    fileSystemInstance.addContentToFile("/a/b/c", "TEST_DATA")

    assert fileSystemInstance.directories == {"a": {"b": {"c": "\n"}}}
    assert fileSystemInstance.files == {"/a/b/c": "TEST_DATA"}

def test_should_be_able_to_read_content_from_file():
    fileSystemInstance = FileSystem()

    fileSystemInstance.addContentToFile("/a/b/c", "TEST_DATA")

    assert fileSystemInstance.readContentFromFile("/a/b/c") == "TEST_DATA"

def test_should_be_able_to_list_file():
    fileSystemInstance = FileSystem()

    fileSystemInstance.addContentToFile("/a/b/c", "TEST_DATA")

    assert fileSystemInstance.ls("/a/b/c") == ["c"]

def test_should_be_able_to_list_folder_files():
    fileSystemInstance = FileSystem()

    fileSystemInstance.addContentToFile("/a/b/c", "TEST_DATA")
    fileSystemInstance.mkdir("/a/b/d")

    assert fileSystemInstance.ls("/a/b") == ["c", "d"]

def test_should_be_able_to_list_folder_files():
    fileSystemInstance = FileSystem()

    fileSystemInstance.addContentToFile("/a/b/c", "TEST_DATA")
    fileSystemInstance.mkdir("/a/b/d")

    assert fileSystemInstance.ls("/a/b") == ["c", "d"]


def test_should_return_none_when_folder_does_not_exist():
    fileSystemInstance = FileSystem()

    fileSystemInstance.mkdir("/a/b/d")

    assert fileSystemInstance.ls("/a/b/k") == []

def test_should_return_first_directory_when_slash_provided():
    fileSystemInstance = FileSystem()

    fileSystemInstance.mkdir("/a/b/d")

    assert fileSystemInstance.ls("/") == ["a"]
