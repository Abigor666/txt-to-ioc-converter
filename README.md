# txt-to-ioc-converter
Import hashes from txt file to OpenIOC 1.1 format
usage: ioc-converter.py [-h] -f FILE -type {md5,sha256} output

Convert list of hashes in OpenIOC 1.1.

positional arguments:
  output                output file OpenIOC

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  input file with hashes
  -type {md5,sha256}, --hash_type {md5,sha256}
                        hash type (md5 or sha256)
