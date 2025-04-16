import os,stat
import re

# A script in a build process needs to update the build version number in 2
# locations.
# - The version number will be in an environment variable "BuildNum"
# - The files to be modified will be under "$SourcePath/develop/global/src"
# directory
# - The "SConstruct" file has a line "point=123," (where 123
# (just an example) should be updated with the value of "BuildNum"
# Environment variable)
# - The "VERSION"file has a line "ADLMSDK_VERSION_POINT= 123" (where 123
# (just an example) should be updated with the value of "BuildNum"
# Environment variable)


def updateSconstruct():
    """Update the build number in the SConstruct file"""
    path = os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct") 
    updatePath = os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct1")
    updateBuildNum = os.environ["BuildNum"]

    # not sure of the mode required
    os.chmod(path, stat.S_IWUSR)

    fin = open(path, 'r')
    fout = open(updatePath, 'w')

    for line in fin:
        newLine=re.sub("point\=[\d]+","point="+updateBuildNum,line)
        fout.write(newLine)

    fout.close()    
    os.remove(path)
    os.rename(updatePath, path)

def updateVersion():
    """Update the build number in the VERSION file"""
    path = os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION")
    updatePath = os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION1")
    updateBuildNum = os.environ["BuildNum"]

    # not sure of the mode required
    os.chmod(path, stat.S_IWUSR)

    fin = open(path, 'r')
    fout = open(updatePath, 'w')

    for line in fin:
        newLine=re.sub("ADLMSDK_VERSION_POINT=[\d]+","ADLMSDK_VERSION_POINT="+updateBuildNum,line)
        fout.write(newLine)

    fout.close()
    os.remove(path)
    os.rename(updatePath, path)


def main():
    updateSconstruct()
    updateVersion()
    main()