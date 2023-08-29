from __future__ import annotations
import os

def getFilesAndFolders(path:str) -> list[str]:
    return [file for file in os.listdir(path)]

def filterForHTML(filelist:list[str]) -> list[str]:
    return [file for file in filelist if ".html" in file]

def filterForFolder(filelist:list[str]) -> list[str]:
    return [file for file in filelist if "." not in file]

def checkIfFolderHasSubfolder():
    pass

def checkIfFolderHasHtmlFile():
    pass

class folderIndex:
    def __init__(self, path: str, subfolderList:list[str] | None = None, htmlFileList:list[str] | None = None) -> None:
        self.path = path
        self.subfolderList = filterForFolder(getFilesAndFolders(path)) if subfolderList is None else subfolderList
        self.htmlFileList = filterForHTML(getFilesAndFolders(path)) if htmlFileList is None else htmlFileList

    def createHtmlList(self):
        htmlList = f'''<h1>{self.path}</h1>
<h2>Folder</h2>
<ul>'''
        for i in self.subfolderList:
            htmlList += f"<li><a href='{self.path}{i}/index.html'>{i}</a></li>"


def main():
    path="./"
    rootFolderIndex = folderIndex(path)
    print(f"HTML LIST:\n {rootFolderIndex.htmlFileList}")
    print(f"FOLDER LIST:\n {rootFolderIndex.subfolderList}")

if __name__ == "__main__":
    main()