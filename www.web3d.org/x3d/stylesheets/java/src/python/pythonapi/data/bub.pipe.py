import X3Dpackage


X3D0 = (X3Dpackage.X3D().setProfile("Immersive").setVersion("3.3")
      .setHead(X3Dpackage.head()
        .addComponent(X3Dpackage.component().setName("Shaders").setLevel(1))
        .addComponent(X3Dpackage.component().setName("CubeMapTexturing").setLevel(1))
        .addMeta(X3Dpackage.meta().setName("title").setContent("bub.x3d"))
        .addMeta(X3Dpackage.meta().setName("creator").setContent("John Carlson"))
        .addMeta(X3Dpackage.meta().setName("description").setContent("3 prismatic spheres"))
        .addMeta(X3Dpackage.meta().setName("generator").setContent("X3D-Edit, https://savage.nps.edu/X3D-Edit"))
        .addMeta(X3Dpackage.meta().setName("identifier").setContent("https://coderextreme.net/X3DJSONLD/bub.x3d")))
      .setScene(X3Dpackage.Scene()
        .addChildren(X3Dpackage.NavigationInfo().setType(["EXAMINE","ANY"]))
        .addChildren(X3Dpackage.Background().setBackUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]).setBottomUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]).setFrontUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]).setLeftUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]).setRightUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]).setTopUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"]))
        .addChildren(X3Dpackage.Viewpoint().setPosition([0,0,20]).setDescription("Look at the bubbles flying"))
        .addChildren(X3Dpackage.ProtoDeclare().setName("Bubble")
          .setProtoBody(X3Dpackage.ProtoBody()
            .addChildren(X3Dpackage.Transform().setDEF("transform").setTranslation([0,0,0])
              .addChildren(X3Dpackage.Shape().setDEF("myShape")
                .setAppearance(X3Dpackage.Appearance()
                  .setMaterial(X3Dpackage.Material().setDiffuseColor([.7,.7,.7]).setSpecularColor([.5,.5,.5]))
                  .setTexture(X3Dpackage.ComposedCubeMapTexture().setDEF("texture")
                    .setBack(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_back.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_back.png"]))
                    .setBottom(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_bottom.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_bottom.png"]))
                    .setFront(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_front.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_front.png"]))
                    .setLeft(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_left.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_left.png"]))
                    .setRight(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_right.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_right.png"]))
                    .setTop(X3Dpackage.ImageTexture().setUrl(["../resources/images/all_probes/stpeters_cross/stpeters_top.png","https://coderextreme.net/X3DJSONLD/images/all_probes/stpeters_cross/stpeters_top.png"])))
                  #
#					<ComposedShader DEF='gl' language=\"GLSL\">
#					  <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/>
#					  <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/>
#					  <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/>
#
#					  <ShaderPart url='\"../shaders/gl.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/gl.vs\"' type='VERTEX'></ShaderPart>
#					  <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart>
#					</ComposedShader>
#					<ComposedShader DEF='freewrl' language=\"GLSL\">
#					  <field name='fw_textureCoodGenType' type='SFInt32' accessType=\"inputOutput\" value='0'/>
#					  <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/>
#					  <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/>
#
#					  <ShaderPart url='\"../shaders/freewrl.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/freewrl.vs\"' type='VERTEX'></ShaderPart>
#					  <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart>
#					</ComposedShader>
#					

                  .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL").setDEF("x3dom")
                    .addField(X3Dpackage.field().setName("cube").setType("SFInt32").setAccessType("inputOutput").setValue("0"))
                    .addField(X3Dpackage.field().setName("chromaticDispertion").setType("SFVec3f").setAccessType("inputOutput").setValue("0.98 1.0 1.033"))
                    .addField(X3Dpackage.field().setName("bias").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                    .addField(X3Dpackage.field().setName("scale").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                    .addField(X3Dpackage.field().setName("power").setType("SFFloat").setAccessType("inputOutput").setValue("2.0"))
                    .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/x3dom.vs","https://coderextreme.net/X3DJSONLD/shaders/x3dom.vs"]).setType("VERTEX"))
                    .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs"]).setType("FRAGMENT")))
                  #
#					<ComposedShader DEF='instant' language=\"GLSL\">
#					  <field name='cube' type='SFInt32' accessType=\"inputOutput\" value='0'/>
#					  <field name='chromaticDispertion' type='SFVec3f' accessType=\"inputOutput\" value='0.98 1.0 1.033'/>
#					  <field name='bias' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='scale' type='SFFloat' accessType=\"inputOutput\" value='0.5'/>
#					  <field name='power' type='SFFloat' accessType=\"inputOutput\" value='2.0'/>
#
#                              <ShaderPart url='\"../shaders/instant.vs\" \"https://coderextreme.net/X3DJSONLD/shaders/instant.vs\"' type='VERTEX'></ShaderPart>
#                              <ShaderPart url='\"../shaders/pc_bubbles.fs\" \"https://coderextreme.net/X3DJSONLD/shaders/pc_bubbles.fs\"' type='FRAGMENT'></ShaderPart>
#                            </ComposedShader>
#                            

                  .addShaders(X3Dpackage.ComposedShader(setLanguage = "GLSL").setDEF("cobweb")
                    .addField(X3Dpackage.field().setName("cube").setType("SFNode").setAccessType("inputOutput")
                      .addChildren(X3Dpackage.ComposedCubeMapTexture().setUSE("texture")))
                    .addField(X3Dpackage.field().setName("chromaticDispertion").setType("SFVec3f").setAccessType("inputOutput").setValue("0.98 1.0 1.033"))
                    .addField(X3Dpackage.field().setName("bias").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                    .addField(X3Dpackage.field().setName("scale").setType("SFFloat").setAccessType("inputOutput").setValue("0.5"))
                    .addField(X3Dpackage.field().setName("power").setType("SFFloat").setAccessType("inputOutput").setValue("2.0"))
                    .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/cobweb.vs","https://coderextreme.net/X3DJSONLD/shaders/cobweb.vs"]).setType("VERTEX"))
                    .addParts(X3Dpackage.ShaderPart().setUrl(["../shaders/pc_bubbles.fs","https://coderextreme.net/X3DJSONLD/shaders/pc.fs"]).setType("FRAGMENT"))))
                .setGeometry(X3Dpackage.Sphere())))
            .addChildren(X3Dpackage.Script().setDEF("Bounce")
              .addField(X3Dpackage.field().setName("translation").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
              .addField(X3Dpackage.field().setName("velocity").setAccessType("inputOutput").setType("SFVec3f").setValue("0 0 0"))
              .addField(X3Dpackage.field().setName("set_fraction").setAccessType("inputOnly").setType("SFTime")).setSourceCode('''ecmascript:\n"+
"			function initialize() {\n"+
"			    translation = new SFVec3f(0, 0, 0);\n"+
"			    velocity = new SFVec3f(\n"+
"			    	Math.random() - 0.5,\n"+
"				Math.random() - 0.5,\n"+
"				Math.random() - 0.5);\n"+
"			}\n"+
"			function set_fraction() {\n"+
"			    translation = new SFVec3f(\n"+
"			    	translation.x + velocity.x,\n"+
"				translation.y + velocity.y,\n"+
"				translation.z + velocity.z);\n"+
"			    if (Math.abs(translation.x) > 10) {\n"+
"				initialize();\n"+
"			    } else if (Math.abs(translation.y) > 10) {\n"+
"				initialize();\n"+
"			    } else if (Math.abs(translation.z) > 10) {\n"+
"				initialize();\n"+
"			    } else {\n"+
"				velocity.x += Math.random() * 0.2 - 0.1;\n"+
"				velocity.y += Math.random() * 0.2 - 0.1;\n"+
"				velocity.z += Math.random() * 0.2 - 0.1;\n"+
"			    }\n"+
"			}\n"+
"               ''')
)
            .addChildren(X3Dpackage.TimeSensor().setDEF("TourTime").setCycleInterval(0.150).setLoop(True))
            .addChildren(X3Dpackage.ROUTE().setFromNode("TourTime").setFromField("cycleTime").setToNode("Bounce").setToField("set_fraction"))
            .addChildren(X3Dpackage.ROUTE().setFromNode("Bounce").setFromField("translation_changed").setToNode("transform").setToField("set_translation"))))
        .addChildren(X3Dpackage.ProtoInstance().setName("Bubble"))
        .addChildren(X3Dpackage.ProtoInstance().setName("Bubble"))
        .addChildren(X3Dpackage.ProtoInstance().setName("Bubble"))))

