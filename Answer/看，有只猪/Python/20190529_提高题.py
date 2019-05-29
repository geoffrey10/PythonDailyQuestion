#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


def word_counter(file_path):
    counter = {}
    if not os.path.exists(file_path):
        print(f"the file {file_path} is not exist")
    with open(file_path, 'r') as file:
        for line in file.readlines():
            for word in line:
                if word.isspace():
                    continue
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1

    for word, count in counter.items():
        print(f"{word}:{count}")
