import x3dpsail as x3d
X3D0 = x3d.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
# x3dVersionComparisonTest for this model: supportsX3dVersion(X3DObject.VERSION_3_0)=true 
head1 = x3d.head()
# comment #1 
# comment #2 
# comment #3 
# comment #4 
component2 = x3d.component()
component2.setName("Navigation")
component2.setLevel(3)

head1.addComponent(component2)
component3 = x3d.component()
component3.setName("Layering")
component3.setLevel(1)

head1.addComponent(component3)
component4 = x3d.component()
component4.setName("Shaders")
component4.setLevel(1)

head1.addComponent(component4)
component5 = x3d.component()
component5.setName("CADGeometry")
component5.setLevel(2)

head1.addComponent(component5)
component6 = x3d.component()
component6.setName("DIS")
component6.setLevel(2)

head1.addComponent(component6)
component7 = x3d.component()
component7.setName("H-Anim")
component7.setLevel(1)

head1.addComponent(component7)
unit8 = x3d.unit()
unit8.setName("AngleUnitConversion")
unit8.setCategory("angle")
unit8.setConversionFactor(1.0)

head1.addUnit(unit8)
unit9 = x3d.unit()
unit9.setName("LengthUnitConversion")
unit9.setCategory("length")
unit9.setConversionFactor(1.0)

head1.addUnit(unit9)
unit10 = x3d.unit()
unit10.setName("ForceFromPoundsToNewtons")
unit10.setCategory("force")
unit10.setConversionFactor(4.4482)

head1.addUnit(unit10)
meta11 = x3d.meta()
meta11.setContent("HelloWorldProgramOutput.x3d")
meta11.setName("title")

head1.addMeta(meta11)
meta12 = x3d.meta()
meta12.setContent("continued development and testing in progress")
meta12.setName("info")

head1.addMeta(meta12)
meta13 = x3d.meta()
meta13.setContent("Example HelloWorldProgram creates an X3D model using the X3D Java Scene Access Interface Library (X3DJSAIL)")
meta13.setName("description")

head1.addMeta(meta13)
meta14 = x3d.meta()
meta14.setContent("http://www.web3d.org/specifications/java/X3DJSAIL.html")
meta14.setName("reference")

head1.addMeta(meta14)
meta15 = x3d.meta()
meta15.setContent("HelloWorldProgramOutput.java")
meta15.setName("generator")

head1.addMeta(meta15)
meta16 = x3d.meta()
meta16.setContent("6 September 2016")
meta16.setName("created")

head1.addMeta(meta16)
meta17 = x3d.meta()
meta17.setContent("19 June 2019")
meta17.setName("modified")

head1.addMeta(meta17)
meta18 = x3d.meta()
meta18.setContent("X3D Java Scene Access Interface Library (X3DJSAIL)")
meta18.setName("generator")

head1.addMeta(meta18)
meta19 = x3d.meta()
meta19.setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgram.java")
meta19.setName("generator")

head1.addMeta(meta19)
meta20 = x3d.meta()
meta20.setContent("Netbeans http://www.netbeans.org")
meta20.setName("generator")

head1.addMeta(meta20)
meta21 = x3d.meta()
meta21.setContent("Don Brutzman")
meta21.setName("creator")

head1.addMeta(meta21)
meta22 = x3d.meta()
meta22.setContent("https://sourceforge.net/p/x3d/code/HEAD/tree/www.web3d.org/x3d/stylesheets/java/examples/HelloWorldProgramOutput.x3d")
meta22.setName("reference")

head1.addMeta(meta22)
meta23 = x3d.meta()
meta23.setContent("Console output, ClassicVRML encoding, VRML97 encoding and pretty-print documentation:")
meta23.setName("reference")

head1.addMeta(meta23)
meta24 = x3d.meta()
meta24.setContent("HelloWorldProgramOutput.txt")
meta24.setName("reference")

head1.addMeta(meta24)
meta25 = x3d.meta()
meta25.setContent("HelloWorldProgramOutput.x3dv")
meta25.setName("reference")

head1.addMeta(meta25)
meta26 = x3d.meta()
meta26.setContent("HelloWorldProgramOutput.wrl")
meta26.setName("reference")

head1.addMeta(meta26)
meta27 = x3d.meta()
meta27.setContent("HelloWorldProgramOutput.html")
meta27.setName("reference")

head1.addMeta(meta27)
meta28 = x3d.meta()
meta28.setContent("https://savage.nps.edu/X3dValidator?url=http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d")
meta28.setName("reference")

head1.addMeta(meta28)
meta29 = x3d.meta()
meta29.setContent("http://www.web3d.org/specifications/java/examples/HelloWorldProgramOutput.x3d")
meta29.setName("identifier")

head1.addMeta(meta29)
meta30 = x3d.meta()
meta30.setContent("../license.html")
meta30.setName("license")

head1.addMeta(meta30)

X3D0.setHead(head1)
Scene31 = x3d.Scene()
ViewpointGroup32 = x3d.ViewpointGroup()
ViewpointGroup32.setDescription("Available viewpoints")
Viewpoint33 = x3d.Viewpoint()
Viewpoint33.setDEF("DefaultView")
Viewpoint33.setDescription("Hello X3DJSAIL")

