#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project: Checking for Properly Nested Brackets

Description: Looking to make sure brackets of different types are nested properly. if they are return YES if not return NO with index number of issue

ex: [] , {} , () , <> , (**)

answer should look like
Yes
NO 6  (index of issue)

Author: Aaron Jackson
Github: TimeApollo
"""
__author__ = '__TimeApollo__'

# used for testing in the main function
answers_list = [
    'NO 6',
    'YES',
    'NO 17',
    'YES',
    'NO 10',
    'NO 17',
    'NO 6',
    'YES',
    'YES',
    'YES',
    'NO 13',
    'YES'
]

# helper dictionary for looking up what character should be found
bracket_close_dict = {
    ")": "(",
    "*)": "(*",
    ">": "<",
    "}": "{",
    "]": "[" 
}

# helper list to see if character is being looked for
bracket_open_list = [
   '(',
   '(*',
   '<',
   '{',
   '['
]

import sys
import itertools

def bracket_list_creator( text_line ):
    """splits string into a list of each char. (* or *) count as single char"""
    split_text = list(text_line)
    text_line = []
    while len(split_text):
        if split_text[0] != '*':
            if split_text[0] == '(' and split_text[1] == '*': 
                single = split_text.pop(0) + split_text.pop(0)
                text_line.append(single)
            else:
                text_line.append(split_text.pop(0))
        else:
            if len(split_text) > 1 and split_text[1] == ')':
                single = split_text.pop(0) + split_text.pop(0)
                text_line.append(single)
            else:
                text_line.append(split_text.pop(0))
    return text_line

def check_brackets( text_line ):
    """makes FILO stack of opening brackets as they are found."""
    """if closing bracket found, checks if it is match to top item in stack"""
    """if match, deletes from stack, else it returns NO with index of error location"""
    """if all match, returns YES"""
    text_line = bracket_list_creator( text_line )
    bracket_open_stack = []

    for index , char in enumerate(text_line , 1):
        if char in bracket_open_list:
            bracket_open_stack.append(char)
        elif char in bracket_close_dict:
            if bracket_close_dict[char] == bracket_open_stack[-1]:
                del bracket_open_stack[-1]
            else:
                return 'NO ' + str(index)
        else:
            continue
    
    if len(bracket_open_stack):
        return 'NO ' + str(len(text_line) + 1)

    return 'YES'

def main():
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print('usage: python brackets.py file-to-read  { --test }')
        sys.exit(1)

    with open( sys.argv[1] , 'r' ) as text:
        text_lines = [line.rstrip() for line in text]
    # for testing
    if len(sys.argv) == 3:
        for line , answer in itertools.izip(text_lines , answers_list):
            print('input: {}    Expected: {}     Got: {}'.format(line , answer , check_brackets(line)))
    # for actual running
    else:
        for line in text_lines:
            print(check_brackets(line))
    
    
        

if __name__ == '__main__':
    main()
