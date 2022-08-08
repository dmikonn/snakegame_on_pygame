# PyImageCompressor

A simple command line image compressor on Python. Takes an local image file and option arguments and returns a file with less size.

## Requirements

- [Python 3](https://www.python.org/)
- [Pillow](https://python-pillow.org/)
- [openpyxl](https://pypi.org/project/openpyxl/) 

## Installation

Clone the repo using this command:

```commandline
git clone https://github.com/dmikonn/py_image_compressor
```

Or just download the [zip](https://github.com/dmikonn/py_image_compressor/archive/master.zip).

Install the dependencies:

```commandline
python -m pip install -r requirements.txt
```
## Usage

At start, either set pycompress as executable, or execute it manually with your python interpreter.

```text
Usage: pycompress [OPTIONS] image [filepath]...

URL:
  Path to file. By default the script is looking for the given filename in the same folder.

Options:

    -h,  --help         show help
    
    -j,  --to-jpg       convert the image to the JPEG format
    
    -q   --quality      set quality of the output image, ranging 
                        from a minimum of 0 (worst) to a maximum of 95 (best); 
                        with 90 set as a default 
    -r   --resize-ratio resizing ratio proportionally, from 0 to 1 
                        (for example, setting it to 0.5 will multiply 
                        width & height of the image by 0.5); 
                        with 1.0 set as default
    -w   --width        forces the new width image, make sure to set it with the "height" parameter
    -hh  --height       forces the new height for the image, make sure to set it with the "width" parameter



For example:

```commandline
pycompress /home/user/Pictures/awesome-cat-picture.jpg
```

This will make a converted copy of the input file with the quality of 90.

Another one:

```commandline
pycompress -j -r 0.4 very-fun-meme.png
```

This will make a converted jpg copy of the input png file with the quality of 90 and scale of 0.4 of the original file resolution.


To run on he multiple files at once, add some bash magic. Like this:
```
$ for i in *.png; do .pycompress -j "$i".png; done
```
This fill iterate through all png files in a folder, compressing them and converting to jpg (the type of job this script was concieved for) 

**Attention**: by default, if the file with output filename exist, it **will be replaced**. Though as the script just copy the input file name and adds "compressed" to it, it's far too marginal sitution to work around.  
