#!/usr/bin/env python3

def word_frequencies(filename):
    result = {}
    with open(filename, "r") as my_file:
        for line in my_file:
            line = line.split()
            for word in line:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if word in result:
                    result[word] += 1
                else:
                    result[word] = 1
    return result

def main():
    pass

if __name__ == "__main__":
    main()
    word_frequencies(filename="src/alice.txt")
