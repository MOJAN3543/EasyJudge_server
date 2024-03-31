import os
class FileHandler():
    def __init__(self, filename, contents):
        self.filename = filename
        self.contents = contents.replace('�', '?')
    def create(self):
        if self.filename == "":
            return False
        with open(self.filename, 'wt') as src:
            for line in self.contents:
                src.write(line)
        return True
    def remove(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            return True
        return False

class FileChecker():
    def __init__(self):
        self.fileList = []
    def getFiles(self):
        path = './'
        self.fileList = os.listdir(path)
        return self.fileList
    def getNewFiles(self):
        tmpFileList = self.fileList
        self.getFiles()
        return [file for file in self.fileList if file not in tmpFileList]

class FileReader():
    def __init__(self, filename):
        self.filename = filename
    def read(self):
        ret = ""
        with open(self.filename, "r") as src:
            ret = src.read()
        return ret
    def remove(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            return True
        return False