ViewpointGroup32.addChildren(Viewpoint33)
Viewpoint34 = x3d.Viewpoint()
Viewpoint34.setDEF("TopDownView")
Viewpoint34.setDescription("top-down view from above")
Viewpoint34.setOrientation([1,0,0,-1.570796])
Viewpoint34.setPosition([0,100,0])

ViewpointGroup32.addChildren(Viewpoint34)

Scene31.addChildren(ViewpointGroup32)
NavigationInfo35 = x3d.NavigationInfo()
NavigationInfo35.setAvatarSize([0.25,1.6,0.75])
NavigationInfo35.setTransitionType(["LINEAR"])
NavigationInfo35.setType(["EXAMINE","FLY","ANY"])

Scene31.addChildren(NavigationInfo35)
WorldInfo36 = x3d.WorldInfo()
WorldInfo36.setDEF("WorldInfoDEF")
WorldInfo36.setTitle("HelloWorldProgram produced by X3D Java SAI Library (X3DJSAIL)")

Scene31.addChildren(WorldInfo36)
WorldInfo37 = x3d.WorldInfo()
WorldInfo37.setUSE("WorldInfoDEF")

Scene31.addChildren(WorldInfo37)
WorldInfo38 = x3d.WorldInfo()
WorldInfo38.setUSE("WorldInfoDEF")

Scene31.addChildren(WorldInfo38)
MetadataString39 = x3d.MetadataString()
MetadataString39.setDEF("scene.addChildMetadata")
MetadataString39.setName("test")
MetadataString39.setValue(["Top-level root Metadata node beneath Scene needs to be one of '-children' in JSON encoding"])

Scene31.addMetadata(MetadataString39)
LayerSet40 = x3d.LayerSet()
LayerSet40.setDEF("scene.addChildLayerSetTest")
LayerSet40.setOrder([0])

Scene31.addLayerSet(LayerSet40)
Transform41 = x3d.Transform()
Transform41.setDEF("LogoGeometryTransform")
Transform41.setTranslation([0,1.5,0])
Anchor42 = x3d.Anchor()
Anchor42.setDescription("select for X3D Java SAI Library (X3DJSAIL) description")
Anchor42.setUrl(["../X3DJSAIL.html","http://www.web3d.org/specifications/java/X3DJSAIL.html"])
Shape43 = x3d.Shape()
Shape43.setDEF("BoxShape")
Appearance44 = x3d.Appearance()
Material45 = x3d.Material()
Material45.setDEF("GreenMaterial")
Material45.setDiffuseColor([0,1,1])
Material45.setEmissiveColor([0.8,0,0])
Material45.setTransparency(0.1)

Appearance44.setMaterial(Material45)
ImageTexture46 = x3d.ImageTexture()
ImageTexture46.setUrl(["images/X3dJavaSceneAccessInterfaceSaiLibrary.png","http://www.web3d.org/specifications/java/examples/images/X3dJavaSceneAccessInterfaceSaiLibrary.png"])

Appearance44.setTexture(ImageTexture46)

Shape43.setAppearance(Appearance44)
Box47 = x3d.Box()
Box47.setDEF("test-NMTOKEN_regex.0123456789")
Box47.setCssClass("untextured")

Shape43.setGeometry(Box47)

Anchor42.addChildren(Shape43)

Transform41.addChildren(Anchor42)

Scene31.addChildren(Transform41)
Shape48 = x3d.Shape()
Shape48.setDEF("LineShape")
Appearance49 = x3d.Appearance()
Material50 = x3d.Material()
Material50.setEmissiveColor([0.6,0.19607843,0.8])

Appearance49.setMaterial(Material50)

Shape48.setAppearance(Appearance49)
IndexedLineSet51 = x3d.IndexedLineSet()
IndexedLineSet51.setCoordIndex([0,1,2,3,4,0])
# Coordinate 3-tuple point count: 6 
Coordinate52 = x3d.Coordinate()
Coordinate52.setPoint([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0])

IndexedLineSet51.setCoord(Coordinate52)

Shape48.setGeometry(IndexedLineSet51)

Scene31.addChildren(Shape48)
PositionInterpolator53 = x3d.PositionInterpolator()
PositionInterpolator53.setDEF("BoxPathAnimator")
PositionInterpolator53.setKey([0,0.125,0.375,0.625,0.875,1])
PositionInterpolator53.setKeyValue([0,1.5,0,2,1.5,0,2,1.5,-2,-2,1.5,-2,-2,1.5,0,0,1.5,0])

Scene31.addChildren(PositionInterpolator53)
TimeSensor54 = x3d.TimeSensor()
TimeSensor54.setDEF("OrbitClock")
TimeSensor54.setCycleInterval(8.0)
TimeSensor54.setLoop(True)

Scene31.addChildren(TimeSensor54)
ROUTE55 = x3d.ROUTE()
ROUTE55.setFromField("fraction_changed")
ROUTE55.setFromNode("OrbitClock")
ROUTE55.setToField("set_fraction")
ROUTE55.setToNode("BoxPathAnimator")

