import zipfile

#compression option makes zipfile compress
with zipfile.ZipFile("data/code_comp.zip",'w',compression=zipfile.ZIP_DEFLATED) as zip:
    zip.write("os_check_file_5mb.py")
    zip.write("shutil_file_duplicate.py")

#decompress zipfile
with zipfile.ZipFile("data/code_comp.zip",'r') as zip:
    zip.extractall("data/decompressed_code")
