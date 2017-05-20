import platform
import os

OSstring = "";
fsDir = "";

def checkOS():
	OSstring = platform.platform()

	if "centos-7" in OSstring:
        	fsDir = "/opt/certdeploy"
		print OSstring;
		print fsDir;
        	return "centos-7";

def checkDir():
	if(os.path.exists(fsDir)):
		print fsDir+" does exist";
		if(os.path.isdir(fsDir)):
			print fsDir+" is a directory";
		else: print fsDir+" is not a directory";
	else: print fsDir+" does not exist";		

checkOS();
checkDir();
