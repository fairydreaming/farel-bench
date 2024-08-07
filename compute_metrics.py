#!/usr/bin/env python3

import os
import re
import sys
import pandas as pd
import argparse

def extract_accuracy_values(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    accuracy_values = {}
    for line in reversed(lines):
        match = re.match(r'([ \w]+):\s([\d.]+)', line)
        if match:
            class_name, accuracy = match.groups()
            accuracy_values[class_name] = float(accuracy)
        elif line.strip() == '':
            break
    
    # reverse the order of family relationships since we read them from last to first
    return { key: accuracy_values[key] for key in reversed(list(accuracy_values.keys())) }

def process_logs(directory):
    log_files = [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files if file.endswith('.log')]
    data = []
    for file_path in log_files:
        accuracy_values = extract_accuracy_values(file_path)
        data.append(accuracy_values)
    
    df = pd.DataFrame(data, index=[os.path.basename(log_file).replace(".log", "") for log_file in log_files])
    df.insert(loc = 0, column = 'FaRel', value = df.mean(axis=1).round(2))
    df = df.sort_values(['FaRel'], ascending=False)
    df = df.reset_index(names='Model')
    df.insert(loc = 0, column = 'Nr', value = df['FaRel'].rank(method='min', ascending=False).astype('int32'))
    
    return df

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="Directory containing farel-bench log files.")
args = parser.parse_args()

directory = args.dir
result_df = process_logs(directory)
result_df.columns = map(lambda c: c.replace("grand", "grand-"), result_df.columns)
print(result_df.to_markdown(floatfmt=".2f", index=False))