Scene31.addChildren(ROUTE55)
ROUTE56 = x3d.ROUTE()
ROUTE56.setFromField("value_changed")
ROUTE56.setFromNode("BoxPathAnimator")
ROUTE56.setToField("set_translation")
ROUTE56.setToNode("LogoGeometryTransform")

Scene31.addChildren(ROUTE56)
Transform57 = x3d.Transform()
Transform57.setDEF("TextTransform")
Transform57.setTranslation([0,-1.5,0])
Shape58 = x3d.Shape()
Appearance59 = x3d.Appearance()
Material60 = x3d.Material()
Material60.setUSE("GreenMaterial")

Appearance59.setMaterial(Material60)

Shape58.setAppearance(Appearance59)
Text61 = x3d.Text()
Text61.setString(["X3D Java","SAI Library","X3DJSAIL"])
# Comment example A, plain quotation marks: He said, \"Immel did it!\" 
# Comment example B, XML character entities: He said, &quot;Immel did it!&quot; 
MetadataSet62 = x3d.MetadataSet()
MetadataSet62.setName("EscapedQuotationMarksMetadataSet")
MetadataString63 = x3d.MetadataString()
MetadataString63.setName("quotesTestC")
MetadataString63.setValue(["MFString example C, backslash-escaped quotes: He said, \"Immel did it!\""])

MetadataSet62.setValue(MetadataString63)
MetadataString64 = x3d.MetadataString()
MetadataString64.setName("extraChildTest")
MetadataString64.setValue(["checks MetadataSetObject addValue() method"])

MetadataSet62.setValue(MetadataString64)

Text61.setMetadata(MetadataSet62)
FontStyle65 = x3d.FontStyle()
FontStyle65.setFamily(["SERIF"])
FontStyle65.setJustify(["MIDDLE","MIDDLE"])

Text61.setFontStyle(FontStyle65)

Shape58.setGeometry(Text61)

Transform57.addChildren(Shape58)
Collision66 = x3d.Collision()
# test containerField='proxy' 
Shape67 = x3d.Shape()
Shape67.setDEF("ProxyShape")
# alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\"' 
# alternative XML encoding: Text string='\"One, Two, Comment\" \"\" \"He said, \\&quot;Immel did it!\\&quot;\" \"\"' 
# alternative Java source: .setString(new String [] {\"One, Two, Comment\", \"\", \"He said, \\\"Immel did it!\\\"\"}) 
# reference: http://www.web3d.org/x3d/content/examples/Basic/X3dSpecifications/StringArrayEncodingExamplesIndex.html 
Text68 = x3d.Text()
Text68.setString(["One, Two, Text","","He said, \"Immel did it!\" \"\""])

Shape67.setGeometry(Text68)

Collision66.setProxy(Shape67)

Transform57.addChildren(Collision66)
# It's a beautiful world 
# ... for you! 
# https://en.wikipedia.org/wiki/Beautiful_World_(Devo_song) 

Scene31.addChildren(Transform57)
# repeatedly spin 180 degrees as a readable special effect 
OrientationInterpolator69 = x3d.OrientationInterpolator()
OrientationInterpolator69.setDEF("SpinInterpolator")
OrientationInterpolator69.setKey([0,0.5,1])
OrientationInterpolator69.setKeyValue([0,1,0,4.712389,0,1,0,0,0,1,0,1.5707964])

Scene31.addChildren(OrientationInterpolator69)
TimeSensor70 = x3d.TimeSensor()
TimeSensor70.setDEF("SpinClock")
TimeSensor70.setCycleInterval(5.0)
TimeSensor70.setLoop(True)

Scene31.addChildren(TimeSensor70)
ROUTE71 = x3d.ROUTE()
ROUTE71.setFromField("fraction_changed")
ROUTE71.setFromNode("SpinClock")
ROUTE71.setToField("set_fraction")
ROUTE71.setToNode("SpinInterpolator")

Scene31.addChildren(ROUTE71)
ROUTE72 = x3d.ROUTE()
ROUTE72.setFromField("value_changed")
ROUTE72.setFromNode("SpinInterpolator")
ROUTE72.setToField("rotation")
ROUTE72.setToNode("TextTransform")

Scene31.addChildren(ROUTE72)
Group73 = x3d.Group()
Group73.setDEF("BackgroundGroup")
Background74 = x3d.Background()
Background74.setDEF("GradualBackground")

Group73.addChildren(Background74)
Script75 = x3d.Script()
Script75.setDEF("colorTypeConversionScript")
field76 = x3d.field()
field76.setName("colorInput")
field76.setAccessType("inputOnly")
field76.setType("SFColor")

Script75.addField(field76)
field77 = x3d.field()
field77.setName("colorsOutput")
field77.setAccessType("outputOnly")
field77.setType("MFColor")

Script75.addField(field77)

Script75.setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"function colorInput (eventValue) // Example source code\n"+
"{\n"+
"   colorsOutput = new MFColor(eventValue); // assigning value sends output event\n"+
"// Browser.print('colorInput=' + eventValue + ', colorsOutput=' + colorsOutput + '\\n');\n"+
"}\n"+
"''')

