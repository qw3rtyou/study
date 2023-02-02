import os

size=os.path.getsize("os_print_os_name.py")

#1000byte=1kb
#1000kb=1mb
def byte_to_mb(size):
    return size//1000000

print("용량: {}MB".format(byte_to_mb(size)))