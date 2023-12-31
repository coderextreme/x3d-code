from X3Dpackage import *
X3D0 = X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = head()
component2 = component()
component2.setName("Shaders")
component2.setLevel(1)
head1.addComponent(component2)
component3 = component()
component3.setName("CubeMapTexturing")
component3.setLevel(1)
head1.addComponent(component3)
meta4 = meta()
meta4.setName("title")
meta4.setContent("flowers4.x3d")
head1.addMeta(meta4)
meta5 = meta()
meta5.setName("creator")
meta5.setContent("John Carlson")
head1.addMeta(meta5)
meta6 = meta()
meta6.setName("generator")
meta6.setContent("manual")
head1.addMeta(meta6)
meta7 = meta()
meta7.setName("identifier")
meta7.setContent("https://coderextreme.net/X3DJSONLD/flowers4.x3d")
head1.addMeta(meta7)
meta8 = meta()
meta8.setName("description")
meta8.setContent("an animated flower")
head1.addMeta(meta8)
X3D0.setHead(head1)
Scene9 = Scene()
NavigationInfo10 = NavigationInfo()
NavigationInfo10.setType(["EXAMINE","ANY"])
Scene9.addChildren(NavigationInfo10)
Background11 = Background()
Background11.setBackUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"])
Background11.setBottomUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"])
Background11.setFrontUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"])
Background11.setLeftUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"])
Background11.setRightUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"])
Background11.setTopUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])
Scene9.addChildren(Background11)
Transform12 = Transform()
Transform12.setDEF("transform")
Shape13 = Shape()
Appearance14 = Appearance()
Material15 = Material()
Material15.setDiffuseColor([.7,.7,.7])
Material15.setSpecularColor([.5,.5,.5])
Appearance14.setMaterial(Material15)
ComposedCubeMapTexture16 = ComposedCubeMapTexture()
ImageTexture17 = ImageTexture()
ImageTexture17.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"])
ComposedCubeMapTexture16.setBack(ImageTexture17)
ImageTexture18 = ImageTexture()
ImageTexture18.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"])
ComposedCubeMapTexture16.setBottom(ImageTexture18)
ImageTexture19 = ImageTexture()
ImageTexture19.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"])
ComposedCubeMapTexture16.setFront(ImageTexture19)
ImageTexture20 = ImageTexture()
ImageTexture20.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"])
ComposedCubeMapTexture16.setLeft(ImageTexture20)
ImageTexture21 = ImageTexture()
ImageTexture21.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"])
ComposedCubeMapTexture16.setRight(ImageTexture21)
ImageTexture22 = ImageTexture()
ImageTexture22.setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])
ComposedCubeMapTexture16.setTop(ImageTexture22)
Appearance14.setTexture(ComposedCubeMapTexture16)
ComposedShader23 = ComposedShader(language = "GLSL")
ComposedShader23.setDEF("shader")
field24 = field()
field24.setName("cube")
field24.setType("SFInt32")
field24.setAccessType("inputOutput")
field24.setValue("0")
ComposedShader23.addField(field24)
field25 = field()
field25.setName("chromaticDispertion")
field25.setAccessType("inputOutput")
field25.setType("SFVec3f")
field25.setValue("0.98 1.0 1.033")
ComposedShader23.addField(field25)
field26 = field()
field26.setName("bias")
field26.setType("SFFloat")
field26.setAccessType("inputOutput")
field26.setValue("0.5")
ComposedShader23.addField(field26)
field27 = field()
field27.setName("scale")
field27.setType("SFFloat")
field27.setAccessType("inputOutput")
field27.setValue("0.5")
ComposedShader23.addField(field27)
field28 = field()
field28.setName("power")
field28.setType("SFFloat")
field28.setAccessType("inputOutput")
field28.setValue("2")
ComposedShader23.addField(field28)
ShaderPart29 = ShaderPart()
ShaderPart29.setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"])
ShaderPart29.setType("VERTEX")
ComposedShader23.addParts(ShaderPart29)
ShaderPart30 = ShaderPart()
ShaderPart30.setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"])
ShaderPart30.setType("FRAGMENT")
ComposedShader23.addParts(ShaderPart30)
Appearance14.addShaders(ComposedShader23)
Shape13.setAppearance(Appearance14)
#
#                <Sphere>
#		
IndexedFaceSet31 = IndexedFaceSet(convex = False, creaseAngle = 0)
IndexedFaceSet31.setDEF("Orbit")
Coordinate32 = Coordinate()
Coordinate32.setDEF("OrbitCoordinates")
IndexedFaceSet31.setCoord(Coordinate32)
Shape13.setGeometry(IndexedFaceSet31)
Transform12.addChildren(Shape13)
Scene9.addChildren(Transform12)
Script33 = Script()
Script33.setDEF("OrbitScript")
field34 = field()
field34.setAccessType("inputOnly")
field34.setName("set_fraction")
field34.setType("SFFloat")
Script33.addField(field34)
field35 = field()
field35.setAccessType("inputOutput")
field35.setName("coordinates")
field35.setType("MFVec3f")
Script33.addField(field35)
field36 = field()
field36.setAccessType("outputOnly")
field36.setName("coordIndexes")
field36.setType("MFInt32")
Script33.addField(field36)

