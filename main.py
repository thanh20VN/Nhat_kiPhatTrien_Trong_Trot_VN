import csv
import json
from menudk import *

with open("data/user.json", "r") as f:
    us = json.load(f)

ab = []
with open("data/tree.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        ab.append(row)

dkdn(us,ab)

