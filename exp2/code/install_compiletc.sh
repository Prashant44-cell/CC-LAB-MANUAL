#!/bin/sh
# Commands executed inside TinyCore Linux VM terminal

# Step 1: Download and install GCC compiler package
tc@box:~$ tce-load -wi compiletc

# Step 2: Open text editor and write C code
tc@box:~$ sudo editor demo.c

# Step 3: Compile C program using cc
tc@box:~$ cc demo.c -o demo

# Step 4: Execute compiled binary
tc@box:~$ ./demo
