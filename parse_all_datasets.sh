#!/bin/bash

for doc in train test dev; do
    python parse_multitrigger.py \
        -o "mturk_${doc}_output.csv" \
        -b "./datasets/${doc}.jsonl"
done