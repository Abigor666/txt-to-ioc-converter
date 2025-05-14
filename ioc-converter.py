import argparse
import uuid
from datetime import datetime

def read_hashes(file_path):
    """Reads hashes from the specified file and returns them as a list."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def create_indicator_items(hashes, hash_type):
    """Creates indicator items for the list of hashes."""
    indicator_items = []
    for h in hashes:
        item = f"""
        <IndicatorItem id="{uuid.uuid4()}" condition="is" negate="false" preserve-case="false">
          <Context document="FileItem" search="FileItem/{hash_type}sum" type="mir" />
          <Content type="{hash_type}">{h}</Content>
        </IndicatorItem>
        """
        indicator_items.append(item.strip())
    return "\n".join(indicator_items)

def create_openioc_format(hashes, hash_type):
    """Creates OpenIOC content based on the hashes."""
    unique_id = str(uuid.uuid4())
    last_modified = datetime.now().isoformat()
    short_description = f"Hashes of type {hash_type.upper()}"
    description = f"List of {hash_type.upper()} hashes"
    authored_date = last_modified

    indicator_items = create_indicator_items(hashes, hash_type)

    return f"""<?xml version="1.0" encoding="utf-8"?>
<OpenIOC published-date="0001-01-01T00:00:00" id="{unique_id}" last-modified="{last_modified}" xmlns="http://openioc.org/schemas/OpenIOC_1.1" xmlns:old="http://schemas.mandiant.com/2010/ioc" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <metadata>
    <short_description>{short_description}</short_description>
    <description>{description}</description>
    <keywords></keywords>
    <authored_date>{authored_date}</authored_date>
    <links />
  </metadata>
  <criteria>
    <Indicator operator="OR" id="{uuid.uuid4()}">
      {indicator_items}
    </Indicator>
  </criteria>
  <parameters />
</OpenIOC>
"""

def write_ioc_file(output_path, ioc_content):
    """Writes OpenIOC content to the specified output file."""
    with open(output_path, 'w') as file:
        file.write(ioc_content)

def main():
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description='Convert hash lists to OpenIOC format.')
    parser.add_argument('-f', '--file', required=True, help='Input file with hashes')
    parser.add_argument('-type', '--hash_type', required=True, choices=['md5', 'sha256'], help='Type of hash (md5 or sha256)')
    parser.add_argument('output', help='Output OpenIOC file')

    args = parser.parse_args()

    # Read hashes from the file
    hashes = read_hashes(args.file)
    # Create OpenIOC content
    ioc_content = create_openioc_format(hashes, args.hash_type)
    # Write content to the output file
    write_ioc_file(args.output, ioc_content)

if __name__ == '__main__':
    main()
