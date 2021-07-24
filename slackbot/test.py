<code><source lang="python">
def BuildFileList(path, mask, flist):
	import os
	lPath = path
	lsFiles =  os.listdir(lPath)
	for f in lsFiles:
	        fName = path + '\\' + f 
		if (os.path.isdir(fName)):
			BuildFileList(fName, mask, flist)
		else:
			if (fName.find(mask) >= 0):
				flist.append(fName)
</source></code>