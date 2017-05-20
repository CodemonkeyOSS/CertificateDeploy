import platform
import os

def main():
	fsDir = checkOS();

	# print fsDir;	
	if(len(fsDir) > 0): statDirs(fsDir);
	

# Checks the OS and sets the fsDir variable
def checkOS():
	OSstring = platform.platform()

        # Checks for CentOS
	if "centos" in OSstring: print "centos found!"; return  "/opt/certdeploy";

# Checks for necessary directories and creates them if needed
def statDirs(fsDir):
	if(os.path.exists(fsDir)):
		print fsDir+" does exist";
		if(os.path.isdir(fsDir)):
			print fsDir+" is a directory";
		else: print fsDir+" is not a directory";
	else: 
		print '{} does not exist, creating it now'.format(fsDir);
		makeDirs(fsDir);		

def makeDirs(targetDir):
	try:
		os.makedirs(fsDir);
	except OSError:
		if not os.path.isdir(fsDir):
			raise;

main();
