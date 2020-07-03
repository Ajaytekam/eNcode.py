#!/usr/bin/python3

import argparse
import random

def EncodeStr(Instr):
    encodedStr = ""
    for ch in Instr:
       encodedStr+="&#"+str(ord(ch))+";"
    return encodedStr

def Write(data):
    # generate filename
    rnd = (random.randint(11111,99999))
    Srnd = f'{rnd}'
    filename = "EncodedStr_"+ Srnd + ".txt"
    file = open(filename, "w")
    file.write(data)
    file.close()
    print("Written To File: "+filename)

def main():
    # 
    parser = argparse.ArgumentParser()
    parser.add_argument("String", help="String to encode")
    parser.add_argument("-w", "--write", help="Write Encoded string into a file", action="store_true")
    args = parser.parse_args()
    OPStr = EncodeStr(args.String)
    if args.write:
        Write(OPStr)
    else:
        print(OPStr)
    
if __name__ == "__main__":
    main()
