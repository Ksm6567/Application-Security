import sys
import os
import psutil
import config

import subprocess

def test_build(file_name):
    try:
        result = subprocess.run(['python', file_name], check=True)
        print(f'{file_name} 빌드 성공')
    except subprocess.CalledProcessError:
        print(f'{file_name} 빌드 실패')

if __name__ == "__main__":
    test_build('test\\unitest_ftp.py')
    # test_build('test\\unitest_db.py')