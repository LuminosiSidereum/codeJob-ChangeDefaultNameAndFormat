# Change the Default Name of Picutres
### Short description of the program
Changes the default name of pictures in the working directory into the format: `picutreName-YYMMDD_consecutiveNumer`

The `pictureName` and the date can be edited seperatly.
Only the files ending with
- jpg
- jpeg
- png
- gif
- tif, tiff
- mov
- mp4
- avi

are renamed.

Additionally the files in the heic format are converted into tiff format.
The original heic files are not deleted.
Instead they are moved into the subdircetory **"Orginaldateien (HEIC)"**.

The working directory is always set to the directory of the python script.
