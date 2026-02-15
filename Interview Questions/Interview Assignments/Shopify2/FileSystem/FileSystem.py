from typing import List, Optional, Dict
from collections import defaultdict

class FileSystem:

    def __init__(self):
        self.directories = {}
        self.files = defaultdict(str)

    def _traverse(self, path: str) -> Optional[dict]:
        node = self.directories
        if path == "/":
            return node
        
        folders = path.split("/")[1:]
        
        for folder in folders:
            if folder not in node:
                return None
            
            node = node[folder]

        return node

    def createDirectories(self, path: str) -> dict:
        folders = path.split("/")[1:]

        node = self.directories
        for folder in folders:
            if folder not in node:
                node[folder] = {}

            node = node[folder]

        return node

    def ls(self, path: str) -> List[str]:
        if path in self.files:
            return [path.split("/")[-1]]
        
        node = self._traverse(path)

        if node is None:
            return []
        
        return sorted(node.keys())

    def mkdir(self, path: str) -> None:
        self.createDirectories(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = filePath.split("/")
        folderPath = "/".join(parts[:-1])

        node = self.createDirectories(folderPath)

        node[parts[-1]] = "\n"
        self.files[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]