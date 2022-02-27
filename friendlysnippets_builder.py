#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
friendly snippets generator

__Author__ = snakesgun
__Version__ = 1.0
__Maintainer__ = snakesgun
__Email__ = snakesgun@gmail.com
__Status__ = Dev
__Date__ = 2022-02-27
"""
import argparse
import json

parser = argparse.ArgumentParser(
    description='gitignore snippets generator for friendly snippets')
parser.add_argument('input', help='input ignore file')
parser.add_argument('output', help="output snippets")
parser.add_argument('--name', help='template name')


def main():
    args = parser.parse_args()
    with open(args.input, 'r', encoding='utf-8') as input_file:
        inline = input_file.read()
        template_dict = {
            args.name: {
                "perfix": args.name,
                "body": [
                    inline
                ],
                "description": "{} Gitignore Templat".format(args.name)
            }
        }
    with open(args.output, 'w', encoding='utf-8') as output_file:
        json.dump(template_dict, output_file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
