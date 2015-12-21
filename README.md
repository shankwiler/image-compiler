# image-compiler

### What it does

Adds files vertically, like so:

1.png 

![1](http://i.imgur.com/g9MgjJH.png)

2.png 

![2](http://i.imgur.com/QRNeYvx.png)

3.png 

![3](http://i.imgur.com/JerZP7Q.png)

compilation.png 

![compilation](http://i.imgur.com/zsO75hl.png)

### How to use it

`image-compiler.py` is dependent on Pillow, an image library. 

Get it with `pip install Pillow`

To use the script:

`python3 image-compiler.py file1 file2 file3 file4`

To compile all the files in the directory, assuming they're all images besides the python file:

`python3 image-compiler.py *`