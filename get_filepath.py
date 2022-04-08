import os
import sys

# Start: Search File & Create Full Path


class SearchFile():
    def __init__(self, searchPhrase):
        self.searchPhrase = searchPhrase

    def searchProject(self):
        result = []
        cwd = os.getcwd()
        for root, dirs, files in os.walk(cwd):
            if self.searchPhrase in dirs or self.searchPhrase in files:
                #             print(dirs)
                #             print(files)
                if len(dirs) != 0:
                    for dire in dirs:
                        if self.searchPhrase == dire:
                            sr = {
                                "dir": dire,
                                "path": root
                            }
                            result.append(sr)
                if len(files) != 0:
                    for file in files:
                        if self.searchPhrase == file:
                            sr = {
                                "file": file,
                                "path": root
                            }
                            result.append(sr)

        return result

    def completePath(self):
        searchres = self.searchProject()
        if searchres:
            fileInfo = searchres[0]

            fileType = [*fileInfo][0]
            print(fileType)
            compPath = os.path.join(fileInfo['path'], fileInfo[f'{fileType}'])
            return compPath
# END - Search File & Create Complete Path

    # following function is for resolving Pyinstaller error regarding path not found

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """

        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
