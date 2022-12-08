import sys


class DLLNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._len = 0

    def add(self, val):
        node = DLLNode(val)
        if self._head:
            node.next = self._head
            self._head.prev = node
        self._head = node
        self._len += 1

    def remove(self):
        self._head = self._head.next
        self._head.prev = None
        self._len -= 1

    def poll(self, name=None):
        if not (name and self._head):
            return self._head
        head = self._head
        while head.val.name != name:
            head = head.next
        return head

    def __len__(self):
        return self._len


class Queue:
    def __init__(self):
        self._queue = DoublyLinkedList()

    def add(self, val):
        self._queue.add(val)

    def remove(self):
        self._queue.remove()

    def poll(self, name=None):
        node = self._queue.poll(name=name)
        return node.val if node else node

    def is_empty(self):
        return len(self._queue) == 0

    def __len__(self):
        return len(self._queue)


class Dir:
    def __init__(self, name, parent, children=None, files=None):
        self.parent = parent
        self.name = name
        self.files = files or []
        self.children = children or []

    def append(self, child):
        if isinstance(child, Dir):
            self.children.append(child)
        else:
            self.files.append(child)


class FileSystem:
    def __init__(self):
        self.size_map = dict()
        self._q = Queue()

    def __repr__(self):
        root = self.root
        total = self.fsize(root)
        return self.display()

    @property
    def curr(self):
        return self._q.poll()

    @property
    def root(self):
        return self._q.poll(name='/')

    def mkdir(self, name):
        _dir = Dir(name=name, parent=self.curr)
        if self._q.is_empty() and name == '/':
            self._q.add(_dir)
        else:
            self.curr.children.append(_dir)

    def touch(self, name, size):
        keys = ('name', 'size')
        self.curr.files.append(dict(zip(keys, (name, size))))

    def change_dir(self, name):
        if name == "..":
            self._q.remove()
        elif name == '/':
            root = self.root
            while self.curr is not root:
                self._q.remove()
        else:
            _dir = [c for c in self.curr.children if c.name == name][0]
            self._q.add(_dir)

    def display(self, root=None, indent=2):
        root = root or self.root
        parent = root.parent.name if root.parent else root.parent
        sstr = f'{parent} -> {root.name}'
        _repr = [f"– {root.name} (dir, parent={parent}, size={self.size_map[sstr]})"]
        for f in root.files:
            _repr.extend(
                ["\n", " " * indent, f'- {f["name"]}(file, size={f["size"]})']
            )
        for c in root.children:
            _repr.extend(["\n", " " * indent, self.display(c, indent+4)])
        return "".join(_repr)

    def fsize(self, directory):
        s = 0
        for d in directory.children:
            s += self.fsize(d)
        for f in directory.files:
            s += f["size"]
        pname = directory.parent.name if directory.parent else directory.parent
        self.size_map[f'{pname} -> {directory.name}'] = self.size_map.get(f'{pname} -> {directory.name}', 0) + s
        return s


def main(file):
    ans = 0
    MAX_SIZE = 100000
    dir_map = set()
    fs = FileSystem()
    fs.mkdir('/')
    dir_map.add('None -> /')
    with open(file) as f:
        for l in f.readlines():
            l = l.strip().strip("\n")
            if not l.startswith("$"):
                if l.startswith("dir"):
                    _, name = l.split()
                    parent = fs.curr.name
                    dir_edge = f'{parent} -> {name}'
                    if dir_edge not in dir_map:
                        fs.mkdir(name=name)
                else:
                    size, name = l.split()
                    size = int(size)
                    fs.touch(name=name, size=size)
            else:
                ops = l.split()
                if len(ops) == 3:
                    _, op, target = ops
                    assert op == 'cd', 'only cd & ls operations are supported by fs.'
                    fs.change_dir(target)
    print(f"File structure:")
    print(fs)
    return sum([v for v in fs.size_map.values() if v <= MAX_SIZE])


file = sys.argv[1]
print(f"fsize: {main(file)}")