Group73.addChildren(Script75)
ColorInterpolator78 = x3d.ColorInterpolator()
ColorInterpolator78.setDEF("ColorAnimator")
ColorInterpolator78.setKey([0,0.5,1])
ColorInterpolator78.setKeyValue([0.9411765,1,1,0.29411766,0,0.50980395,0.9411765,1,1])
# AZURE to INDIGO and back again 

Group73.addChildren(ColorInterpolator78)
TimeSensor79 = x3d.TimeSensor()
TimeSensor79.setDEF("ColorClock")
TimeSensor79.setCycleInterval(60.0)
TimeSensor79.setLoop(True)

Group73.addChildren(TimeSensor79)
ROUTE80 = x3d.ROUTE()
ROUTE80.setFromField("colorsOutput")
ROUTE80.setFromNode("colorTypeConversionScript")
ROUTE80.setToField("skyColor")
ROUTE80.setToNode("GradualBackground")

Group73.addChildren(ROUTE80)
ROUTE81 = x3d.ROUTE()
ROUTE81.setFromField("value_changed")
ROUTE81.setFromNode("ColorAnimator")
ROUTE81.setToField("colorInput")
ROUTE81.setToNode("colorTypeConversionScript")

Group73.addChildren(ROUTE81)
ROUTE82 = x3d.ROUTE()
ROUTE82.setFromField("fraction_changed")
ROUTE82.setFromNode("ColorClock")
ROUTE82.setToField("set_fraction")
ROUTE82.setToNode("ColorAnimator")

Group73.addChildren(ROUTE82)

Scene31.addChildren(Group73)
ProtoDeclare83 = x3d.ProtoDeclare()
ProtoDeclare83.setName("ArtDeco01Material")
ProtoDeclare83.setAppinfo("tooltip: ArtDeco01Material prototype is a Material node")
ProtoInterface84 = x3d.ProtoInterface()
field85 = x3d.field()
field85.setName("description")
field85.setAccessType("inputOutput")
field85.setAppinfo("tooltip for descriptionField")
field85.setType("SFString")
field85.setValue("ArtDeco01Material prototype is a Material node")

ProtoInterface84.addField(field85)
field86 = x3d.field()
field86.setName("enabled")
field86.setAccessType("inputOutput")
field86.setType("SFBool")
field86.setValue("true")

ProtoInterface84.addField(field86)

ProtoDeclare83.setProtoInterface(ProtoInterface84)
ProtoBody87 = x3d.ProtoBody()
# Initial node of ProtoBody determines prototype node type 
Material88 = x3d.Material()
Material88.setAmbientIntensity(0.25)
Material88.setDiffuseColor([0.282435,0.085159,0.134462])
Material88.setShininess(0.127273)
Material88.setSpecularColor([0.276305,0.11431,0.139857])

ProtoBody87.addChildren(Material88)
# [HelloWorldProgram diagnostic] should be connected to scene graph: artDeco01ProtoDeclare.getNodeType()=\"Material\" 
# presence of follow-on TouchSensor shows that additional nodes are allowed in ProtoBody after initial node, regardless of node types 
TouchSensor89 = x3d.TouchSensor()
TouchSensor89.setDescription("within ProtoBody")
IS90 = x3d.IS()
connect91 = x3d.connect()
connect91.setNodeField("description")
connect91.setProtoField("description")

IS90.addConnect(connect91)
connect92 = x3d.connect()
connect92.setNodeField("enabled")
connect92.setProtoField("enabled")

IS90.addConnect(connect92)

TouchSensor89.setIS(IS90)

ProtoBody87.addChildren(TouchSensor89)

ProtoDeclare83.setProtoBody(ProtoBody87)

Scene31.addChildren(ProtoDeclare83)
ExternProtoDeclare93 = x3d.ExternProtoDeclare()
ExternProtoDeclare93.setName("ArtDeco02Material")
ExternProtoDeclare93.setAppinfo("this is a different Material node")
ExternProtoDeclare93.setUrl(["http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3d#ArtDeco02Material","http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/ArtDecoPrototypesExcerpt.x3dv#ArtDeco02Material"])
# [HelloWorldProgram diagnostic] artDeco02ExternProtoDeclare.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 
field94 = x3d.field()
field94.setName("description")
field94.setAccessType("inputOutput")
field94.setAppinfo("tooltip for descriptionField")
field94.setType("SFString")

ExternProtoDeclare93.addField(field94)

Scene31.addChildren(ExternProtoDeclare93)
# Tested ArtDeco01ProtoInstance, ArtDeco02ProtoInstance for improper node type when ProtoInstance is added in wrong place 
Shape95 = x3d.Shape()
Shape95.setDEF("TestShape1")
Appearance96 = x3d.Appearance()
Appearance96.setDEF("TestAppearance1")
# ArtDeco01Material prototype goes here... TODO ensure setContainerField is handled in exported Java 
ProtoInstance97 = x3d.ProtoInstance()
ProtoInstance97.setName("ArtDeco01Material")
# [HelloWorldProgram diagnostic] ArtDeco01ProtoInstance.getNodeType()=\"Material\" 
fieldValue98 = x3d.fieldValue()
fieldValue98.setName("description")
fieldValue98.setValue("ArtDeco01Material can substitute for a Material node")

