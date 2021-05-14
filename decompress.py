i = 999
while i > 0:
	

	import os, tarfile, zipfile, pathlib, fnmatch, py7zr

	name = "decompress"
	filename = "%s%d" % (name, i,)
	tarext = "tar.gz"
	zipext = "zip"
	sevenzipext = "7z"
	tar_file = "%s%d.%s" % (name, i, tarext)
	zip_file = "%s%d.%s" % (name, i, zipext)
	sevenzip_file = "%s%d.%s" % (name, i, sevenzipext)
	dir_path = './'
	#tarpath = os.path.join(dir_path, tar_file)
	#zippath = os.path.join(dir_path, zip_file)
	#filepath = os.path.join(dir_path, filename)


#using FNMATCH
	for filename in os.listdir('./'):
		if fnmatch.fnmatch(filename, '*.tar.gz'):
			my_file = tarfile.open(filename)
			my_file.extractall()
			my_file.close()
			os.remove(filename)
			print ("extracting", (tar_file))
		elif fnmatch.fnmatch(filename, '*.zip'):
			my_file = zipfile.ZipFile(filename)
			my_file.extractall()
			my_file.close()
			os.remove(filename)
			print ("extracting", (zip_file))
		elif fnmatch.fnmatch(filename, '*.7z'):
			my_file = py7zr.SevenZipFile(filename)
			my_file.extractall()
			my_file.close()
			os.remove(filename)
			print ("extracting", (sevenzip_file))


	i = i - 1


#using ENDSWITCH (error that .endswitch is not defined)

#	for filename in os.listdir('./'):
#		if filename.endswitch('.tar.gz'):
#			my_file = tarfile.open(tarpath)
#			my_file.extractall()
#			my_file.close()
#		elif filename.endswitch('.zip'):
#			myfile = zipfile.ZipFile(zippath)
#			my_file.extractall()
#			my_file.close()

#using REGEX
