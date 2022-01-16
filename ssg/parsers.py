from typing import List
from pathlib import Path
import shutil


class Parser:
    def __init__(self):
        self.extentions= List[str]

    def valid_extension(self, extension):
        if extension in self.extentions:
            return True
        else:
            return False

    def parse(self, path, source, dest):
        self.path = Path(path)
        self.source = Path(source)
        self.dest = Path(dest)

        raise NotImplementedError

    def read(self, path):
        with open(path) as file:
            return file.read

    def write(self, path, dest, content, ext ="html"):
        self.full_path = self.dest/path.with_suffix(ext).name
        with open(self.full_path) as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest/source)

class ResourceParser(Parser):
    def __init__ (self)
        self.extensions =[".jpg0", ".png",".gif", ".css", ".html"]
        Parser.copy(self.path, self.source, self.dest)





