import x3dpsail as x3d
X3D0 = x3d.X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.3")
head1 = x3d.head()
meta2 = x3d.meta()
meta2.setContent("HelloWorld.x3d")
meta2.setName("title")

head1.addMeta(meta2)
meta3 = x3d.meta()
meta3.setContent("Simple X3D scene example: Hello World!")
meta3.setName("description")

head1.addMeta(meta3)
meta4 = x3d.meta()
meta4.setContent("30 October 2000")
meta4.setName("created")

head1.addMeta(meta4)
meta5 = x3d.meta()
meta5.setContent("14 April 2017")
meta5.setName("modified")

head1.addMeta(meta5)
meta6 = x3d.meta()
meta6.setContent("Don Brutzman")
meta6.setName("creator")

head1.addMeta(meta6)
meta7 = x3d.meta()
meta7.setContent("HelloWorld.tall.png")
meta7.setName("Image")

head1.addMeta(meta7)
meta8 = x3d.meta()
meta8.setContent("http://en.wikipedia.org/wiki/Hello_world")
meta8.setName("reference")

head1.addMeta(meta8)
meta9 = x3d.meta()
meta9.setContent("https://en.wikipedia.org/wiki/Hello#.22Hello.2C_World.22_computer_program")
meta9.setName("reference")

head1.addMeta(meta9)
meta10 = x3d.meta()
meta10.setContent("https://en.wikipedia.org/wiki/\"Hello,_World!\"_program")
meta10.setName("reference")

head1.addMeta(meta10)
meta11 = x3d.meta()
meta11.setContent("http://en.wikibooks.org/w/index.php?title=Computer_Programming/Hello_world")
meta11.setName("reference")

head1.addMeta(meta11)
meta12 = x3d.meta()
meta12.setContent("http://www.HelloWorldExample.net")
meta12.setName("reference")

head1.addMeta(meta12)
meta13 = x3d.meta()
meta13.setContent("http://www.web3D.org")
meta13.setName("reference")

head1.addMeta(meta13)
meta14 = x3d.meta()
meta14.setContent("http://www.web3d.org/realtime-3d/news/internationalization-x3d")
meta14.setName("reference")

head1.addMeta(meta14)
meta15 = x3d.meta()
meta15.setContent("http://www.web3d.org/x3d/content/examples/HelloWorld.x3d")
meta15.setName("reference")

head1.addMeta(meta15)
meta16 = x3d.meta()
meta16.setContent("http://X3dGraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes")
meta16.setName("reference")

head1.addMeta(meta16)
meta17 = x3d.meta()
meta17.setContent("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter01TechnicalOverview/HelloWorld.x3d")
meta17.setName("identifier")

head1.addMeta(meta17)
meta18 = x3d.meta()
meta18.setContent("http://www.web3d.org/x3d/content/examples/license.html")
meta18.setName("license")

head1.addMeta(meta18)
meta19 = x3d.meta()
meta19.setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit")
meta19.setName("generator")

head1.addMeta(meta19)
# Alternate encodings: VRML97, X3D ClassicVRML Encoding, X3D Compressed Binary Encoding (CBE), X3DOM, JSON 
meta20 = x3d.meta()
meta20.setContent("HelloWorld.wrl")
meta20.setName("reference")

head1.addMeta(meta20)
meta21 = x3d.meta()
meta21.setContent("HelloWorld.x3dv")
meta21.setName("reference")

head1.addMeta(meta21)
meta22 = x3d.meta()
meta22.setContent("HelloWorld.x3db")
meta22.setName("reference")

head1.addMeta(meta22)
meta23 = x3d.meta()
meta23.setContent("HelloWorld.xhtml")
meta23.setName("reference")

head1.addMeta(meta23)
meta24 = x3d.meta()
meta24.setContent("HelloWorld.json")
meta24.setName("reference")

head1.addMeta(meta24)

X3D0.setHead(head1)
Scene25 = x3d.Scene()
# Example scene to illustrate X3D nodes and fields (XML elements and attributes) 
WorldInfo26 = x3d.WorldInfo()
WorldInfo26.setTitle("Hello world!")

Scene25.addChildren(WorldInfo26)
Group27 = x3d.Group()
Viewpoint28 = x3d.Viewpoint()
Viewpoint28.setDEF("ViewUpClose")
Viewpoint28.setCenterOfRotation([0,-1,0])
Viewpoint28.setDescription("Hello world!")
Viewpoint28.setPosition([0,-1,7])

Group27.addChildren(Viewpoint28)
Transform29 = x3d.Transform()
Transform29.setRotation([0,1,0,3])
Shape30 = x3d.Shape()
Sphere31 = x3d.Sphere()

Shape30.setGeometry(Sphere31)
Appearance32 = x3d.Appearance()
Material33 = x3d.Material()
Material33.setDEF("MaterialLightBlue")
Material33.setDiffuseColor([0.1,0.5,1])

Appearance32.setMaterial(Material33)
ImageTexture34 = x3d.ImageTexture()
ImageTexture34.setDEF("ImageCloudlessEarth")
ImageTexture34.setUrl(["earth-topo.png","earth-topo.jpg","earth-topo-small.gif","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.png","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.jpg","http://www.web3d.org/x3d/content/examples/Basic/earth-topo-small.gif"])

Appearance32.setTexture(ImageTexture34)

Shape30.setAppearance(Appearance32)

Transform29.addChildren(Shape30)

Group27.addChildren(Transform29)
Transform35 = x3d.Transform()
Transform35.setTranslation([0,-2,0])
Shape36 = x3d.Shape()
Text37 = x3d.Text()
Text37.setDEF("TextMessage")
Text37.setString(["Hello","world!"])
FontStyle38 = x3d.FontStyle()
FontStyle38.setJustify(["MIDDLE","MIDDLE"])

Text37.setFontStyle(FontStyle38)

Shape36.setGeometry(Text37)
Appearance39 = x3d.Appearance()
Material40 = x3d.Material()
Material40.setUSE("MaterialLightBlue")

Appearance39.setMaterial(Material40)

Shape36.setAppearance(Appearance39)

Transform35.addChildren(Shape36)

Group27.addChildren(Transform35)

Scene25.addChildren(Group27)

X3D0.setScene(Scene25)
X3D0.toFileX3D("examples/HelloWorld_RoundTrip.x3d")
