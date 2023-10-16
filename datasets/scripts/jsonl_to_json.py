#!/usr/bin/env python3
import sys
import json

if len(sys.argv) < 2:
    print('Usage: python jsonl_to_json.py <filename>')
    exit(1)
fname = sys.argv[1]
jsonl_file = open(fname, 'r')
json_list = list(jsonl_file)
jsonl_file.close()

obj = [json.loads(entry) for entry in json_list]
json.dump(obj, open(fname.removesuffix('.jsonl') + '.json', 'w'))
