from __future__ import annotations
import os

def getFilesAndFolders(path:str) -> list[str]:
    return [file for file in os.listdir(path)]

def filterForHTML(filelist:list[str]) -> list[str]:
    return [file for file in filelist if ".html" in file]

def filterForFolder(filelist:list[str]) -> list[str]:
    return [file for file in filelist if "." not in file]

class folderIndex:
    def __init__(self, path: str, subfolderList:list[str] | None = None, htmlFileList:list[str] | None = None) -> None:
        self.path = path
        self.subfolderList = filterForFolder(getFilesAndFolders(path)) if subfolderList is None else subfolderList
        self.htmlFileList = filterForHTML(getFilesAndFolders(path)) if htmlFileList is None else htmlFileList

def main():
    path="./"
    rootFolderIndex = folderIndex(path)
    print(f"HTML LIST:\n {rootFolderIndex.htmlFileList}")
    print(f"FOLDER LIST:\n {rootFolderIndex.subfolderList}")

if __name__ == "__main__":
    main()