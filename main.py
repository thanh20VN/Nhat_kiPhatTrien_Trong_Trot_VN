import csv
import json
from menudk import *
import os
import urllib.request
import zipfile

duong_dan = "data"

if not os.path.exists(duong_dan):
    url = "https://github.com/thanh20VN/Nhat_kiPhatTrien_Trong_Trot_VN/releases/download/data/data.zip"
    ten_file = "data.zip"
    
    urllib.request.urlretrieve(url, ten_file)

    with zipfile.ZipFile(ten_file, 'r') as zip_ref:
        zip_ref.extractall(".")
    os.remove('data.zip')

with open("data/user.json", "r") as f:
    us = json.load(f)

ab = []
with open("data/tree.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        ab.append(row)

dkdn(us,ab)

