# feh-spritesheet-converter
Transforms FEH spritesheets into separated images

## Requirements
`webptools` must be installed: https://pypi.org/project/webptools/

## Usage
.plist and .png files should be put into the input folder
Example input folder (using Item and Item_2 from assets/Common/UI:
```
input/
	* Item.plist
	* Item.png
	* Item_2.plist
	* Item_2.png
main.py
```

Separated images are exported into the output folder

Run using `py/python main.py`