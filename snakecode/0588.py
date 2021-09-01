# import re

class INode:
    def __init__(self, name: str) -> None:
        self.name = name

    def ls(self) -> list[str]:
        return [self.name]

class DirNode(INode):
    def __init__(self, name: str):
        super().__init__(name)
        self.children: dict[str, INode] = {}

    def ls(self) -> list[str]:
        return sorted(self.children.keys())

class FileNode(INode):
    def __init__(self, name: str, content: str = ''):
        super().__init__(name)
        self.content = content

class FileSystem:
    def __init__(self):
        self.root = DirNode('')
        self.sep = '/'
        self.voidName = '#'

    # noDirExist: no dir should exist before, recursive: create if not exist
    def _touch(self, path: str, noDirExist: bool = False, recursive: bool = False, createType: type = FileNode) -> INode:
        cur = self.root
        if path == self.sep:
            return cur
        names = path.split(self.sep)[1:]
        for i, name in enumerate(names):
            if type(cur) is DirNode:
                # if i < len(names)-2 and re.match('^[a-zA-Z0-9_]+$', name):
                nextNode = cur.children.get(name, FileNode(self.voidName))
            else: 
                raise FileNotFoundError(f"No such file or directory {path}")
            if noDirExist and i == len(names)-1 and type(nextNode) is DirNode:
                raise FileExistsError(f'Directory {path} exists')
            if nextNode.name == self.voidName:
                if i < len(names)-1 and not recursive:
                    raise FileNotFoundError(f"No such file or directory {path}")
                nextNode = DirNode(name) if i < len(names)-1 else createType(name)
                cur.children[name] = nextNode
            cur = nextNode
        return cur

    # GET /path [OK, 404]
    def ls(self, path: str) -> list[str]:
        node = self._touch(path)
        return node.ls()

    # POST /path?type=dir [201 Created, 202 Accepted, 204 No Content, 400 Bad Request, 409 Conflict]
    def mkdir(self, path: str, recursive: bool = False) -> None:
        node = self._touch(path, noDirExist=True, recursive=recursive, createType=DirNode)
        if type(node) is FileNode:
            raise FileExistsError(f'Cannot create directory, file {path} exists')

    # PUT /path?type=file; body: content  [201 Created, 202 Accepted, 204 No Content, 400 Bad Request, 409 Conflict]
    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._touch(filePath, noDirExist=True, recursive=True, createType=FileNode)
        if type(node) is FileNode:
            node.content += content
        else:
            raise IsADirectoryError(f'Cannot write file {filePath}, it is a directory')
    
    # Get /path?type=detail # GET /path [OK, 404]
    def readContentFromFile(self, filePath: str) -> str:
        node = self._touch(filePath)
        if type(node) is FileNode:
            return node.content
        else:
            raise IsADirectoryError(f'Cannot read file {filePath}, it is a directory')


# Your FileSystem object will be instantiated and called as such:
fs = FileSystem()
print('print ls /', fs.ls('/'))
fs.mkdir('/home')
fs.mkdir('/home/user/bob', recursive=True)
print('print ls /home/user', fs.ls('/home/user'))
print('print ls /home/user/bob', fs.ls('/home/user/bob'))
fs.addContentToFile('/home/user/alice/text', "Hello World! ")
print('print ls /home/user/alice/text', fs.ls('/home/user/alice/text'))
print('read file', fs.readContentFromFile('/home/user/alice/text'))
fs.addContentToFile('/home/user/alice/text', "I'm alice.")
print('read file', fs.readContentFromFile('/home/user/alice/text'))
# print('print ls /home/user/alice/text/bad', fs.ls('/home/user/alice/text/bad'))
# print('read file bad', fs.readContentFromFile('/home/user/alice'))
# print('read file bad', fs.readContentFromFile('/home/user/alice'))
fs.mkdir('/home/user/alice/likes')
print('read file again!', fs.readContentFromFile('/home/user/alice/text'))