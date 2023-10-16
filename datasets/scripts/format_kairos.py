#!/usr/bin/env python3
import json
import argparse

parser = argparse.ArgumentParser(description='Formats KAIROS event roles. Insert roles directly into templates instead of <arg{i}>.')
parser.add_argument('src', type=argparse.FileType(mode = "r"), help='Input file')
parser.add_argument('dest', type=argparse.FileType(mode = "w"), help='Output file')
args = parser.parse_args()

with args.src:
    event_roles = json.load(args.src)

for key, value in event_roles.items():
    template = value['template']
    roles = value['roles']
    for i, role in enumerate(roles, start=1):
        template = template.replace(f"<arg{i}>", f"[{role}]", 1)
    event_roles[key]['template'] = template

with args.dest:
    json.dump(event_roles, args.dest, indent=2)