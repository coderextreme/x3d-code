from X3Dpackage import *
X3D0 = X3D()
X3D0.setProfile("Immersive")
X3D0.setVersion("3.2")
head1 = head()
meta2 = meta()
meta2.setContent("CloudsProcedural4.x3d")
meta2.setName("title")
head1.addMeta(meta2)
meta3 = meta()
meta3.setContent("X3D utilizing ecmascript to develop quasi volumetric 3D clouds from png image textured billboard nodes.")
meta3.setName("description")
head1.addMeta(meta3)
meta4 = meta()
meta4.setContent("Capt Darren W. Murphy")
meta4.setName("creator")
head1.addMeta(meta4)
meta5 = meta()
meta5.setContent("1 November 2007")
meta5.setName("created")
head1.addMeta(meta5)
meta6 = meta()
meta6.setContent("14 January 2014")
meta6.setName("modified")
head1.addMeta(meta6)
meta7 = meta()
meta7.setContent("https://savage.nps.edu/Savage/Environment/Atmosphere/CloudsProcedural4.x3d")
meta7.setName("identifier")
head1.addMeta(meta7)
meta8 = meta()
meta8.setContent("X3D-Edit, http://www.web3d.org/x3d/content/README.X3D-Edit.html")
meta8.setName("generator")
head1.addMeta(meta8)
meta9 = meta()
meta9.setContent("../../license.html")
meta9.setName("license")
head1.addMeta(meta9)
meta10 = meta()
meta10.setContent("fix links")
meta10.setName("TODO")
head1.addMeta(meta10)
X3D0.setHead(head1)
Scene11 = Scene()
# A png image file for the cloud texture must be designated in the ecmascript node. 
Viewpoint12 = Viewpoint()
Viewpoint12.setDescription("Main")
Viewpoint12.setJump(False)
Viewpoint12.setOrientation([0,1,0,1.57])
Viewpoint12.setPosition([50000,1000,42000])
Scene11.addChildren(Viewpoint12)
Viewpoint13 = Viewpoint()
Viewpoint13.setDescription("Light House Tower")
Viewpoint13.setJump(False)
Viewpoint13.setOrientation([0,1,0,1.3])
Viewpoint13.setPosition([45000,1290,44000])
Scene11.addChildren(Viewpoint13)
Viewpoint14 = Viewpoint()
Viewpoint14.setDescription("centerWest")
Viewpoint14.setJump(False)
Viewpoint14.setOrientation([0,1,0,2.5])
Viewpoint14.setPosition([48000,1000,20000])
Scene11.addChildren(Viewpoint14)
Background15 = Background()
Background15.setGroundColor([0,0,1])
Background15.setSkyColor([0,0,1])
Scene11.addChildren(Background15)
DirectionalLight16 = DirectionalLight()
DirectionalLight16.setAmbientIntensity(1)
DirectionalLight16.setDirection([-1,0,0])
DirectionalLight16.setGlobal(True)
Scene11.addChildren(DirectionalLight16)
Group17 = Group()
Group17.setDEF("Terrain")
Transform18 = Transform()
Transform18.setScale([50,50,50])
Transform18.setTranslation([25000,0,25000])
Inline19 = Inline()
Inline19.setUrl(["MontereyBayLargeMesh.x3d","https://savage.nps.edu/Savage/Environment/Atmosphere/MontereyBayLargeMesh.x3d","MontereyBayLargeMesh.wrl","https://savage.nps.edu/Savage/Environment/Atmosphere/MontereyBayLargeMesh.wrl"])
Transform18.addChildren(Inline19)
Group17.addChildren(Transform18)
Transform20 = Transform()
Transform20.setRotation([1,0,0,1.57])
Transform20.setTranslation([25000,0,25000])
Shape21 = Shape()
Rectangle2D22 = Rectangle2D(size = [77000,55000])
Shape21.setGeometry(Rectangle2D22)
Appearance23 = Appearance()
ImageTexture24 = ImageTexture()
ImageTexture24.setUrl(["ocean.png","https://savage.nps.edu/Savage/Environment/Atmosphere/ocean.png"])
Appearance23.setTexture(ImageTexture24)
Shape21.setAppearance(Appearance23)
Transform20.addChildren(Shape21)
Group17.addChildren(Transform20)
Scene11.addChildren(Group17)
Group25 = Group()
Group25.setDEF("Placemarks")
Transform26 = Transform()
Transform26.setScale([50,50,50])
Transform26.setTranslation([45000,30,44000])
Inline27 = Inline()
Inline27.setUrl(["Lighthouse.x3d","https://savage.nps.edu/Savage/Environment/Atmosphere/Lighthouse.x3d","Lighthouse.wrl","https://savage.nps.edu/Savage/Environment/Atmosphere/Lighthouse.wrl"])
Transform26.addChildren(Inline27)
Group25.addChildren(Transform26)
Scene11.addChildren(Group25)
Group28 = Group()
Group28.setDEF("Clouds")
Transform29 = Transform()
Transform29.setDEF("Cumulus")
Group28.addChildren(Transform29)
Transform30 = Transform()
Transform30.setDEF("Cirrus")
Group28.addChildren(Transform30)
Transform31 = Transform()
Transform31.setDEF("Fog")
Group28.addChildren(Transform31)
Script32 = Script(directOutput = True)
Script32.setDEF("PixelScript")
field33 = field()
field33.setAccessType("initializeOnly")
field33.setName("Cumulus")
field33.setType("SFNode")
Transform34 = Transform()
Transform34.setUSE("Cumulus")
field33.addChildren(Transform34)
Script32.addField(field33)
field35 = field()
field35.setAccessType("initializeOnly")
field35.setName("Cirrus")
field35.setType("SFNode")
Transform36 = Transform()
Transform36.setUSE("Cirrus")
field35.addChildren(Transform36)
Script32.addField(field35)
field37 = field()
field37.setAccessType("initializeOnly")
field37.setName("Fog")
field37.setType("SFNode")
Script32.addField(field37)

