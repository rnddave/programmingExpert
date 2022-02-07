"""
File System Implementation
_+_+_+_+_+_+_+_+_+_+_+_+_+_

Implement simple [FileSystem] class that mimic the way computer FileSystem works.

Tree-like structure composed of nodes, each of which is either a [File] or a [Directory]

[File] = [name] and [contents]
-- [write] method
-- override the [__len__] dunder method which returns the number of characters in that file 

[Directory] = [name] and [children] 
-- [children] is a directory that stores the name of it's children nodes as {keys} and the nodes themselves as {values}
-- Direcotries have the [add] and [delete] method 

for convenience [__str__] of each class have been provided to begin

following: 
- [create_directory(path)] = create a [Directory] inside [FileSystem] at location specified
-- if path is malformed or impossible, raise a [ValueError] 

- [read_file(path)] = return contents of a file at the path provided 
-- if no file at location specified, the raise [ValueError]

- [delete_directory_or_file(path)] = delete node located at [path]
-- should work on files and directories
-- if no node at specified [path] then raise [ValueError]

- [size()] = return number of characters across all files in your [FileSystem]

- [find_bottom_node(node_names)] = private helper method
-- take a list of node names
-- traverse [FileSystem] downwards until last node in list

-------------

all methods accepting [path] need to validate the [path]

"""

class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        # Write your code here.
        pass

    def create_file(self, path, contents):
        # Write your code here.
        pass

    def read_file(self, path):
        # Write your code here.
        pass

    def delete_directory_or_file(self, path):
        # Write your code here.
        pass

    def size(self):
        # Write your code here.
        pass

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")


    def _find_bottom_node(self, node_names):
        # Write your code here.
        pass


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)


"""
 _+_+_+_+_ STARTING CODE +_+_+_+_+

class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        # Write your code here.
        pass

    def create_file(self, path, contents):
        # Write your code here.
        pass

    def read_file(self, path):
        # Write your code here.
        pass

    def delete_directory_or_file(self, path):
        # Write your code here.
        pass

    def size(self):
        # Write your code here.
        pass

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")


    def _find_bottom_node(self, node_names):
        # Write your code here.
        pass


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)

"""
