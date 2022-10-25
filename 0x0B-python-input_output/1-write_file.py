#!/usr/bin/python3
'''
Contains write_file module
'''

def write_file(filename="", text=""):
    with open('filename', 'w', encoding='utf-8') as f:
        return f.write(text)
