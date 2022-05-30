import os

band = 'b8a'
date = '20220404'
tmp = date + "/"

os.system(f'python download_file.py --band {band} --date {date} --dest {tmp}')