ProtoInstance97.addFieldValue(fieldValue98)

Appearance96.setMaterial(ProtoInstance97)

Shape95.setAppearance(Appearance96)
Sphere99 = x3d.Sphere()
Sphere99.setRadius(0.001)

Shape95.setGeometry(Sphere99)

Scene31.addChildren(Shape95)
Shape100 = x3d.Shape()
Shape100.setDEF("TestShape2")
Appearance101 = x3d.Appearance()
Appearance101.setDEF("TestAppearance2")
# ArtDeco02Material prototype goes here... TODO ensure setContainerField is handled in exported Java 
ProtoInstance102 = x3d.ProtoInstance()
ProtoInstance102.setDEF("ArtDeco02MaterialDEF")
ProtoInstance102.setName("ArtDeco02Material")
# [HelloWorldProgram diagnostic] ArtDeco02ProtoInstance.getNodeType()=\"ERROR_UNKNOWN_EXTERNPROTODECLARE_NODE_TYPE: ExternProtoDeclare name='ArtDeco02Material' type cannot be remotely accessed at run time. TODO X3DJSAIL needs to add further capability that retrieves the ExternProtoDeclare file.\" 
fieldValue103 = x3d.fieldValue()
fieldValue103.setName("description")
fieldValue103.setValue("ArtDeco02Material can substitute for another Material node")

ProtoInstance102.addFieldValue(fieldValue103)

Appearance101.setMaterial(ProtoInstance102)

Shape100.setAppearance(Appearance101)
Cone104 = x3d.Cone()
Cone104.setBottomRadius(0.001)
Cone104.setHeight(0.001)

Shape100.setGeometry(Cone104)

Scene31.addChildren(Shape100)
Shape105 = x3d.Shape()
Shape105.setDEF("TestShape3")
Appearance106 = x3d.Appearance()
Appearance106.setDEF("TestAppearance3")
# ArtDeco02Material ProtoInstance USE goes here. Note that name field is NOT defined as part of ProtoInstance USE. 
ProtoInstance107 = x3d.ProtoInstance()
ProtoInstance107.setUSE("ArtDeco02MaterialDEF")

Appearance106.setMaterial(ProtoInstance107)

Shape105.setAppearance(Appearance106)
Cylinder108 = x3d.Cylinder()
Cylinder108.setHeight(0.001)
Cylinder108.setRadius(0.001)

Shape105.setGeometry(Cylinder108)

Scene31.addChildren(Shape105)
Inline109 = x3d.Inline()
Inline109.setDEF("inlineSceneDef")
Inline109.setUrl(["someOtherScene.x3d","http://www.web3d.org/specifications/java/examples/someOtherScene.x3d"])

Scene31.addChildren(Inline109)
IMPORT110 = x3d.IMPORT()
IMPORT110.setAS("WorldInfoDEF2")
IMPORT110.setImportedDEF("WorldInfoDEF")
IMPORT110.setInlineDEF("inlineSceneDef")

Scene31.addChildren(IMPORT110)
EXPORT111 = x3d.EXPORT()
EXPORT111.setAS("WorldInfoDEF3")
EXPORT111.setLocalDEF("WorldInfoDEF")

Scene31.addChildren(EXPORT111)
ProtoDeclare112 = x3d.ProtoDeclare()
ProtoDeclare112.setName("MaterialModulator")
ProtoDeclare112.setAppinfo("mimic a Material node and modulate fields as an animation effect")
ProtoDeclare112.setDocumentation("http://x3dgraphics.com/examples/X3dForWebAuthors/Chapter14Prototypes/MaterialModulatorIndex.html")
ProtoInterface113 = x3d.ProtoInterface()
field114 = x3d.field()
field114.setName("enabled")
field114.setAccessType("inputOutput")
field114.setType("SFBool")
field114.setValue("true")

ProtoInterface113.addField(field114)
field115 = x3d.field()
field115.setName("diffuseColor")
field115.setAccessType("inputOutput")
field115.setType("SFColor")
field115.setValue("0 0 0")

ProtoInterface113.addField(field115)
field116 = x3d.field()
field116.setName("emissiveColor")
field116.setAccessType("inputOutput")
field116.setType("SFColor")
field116.setValue("0.05 0.05 0.5")

ProtoInterface113.addField(field116)
field117 = x3d.field()
field117.setName("specularColor")
field117.setAccessType("inputOutput")
field117.setType("SFColor")
field117.setValue("0 0 0")

ProtoInterface113.addField(field117)
field118 = x3d.field()
field118.setName("transparency")
field118.setAccessType("inputOutput")
field118.setType("SFFloat")
field118.setValue("0.0")

ProtoInterface113.addField(field118)
field119 = x3d.field()
field119.setName("shininess")
field119.setAccessType("inputOutput")
field119.setType("SFFloat")
field119.setValue("0.0")

