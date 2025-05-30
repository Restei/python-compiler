# PYTHON COMPILER PROJECT

This project is a Python implementation of the front-end part of a compiler. It generates a Abstract Syntaxic Tree (AST) in an HTML file.

## Features

This compiler makes a lexical and syntaxical analysis of a mini python file and then generates the output in an HTML file called AST using mermaid script.

## Installing & Running

Project developped using Python 3.11.9
Install requirements:

``` bash  
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

To run the compiler, you need to add the file you need to compile in the directory mini_python and set the variable fichier to \<filename> in main.py then execute :

``` bash
$ python3 main.py
 ```
