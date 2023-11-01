from X3Dpackage import *
X3D0 = X3D()
X3D0.profile = "Interchange"
X3D0.version = "3.0"

head1 = head()

meta2 = meta()
meta2.content = "gridBack.x3d"
meta2.name = "title"
head1.addMeta([meta2])

meta3 = meta()
meta3.content = "Checkerboard grid background for X3D/VRML materials selection."
meta3.name = "description"
head1.addMeta([meta3])

meta4 = meta()
meta4.content = "David Roussel"
meta4.name = "creator"
head1.addMeta([meta4])

meta5 = meta()
meta5.content = "James Harney, Don Brutzman NPS"
meta5.name = "translator"
head1.addMeta([meta5])

meta6 = meta()
meta6.content = "8 April 2002"
meta6.name = "created"
head1.addMeta([meta6])

meta7 = meta()
meta7.content = "12 January 2014"
meta7.name = "modified"
head1.addMeta([meta7])

meta8 = meta()
meta8.content = "http://vrmlstuff.free.fr/materials"
meta8.name = "reference"
head1.addMeta([meta8])

meta9 = meta()
meta9.content = "Universal Media Material Library"
meta9.name = "subject"
head1.addMeta([meta9])

meta10 = meta()
meta10.content = "http://www.web3d.org/x3d/content/examples/Basic/UniversalMediaMaterials/gridBack.x3d"
meta10.name = "identifier"
head1.addMeta([meta10])

meta11 = meta()
meta11.content = "Vrml97ToX3dNist, http://ovrt.nist.gov/v2_x3d.html"
meta11.name = "generator"
head1.addMeta([meta11])

meta12 = meta()
meta12.content = "../license.html"
meta12.name = "license"
head1.addMeta([meta12])
X3D0.head = head1

Scene13 = Scene()

Shape14 = Shape()

Appearance15 = Appearance()

Material16 = Material()
Material16.ambientIntensity = 0.01
Material16.diffuseColor = [1.0,1.0,1.0]
Material16.shininess = 0.05
Appearance15.material = Material16
Shape14.appearance = Appearance15

IndexedFaceSet17 = IndexedFaceSet(colorIndex = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], colorPerVertex = False, coordIndex = [0,8,9,1,-1,1,9,10,2,-1,2,10,11,3,-1,3,11,12,4,-1,4,12,13,5,-1,5,13,14,6,-1,6,14,15,7,-1,8,16,17,9,-1,9,17,18,10,-1,10,18,19,11,-1,11,19,20,12,-1,12,20,21,13,-1,13,21,22,14,-1,14,22,23,15,-1,16,24,25,17,-1,17,25,26,18,-1,18,26,27,19,-1,19,27,28,20,-1,20,28,29,21,-1,21,29,30,22,-1,22,30,31,23,-1,24,32,33,25,-1,25,33,34,26,-1,26,34,35,27,-1,27,35,36,28,-1,28,36,37,29,-1,29,37,38,30,-1,30,38,39,31,-1,32,40,41,33,-1,33,41,42,34,-1,34,42,43,35,-1,35,43,44,36,-1,36,44,45,37,-1,37,45,46,38,-1,38,46,47,39,-1,40,48,49,41,-1,41,49,50,42,-1,42,50,51,43,-1,43,51,52,44,-1,44,52,53,45,-1,45,53,54,46,-1,46,54,55,47,-1,48,56,57,49,-1,49,57,58,50,-1,50,58,59,51,-1,51,59,60,52,-1,52,60,61,53,-1,53,61,62,54,-1,54,62,63,55,-1], normalPerVertex = False)

Coordinate18 = Coordinate()
Coordinate18.point = [-5.25,5.25,0.0,-3.75,5.25,0.0,-2.25,5.25,0.0,-0.75,5.25,0.0,0.75,5.25,0.0,2.25,5.25,0.0,3.75,5.25,0.0,5.25,5.25,0.0,-5.25,3.75,0.0,-3.75,3.75,0.0,-2.25,3.75,0.0,-0.75,3.75,0.0,0.75,3.75,0.0,2.25,3.75,0.0,3.75,3.75,0.0,5.25,3.75,0.0,-5.25,2.25,0.0,-3.75,2.25,0.0,-2.25,2.25,0.0,-0.75,2.25,0.0,0.75,2.25,0.0,2.25,2.25,0.0,3.75,2.25,0.0,5.25,2.25,0.0,-5.25,0.75,0.0,-3.75,0.75,0.0,-2.25,0.75,0.0,-0.75,0.75,0.0,0.75,0.75,0.0,2.25,0.75,0.0,3.75,0.75,0.0,5.25,0.75,0.0,-5.25,-0.75,0.0,-3.75,-0.75,0.0,-2.25,-0.75,0.0,-0.75,-0.75,0.0,0.75,-0.75,0.0,2.25,-0.75,0.0,3.75,-0.75,0.0,5.25,-0.75,0.0,-5.25,-2.25,0.0,-3.75,-2.25,0.0,-2.25,-2.25,0.0,-0.75,-2.25,0.0,0.75,-2.25,0.0,2.25,-2.25,0.0,3.75,-2.25,0.0,5.25,-2.25,0.0,-5.25,-3.75,0.0,-3.75,-3.75,0.0,-2.25,-3.75,0.0,-0.75,-3.75,0.0,0.75,-3.75,0.0,2.25,-3.75,0.0,3.75,-3.75,0.0,5.25,-3.75,0.0,-5.25,-5.25,0.0,-3.75,-5.25,0.0,-2.25,-5.25,0.0,-0.75,-5.25,0.0,0.75,-5.25,0.0,2.25,-5.25,0.0,3.75,-5.25,0.0,5.25,-5.25,0.0]
IndexedFaceSet17.coord = Coordinate18

Color19 = Color()
Color19.color = [0.5,0.5,0.5,0.75,0.75,0.75]
IndexedFaceSet17.color = Color19
Shape14.geometry = IndexedFaceSet17
Scene13.addChildren([Shape14])
X3D0.scene = Scene13
