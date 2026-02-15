# File System Operations
# Problem: Implement a file search system.

# /home/island
# /home/test
# /home/test2/hello
# /hello/world

# input -> hello ?

from collections import defaultdict


class FileSearch:
    def __init__(self):
        self.fileDirectories = defaultdict(list)
        self.fileExtensionSearch = defaultdict(list)
        self.trieFileSearch = {}

    def _addToTrie(self, file):
        node = self.trieFileSearch

        for c in file:
            if c not in node:
                node[c] = {}

            node = node[c]

        node[c] = "*"

    def addDirectories(self, directory):
        splitDir = directory.split("/")

        file = splitDir[-1]

        self.fileDirectories[file].append("".join(splitDir[:-1]))
        self.fileExtensionSearch[file.split(".")[-1]].append(file)

    def searchFile(self, file):
        if file in self.fileDirectories:
            return self.fileDirectories[file]

        return []

    def searchByExtension(self, ext):
        if ext in self.fileExtensionSearch:
            return self.fileExtensionSearch[ext]

        return []

    def searchByPattern(self, pat):
        node = self.trieFileSearch

        for c in pat:
            if c not in node:
                return False

            node = node[c]

        return True
