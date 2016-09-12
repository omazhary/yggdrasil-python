#!/usr/bin/env python

import json

class TupleInput :
    """This class represents the set of data that a user can input for analysis"""

    data = None

    def __init__(self, input_mode, input_string = "", input_file = ""):

        if input_string == "" and input_file != "" and input_file.endswith("json"):
            with open(input_file) as json_file:
                input_string = json_file.read()
        self.data = self.parse_from_json(input_string)

    def parse_from_json(self, json_string):
        """This function should convert a json string to an array of dictionaries representing tuples"""
        return json.loads(json_string)

class Node:
    """This class represents a generic node in a tree"""

    data = None
    children = None
    level = None

    def __init__(self, value, new_level = 0):
        self.data = value
        self.children = []
        self.level = new_level

    def add_child(self, child):
        """Add a child to this node"""
        self.children.append(child)

    def remove_child(self, child):
        """Recursively remove children if there are any, if not, remove the requested child"""
        if len(child.children) == 0:
            self.children.remove(child)
        else:
            for element in child.children:
                child.remove_child(element)

class Tree:
    """This class represents a generic tree"""

    root_node = None

    def __init__(self, root):
        self.root_node = root

    def traverse(self):
        nodes = [self.root_node]
        for child in nodes:
            print (child.level * "\t") + child.data
            for grandchild in child.children:
                nodes.insert(nodes.index(child) + 1, grandchild)


if __name__ == "__main__":
    print "Welcome to Yggdrasil!!"
    print "Reading your data..."
    #input_source = TupleInput("file", "", "test.json")
    root = Node("great-grandpa")
    tree = Tree(root)
    grandpa = Node("gramps", 1)
    grandpa.add_child(Node("pops", 2))
    grandpa.add_child(Node("auntie", 2))
    grandpa.children[0].add_child(Node("brother", 3))
    grandpa.children[0].add_child(Node("me!", 3))
    grandpa.children[1].add_child(Node("cousin", 3))
    root.add_child(grandpa)
    tree.traverse()