ProtoInterface113.addField(field119)
field120 = x3d.field()
field120.setName("ambientIntensity")
field120.setAccessType("inputOutput")
field120.setType("SFFloat")
field120.setValue("0.0")

ProtoInterface113.addField(field120)

ProtoDeclare112.setProtoInterface(ProtoInterface113)
ProtoBody121 = x3d.ProtoBody()
Material122 = x3d.Material()
Material122.setDEF("MaterialNode")
IS123 = x3d.IS()
connect124 = x3d.connect()
connect124.setNodeField("diffuseColor")
connect124.setProtoField("diffuseColor")

IS123.addConnect(connect124)
connect125 = x3d.connect()
connect125.setNodeField("emissiveColor")
connect125.setProtoField("emissiveColor")

IS123.addConnect(connect125)
connect126 = x3d.connect()
connect126.setNodeField("specularColor")
connect126.setProtoField("specularColor")

IS123.addConnect(connect126)
connect127 = x3d.connect()
connect127.setNodeField("transparency")
connect127.setProtoField("transparency")

IS123.addConnect(connect127)
connect128 = x3d.connect()
connect128.setNodeField("shininess")
connect128.setProtoField("shininess")

IS123.addConnect(connect128)
connect129 = x3d.connect()
connect129.setNodeField("ambientIntensity")
connect129.setProtoField("ambientIntensity")

IS123.addConnect(connect129)

Material122.setIS(IS123)

ProtoBody121.addChildren(Material122)
# Only first node (the node type) is renderable, others are along for the ride 
Script130 = x3d.Script()
Script130.setDEF("MaterialModulatorScript")
field131 = x3d.field()
field131.setName("enabled")
field131.setAccessType("inputOutput")
field131.setType("SFBool")

Script130.addField(field131)
field132 = x3d.field()
field132.setName("diffuseColor")
field132.setAccessType("inputOutput")
field132.setType("SFColor")

Script130.addField(field132)
field133 = x3d.field()
field133.setName("newColor")
field133.setAccessType("outputOnly")
field133.setType("SFColor")

Script130.addField(field133)
field134 = x3d.field()
field134.setName("clockTrigger")
field134.setAccessType("inputOnly")
field134.setType("SFTime")

Script130.addField(field134)
IS135 = x3d.IS()
connect136 = x3d.connect()
connect136.setNodeField("enabled")
connect136.setProtoField("enabled")

IS135.addConnect(connect136)
connect137 = x3d.connect()
connect137.setNodeField("diffuseColor")
connect137.setProtoField("diffuseColor")

IS135.addConnect(connect137)

Script130.setIS(IS135)

Script130.setSourceCode('''\n"+
"ecmascript:\n"+
"function initialize ()\n"+
"{\n"+
"    newColor = diffuseColor; // start with correct color\n"+
"}\n"+
"function set_enabled (newValue)\n"+
"{\n"+
"	enabled = newValue;\n"+
"}\n"+
"function clockTrigger (timeValue)\n"+
"{\n"+
"    if (!enabled) return;\n"+
"    red   = newColor.r;\n"+
"    green = newColor.g;\n"+
"    blue  = newColor.b;\n"+
"    \n"+
"    // note different modulation rates for each color component, % is modulus operator\n"+
"    newColor = new SFColor ((red + 0.02) % 1, (green + 0.03) % 1, (blue + 0.04) % 1);\n"+
"	if (enabled)\n"+
"	{\n"+
"		Browser.print ('diffuseColor=(' + red + ',' + green + ',' + blue + ') newColor=' + newColor.toString() + '\\n');\n"+
"	}\n"+
"}\n"+
"''')

ProtoBody121.addChildren(Script130)

ProtoDeclare112.setProtoBody(ProtoBody121)

Scene31.addChildren(ProtoDeclare112)
# Test success: declarative statement createDeclarativeShapeTests() 
Group138 = x3d.Group()
Group138.setDEF("DeclarativeGroupExample")
Shape139 = x3d.Shape()
MetadataString140 = x3d.MetadataString()
MetadataString140.setDEF("FindableMetadataStringTest")
MetadataString140.setName("findThisNameValue")
MetadataString140.setValue(["test case"])

Shape139.setMetadata(MetadataString140)
Appearance141 = x3d.Appearance()
Appearance141.setDEF("DeclarativeAppearanceExample")
# DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance 
ProtoInstance142 = x3d.ProtoInstance()
ProtoInstance142.setDEF("MyMaterialModulator")
ProtoInstance142.setName("MaterialModulator")

Appearance141.setMaterial(ProtoInstance142)

Shape139.setAppearance(Appearance141)
Cone143 = x3d.Cone()
Cone143.setBottom(False)
Cone143.setBottomRadius(0.05)
Cone143.setHeight(0.1)

Shape139.setGeometry(Cone143)

Group138.addChildren(Shape139)
# Test success: declarativeGroup.addChild() singleton pipeline method 

