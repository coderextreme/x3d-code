import org.web3d.x3d.jsail.Core.*;
import org.web3d.x3d.jsail.fields.*;
import org.web3d.x3d.jsail.Geometry3D.*;
import org.web3d.x3d.jsail.Grouping.*;
import org.web3d.x3d.jsail.Navigation.*;
import org.web3d.x3d.jsail.Shape.*;
import org.web3d.x3d.jsail.Text.*;
import org.web3d.x3d.jsail.Texturing.*;

// Javadoc annotations follow, see below for Java source code.
/**
 * <p> Special test case: simple X3D scene example: Hello World!. </p>
 <p> Related links: <a href="../../../Chapter01-TechnicalOverview/HelloWorld.java">HelloWorld.java</a> source, <a href="../../../Chapter01-TechnicalOverview/HelloWorldIndex.html" target="_top">HelloWorld catalog page</a>, <a href="https://www.web3d.org/x3d/content/examples/X3dResources.html" target="_blank">X3D Resources</a>, <a href="https://www.web3d.org/x3d/content/examples/X3dSceneAuthoringHints.html" target="_blank">X3D Scene Authoring Hints</a>, and <a href="https://www.web3d.org/x3d/content/X3dTooltips.html" target="_blank">X3D Tooltips</a>. </p>
	<table style="color:black; border:0px solid; border-spacing:10px 0px;">
        <caption>Scene Meta Information</caption>
		<tr style="background-color:silver; border-color:silver;">
			<td style="text-align:center; padding:10px 0px;"><i>meta tags</i></td>
			<td style="text-align:left;   padding:10px 0px;">&nbsp; Document Metadata </td>
		</tr>

		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> title </i> </td>
			<td> <a href="../../../Chapter01-TechnicalOverview/HelloWorld.x3d">HelloWorld.x3d</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> description </i> </td>
			<td> Special test case: simple X3D scene example: Hello World! </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> created </i> </td>
			<td> 30 October 2000 </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> modified </i> </td>
			<td> 16 April 2018 </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> creator </i> </td>
			<td> Don Brutzman </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> Image </i> </td>
			<td> <a href="../../../Chapter01-TechnicalOverview/images/HelloWorld.tall.png">images/HelloWorld.tall.png</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> <a href="http://en.wikipedia.org/wiki/Hello_world" target="_blank">http://en.wikipedia.org/wiki/Hello_world</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> <a href="http://en.wikipedia.org/wiki/Hello#%22Hello,_World%22_computer_program" target="_blank">http://en.wikipedia.org/wiki/Hello#"Hello,_World"_computer_program</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> <a href="http://en.wikibooks.org/w/index.php?title=Computer_Programming/Hello_world" target="_blank">http://en.wikibooks.org/w/index.php?title=Computer_Programming/Hello_world</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> <a href="http://www.HelloWorldExample.net" target="_blank">http://www.HelloWorldExample.net</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> <a href="http://www.web3D.org" target="_blank">http://www.web3D.org</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> <a href="http://www.web3d.org/realtime-3d/news/internationalization-x3d" target="_blank">http://www.web3d.org/realtime-3d/news/internationalization-x3d</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> <a href="http://www.web3d.org/x3d/content/examples/HelloWorld.x3d" target="_blank">http://www.web3d.org/x3d/content/examples/HelloWorld.x3d</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> <a href="http://X3dGraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes" target="_blank">http://X3dGraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> identifier </i> </td>
			<td> <a href="http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter01-TechnicalOverview/HelloWorld.x3d" target="_blank">http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter01-TechnicalOverview/HelloWorld.x3d</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> license </i> </td>
			<td> <a href="http://www.web3d.org/x3d/content/examples/license.html" target="_blank">http://www.web3d.org/x3d/content/examples/license.html</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> generator </i> </td>
			<td> X3D-Edit 3.3, <a href="https://savage.nps.edu/X3D-Edit" target="_blank">https://savage.nps.edu/X3D-Edit</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> HelloWorld.wrl </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> <a href="../../../Chapter01-TechnicalOverview/HelloWorld.x3dv">HelloWorld.x3dv</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> <a href="../../../Chapter01-TechnicalOverview/HelloWorld.x3db">HelloWorld.x3db</a> </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> HelloWorld.xhtml </td>
		</tr>
		<tr>
			<td style="text-align:right; vertical-align: text-top;"> <i> reference </i> </td>
			<td> <a href="../../../Chapter01-TechnicalOverview/HelloWorld.json">HelloWorld.json</a> </td>
		</tr>
		<tr style="background-color:silver; border-color:silver;">
			<td style="text-align:center;" colspan="2">  &nbsp; </td>
		</tr>
	</table>

	<p>
		This program uses the
		<a href="https://www.web3d.org/specifications/java/X3DJSAIL.html" target="_blank">X3D Java Scene Access Interface Library (X3DJSAIL)</a>.
		It has been produced using the 
		<a href="https://www.web3d.org/x3d/stylesheets/X3dToJava.xslt" target="_blank">X3dToJava.xslt</a>
		stylesheet to create Java source code from an <code>.x3d</code> model.
	</p>

	* @author Don Brutzman
 */

