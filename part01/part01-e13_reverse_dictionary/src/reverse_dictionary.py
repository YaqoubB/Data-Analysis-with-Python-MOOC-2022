#!/usr/bin/env python3

def reverse_dictionary(d):
    d1 = {}
    for key, value in d.items():
        if len(value) == 1:
            value = value[0]
            if value not in d1:
                d1[value] = [key]
            else:
                d1[value].append(key)
        else:
            for i in value:
                if i not in d1:
                    d1[i] = [key]
                else:
                    d1[i].append(key)
    return d1

def main(d):
    return reverse_dictionary(d)

if __name__ == "__main__":
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(main(d))
