import os
import sys
if sys.argv[2][0]=='-':
    path=sys.argv[3]
    dirs=os.listdir(path)
    for file in dirs:
        filename=os.path.join(path,file)
        os.system(sys.argv[1]+" "+ sys.argv[2]+" "+filename+ " " + sys.argv[4] +file)
else:
    path=sys.argv[2]
    dirs=os.listdir(path)
    for file in dirs:
        filename=os.path.join(path,file)
        os.system(sys.argv[1]+" "+filename+ " " + sys.argv[3] +file)