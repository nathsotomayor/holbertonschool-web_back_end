#!/usr/bin/env python3
"""
0x04-pagination
Holberton Web Stack programming Spec ― Back-end
"""
import requests

URL = 'https://holbertonintranet.s3.amazonaws.com/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210323%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210323T153049Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c5260561b2d189b5f12e07c9335c378aa2048e69c515803e57c78ed20e894b32'

DATA_FILE = "Popular_Baby_Names.csv"


def download_csv(URL: str, FILENAME: str):
    """
    Helper method that downloads csv data from URL
    and saves content in to a file
    """
    req = requests.get(URL)
    content = req.content
    with open(DATA_FILE, 'wb') as csv_file:
        csv_file.write(content)


download_csv(URL, DATA_FILE)