Scene31.addChildren(Group138)
# Test success: declarative statement addChild() 
# Test success: x3dModel.findNodeByDEF(DeclarativeAppearanceExample) = <Appearance DEF='DeclarativeAppearanceExample'/> i.e. <Appearance DEF='DeclarativeAppearanceExample'> <!- - DeclarativeMaterialExample gets overridden by subsequently added MaterialModulator ProtoInstance - -> <ProtoInstance DEF='MyMaterialModulator' name='MaterialModulator' containerField='material'/> </Appearance> 
# Test success: x3dModel.findElementByNameValue(findThisNameValue) = <MetadataString DEF='FindableMetadataStringTest' name='findThisNameValue' value='\"test case\"'/> 
# Test success: x3dModel.findElementByNameValue(\"ArtDeco01Material\", \"ProtoDeclare\") found 
# Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoDeclare\") found 
# Test success: x3dModel.findElementByNameValue(\"MaterialModulator\", \"ProtoInstance\") found 
Group144 = x3d.Group()
Group144.setDEF("TestFieldObjectsGroup")
# testFieldObjects() results 
# SFBool default=true, true=true, false=false, negate()=true 
# MFBool default=, initial=true false true, negate()=false true false 
# SFFloat default=0.0, initial=1.0, setValue(2)=2.0, setValue(3.0f)=3.0, setValue(4.0)=4.0 
# MFFloat default=, initial=1 2 3, append(5)=1 2 3 5, inserts(3,4)(0,0)=0 1 2 3 4 5, append(6)=0 1 2 3 4 5 6, size()=7 
# ... get1Value[3]=3.0, remove[1]=0 2 3 4 5 6, set1Value(0,10)=10 2 3 4 5 6, multiply(2)=20 4 6 8 10 12, clear= 
# SFVec3f default=0 0 0, initial=1 2 3, setValue=4 5 6, multiply(2)=8 10 12, normalize()=0.45584232 0.5698029 0.68376344, regex matches()=true 
# regex test SFVec3f().matches(\"1 2 3\")=true, regex test SFVec3f().matches(\"1 2 3 4\")=false, regex test (SFRotationObject.matches(\"0 0 0 0\")=true, failure detecting illegal (zero axis) rotation value 

Scene31.addChildren(Group144)
Sound145 = x3d.Sound()
Sound145.setLocation([0,1.6,0])
# set sound-ellipsoid location height at 1.6m to match typical avatar height 
AudioClip146 = x3d.AudioClip()
AudioClip146.setDescription("chimes")
AudioClip146.setUrl(["chimes.wav","http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/chimes.wav"])
# Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Sounds/AudioClip/default.x3d 

Sound145.setSource(AudioClip146)

Scene31.addChildren(Sound145)
Sound147 = x3d.Sound()
Sound147.setLocation([0,1.6,0])
# set sound-ellipsoid location height at 1.6m to match typical avatar height 
MovieTexture148 = x3d.MovieTexture()
MovieTexture148.setDescription("mpgsys.mpg from ConformanceNist suite")
MovieTexture148.setUrl(["mpgsys.mpg","http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpgsys.mpg"])
# Scene example fragment from http://www.web3d.org/x3d/content/examples/ConformanceNist/Appearance/MovieTexture/mpeg1-systems.x3d 
# Expected containerField='source', allowed containerField values=\"texture\" \"source\" \"back\" \"bottom\" \"front\" \"left\" \"right\" \"top\" \"backTexture\" \"bottomTexture\" \"frontTexture\" \"leftTexture\" \"rightTexture\" \"topTexture\" \"watchList\" 

Sound147.setSource(MovieTexture148)

Scene31.addChildren(Sound147)
# Test success: AnchorObject.isNode()=true, siteAnchor.isNode()=true 
# Test success: AnchorObject.isStatement()=false, siteAnchor.isStatement()=false 
# Test success: ROUTEObject.isNode()=false, orbitPositionROUTE.isNode()=false 
# Test success: ROUTEObject.isStatement()=true, orbitPositionROUTE.isStatement()=true 
# Test success: CommentsBlock.isNode()=false, testComments.isNode()=false 
# Test failure: CommentsBlock.isStatement()=true, testComments.isStatement()=true 
Shape149 = x3d.Shape()
Shape149.setDEF("ExtrusionShape")
# ExampleExtrusion isCrossSectionClosed()=true, crossSection='[1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0]' 
# ExampleExtrusion isSpineClosed()=false, spine='[0.0, 0.0, 0.0, 0.0, 1.0, 0.0]' 
Appearance150 = x3d.Appearance()
Appearance150.setDEF("TransparentAppearance")
Material151 = x3d.Material()
Material151.setTransparency(1.0)

Appearance150.setMaterial(Material151)

Shape149.setAppearance(Appearance150)
Extrusion152 = x3d.Extrusion()
Extrusion152.setDEF("ExampleExtrusion")

Shape149.setGeometry(Extrusion152)

Scene31.addChildren(Shape149)
Group153 = x3d.Group()
# Test MFNode children array as an ordered list consisting of comments, statements, ProtoInstance and nodes 
ProtoDeclare154 = x3d.ProtoDeclare()
ProtoDeclare154.setName("NewWorldInfo")
ProtoInterface155 = x3d.ProtoInterface()
field156 = x3d.field()
field156.setName("description")
field156.setAccessType("initializeOnly")
field156.setType("SFString")

