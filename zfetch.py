#!/usr/bin/env python

""" Script to download video files from zcam cameras """
import sys
import wget
import requests
import pathlib

IP = "10.98.32.1"
argc = len(sys.argv)

if argc == 2:
    DCIM = sys.argv[1]
elif argc == 3:
    IP = sys.argv[1]
    DCIM = sys.argv[2]
else:
    print("Usage: zfetch.py <IP> <DCIM>")
    sys.exit(1)

URL = f"http://{IP}/DCIM/{DCIM}"
response = requests.get(URL)
files = response.json()["files"]

files_count = len(files)
for i in range(0, files_count):
    file = files[i]
    print(f"\nDownload: {file} {i+1}/{files_count}")
    if pathlib.Path(file).is_file():
        print("File f{file} exists")
        continue
    url = f"http://{IP}/DCIM/{DCIM}/{file}"
    response = wget.download(url)