Script32.setSourceCode('''\n"+
"ecmascript:\n"+
"\n"+
"\n"+
"function cumulustranslation() // These values designate the boundary location of the cloud\n"+
"{\n"+
"	X = 50000*Math.random();          //  X horizontal range\n"+
"	Y = 1000 + 300*Math.random();	 //  Y vertical base + range\n"+
"	Z = 50000*Math.random();         // z horizontal range\n"+
"\n"+
"	randomt = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"	return randomt;\n"+
"	\n"+
"}\n"+
"\n"+
"\n"+
"\n"+
"function cumulusscale() // these values scale a cloud within a designated size\n"+
"{\n"+
"\n"+
"	maxscale = 1;\n"+
"\n"+
"	scale = Math.round(9+maxscale*Math.random());\n"+
"	X = 1.5*scale;\n"+
"	Y = scale;\n"+
"	Z = scale;\n"+
"\n"+
"	randomscale = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"	return randomscale;\n"+
"	\n"+
"}\n"+
"\n"+
"\n"+
"function cirrustranslation() // These values designate the boundary location of the cloud\n"+
"{\n"+
"	X = 50000*Math.random();          //  X horizontal range\n"+
"	Y = 8000 + 1000*Math.random();	 //  Y vertical base + range\n"+
"	Z = 50000*Math.random();         // z horizontal range\n"+
"\n"+
"	randomt = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"	return randomt;\n"+
"	\n"+
"}\n"+
"\n"+
"\n"+
"\n"+
"function cirrusscale() // these values scale a cloud within a designated size\n"+
"{\n"+
"\n"+
"	maxscale = 1;\n"+
"\n"+
"	scale = Math.round(9+maxscale*Math.random());\n"+
"	X = 1.5*scale;\n"+
"	Y = 2*Math.random();\n"+
"	Z = 1.5*scale;\n"+
"\n"+
"	randomscale = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"	return randomscale;\n"+
"	\n"+
"}\n"+
"\n"+
"\n"+
"function cumulussectiontranslation() // These random values place another portion of cumulus type cloud\n"+
"{\n"+
"\n"+
"	randomtheta = 6.28319*Math.random();\n"+
"	randomphi = .7854*Math.random();\n"+
"	randomradius = 90 + 5*Math.random();//the first whole number should be close to the sectionradius\n"+
"\n"+
"	X = randomradius*Math.cos(randomtheta)*Math.sin(randomphi);\n"+
"	Z = randomradius*Math.sin(randomtheta)*Math.sin(randomphi);\n"+
"	Y = randomradius*Math.cos(randomphi);\n"+
"	\n"+
"\n"+
"	randomt = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"	return randomt;\n"+
"	\n"+
"}\n"+
"\n"+
"function cirrussectiontranslation() // These random values place another portion of cirrus type cloud\n"+
"{\n"+
"\n"+
"	randomtheta = 6.28319*Math.random();\n"+
"	randomphi = .7854*Math.random();\n"+
"	randomradius = 90 + 5*Math.random();//the first whole number should be close to the sectionradius\n"+
"\n"+
"	X = randomradius*Math.cos(randomtheta)*Math.sin(randomphi);\n"+
"	Z = randomradius*Math.sin(randomtheta)*Math.sin(randomphi);\n"+
"	Y = randomradius*Math.cos(randomphi);\n"+
"	\n"+
"\n"+
"	randomt = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"	return randomt;\n"+
"	\n"+
"}\n"+
"\n"+
"\n"+
"function rotation() // This random value is for the billboard rotation not used in this script\n"+
"{\n"+
"\n"+
"\n"+
"	radians = 6.28*Math.random();\n"+
"\n"+
"	randomr = new String('0 0 1 ' + radians );\n"+
"	\n"+
"	\n"+
"	return randomr;\n"+
"	\n"+
"}\n"+
"\n"+
"function cumulus()\n"+
"{\n"+
"\n"+
"maxi = 20;  // number of clouds\n"+
"\n"+
"maxj = 5; // denotes how many portions affecting the size of the cloud\n"+
"\n"+
"maxk = 8;  // number of billboards indicating cloud density\n"+
"\n"+
"sectionradius = 100;  //radius of individual cloud sections\n"+
"\n"+
"\n"+
"\n"+
"\n"+
"\n"+
"for (var i=0; i < maxi; i++) \n"+
"{\n"+
"\n"+
"\n"+
"\n"+
"CloudStringA = '	Transform {		\\n' +\n"+
"'    scale '+ cumulusscale() + '               	\\n' +\n"+
"'    translation '+ cumulustranslation() + '    \\n' +    // cloud placement\n"+
"'    children [	                                \\n';\n"+
"\n"+
"\n"+
"CloudStringB = new Array();\n"+
"CloudStringF = new Array();\n"+
"\n"+
"   	for (var j=0; j < maxj; j++)\n"+
"   	{\n"+
"\n"+
"	radius = 0;\n"+
"\n"+
"	CloudStringB[j]= '  Transform {		    	       \\n' +\n"+
"	'    translation '+ cumulussectiontranslation() + '    \\n' +     // section placement\n"+
"	'    children [	                                       \\n';\n"+
"\n"+
"	\n"+
"	CloudStringC = new Array();\n"+
"	image = new String();\n"+
"\n"+
"      		for (var k=1; k < maxk; k++)  // maxk value denotes how many textured billboards make up the cloud \n"+
"      		{\n"+
"\n"+
"\n"+
"		randomtheta = 6.28319*Math.random();\n"+
"		randomphi = 1.57079*Math.random();\n"+
"		radius = radius+(sectionradius/maxk); // radius incremental steps based on billow radius and max billboards\n"+
"\n"+
"		X = radius*Math.cos(randomtheta)*Math.sin(randomphi);\n"+
"		Z = radius*Math.sin(randomtheta)*Math.sin(randomphi);\n"+
"		Y = radius*Math.cos(randomphi);\n"+
"\n"+
"\n"+
"		if (Y <= 30) //cloud shading and lighting control\n"+
"  	{	\n"+
"	image = ' \\\"CloudTexture1_5.png\\\" \\\"https://savage.nps.edu/Savage/Environment/Spheretexture.png\\\" \\n';\n"+
"  	}\n"+
"\n"+
"  		else\n"+
"  	{	\n"+
"	image = ' \\\"CloudTexture1_4.png\\\" \\\"https://savage.nps.edu/Savage/Environment/Spheretexture.png\\\" \\n';\n"+
"  	}\n"+
"\n"+
"	\n"+
"		\n"+
"		Billboardtranslation = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"		CloudStringC[k] = '	Transform {		                \\n' +\n"+
"		'            translation '+ Billboardtranslation   + '          \\n' +     // random billboard placement within radius designated above\n"+
"		'	  children [	                                        \\n' +\n"+
"		'	      Billboard {	                                \\n' +\n"+
"		'	        axisOfRotation 0 0 0	                        \\n' +     // 0 0 0 designates rotation on all axis\n"+
"		'	        children [	                                \\n' +\n"+
"		'	            Transform {	                		\\n' +\n"+
"		'	              rotation  0 0 0 0 		        \\n' +     // a rotation of the individual billboards can be defined\n"+
"		'	              children [	                        \\n' +\n"+
"		'	                  Shape {	                        \\n' +\n"+
"		'	                    appearance Appearance {	        \\n' +\n"+
"		'				material Material {		\\n' +\n"+
"		'				                }  		\\n' +\n"+
"		'	                      texture ImageTexture {	        \\n' +\n"+
"		'	                        url [ ' + image + ' ]           \\n' + \n"+
"		'	                      }	                                \\n' +\n"+
"		'	                    }	                                \\n' +\n"+
"		'	                    geometry IndexedFaceSet {	        \\n' +     // define type of geometry to texture\n"+
"		'	                      coordIndex [ 0, 1, 2, 3 ]	        \\n' +\n"+
"		'			      solid FALSE		        \\n' +\n"+
"		'	                      coord Coordinate {	        \\n' +\n"+
"		'	                        point [ 50 50 0,	        \\n' +     // define size of the geometry. Here 100 meter 2D square.\n"+
"		'	                                50 -50 0,	        \\n' +\n"+
"		'	                               -50 -50 0,	        \\n' +\n"+
"		'	                               -50 50 0 ]	        \\n' +\n"+
"		'	                      }	                                \\n' +\n"+
"		'	                    }	                                \\n' +\n"+
"		'	                  }	                                \\n' +\n"+
"		'	              ]	                                        \\n' +\n"+
"		'	            }	                                        \\n' +\n"+
"		'	       ]	                                        \\n' +\n"+
"		'	   }	                                                \\n' +\n"+
"		'      ]	                                                \\n' +\n"+
"		'     }	                                                        \\n';      \n"+
"		\n"+
"\n"+
"		}\n"+
"\n"+
"	CloudStringD = CloudStringC.join(' ');\n"+
"\n"+
"	\n"+
"	CloudStringE = '   ]	                 \\n' +\n"+
"	'	}	                         \\n';\n"+
"\n"+
"	CloudStringF[j] = CloudStringB[j] + CloudStringD +CloudStringE;\n"+
"\n"+
"\n"+
"	}\n"+
"\n"+
"CloudStringG = CloudStringF.join(' ');\n"+
"\n"+
"CloudStringH = '      ]	                                        \\n' +\n"+
"'     }	                                                        \\n' +\n"+
"'#########################################################      \\n';\n"+
"\n"+
"CloudString = CloudStringA + CloudStringG + CloudStringH;\n"+
"\n"+
"\n"+
"\n"+
"newNode = Browser.createVrmlFromString(CloudString);\n"+
"Cumulus.children[i] = newNode[0];\n"+
"\n"+
"\n"+
"   }\n"+
"\n"+
"}\n"+
"\n"+
"function cirrus()\n"+
"\n"+
"{\n"+
"\n"+
"maxi = 2;  // number of clouds\n"+
"\n"+
"maxj = 5; // denotes how many portions affecting the size of the cloud\n"+
"\n"+
"maxk = 8;  // number of billboards indicating cloud density\n"+
"\n"+
"sectionradius = 1000;  //radius of individual cloud sections\n"+
"\n"+
"\n"+
"\n"+
"\n"+
"\n"+
"for (var i=0; i < maxi; i++) \n"+
"{\n"+
"\n"+
"\n"+
"\n"+
"CloudStringA = '	Transform {		 \\n' +\n"+
"'    scale '+ cirrusscale() + '               	 \\n' +\n"+
"'    translation '+ cirrustranslation() + '      \\n' +    // cloud placement\n"+
"'    children [	                                 \\n';\n"+
"\n"+
"\n"+
"CloudStringB = new Array();\n"+
"CloudStringF = new Array();\n"+
"\n"+
"   	for (var j=0; j < maxj; j++)\n"+
"   	{\n"+
"\n"+
"	radius = 0;\n"+
"\n"+
"	CloudStringB[j]= '  Transform {		    	      \\n' +\n"+
"	'    translation '+ cirrussectiontranslation() + '    \\n' +     // section placement\n"+
"	'    children [	                                      \\n';\n"+
"\n"+
"	\n"+
"	CloudStringC = new Array();\n"+
"\n"+
"      		for (var k=1; k < maxk; k++)  // maxk value denotes how many textured billboards make up the cloud \n"+
"      		{\n"+
"\n"+
"\n"+
"		randomtheta = 6.28319*Math.random();\n"+
"		randomphi = 1.57079*Math.random();\n"+
"		radius = radius+(sectionradius/maxk); // radius incremental steps based on section radius and max billboards\n"+
"\n"+
"		X = radius*Math.cos(randomtheta)*Math.sin(randomphi);\n"+
"		Z = radius*Math.sin(randomtheta)*Math.sin(randomphi);\n"+
"		Y = radius*Math.cos(randomphi);\n"+
"		\n"+
"		Billboardtranslation = new String(X+' '+Y+' '+Z);\n"+
"\n"+
"		CloudStringC[k] = '	Transform {		                \\n' +\n"+
"		'            translation '+ Billboardtranslation   + '          \\n' +     // random billboard placement within radius designated above\n"+
"		'	  children [	                                        \\n' +\n"+
"		'	      Billboard {	                                \\n' +\n"+
"		'	        axisOfRotation 0 0 0	                        \\n' +     // 0 0 0 designates rotation on all axis\n"+
"		'	        children [	                                \\n' +\n"+
"		'	            Transform {	                		\\n' +\n"+
"		'	              rotation '  + rotation() + '	        \\n' +\n"+
"		'	              children [	                        \\n' +\n"+
"		'	                  Shape {	                        \\n' +\n"+
"		'	                    appearance Appearance {	        \\n' +\n"+
"		'			    material Material {			\\n' +\n"+
"		'			    }					\\n' +\n"+
" 		'	                      texture ImageTexture {	        \\n' +\n"+
"		'	                        url [\\\"cloudtexture3.png\\\" \\\"https://savage.nps.edu/Savage/Environment/cloudtexture1_4.png\\\" ] \\n' +\n"+
"		'	                      }	                                \\n' +\n"+
"		'	                    }	                                \\n' +\n"+
"		'	                    geometry IndexedFaceSet {	        \\n' +     // define type of geometry to texture\n"+
"		'	                      coordIndex [ 0, 1, 2, 3 ]	        \\n' +\n"+
"		'			      solid FALSE		        \\n' +\n"+
"		'	                      coord Coordinate {	        \\n' +\n"+
"		'	                        point [ 500 500 0,	        \\n' +     // define size of the geometry. Here 100 meter 2D square.\n"+
"		'	                                500 -500 0,	        \\n' +\n"+
"		'	                               -500 -500 0,	        \\n' +\n"+
"		'	                               -500 500 0 ]	        \\n' +\n"+
"		'	                      }	                                \\n' +\n"+
"		'	                    }	                                \\n' +\n"+
"		'	                  }	                                \\n' +\n"+
"		'	              ]	                                        \\n' +\n"+
"		'	            }	                                        \\n' +\n"+
"		'	       ]	                                        \\n' +\n"+
"		'	   }	                                                \\n' +\n"+
"		'      ]	                                                \\n' +\n"+
"		'     }	                                                        \\n';      \n"+
"		\n"+
"\n"+
"		}\n"+
"\n"+
"	CloudStringD = CloudStringC.join(' ');\n"+
"\n"+
"	CloudStringE = '   ]	                 \\n' +\n"+
"	'	}	                         \\n';\n"+
"\n"+
"	CloudStringF[j] = CloudStringB[j] + CloudStringD +CloudStringE;\n"+
"\n"+
"\n"+
"	}\n"+
"\n"+
"CloudStringG = CloudStringF.join(' ');\n"+
"\n"+
"CloudStringH = '      ]	                                        \\n' +\n"+
"'     }	                                                        \\n' +\n"+
"'#########################################################      \\n';\n"+
"\n"+
"CloudString = CloudStringA + CloudStringG + CloudStringH;\n"+
"\n"+
"\n"+
"\n"+
"newNode = Browser.createVrmlFromString(CloudString);\n"+
"Cirrus.children[i] = newNode[0];\n"+
"\n"+
"  }\n"+
"\n"+
"}\n"+
"\n"+
"\n"+
"function initialize()\n"+
"\n"+
"{\n"+
"\n"+
"cumulus();\n"+
"\n"+
"cirrus();\n"+
"}\n"+
"''')
Group28.addChildren(Script32)
DirectionalLight38 = DirectionalLight()
DirectionalLight38.setAmbientIntensity(1)
DirectionalLight38.setColor([1,0,0])
DirectionalLight38.setDirection([-1,-1,0])
DirectionalLight38.setGlobal(True)
Group28.addChildren(DirectionalLight38)
Scene11.addChildren(Group28)
X3D0.setScene(Scene11)