ProtoInterface155.addField(field156)

ProtoDeclare154.setProtoInterface(ProtoInterface155)
ProtoBody157 = x3d.ProtoBody()
WorldInfo158 = x3d.WorldInfo()

ProtoBody157.addChildren(WorldInfo158)

ProtoDeclare154.setProtoBody(ProtoBody157)

Group153.addChildren(ProtoDeclare154)
ProtoInstance159 = x3d.ProtoInstance()
ProtoInstance159.setDEF("Proto1")
ProtoInstance159.setName("NewWorldInfo")
fieldValue160 = x3d.fieldValue()
fieldValue160.setName("description")
fieldValue160.setValue("testing 1 2 3")

ProtoInstance159.addFieldValue(fieldValue160)

Group153.addChildren(ProtoInstance159)
Group161 = x3d.Group()
Group161.setDEF("Node2")
# intentionally empty 

Group153.addChildren(Group161)
ProtoInstance162 = x3d.ProtoInstance()
ProtoInstance162.setDEF("Proto3")
ProtoInstance162.setName("NewWorldInfo")

Group153.addChildren(ProtoInstance162)
Transform163 = x3d.Transform()
Transform163.setDEF("Node4")
# intentionally empty 

Group153.addChildren(Transform163)
# Test satisfactorily creates MFNode children array as an ordered list with mixed content 

Scene31.addChildren(Group153)
ProtoDeclare164 = x3d.ProtoDeclare()
ProtoDeclare164.setName("ShaderProto")
ProtoBody165 = x3d.ProtoBody()
ProgramShader166 = x3d.ProgramShader()

ProtoBody165.addChild(ProgramShader166)

ProtoDeclare164.setProtoBody(ProtoBody165)

Scene31.addChildren(ProtoDeclare164)
Shape167 = x3d.Shape()
Appearance168 = x3d.Appearance()
# Test MFNode shaders array as an ordered list consisting of comments, ProtoInstance and nodes 
# Test satisfactorily creates MFNode shaders array as an ordered list with mixed content 
ProgramShader169 = x3d.ProgramShader()
ProgramShader169.setDEF("TestShader1")
ShaderProgram170 = x3d.ShaderProgram()
ShaderProgram170.setDEF("TestShader2")

ProgramShader169.addPrograms(ShaderProgram170)

Appearance168.addShaders(ProgramShader169)
ProtoInstance171 = x3d.ProtoInstance()
ProtoInstance171.setDEF("TestShader3")
ProtoInstance171.setName("ShaderProto")

Appearance168.addChild(ProtoInstance171)
ComposedShader172 = x3d.ComposedShader()
ComposedShader172.setDEF("TestShader4")
ShaderPart173 = x3d.ShaderPart()
ShaderPart173.setDEF("TestShader5")

ComposedShader172.addParts(ShaderPart173)

Appearance168.addShaders(ComposedShader172)

Shape167.setAppearance(Appearance168)

Scene31.addChildren(Shape167)
Transform174 = x3d.Transform()
Transform174.setDEF("SpecialtyNodes")
CADLayer175 = x3d.CADLayer()
CADAssembly176 = x3d.CADAssembly()
CADPart177 = x3d.CADPart()
CADFace178 = x3d.CADFace()

CADPart177.addChildren(CADFace178)

CADAssembly176.addChildren(CADPart177)

CADLayer175.addChildren(CADAssembly176)

Transform174.addChildren(CADLayer175)
EspduTransform179 = x3d.EspduTransform()
EspduTransform179.setGeoSystem(["GD","WE"])

Transform174.addChildren(EspduTransform179)
ReceiverPdu180 = x3d.ReceiverPdu()
ReceiverPdu180.setGeoSystem(["GD","WE"])

Transform174.addChildren(ReceiverPdu180)
SignalPdu181 = x3d.SignalPdu()
SignalPdu181.setGeoSystem(["GD","WE"])

Transform174.addChildren(SignalPdu181)
TransmitterPdu182 = x3d.TransmitterPdu()
TransmitterPdu182.setGeoSystem(["GD","WE"])

Transform174.addChildren(TransmitterPdu182)
DISEntityManager183 = x3d.DISEntityManager()
DISEntityTypeMapping184 = x3d.DISEntityTypeMapping()

DISEntityManager183.addMapping(DISEntityTypeMapping184)

Transform174.addChildren(DISEntityManager183)
HAnimHumanoid185 = x3d.HAnimHumanoid()
HAnimHumanoid185.setDEF("TestHumanoidDEF")
HAnimHumanoid185.setName("TestHumanoid")
HAnimHumanoid185.setVersion("2.0")

Transform174.addChildren(HAnimHumanoid185)

Scene31.addChildren(Transform174)

X3D0.setScene(Scene31)
X3D0.toFileX3D("HelloWorldProgramOutput_CommandLineUnzipped_RoundTrip.x3d")
