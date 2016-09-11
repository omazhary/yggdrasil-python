#!/usr/bin/env python

import json

class TupleInput :
    """This class represents the set of data that a user can input for analysis"""
    data = None

    def __init__(self, input_mode, input_string = "", input_file = ""):
        print "This is the constructor!!"
        if input_string == "" and input_file != "" and input_file.endswith("json"):
            with open(input_file) as json_file:
                input_string = json_file.read()
        self.data = self.parse_from_json(input_string)

    def parse_from_json(self, json_string):
        """This function should convert a json string to an array of dictionaries representing tuples"""
        return json.loads(json_string)


if __name__ == "__main__":
    print "Welcome to Yggdrasil!!"
    print "Reading your data..."
    input_source = TupleInput("file", "", "test.json")
    print input_source.data['tuples'][3]['tc2']