Script33.setSourceCode('''\n"+
"\n"+
"ecmascript:\n"+
"\n"+
"var e = 5;\n"+
"var f = 5;\n"+
"var g = 5;\n"+
"var h = 5;\n"+
"\n"+
"function initialize() {\n"+
"     resolution = 100;\n"+
"     updateCoordinates(resolution);\n"+
"     var cis = [];\n"+
"     for ( i = 0; i < resolution-1; i++) {\n"+
"     	for ( j = 0; j < resolution-1; j++) {\n"+
"	     cis.push(i*resolution+j);\n"+
"	     cis.push(i*resolution+j+1);\n"+
"	     cis.push((i+1)*resolution+j+1);\n"+
"	     cis.push((i+1)*resolution+j);\n"+
"	     cis.push(-1);\n"+
"	}\n"+
"    }\n"+
"    coordIndexes = new MFInt32(cis);\n"+
"}\n"+
"\n"+
"function updateCoordinates(resolution) {\n"+
"     theta = 0.0;\n"+
"     phi = 0.0;\n"+
"     delta = (2 * 3.141592653) / (resolution-1);\n"+
"     var crds = [];\n"+
"     for ( i = 0; i < resolution; i++) {\n"+
"     	for ( j = 0; j < resolution; j++) {\n"+
"		rho = e + f * Math.cos(g * theta) * Math.cos(h * phi);\n"+
"		crds.push(new SFVec3f(\n"+
"			rho * Math.cos(phi) * Math.cos(theta),\n"+
"			rho * Math.cos(phi) * Math.sin(theta),\n"+
"			rho * Math.sin(phi)\n"+
"		));\n"+
"		theta += delta;\n"+
"	}\n"+
"	phi += delta;\n"+
"     }\n"+
"     coordinates = new MFVec3f(crds);\n"+
"}\n"+
"\n"+
"function set_fraction(fraction, eventTime) {\n"+
"	choice = Math.floor(Math.random() * 4);\n"+
"	switch (choice) {\n"+
"	case 0:\n"+
"		e += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 1:\n"+
"		f += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 2:\n"+
"		g += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	case 3:\n"+
"		h += Math.floor(Math.random() * 2) * 2 - 1;\n"+
"		break;\n"+
"	}\n"+
"	if (f < 1) {\n"+
"		f = 10;\n"+
"	}\n"+
"	if (g < 1) {\n"+
"		g = 4;\n"+
"	}\n"+
"	if (h < 1) {\n"+
"		h = 4;\n"+
"	}\n"+
"	resolution = 100;\n"+
"	updateCoordinates(resolution);\n"+
"}\n"+
"      ''')
Scene9.addChildren(Script33)
TimeSensor37 = TimeSensor()
TimeSensor37.setDEF("Clock")
TimeSensor37.setCycleInterval(16)
TimeSensor37.setLoop(True)
Scene9.addChildren(TimeSensor37)
ROUTE38 = ROUTE()
ROUTE38.setFromField("coordIndexes")
ROUTE38.setFromNode("OrbitScript")
ROUTE38.setToField("set_coordIndex")
ROUTE38.setToNode("Orbit")
Scene9.addChildren(ROUTE38)
ROUTE39 = ROUTE()
ROUTE39.setFromField("coordinates")
ROUTE39.setFromNode("OrbitScript")
ROUTE39.setToField("set_point")
ROUTE39.setToNode("OrbitCoordinates")
Scene9.addChildren(ROUTE39)
ROUTE40 = ROUTE()
ROUTE40.setFromField("fraction_changed")
ROUTE40.setFromNode("Clock")
ROUTE40.setToField("set_fraction")
ROUTE40.setToNode("OrbitScript")
Scene9.addChildren(ROUTE40)
X3D0.setScene(Scene9)
