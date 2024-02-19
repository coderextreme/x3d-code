#!env py
import os
import sys

classpath = argv[0]

for oneFileName in sys.argv[1:]:
    print(f"{oneFileName}")
    os.system(f"java -cp {classpath} net.sf.saxon.Transform -warnings:recover -expand:on -s:{oneFileName}.x3d -o:{oneFileName}.py -xsl:../X3dToPython.xslt")
    # insertPackagePrefix={insertPackagePrefix}")
