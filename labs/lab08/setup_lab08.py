import requests
import zipfile
import py_compile
import os

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

def unzip(zipped_file, target_dir='.'):
    with zipfile.ZipFile(zipped_file,'r') as zip_ref:
        zip_ref.extractall(target_dir)

if __name__ == "__main__":
    urlbase = "https://raw.githubusercontent.com"
    repository = "gordon-cs/cps121/main/labs/lab08"
    zip = "lab08-src.zip"
    download_url(f"{urlbase}/{repository}/{zip}", zip)
    unzip(zip)
    f = "dotests.py"
    py_compile.compile(f, f+'c')
    os.remove(f)
    os.remove(zip)
