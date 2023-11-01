from X3Dpackage import *
X3D0 = X3D(profile="Immersive", version="3.0",    head1 = head(    meta2 = meta(content="F16.x3d", name="title"), 
    meta3 = meta(content="F-16, The Fighting Falcon, Turkish Air Force (TUAF), Turkey", name="description"), 
    meta4 = meta(content="Murat ONDER, LTJG, Turkish Navy", name="creator"), 
    meta5 = meta(content="The coordinates of the main body (Except landing gears, nose antenna, flag, weapons, missile holders, cockpit, cockpit seat and fuel tanks) are mostly similar to the model of Soji Yamakawa and used with permission.", name="creator"), 
    meta6 = meta(content="13 July 2003", name="created"), 
    meta7 = meta(content="27 November 2015", name="modified"), 
    meta8 = meta(content="http://www.fas.org/man/dod-101/sys/ac/f-16.htm", name="reference"), 
    meta9 = meta(content="Here is a copy of the permission for the usage of the main hull; -----Original Message----- From: Soji Yamakawa [mailto:soji@andrew.cmu.edu] Sent: Tuesday, September 16, 2003 8:00 PM To: Onder, Murat TUR Subject: Re: VRML model points usage permission Sure. No problem. Soji ----- Original Message ----- From: \"Murat Onder\" <monder@nps.navy.mil> To: <Soji_Yamakawa@cmu.edu>; <PEB01130@nifty.ne.jp> Sent: Monday, September 15, 2003 3:50 PM Subject: VRML model points usage permission Hi Sir, I&apos;m a MS student in Naval Postgraduate School. I'm making a model of Turkish F-16 for my project in a VRML course. For the main hull of the F-16, I want to use the coordinate points of your VRML model since I think that model represents well enough F-16. This is going to be only a student project and will not be used for any commercial purposes. Of course I'll make the citation and put the reference links to your page in the meta files of x3d file. I'd like to know if you can give permission to use those points in my model. V/R, Murat Onder LTJG, TU NAVY", name="permission"), 
    meta10 = meta(content="The landing gears are taken from the Savage Archive, from F18 Blue Angel, then modified and re-animated.", name="reference"), 
    meta11 = meta(content="\"Drawing.jpg\" \"../../../Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Drawing.jpg\" \"https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Drawing.jpg\"", name="drawing"), 
    meta12 = meta(content="\"FrontView.jpg\" \"FrontView2.jpg\" \"Missiles.jpg\" \"../../../Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontView.jpg\" \"https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontView.jpg\" \"../../../Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontView2.jpg\" \"https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontView2.jpg\" \"../../../Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Missiles.jpg\" \"https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Missiles.jpg\"", name="Image"), 
    meta13 = meta(content="https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/F16.x3d", name="identifier"), 
    meta14 = meta(content="F16, F-16, Fighting Falcon", name="subject"), 
    meta15 = meta(content="X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit", name="generator"), 
    meta16 = meta(content="../../license.html", name="license")), 
   Scene17 = Scene(    Transform18 = Transform(DEF="F16Transform",      Transform19 = Transform(DEF="MainFrameTransform", scale=[3,3,3],       Shape20 = Shape(DEF="Nose",        Appearance21 = Appearance(        Material22 = Material(diffuseColor=[.25,.25,.25])), 
       IndexedFaceSet23 = IndexedFaceSet(coordIndex=[24,0,3,-1,4,0,24,-1,25,26,27,-1,28,25,27,-1,27,29,28,-1,27,30,29,-1,27,31,30,-1,3,18,24,-1], creaseAngle=0.5, normalIndex=[16,0,3,-1,4,0,16,-1,17,17,17,-1,18,18,18,-1,19,19,19,-1,20,20,20,-1,21,21,21,-1,3,14,16,-1], solid=False,         Coordinate24 = Coordinate(DEF="coordinates", point=[-0.32,0.36,-4.91,-0.38,0.43,-4.21,0,0.6,-4.2,0,0.5,-4.9,-0.5,0,-4.9,-0.6,0,-4.2,1,0,5.8,1,0,5.3,2.8,-0.4,6.3,2.8,-0.4,6.61,0.31,-0.36,-4.9,0.4,-0.35,-4.2,0,-0.4,-4.2,0,-0.4,-4.9,-0.31,-0.36,-4.9,-0.4,-0.35,-4.2,0.5,0,-4.9,0.6,0,-4.2,0.32,0.36,-4.91,0.38,0.43,-4.21,-1,0,5.8,-1,0,5.3,-2.8,-0.4,6.3,-2.8,-0.4,6.61,0,-0.1,-7,-0.31,-0.36,-4.9,-0.5,0,-4.9,0,-0.1,-7,0,-0.4,-4.9,0.31,-0.36,-4.9,0.5,0,-4.9,0.32,0.36,-4.91,-0.27,0.93,-3.51,0,1.1,-3.6,-0.33,0.5,-3.41,-0.34,0.9,-1.73,0,0.9,-1,0,1.1,-1.8,-0.38,0.64,-1.68,0.34,0.9,-1.73,0,0.9,-1,0.38,0.64,-1.68,0.34,0.9,-1.73,0.27,0.93,-3.51,0.33,0.5,-3.41,0,1.3,-2.8,0.45,1.02,-2.68,0.38,0.64,-1.68,0.53,0.5,-2.56,-0.53,0.5,-2.56,-0.45,1.02,-2.68,-0.53,0.75,0,-0.56,0.66,2.8,0,0.7,2.8,0,0.8,0,-1.1,0.3,0,-1,0.3,2.8,-0.37,0.57,4.9,0,0.59,4.9,-0.7,0.3,4.9,-0.7,0.3,4.9,-0.7,0,7,-0.5,0.49,7,-0.5,0.49,7,0,0.7,7,-1.4,0,0,-1.4,0,3.9,-1.4,0,3.9,-1,0,3.9,-1,0.3,2.8,-1,0.3,4.9,-0.59,0.65,-0.77,-0.8,0.3,-0.6,-1.4,0,-0.7,-1,-0.1,2.8,-0.7,-0.7,-2.5,-0.5,-0.9,-2.5,-0.5,-0.9,-0.6,-0.7,-0.7,-0.6,0,-1,-2.5,0,-1,-0.6,-0.72,-0.12,-2.5,-0.8,-0.3,-2.5,-0.8,-0.3,-0.6,-0.8,-0.3,-2.5,-0.8,-0.3,-0.6,-1.4,0,0,-1.4,0,-0.7,-0.7,-0.1,4.9,-1,-0.1,4.9,-0.5,-0.9,4.9,-0.7,-0.7,4.9,0,-1,4.9,-0.7,-0.1,4.9,-0.5,-0.5,7,-0.7,0,7,0,-0.7,7,-1,0,7.4,-2.8,-0.4,7.1,-2.57,-0.32,7.42,-4.9,0.1,4,-5.1,0.1,4,-5.1,-0.1,4,-4.9,-0.1,4,-5.1,0.1,1.6,-5.1,-0.1,1.6,-4.9,0.1,2.8,-4.9,-0.1,2.8,-0.58,-0.83,3.6,-0.72,-1.4,3.9,-0.69,-1.32,4.9,-0.58,-0.83,4.9,0.58,-0.83,3.6,0.72,-1.4,3.9,0.69,-1.32,4.9,0.58,-0.83,4.9,4.9,-0.1,2.8,5.1,-0.1,1.6,5.1,-0.1,4,4.9,-0.1,4,-0.8,0,-2.5,4.9,0.1,4,5.1,0.1,4,5.1,0.1,1.6,4.9,0.1,2.8,0.59,0.65,-0.77,0.8,0.3,-0.6,0.8,0,-2.5,-0.8,0,-2.5,0.8,-0.3,-0.6,0.72,-0.12,-2.5,0.8,0,-2.5,1,0,7.4,2.8,-0.4,7.1,2.57,-0.32,7.42,-0.7,0,7.4,0.5,-0.9,4.9,0.7,-0.7,4.9,0.5,-0.5,7,-4.9,0,2.8,-4.9,0,3.9,0.7,-0.1,4.9,0.7,0,7,1.4,0,0,4.9,0,2.8,4.9,0,3.9,1.4,0,3.9,1.4,0,-0.7,1.4,0,-0.7,0.7,-0.7,-0.6,0.8,-0.3,-0.6,0.5,-0.9,-0.6,1,-0.1,4.9,1,0.3,4.9,0.7,0,7.4,0.7,0.3,4.9,0.7,-0.1,4.9,0.56,0.66,2.8,0.53,0.75,0,1,0.3,2.8,1.1,0.3,0,0.37,0.57,4.9,0.7,0.3,4.9,0.5,0.49,7,0.7,0,7,0.5,0.49,7,1.4,0,3.9,1.4,0,0,1,0.3,2.8,1,0,3.9,1,-0.1,2.8,0.5,-0.9,-2.5,0.7,-0.7,-2.5,0.8,-0.3,-2.5,0.8,-0.3,-2.5,1,0.3,3.9,0.59,0.65,-0.77,0,0.7,2.8,0,1.4,4.5,0,0.59,4.9,0,3.5,6.8,0,3.5,8.1,0,1.4,7.3,0,0.7,7,0,0.7,7.3,-1,0.3,3.9,0,0.35,7.7,-0.25,0.24,7.7,-0.35,0,7.7,-0.25,-0.25,7.7,0,-0.35,7.7,0.25,-0.25,7.7,0.35,0,7.7,0.25,0.24,7.7,0,-0.2,-2.5,0.7,-0.7,-2.5,0.5,-0.9,-2.5,0,-1,-2.5,-0.5,-0.9,-2.5,-0.7,-0.7,-2.5,0,-0.2,-2.5,-0.72,-0.12,-2.5,0.72,-0.12,-2.5,0.25,0.24,7.7,0.35,0,7.7,-0.35,0,7.7,-0.25,0.24,7.7]), 
        Normal25 = Normal(DEF="normalVector", vector=[-0.68,0.714,-0.166,-0.689,0.721,-0.072,0,0.965,-0.26,0,0.985,-0.175,-0.99,-0.016,-0.138,-0.999,-0.022,-0.037,0.567,-0.819,-0.093,0.561,-0.828,0,0,-1,0,0,-0.997,-0.071,-0.567,-0.819,-0.093,-0.561,-0.828,0,0.99,-0.016,-0.138,0.999,-0.022,-0.037,0.68,0.714,-0.166,0.689,0.721,-0.072,-0.351,0.889,-0.294,-0.868,-0.459,-0.19,-0.13,-0.982,-0.14,0.13,-0.982,-0.14,0.868,-0.459,-0.19,0.872,0.431,-0.231,-0.834,0.445,-0.327,0,0.929,-0.369,-0.88,0.401,-0.256,-0.799,0.577,0.169,-0.58,0.798,0.164,0,0.998,0.065,-0.862,0.486,0.146,0.886,0.219,0.408,0.799,0.577,0.169,0.834,0.445,-0.327,0.88,0.401,-0.256,-0,0.995,-0.096,0.842,0.534,-0.08,0.862,0.486,0.146,0.833,0.549,-0.073,-0.833,0.549,-0.073,-0.842,0.534,-0.08,-0.485,0.87,-0.089,-0.37,0.929,0,0,1,0,-0,1,-0.01,-0.592,0.796,-0.125,-0.573,0.818,0.05,-0.37,0.929,-0.01,0,1,-0.025,-0.487,0.873,0.036,-0.923,0.381,0.05,-0.683,0.704,0.195,0,0.99,0.14,-0.707,0.707,0,-0.385,0.912,0.141,0,0.966,0.259,-0.563,0.826,-0.037,-0.661,0.738,-0.138,-0.521,0.846,-0.115,0,-0.996,0.09,-0.773,-0.436,-0.461,-0.42,-0.781,-0.463,-0.474,-0.881,0,-0.871,-0.492,0,0,-0.891,-0.455,-0.917,0.399,0,-0.881,0.074,-0.467,-0.902,-0.429,-0.039,-0.09,-0.995,0.05,-0.451,-0.892,0,-0.28,-0.959,0.04,-0.468,-0.878,0.097,-0.877,-0.474,0.085,0,-0.997,0.072,-0.693,-0.72,0.045,-0.79,-0.562,0.244,-0.968,0.003,0.25,0,-0.966,0.257,0,0,1,-1,0,0,0.987,0,-0.16,1,0,0,-0.831,-0.551,-0.08,0.563,0.826,-0.037,0.661,0.738,-0.138,0.998,-0.037,-0.049,-0.987,0,-0.16,-0.998,-0.037,-0.049,0.831,-0.551,-0.08,0,-0.999,0.04,0,0.993,0.12,0.468,-0.878,0.097,0.877,-0.474,0.085,0.79,-0.562,0.244,-0.419,-0.897,-0.14,0.693,-0.72,0.045,0.968,0.003,0.25,0.521,0.846,-0.115,0.419,-0.897,-0.14,0.871,-0.492,0,0.902,-0.429,-0.039,0.474,-0.881,0,0.37,0.929,0,0.485,0.87,-0.089,0.573,0.818,0.05,0.592,0.796,-0.125,0.37,0.929,-0.01,0.487,0.873,0.036,0.923,0.381,0.05,0.683,0.704,0.195,0.385,0.912,0.141,0.707,0.707,0,0.42,-0.781,-0.463,0.773,-0.436,-0.461,0.917,0.399,0,0.881,0.074,-0.467,0.09,-0.995,0.05,0.451,-0.892,0,0.28,-0.959,0.04,0.42,0.901,-0.11,0,0.666,0.746,-0.481,0.468,0.741,-0.674,0,0.738,-0.475,-0.475,0.741,0,-0.674,0.738,0.475,-0.475,0.741,0.674,0,0.738,0.481,0.468,0.741,0,0,-1,0,-0.893,-0.45,-0.901,-0.224,-0.372,0.901,-0.224,-0.372,0.841,0.34,0.421,-0.841,0.34,0.421]))), 
      Shape26 = Shape(DEF="Canopy",        Appearance27 = Appearance(        Material28 = Material(diffuseColor=[.25,.25,.25], transparency=0.8)), 
       IndexedFaceSet29 = IndexedFaceSet(coordIndex=[2,32,33,-1,34,32,2,-1,35,36,37,-1,38,36,35,-1,39,40,41,-1,37,36,42,-1,2,43,44,-1,33,43,2,-1,45,37,42,46,-1,46,42,47,48,-1,33,45,46,43,-1,43,46,48,44,-1,34,49,50,32,-1,32,50,45,33,-1,49,38,35,50,-1,50,35,37,45,-1], creaseAngle=0.5, normalIndex=[2,22,23,-1,24,22,2,-1,25,26,27,-1,28,26,25,-1,29,29,29,-1,27,26,30,-1,2,31,32,-1,23,31,2,-1,33,27,30,34,-1,34,30,35,36,-1,23,33,34,31,-1,31,34,36,32,-1,24,37,38,22,-1,22,38,33,23,-1,37,28,25,38,-1,38,25,27,33,-1], solid=False,         Coordinate30 = Coordinate(USE="coordinates"), 
        Normal31 = Normal(USE="normalVector"))), 
      Shape32 = Shape(DEF="MainBodyAndWingEdges",        Appearance33 = Appearance(        Material34 = Material(diffuseColor=[.1796,.1914,.2382])), 
       IndexedFaceSet35 = IndexedFaceSet(coordIndex=[51,52,53,54,-1,55,56,52,51,-1,52,57,58,53,-1,56,59,57,52,-1,60,61,62,-1,57,59,63,-1,57,63,64,-1,58,57,64,-1,56,55,65,66,-1,67,68,69,-1,69,70,60,-1,71,54,36,-1,51,54,71,-1,72,51,71,-1,55,51,72,-1,72,73,55,-1,65,55,73,-1,68,67,74,-1,75,76,77,78,-1,76,79,80,77,-1,81,82,83,-1,84,75,78,85,-1,83,74,67,-1,67,86,87,83,-1,74,88,89,-1,88,74,83,-1,78,77,90,91,-1,77,80,92,90,-1,85,91,93,-1,85,78,91,-1,94,95,93,-1,94,93,91,-1,91,96,94,-1,96,91,90,-1,90,92,96,-1,100,101,102,103,-1,101,104,105,102,-1,104,106,107,105,-1,106,100,103,107,-1,106,104,101,100,-1,103,102,105,107,-1,116,117,118,119,-1,120,81,83,-1,121,122,123,124,-1,116,119,121,124,-1,48,125,126,127,-1,117,116,124,123,-1,128,72,71,49,-1,118,117,123,122,-1,119,118,122,121,-1,129,130,131,-1,89,88,135,97,-1,60,70,97,135,-1,70,89,97,-1,96,92,136,-1,136,137,96,-1,138,96,137,-1,120,83,87,-1,128,73,72,-1,137,141,138,-1,141,142,138,-1,126,147,127,-1,148,129,131,-1,137,149,150,-1,141,137,150,-1,136,92,80,151,-1,137,136,151,149,-1,132,152,153,-1,154,132,153,155,-1,132,154,156,152,-1,54,53,157,158,-1,158,157,159,160,-1,53,58,161,157,-1,157,161,162,159,-1,163,164,155,-1,165,162,161,-1,64,165,161,-1,64,161,58,-1,166,167,160,159,-1,168,169,146,-1,155,153,168,-1,36,54,125,-1,125,54,158,-1,125,158,126,-1,126,158,160,-1,160,147,126,-1,147,160,167,-1,170,146,169,-1,149,151,171,172,-1,151,80,79,171,-1,129,173,130,-1,150,149,172,174,-1,146,170,129,-1,129,148,143,146,-1,152,156,170,-1,129,170,156,-1,156,154,164,-1,154,155,164,-1,168,175,169,-1,175,153,152,169,-1,152,170,169,-1,48,47,125,-1,41,40,176,-1,71,38,49,-1,71,36,38,-1,61,135,88,-1,61,60,135,-1,68,185,69,-1,68,74,89,-1,68,89,70,185,-1], creaseAngle=0.5, normalIndex=[39,40,41,42,-1,43,44,40,39,-1,40,45,46,41,-1,44,47,45,40,-1,48,48,48,-1,45,47,49,-1,45,49,50,-1,46,45,50,-1,44,43,51,52,-1,53,53,53,-1,41,41,41,-1,54,42,26,-1,39,42,54,-1,55,39,54,-1,43,39,55,-1,55,56,43,-1,51,43,56,-1,57,57,57,-1,58,59,60,61,-1,59,62,8,60,-1,63,63,63,-1,64,58,61,65,-1,66,66,66,-1,67,67,67,67,-1,8,8,8,-1,68,68,68,-1,61,60,69,70,-1,60,8,71,69,-1,65,70,72,-1,65,61,70,-1,73,74,72,-1,73,72,70,-1,70,75,73,-1,75,70,69,-1,69,71,75,-1,76,76,76,76,-1,77,77,77,77,-1,78,78,78,78,-1,79,79,79,79,-1,41,41,41,41,-1,8,8,8,8,-1,8,8,8,8,-1,80,80,80,-1,41,41,41,41,-1,77,77,77,77,-1,36,81,82,83,-1,84,84,84,84,-1,85,55,54,37,-1,79,79,79,79,-1,76,76,76,76,-1,86,86,86,-1,87,87,87,87,-1,88,88,88,88,-1,77,77,77,-1,75,71,89,-1,89,90,75,-1,91,75,90,-1,92,92,92,-1,85,56,55,-1,90,93,91,-1,93,94,91,-1,82,95,83,-1,96,96,96,-1,90,97,98,-1,93,90,98,-1,89,71,8,99,-1,90,89,99,97,-1,79,79,79,-1,88,88,88,88,-1,87,87,87,87,-1,42,41,100,101,-1,101,100,102,103,-1,41,46,104,100,-1,100,104,105,102,-1,106,106,106,-1,107,105,104,-1,50,107,104,-1,50,104,46,-1,108,109,103,102,-1,53,53,53,-1,41,41,41,-1,26,42,81,-1,81,42,101,-1,81,101,82,-1,82,101,103,-1,103,95,82,-1,95,103,109,-1,57,57,57,-1,97,99,110,111,-1,99,8,62,110,-1,112,112,112,-1,98,97,111,113,-1,114,114,114,-1,115,115,115,115,-1,8,8,8,-1,116,116,116,-1,77,77,77,-1,77,77,77,-1,79,79,79,-1,79,79,79,79,-1,79,79,79,-1,36,35,81,-1,117,117,117,-1,54,28,37,-1,54,26,28,-1,79,79,79,-1,79,79,79,-1,77,77,77,-1,77,77,77,-1,77,77,77,77,-1], solid=False,         Coordinate36 = Coordinate(USE="coordinates"), 
        Normal37 = Normal(USE="normalVector"))), 
      Shape38 = Shape(DEF="ExhaustExitFlatPanel",        Appearance39 = Appearance(        Material40 = Material(diffuseColor=[.5,.5,.5])), 
       IndexedFaceSet41 = IndexedFaceSet(coordIndex=[186,187,188,189,190,-1,190,191,192,193,186,-1], creaseAngle=0.5, normalIndex=[118,119,120,121,122,-1,122,123,124,125,118,-1], solid=False,         Coordinate42 = Coordinate(USE="coordinates"), 
        Normal43 = Normal(USE="normalVector"))), 
      Shape44 = Shape(DEF="ExhaustEntranceFrontBottomPart",        Appearance45 = Appearance(        Material46 = Material(diffuseColor=[.2304,.2304,.2304])), 
       IndexedFaceSet47 = IndexedFaceSet(coordIndex=[194,130,173,195,196,197,-1,197,198,199,82,81,194,-1], creaseAngle=0.5, normalIndex=[126,126,126,126,126,126,-1,126,126,126,126,126,126,-1], solid=False,         Coordinate48 = Coordinate(USE="coordinates"), 
        Normal49 = Normal(USE="normalVector"))), 
      Shape50 = Shape(DEF="ThirdPartFromNoseUnderCanopy",        Appearance51 = Appearance(        Material52 = Material(diffuseColor=[.6,.6,.6])), 
       IndexedFaceSet53 = IndexedFaceSet(coordIndex=[12,200,201,15,-1,19,48,127,17,-1,15,201,128,5,-1,17,127,202,11,-1,11,202,200,12,-1,5,128,49,1,-1,48,19,44,-1,19,2,44,-1,34,1,49,-1,34,2,1,-1], creaseAngle=0.5, normalIndex=[8,127,128,11,-1,15,36,83,13,-1,11,128,85,5,-1,13,83,129,7,-1,7,129,127,8,-1,5,85,37,1,-1,36,15,32,-1,15,2,32,-1,24,1,37,-1,24,2,1,-1], solid=False,         Coordinate54 = Coordinate(USE="coordinates"), 
        Normal55 = Normal(USE="normalVector"))), 
      Shape56 = Shape(DEF="RearExhaustExitPartLastPartOfMainBody",        Appearance57 = Appearance(        Material58 = Material(diffuseColor=[.37,.37,.37], shininess=.5)), 
       IndexedFaceSet59 = IndexedFaceSet(coordIndex=[64,186,193,165,-1,203,204,164,163,-1,192,191,138,142,-1,191,190,96,138,-1,94,96,190,189,-1,95,94,189,188,-1,63,187,186,64,-1,62,61,205,206,-1], creaseAngle=0.5, normalIndex=[50,118,125,107,-1,130,130,130,130,-1,124,123,91,94,-1,123,122,75,91,-1,73,75,122,121,-1,74,73,121,120,-1,49,119,118,50,-1,131,131,131,131,-1], solid=False,         Coordinate60 = Coordinate(USE="coordinates"), 
        Normal61 = Normal(USE="normalVector"))), 
      Shape62 = Shape(DEF="WingsAndTail",        Appearance63 = Appearance(        Material64 = Material(emissiveColor=[.1796,.1914,.2382])), 
       IndexedFaceSet65 = IndexedFaceSet(colorPerVertex=False, coordIndex=[6,7,8,9,-1,9,8,7,6,-1,20,21,22,23,-1,23,22,21,20,-1,97,20,23,98,99,-1,99,98,23,20,97,-1,108,109,110,111,-1,111,110,109,108,-1,112,113,114,115,-1,115,114,113,112,-1,132,6,9,133,134,-1,134,133,9,6,132,-1,86,139,140,67,-1,67,140,139,86,-1,143,144,145,146,-1,146,145,144,143,-1,177,178,179,-1,179,178,177,-1,178,180,181,182,183,179,-1,179,183,182,181,180,178,-1,182,184,183,-1,183,184,182,-1,177,178,179,-1,179,178,177,-1,178,180,181,182,183,179,-1,179,183,182,181,180,178,-1,182,184,183,-1,183,184,182,-1], creaseAngle=0.5, normalIndex=[50,118,125,107,-1,130,130,130,130,-1,124,123,91,94,-1,123,122,75,91,-1,73,75,122,121,-1,74,73,121,120,-1,49,119,118,50,-1,131,131,131,131,-1], solid=False,         Coordinate66 = Coordinate(USE="coordinates"), 
        Normal67 = Normal(USE="normalVector"))), 
      Shape68 = Shape(DEF="SecondPartAfterNose",        Appearance69 = Appearance(        Material70 = Material(diffuseColor=[.6,.6,.6])), 
       IndexedFaceSet71 = IndexedFaceSet(coordIndex=[0,1,2,3,-1,4,5,1,0,-1,10,11,12,13,-1,14,15,5,4,-1,13,12,15,14,-1,16,17,11,10,-1,18,19,17,16,-1,3,2,19,18,-1], creaseAngle=0.5, normalIndex=[0,1,2,3,-1,4,5,1,0,-1,6,7,8,9,-1,10,11,5,4,-1,9,8,11,10,-1,12,13,7,6,-1,14,15,13,12,-1,3,2,15,14,-1], solid=False,         Coordinate72 = Coordinate(USE="coordinates"), 
        Normal73 = Normal(USE="normalVector")))), 
     Transform74 = Transform(DEF="CockpitTransform", rotation=[1,0,0,-0.1], scale=[0.045,0.045,0.045], translation=[0,1,-10],       Inline75 = Inline(url=["Cockpit.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Cockpit.x3d","Cockpit.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Cockpit.wrl"])), 
     Transform76 = Transform(DEF="SeatTransform", rotation=[-1,0,0,-0.1], scale=[0.9,0.9,0.9], translation=[0,0,-8.3],       Inline77 = Inline(url=["Seat.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Seat.x3d","Seat.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Seat.wrl"])), 
     Transform78 = Transform(DEF="FrontWheelTransform", center=[0,2.5,0], rotation=[-1,0,0,1.92], translation=[0.7,-5.2,-6.5],       # Front wheel is taken from the Savage Library, modified and re-animated.(from F18 Blue Angel) 

      Inline79 = Inline(url=["FrontWheel.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontWheel.x3d","FrontWheel.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FrontWheel.wrl"])), 
     Transform80 = Transform(DEF="RearLeftWheelTransform", center=[0,2.5,0], rotation=[1,0,1,1.92], translation=[-2.95,-5,7],       # Rear wheels are taken from the Savage Library and re-animated (from F18 Blue Angel) 

      Inline81 = Inline(url=["RearLeftWheel.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/RearLeftWheel.x3d","RearLeftWheel.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/RearLeftWheel.wrl"])), 
     Transform82 = Transform(DEF="RearRightWheelTransform", center=[0,2.5,0], rotation=[-1,0,-1,1.92], translation=[2.95,-5,7],       # Rear wheels are taken from the Savage Library and re-animated (from F18 Blue Angel) 

      Inline83 = Inline(url=["RearRightWheel.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/RearRightWheel.x3d","RearRightWheel.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/RearRightWheel.wrl"])), 
     Transform84 = Transform(DEF="CockpitButtonsTransform",       Transform85 = Transform(DEF="UpButtonTransform", rotation=[1,0,0,1.57], scale=[.008,.008,.008], translation=[-0.95,1.05,-10],        Shape86 = Shape(        Cylinder87 = Cylinder(height=1, radius=4), 
        Appearance88 = Appearance(         Material89 = Material(diffuseColor=[1,0,0], shininess=.8))), 
       TouchSensor90 = TouchSensor(DEF="TouchSensorUp", description="click for gears up")), 
      Transform91 = Transform(DEF="DownButtonTransform", rotation=[1,0,0,1.57], scale=[.008,.008,.008], translation=[-0.83,1.05,-10],        Shape92 = Shape(        Cylinder93 = Cylinder(height=1, radius=4), 
        Appearance94 = Appearance(         Material95 = Material(diffuseColor=[1,1,0], shininess=.8))), 
       TouchSensor96 = TouchSensor(DEF="TouchSensorDown", description="click for gears down")), 
      Transform97 = Transform(DEF="GearUpTextTransform", scale=[.06,.06,.06], translation=[-.65,1.55,-10],        Shape98 = Shape(        Text99 = Text(string=["RED Button","Gear Up"]), 
        Appearance100 = Appearance(         Material101 = Material(diffuseColor=[1,0,0])))), 
      Transform102 = Transform(DEF="GearDownTextTransform", scale=[.06,.06,.06], translation=[-.65,1.35,-10],        Shape103 = Shape(        Text104 = Text(length=[5.5], string=["YELLOW Button","Gear Down"]), 
        Appearance105 = Appearance(         Material106 = Material(diffuseColor=[1,1,0])))), 
      Transform107 = Transform(DEF="FireButtonTransform", rotation=[1,0,0,1.57], scale=[.008,.008,.008], translation=[.52,1.6,-10],        Shape108 = Shape(        Cylinder109 = Cylinder(height=1, radius=4), 
        Appearance110 = Appearance(         Material111 = Material(diffuseColor=[0,.75,.18], shininess=.8))), 
       TouchSensor112 = TouchSensor(DEF="FireSensor", description="click to fire")), 
      Transform113 = Transform(DEF="FireTextTransform", scale=[.06,.06,.06], translation=[.36,1.5,-10],        Shape114 = Shape(        Text115 = Text(string=["Target Locked","      FIRE!..","(Green Button)"]), 
        Appearance116 = Appearance(         Material117 = Material(diffuseColor=[0,.75,.18]))))), 
     Viewpoint118 = Viewpoint(description="F16 Close Look-up", orientation=[-0.559,-0.827,-0.057,1.3534], position=[-28.7,19.9,17.4]), 
     Viewpoint119 = Viewpoint(description="Cockpit", orientation=[-1,0,0,0.1249], position=[0,1.5,-7.9]), 
     Viewpoint120 = Viewpoint(DEF="LandingGearAnimationView", description="Landing Gear Animation View", orientation=[-0.003,1,-0.012,2.5741], position=[16.1,-5.8,-24.6]), 
     Viewpoint121 = Viewpoint(description="Cockpit Left View", orientation=[-0.276,-0.922,-0.271,1.2338], position=[-6.7,6.1,-3.9]), 
     Viewpoint122 = Viewpoint(description="F-16 Front View", orientation=[-0.007,0.995,0.102,3.1152], position=[-0.1,13.4,-65]), 
     Viewpoint123 = Viewpoint(description="Cockpit Target View", orientation=[-0.834,-0.523,-0.176,0.0875], position=[0,2.4,-7.9]), 
     Transform124 = Transform(DEF="NoseAntennaTransform", rotation=[1,0,0,1.57], translation=[0,-.275,-21],       Shape125 = Shape(       Cylinder126 = Cylinder(radius=.05), 
       Appearance127 = Appearance(        Material128 = Material(diffuseColor=[.5,.5,.5], shininess=.5))))), 
    TimeSensor129 = TimeSensor(DEF="WheelUp", cycleInterval=8), 
    OrientationInterpolator130 = OrientationInterpolator(DEF="GearUpInterpolator", key=[0,0.5,1.0], keyValue=[1,0,0,0.0,1,0,0,-0.79,1,0,0,-1.92]), 
    ROUTE131 = ROUTE(fromField="touchTime", fromNode="TouchSensorUp", toField="set_startTime", toNode="WheelUp"), 
    ROUTE132 = ROUTE(fromField="fraction_changed", fromNode="WheelUp", toField="set_fraction", toNode="GearUpInterpolator"), 
    ROUTE133 = ROUTE(fromField="value_changed", fromNode="GearUpInterpolator", toField="set_rotation", toNode="FrontWheelTransform"), 
    TimeSensor134 = TimeSensor(DEF="WheelDown", cycleInterval=8), 
    OrientationInterpolator135 = OrientationInterpolator(DEF="GearDownInterpolator", key=[0,0.5,1.0], keyValue=[1,0,0,-1.92,1,0,0,-0.79,1,0,0,0.0]), 
    ROUTE136 = ROUTE(fromField="touchTime", fromNode="TouchSensorDown", toField="set_startTime", toNode="WheelDown"), 
    ROUTE137 = ROUTE(fromField="fraction_changed", fromNode="WheelDown", toField="set_fraction", toNode="GearDownInterpolator"), 
    ROUTE138 = ROUTE(fromField="value_changed", fromNode="GearDownInterpolator", toField="set_rotation", toNode="FrontWheelTransform"),     # Animation commands for Rear Right Wheel Starts 

    TimeSensor139 = TimeSensor(DEF="RRearUp1", cycleInterval=8), 
    TimeSensor140 = TimeSensor(DEF="RRearDown1", cycleInterval=8), 
    OrientationInterpolator141 = OrientationInterpolator(DEF="RRearInterUp1", key=[0,0.5,1.0], keyValue=[-1,0,-1,0.0,-1,0,-1,0.44,-1,0,-1,1.92]), 
    OrientationInterpolator142 = OrientationInterpolator(DEF="RRearInterDown1", key=[0,0.5,1.0], keyValue=[-1,0,-1,1.92,-1,0,-1,0.44,-1,0,-1,0.0]), 
    ROUTE143 = ROUTE(fromField="touchTime", fromNode="TouchSensorDown", toField="set_startTime", toNode="RRearDown1"), 
    ROUTE144 = ROUTE(fromField="touchTime", fromNode="TouchSensorUp", toField="set_startTime", toNode="RRearUp1"), 
    ROUTE145 = ROUTE(fromField="fraction_changed", fromNode="RRearDown1", toField="set_fraction", toNode="RRearInterDown1"), 
    ROUTE146 = ROUTE(fromField="fraction_changed", fromNode="RRearUp1", toField="set_fraction", toNode="RRearInterUp1"), 
    ROUTE147 = ROUTE(fromField="value_changed", fromNode="RRearInterDown1", toField="set_rotation", toNode="RearRightWheelTransform"), 
    ROUTE148 = ROUTE(fromField="value_changed", fromNode="RRearInterUp1", toField="set_rotation", toNode="RearRightWheelTransform"),     # Animation commands for Rear Left Wheel 

    TimeSensor149 = TimeSensor(DEF="LRearUp1", cycleInterval=8), 
    TimeSensor150 = TimeSensor(DEF="LRearDown1", cycleInterval=8), 
    OrientationInterpolator151 = OrientationInterpolator(DEF="LRearInterUp1", key=[0,0.5,1.0], keyValue=[1,0,1,0.0,1,0,1,0.44,1,0,1,1.92]), 
    OrientationInterpolator152 = OrientationInterpolator(DEF="LRearInterDown1", key=[0,0.5,1.0], keyValue=[1,0,1,1.92,1,0,1,0.44,1,0,1,0.0]), 
    ROUTE153 = ROUTE(fromField="touchTime", fromNode="TouchSensorDown", toField="set_startTime", toNode="LRearDown1"), 
    ROUTE154 = ROUTE(fromField="touchTime", fromNode="TouchSensorUp", toField="set_startTime", toNode="LRearUp1"), 
    ROUTE155 = ROUTE(fromField="fraction_changed", fromNode="LRearDown1", toField="set_fraction", toNode="LRearInterDown1"), 
    ROUTE156 = ROUTE(fromField="fraction_changed", fromNode="LRearUp1", toField="set_fraction", toNode="LRearInterUp1"), 
    ROUTE157 = ROUTE(fromField="value_changed", fromNode="LRearInterDown1", toField="set_rotation", toNode="RearLeftWheelTransform"), 
    ROUTE158 = ROUTE(fromField="value_changed", fromNode="LRearInterUp1", toField="set_rotation", toNode="RearLeftWheelTransform"), 
    Background159 = Background(groundAngle=[1.309,1.570796], groundColor=[0,0.3,.7,0,0.35,0.75,0,0.4,0.8], skyAngle=[1.309,1.571], skyColor=[0,0.3,0.8,0,0.5,1,1,1,1]), 
    Transform160 = Transform(DEF="RightmostAmraamTransform", rotation=[-1,0,0,1.57], scale=[1.4,1.4,1.4], translation=[15.65,0,4.5],      Inline161 = Inline(DEF="Amraam", url=["../../Weapons/Missiles/Amraam.x3d","https://savage.nps.edu/Savage/Weapons/Missiles/Amraam.x3d","../../Weapons/Missiles/Amraam.wrl","https://savage.nps.edu/Savage/Weapons/Missiles/Amraam.wrl"])), 
    Transform162 = Transform(DEF="LeftmostAmraamTransform", rotation=[-1,0,0,1.57], scale=[1.4,1.4,1.4], translation=[-15.65,0,4.5],      Inline163 = Inline(USE="Amraam")), 
    Transform164 = Transform(DEF="SidewinderHolderTransformRight", rotation=[0,1,0,1.57], scale=[6,3,3], translation=[9,-1.125,8],      Inline165 = Inline(DEF="SidewinderHolder", url=["SidewinderHolder.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/SidewinderHolder.x3d","SidewinderHolder.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/SidewinderHolder.wrl"])), 
    Transform166 = Transform(DEF="SidewinderHolderTransformLeft", rotation=[0,1,0,1.57], scale=[6,3,3], translation=[-8.45,-1.125,8],      Inline167 = Inline(USE="SidewinderHolder")), 
    Transform168 = Transform(DEF="TurkishFlagTransformLeft", rotation=[0,-1,0,1.57], scale=[.3,.25,.3], translation=[-.01,8,19.5],      Inline169 = Inline(url=["TurkishFlagLeft.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/TurkishFlagLeft.x3d","TurkishFlagLeft.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/TurkishFlagLeft.wrl"])), 
    Transform170 = Transform(DEF="TurkishFlagTransformRight", rotation=[0,1,0,1.57], scale=[.3,.25,.3], translation=[.01,8,20.5],      Inline171 = Inline(url=["TurkishFlagRight.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/TurkishFlagRight.x3d","TurkishFlagRight.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/TurkishFlagRight.wrl"])), 
    Transform172 = Transform(DEF="AmraamHolderTransformLeft", translation=[-12,-.176,10.7],      Inline173 = Inline(DEF="AmraamHolder", url=["AmraamHolder.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/AmraamHolder.x3d","AmraamHolder.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/AmraamHolder.wrl"])), 
    Transform174 = Transform(DEF="AmraamHolderTransformRight", translation=[12,-.176,10.7],      Inline175 = Inline(USE="AmraamHolder")), 
    Transform176 = Transform(DEF="AmraamInnerTransformRight", rotation=[-1,0,0,1.57], scale=[1.4,1.4,1.4], translation=[12,-1.6,4.5],      Inline177 = Inline(USE="Amraam")), 
    Transform178 = Transform(DEF="AmraamInnerTransformLeft", rotation=[-1,0,0,1.57], scale=[1.4,1.4,1.4], translation=[-12,-1.6,4.5],      Inline179 = Inline(USE="Amraam")), 
    Transform180 = Transform(DEF="SidewinderTransformLeft", rotation=[-1,0,0,1.57], scale=[1.6,1.6,1.6], translation=[-8.7,-2,3.5],      Inline181 = Inline(DEF="Sidewinder", url=["../../Weapons/Missiles/Sidewinder.x3d","https://savage.nps.edu/Savage/Weapons/Missiles/Sidewinder.x3d","../../Weapons/Missiles/Sidewinder.wrl","https://savage.nps.edu/Savage/Weapons/Missiles/Sidewinder.wrl"])), 
    Transform182 = Transform(DEF="SidewinderTransformRight", rotation=[-1,0,0,1.57], scale=[1.6,1.6,1.6], translation=[8.7,-2,3.5],      Inline183 = Inline(USE="Sidewinder")), 
    Transform184 = Transform(DEF="FuelTankHolderTransformLeft", rotation=[0,1,0,1.57], scale=[1.5,1.5,1.5], translation=[-4.8,-1.125,6],      Inline185 = Inline(DEF="FuelTankHolder", url=["FuelTankHolder.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FuelTankHolder.x3d","FuelTankHolder.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FuelTankHolder.wrl"])), 
    Transform186 = Transform(DEF="FuelTankHolderTransformRight", rotation=[0,1,0,1.57], scale=[1.5,1.5,1.5], translation=[5.3,-1.125,6],      Inline187 = Inline(USE="FuelTankHolder")), 
    Transform188 = Transform(DEF="FuelTankTransformRight", rotation=[-1,0,0,1.57], scale=[1.5,1.5,1.5], translation=[5,-2.85,5.5],      Inline189 = Inline(DEF="FuelTank", url=["FuelTank.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FuelTank.x3d","FuelTank.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/FuelTank.wrl"])), 
    Transform190 = Transform(DEF="FuelTankTransformLeft", rotation=[-1,0,0,1.57], scale=[1.5,1.5,1.5], translation=[-5,-2.85,5.5],      Inline191 = Inline(USE="FuelTank")), 
    Transform192 = Transform(DEF="InlineCoverOfPlaneTansform",      Shape193 = Shape(      Box194 = Box(size=[4.15,.1,20]), 
      Appearance195 = Appearance(       Material196 = Material(diffuseColor=[.25,.25,.25])))), 
    Transform197 = Transform(DEF="TargetHelicopterTransform", translation=[16,-50,-500],      Inline198 = Inline(url=["Target.x3d","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Target.x3d","Target.wrl","https://savage.nps.edu/Savage/AircraftFixedWing/F16-FightingFalcon-Turkey/Target.wrl"])), 
    TimeSensor199 = TimeSensor(DEF="FireClock", cycleInterval=8), 
    PositionInterpolator200 = PositionInterpolator(DEF="MissilePath", key=[0.0,.1,1.0], keyValue=[-15.65,0,4.5,-15.65,-2,4.5,16,-50,-500]), 
    ROUTE201 = ROUTE(fromField="touchTime", fromNode="FireSensor", toField="set_startTime", toNode="FireClock"), 
    ROUTE202 = ROUTE(fromField="fraction_changed", fromNode="FireClock", toField="set_fraction", toNode="MissilePath"), 
    ROUTE203 = ROUTE(fromField="value_changed", fromNode="MissilePath", toField="set_translation", toNode="LeftmostAmraamTransform"), 
    Viewpoint204 = Viewpoint(DEF="MissileLaunchView", description="Missile Fire View", orientation=[0.094,-0.994,0.057,1.1716], position=[-344.3,-142.8,-27.7]), 
    ROUTE205 = ROUTE(fromField="isActive", fromNode="FireSensor", toField="set_bind", toNode="MissileLaunchView"),     # TODO fix type, add filter 
))
