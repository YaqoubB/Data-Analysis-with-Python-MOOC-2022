#!/usr/bin/env python3

import re

def file_extensions(filename):
    file_list = []
    ext_dict = {}
    with open(filename, "r") as my_file:
        for line in my_file:
            line = line.strip()
            ext = re.search(r'\.([A-Za-z0-9]+)$', line)
            if ext:
                ext = ext.group(1)
                if ext in ext_dict:
                    ext_dict[ext].append(line)
                else:
                    ext_dict[ext] = []
                    ext_dict[ext].append(line)
            else:
                file_list.append(line)  

    return (file_list, ext_dict)

def main():
    dict_list = []
    file, dict = file_extensions("src/filenames.txt")
    print(f'{len(file)} files with no extension')
    for key, value in sorted(dict.items()):
        print(f'{key} {len(value)}')
        

if __name__ == "__main__":
    main()
    #print(file_extensions(filename="src/filenames.txt"))

