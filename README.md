# txt-to-ioc-converter
Import hashes from txt file to OpenIOC 1.1 format

## Usage
```
usage: ioc-converter.py [-h] -f FILE -type {md5,sha256} output
positional arguments:
output                output file OpenIOC

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  input file with hashes
    -type {md5,sha256}, --hash_type {md5,sha256}
                          hash type (md5 or sha256)
```
### Example
`python3 ioc-converter.py -f hashes.txt -type md5 myiocfile.ioc`