public class HelloWorld
{
	/** Default constructor to create this object. */
	public HelloWorld ()
	{
	  initialize();
	}

	/** Create and initialize the X3D model for this object. */
	public final void initialize()
	{
  x3dModel = new X3D().setProfile(X3D.PROFILE_IMMERSIVE).setVersion(X3D.VERSION_3_3)
  .setHead(new head()
    .addMeta(new meta().setName(meta.NAME_TITLE      ).setContent("HelloWorld.x3d"))
    .addMeta(new meta().setName(meta.NAME_DESCRIPTION).setContent("Special test case: simple X3D scene example: Hello World!"))
    .addMeta(new meta().setName(meta.NAME_CREATED    ).setContent("30 October 2000"))
    .addMeta(new meta().setName(meta.NAME_MODIFIED   ).setContent("16 April 2018"))
    .addMeta(new meta().setName(meta.NAME_CREATOR    ).setContent("Don Brutzman"))
    .addMeta(new meta().setName(meta.NAME_IMAGE      ).setContent("images/HelloWorld.tall.png"))
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("http://en.wikipedia.org/wiki/Hello_world"))
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("http://en.wikipedia.org/wiki/Hello#\"Hello,_World\"_computer_program"))
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("http://en.wikibooks.org/w/index.php?title=Computer_Programming/Hello_world"))
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("http://www.HelloWorldExample.net"))
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("http://www.web3D.org"))
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("http://www.web3d.org/realtime-3d/news/internationalization-x3d"))
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("http://www.web3d.org/x3d/content/examples/HelloWorld.x3d"))
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("http://X3dGraphics.com/examples/X3dForAdvancedModeling/HelloWorldScenes"))
    .addMeta(new meta().setName(meta.NAME_IDENTIFIER ).setContent("http://X3dGraphics.com/examples/X3dForWebAuthors/Chapter01-TechnicalOverview/HelloWorld.x3d"))
    .addMeta(new meta().setName(meta.NAME_LICENSE    ).setContent("http://www.web3d.org/x3d/content/examples/license.html"))
    .addMeta(new meta().setName(meta.NAME_GENERATOR  ).setContent("X3D-Edit 3.3, https://savage.nps.edu/X3D-Edit"))
    .addComments(" Alternate encodings: VRML97, X3D ClassicVRML Encoding, X3D Compressed Binary Encoding (CBE), X3DOM, JSON ")
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("HelloWorld.wrl"))
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("HelloWorld.x3dv"))
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("HelloWorld.x3db"))
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("HelloWorld.xhtml"))
    .addMeta(new meta().setName(meta.NAME_REFERENCE  ).setContent("HelloWorld.json")))
  .setScene(new Scene()
    .addComments(" Example scene to illustrate X3D nodes and fields (XML elements and attributes) ")
    .addChild(new Group()
      .addChild(new Viewpoint("ViewUpClose").setDescription("Hello world!").setCenterOfRotation(0.0,-1.0,0.0).setPosition(0.0,-1.0,7.0))
      .addChild(new Transform("ScaleFeetToMeters").setRotation(0.0,1.0,0.0,3.0).setScale(0.3048,0.3048,0.3048)
        .addChild(new Shape()
          .setGeometry(new Sphere())
          .setAppearance(new Appearance()
            .setMaterial(new Material("MaterialLightBlue").setDiffuseColor(0.1,0.5,1.0))
            .setTexture(new ImageTexture("ImageCloudlessEarth").setUrl(new String[] {"earth-topo.png","earth-topo.jpg","earth-topo-small.gif","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.png","http://www.web3d.org/x3d/content/examples/Basic/earth-topo.jpg","http://www.web3d.org/x3d/content/examples/Basic/earth-topo-small.gif"})))))
      .addChild(new Transform().setTranslation(0.0,-2.0,0.0)
        .addChild(new Shape()
          .setGeometry(new Text("TextMessage").setString(new String[] {"Hello","world!"})
            .setFontStyle(new FontStyle().setJustify(FontStyle.JUSTIFY_MIDDLE_MIDDLE)))
          .setAppearance(new Appearance()
            .setMaterial(new Material().setUSE("MaterialLightBlue")))))));
    }
	// end of initialize() method

	/** The initialized model object, created within initialize() method. */
	private X3D x3dModel;

	/** 
	 * Provide a 
	 * <a href="https://dzone.com/articles/java-copy-shallow-vs-deep-in-which-you-will-swim" target="_blank">shallow copy</a>
	 * of the X3D model.
	 * @see <a href="https://www.web3d.org/specifications/java/javadoc/org/web3d/x3d/jsail/Core/X3D.html">X3D</a>
	 * @return HelloWorld model
	 */
	public X3D getX3dModel()
	{	  
		return x3dModel;
	}
	   
    /** 
	 * Default main() method provided for test purposes, uses CommandLine to set global ConfigurationProperties for this object.
     * @param args array of input parameters, provided as arguments
	 * @see <a href="https://www.web3d.org/specifications/java/javadoc/org/web3d/x3d/jsail/Core/X3D.html#handleArguments-java.lang.String:A-">X3D.handleArguments(args)</a>
	 * @see <a href="https://www.web3d.org/specifications/java/javadoc/org/web3d/x3d/jsail/Core/X3D.html#validationReport--">X3D.validationReport()</a>
     * @see <a href="https://www.web3d.org/specifications/java/javadoc/org/web3d/x3d/jsail/CommandLine.html">CommandLine</a>
     * @see <a href="https://www.web3d.org/specifications/java/javadoc/org/web3d/x3d/jsail/CommandLine.html#USAGE">CommandLine.USAGE</a>
     * @see <a href="https://www.web3d.org/specifications/java/javadoc/org/web3d/x3d/jsail/ConfigurationProperties.html">ConfigurationProperties</a>
     */
    public static void main(String args[])
    {
        X3D thisExampleX3dModel = new HelloWorld().getX3dModel();

		boolean hasArguments = (args != null) && (args.length > 0);
		boolean validate = true; // default
		boolean argumentsLoadNewModel = false;
		String  fileName = new String();

		if (args != null)
		{
			for (String arg : args)
			{
				if (arg.toLowerCase().startsWith("-v") || arg.toLowerCase().contains("validate"))
				{
					validate = true; // making sure
				}
				if (arg.toLowerCase().endsWith(X3D.FILE_EXTENSION_X3D) ||
					arg.toLowerCase().endsWith(X3D.FILE_EXTENSION_CLASSICVRML) ||
					arg.toLowerCase().endsWith(X3D.FILE_EXTENSION_X3DB) ||
					arg.toLowerCase().endsWith(X3D.FILE_EXTENSION_VRML97) ||
					arg.toLowerCase().endsWith(X3D.FILE_EXTENSION_EXI) ||
					arg.toLowerCase().endsWith(X3D.FILE_EXTENSION_GZIP) ||
					arg.toLowerCase().endsWith(X3D.FILE_EXTENSION_ZIP) ||
					arg.toLowerCase().endsWith(X3D.FILE_EXTENSION_HTML) ||
					arg.toLowerCase().endsWith(X3D.FILE_EXTENSION_XHTML))
				{
					argumentsLoadNewModel = true;
					fileName = arg;
				}
			}
		}
		if      (argumentsLoadNewModel)
			System.out.println("WARNING: \"HelloWorld\" model invocation is attempting to load file \"" + fileName + "\" instead of simply validating itself... file loading ignored.");
		else if (hasArguments) // if no arguments provided, this method produces usage warning
			thisExampleX3dModel.handleArguments(args);

		if (validate)
		{
			System.out.print("Java program \"HelloWorld\" self-validation test results: ");
			String validationResults = thisExampleX3dModel.validationReport();
            if (validationResults.startsWith("\n"))
                System.out.println();
			System.out.println(validationResults.trim());
		}
    }
}
