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
    log_files = [file for file in os.listdir(directory) if file.endswith('.log')]
    data = []
    for file in log_files:
        file_path = os.path.join(directory, file)
        accuracy_values = extract_accuracy_values(file_path)
        print(accuracy_values)
        data.append(accuracy_values)
    
    df = pd.DataFrame(data, index=[log_file.replace(".log", "") for log_file in log_files])
    df.insert(loc = 0, column= 'FaRel', value = df.mean(axis=1))
    df = df.sort_values(['FaRel'], ascending=False)
    
    return df

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="Directory containing farel-bench log files.")
args = parser.parse_args()

directory = args.dir
result_df = process_logs(directory)
print(result_df.reset_index(names=['Model']).to_markdown(floatfmt=".2f"))

