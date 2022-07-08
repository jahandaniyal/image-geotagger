# image-geotagger
A simple Python script to geotag images.

Uses the following packages:
- [pyexiv2](https://github.com/LeoHsiao1/pyexiv2)
- [Rational](https://github.com/escaped/pyexiv2/blob/69dd6448f9831bd826137b7519f9d797b23ab4ec/src/pyexiv2/utils.py#L170) - Author: **Olivier Tilloy** (olivier@tilloy.net)

Please check [Olivier Tilloy's repository](https://github.com/escaped/pyexiv2) which supports additional EXIF operations.

## Build instructions

This package uses poetry to build and maintain dependencies.

Make sure you have installed [poetry](https://python-poetry.org/docs/) before proceeding.

`poetry install`

`poetry shell`

## Installation
**[This is currently in pre-production stage]**

`pip install https://github.com/jahandaniyal/image-geotagger/releases/download/v0.1.0/geotagger-0.1.0-py3-none-any.whl`

## Usage
- Create a folder and name it *samples*
- add an image file and name it *img.jpg*

```python
from geotagger import set_gps_metadata, read_exif_data

# set_gps_metadata(<img_file_path>, lat, lon)
# read_exif_data(<img_file_path>)
# Example,
import pprint

set_gps_metadata("samples/img.jpg", 52.49031917252815, 13.226391594484367)
pprint.pprint(read_exif_data("samples/img.jpg"))

```