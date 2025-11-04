# threading in python 
# Download Manager Demo


import threading
import time

def download_file(file_name):
    print(f"start downloading {file_name}")
    time.sleep(2)
    print(f"finished downloading {file_name}")

files = ['a.zip','b.zip', 'c.zip']
threads = []

for f in files:
    t = threading.Thread(target=download_file, args=(f,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All files download finished")