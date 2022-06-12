# oomlout-OOMP
 OOpen Organization Method for Parts

## Structure

### Part

A part is defined by its ID from which it's name can be back generated. (these links are contained in the \codes folder)

A part also has a a list of tags that defines it. These tags are defined in the details.py file in the parts folder (\parts). This can be a list of tags or calls to a routine that defines a group of tags based on a category. (ie. HEAD-I01-X-PI03-01 calls OOMPtags.addTags(newPart,"HEAD-I01-X-X-X",pins=pins))

### ID

A parts ID has five parts

    TYPE-SIZE-COLOR-DESCRIPTION-INDEX

	* TYPE - This defines the par type (Ex. HEAD - Header, LEDS - LED)
	* SIZE - This is the size category or package of a part (Ex. I01 - 0.1", W04 - 1.4 Watt Resistor, 0603 - 0603 (SMD))
	* COLOR - This is the parts color or material (Ex. R - Red, M - Metal ) (Default X)
	* DESCRIPTION - This is a defining charachteristic of the part and is the same across a type (Ex. PI03 - 3 Pins, O561 - 560 Ohms) (Default XXXX)
	* INDEX - This is an additional piece of information that differentiates a part and chages between type (Ex. 67 - 1% tolerance, RA - right angle) (Default 01)

### Name

A parts name is back calculated from its ID.
    
	SIZE DESCRIPTION COLOR TYPE INDEX

	Ex.
	* LEDS-10-R-FROS-01 - 10 mm Frosted Red LED
	* HEAD-I01-X-PI03-RA - 2.54 mm 3 Pin Header Right Angle

### Tags

A tag consists of a name and a value. Some tags are further defined in a sperate file these are in \codes

### Part Files

	* Summaries
		* Readme.md (generated)  --  A summary of the part in markdown,

	* Images
		* image.jpg  --  Main image.
		* image_RE.jpg  --  Image for size reference (usually beside a sharpened pencil).
		* image_TOP.jpg  --  Image of the top of the part.
		* image_BOTTOM.jpg  --  Image of the bottom of the part.
		
	* Diagrams
		Diagrams are generated from tags, that use templates (templates/diag/). These are compiled to a python script that uses the Simple Inkscape Scripting Extension (https://github.com/spakin/SimpInkScr/) to draw and save svgs, these svgs are then used to genearate png, dxf,and pdf files.
		* diagBBLS.svg (generated)  --  A diagram for adding part to a breadboard layout sheet.
		* diagDIAG.svg (generated)  --  A diagram for adding part to a layout.
		* diagIDEN.svg (generated)  --  A diagram for adding part to a PCB with details.
		* diagSCHEM.svg (generated)  --  A diagram for adding part to a schematic.
		* diagSIMP.svg (generated)  --  A diagram for with only the parts outline.
	
	* Datasheets
		* datasheet.pdf  --  Datasheet for the part.
		* datasheet-C-SUPL  --  If more than one datasheet exists the manufacturers four letter code is added.
		* datasheet.txt (generated)  --  If the datasheet is a duplicate this file has the location in it, if it is hosted externally a link.
		
	* 3D Models
		3D models are generated programatically these routines are in OOMPscad.py, they use SolidPython (https://github.com/SolidCode/SolidPython) to generate .scad files from which stl and pngs are generated.
		* 3dmodel.scad (generated)  --  Scad model of the part. Programatically generated in OOMPscad.py
		* 3dmodel.stl (generated)  --  STL version of 3dmodel.scad
		* 3dmodel.png (generated)  --  Rendered image of 3dmodel.scad (ortho)
		
	* Labels
		Labels are generated using tags and templates these are in templates/label/ they are svgs and use search and replace to generate labels. (%%ID%% is replaced by part ID and tags are format @@%%ID%%,oompPart.oompID,tagName@@). From the svgs pdfs are generated.
		* label-front.svg (generated)  --  A label for a front of a bag.
		* label-front.pdf (generated)  --  PDF version of label-front.svg
		* label-inventory.svg (generated)  --  A label for keeping inventory of a part organized.
		* label-inventory.pdf (generated)  --  PDF version of label-uinventory.svg		
		* label-spec.svg (generated)  --  A label listing part specifications.
		* label-spec.pdf (generated)  --  PDF version of label-spec.svg