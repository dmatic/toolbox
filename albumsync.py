import exifread
import os

sourcedir = ""
ext = ".jpg"

for arg in sys.argv:
    if arg[:10] == "sourcedir:":
        sourcedir = arg[10:]
    if arg[:4] == "ext:":
        sourcedir = arg[4:]


if sourcedir == "":
	print("sourcedir missing")
	exit()

if ext == "":
	print("ext")
	exit()


files = os.listdir(sourcedir)

for file in files:
	if os.path.splitext(file.lower())[1] == ext:
		with open(os.path.join(sourcedir, file), 'rb') as fh:
		    tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
		    dateTaken = tags["EXIF DateTimeOriginal"]

		newname = str(dateTaken)[:4] + str(dateTaken)[5:7] + str(dateTaken)[8:10] + str(dateTaken)[11:13] + str(dateTaken)[14:16] + str(dateTaken)[17:19] + ext

		print (file + " -> " + newname)
		os.rename(os.path.join(sourcedir, file), os.path.join(sourcedir, newname))


		    

