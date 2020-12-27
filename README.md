# eNcode.py : numeric html encoder

Convert string into HTML encoded value (with numeric values of ascii). It is useful in Web Attacks like HTML/Code Injection.  

Usage :  

```shell  
$ ./eNcode.py -h

usage: encode.py [-h] [-w] String

positional arguments:
    String       String to encode

  optional arguments:
    -h, --help   show this help message and exit
    -w, --write  Write Encoded string into a file
```  

Example :  

```shell   
$ ./eNcode.py "<h1>This is test</h1>"  
&#60;&#104;&#49;&#62;&#84;&#104;&#105;&#115;&#32;&#105;&#115;&#32;&#116;&#101;&#115;&#116;&#60;&#47;&#104;&#49;&#62;


$ ./eNcode.py "<h1>This is test</h1>" -w
Written To File: EncodedStr_11549.txt
```  

