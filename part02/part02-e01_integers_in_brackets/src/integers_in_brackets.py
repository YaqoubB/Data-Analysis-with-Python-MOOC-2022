#!/usr/bin/env python3

import re

def integers_in_brackets(s):
    return [int(i) for i in re.findall(r'\[\s*([+-]?\d+)\s*\]', s)]


def main():
    pass

if __name__ == "__main__":
    main()
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx") )
    #returns [12, -43, 12]. So there can be whitespace between the number and the brackets, but no other character besides those that make up the integer.
