import math
import ProfileLib.RegularPolygon

#-----------------------------------------------------------------------------------------------------------------------------------------
#Defining class for Lattice Structure
#-----------------------------------------------------------------------------------------------------------------------------------------

#Pass aspect ratio as array
class Lattice:
    row_nodes = 0
    column_nodes = 0
    node_separation = (1 + math.sqrt(5)) / 2

    def __init__(self,
                 width,
                 length,
                 node_number,
                 connection_shape,
                 aspect_ratio):
        self.width = width
        self.length = length
        self.node_number = node_number
        self.connection_shape = connection_shape
        self.aspect_ratio=aspect_ratio


    def specify_shape(self):
        #For the triangle example, you are overconstraining as you don't need node_number and width and length, but node_number needed for RL case. Node_number could also be used
        #Instead of width and length if you do not want the node numbers to be rounded to the nearest integer during sketching. Example below will use width and length if node_number is not
        #specified, and conversely so.
        if self.node_number is None:
            if self.connection_shape == "triangle" or self.connection_shape == "Triangle":
                self.row_nodes=(self.width/self.node_separation)
                self.column_nodes=(self.length/self.node_separation)
                #----Other shapes----
        else:
            if self.connection_shape == "triangle" or self.connection_shape == "Triangle":
                self.row_nodes=(self.node_number/(self.aspect_ratio[0]+self.aspect_ratio[1]))*(self.aspect_ratio[0])
                self.column_nodes=(self.node_number/(self.aspect_ratio[0]+self.aspect_ratio[1]))*(self.aspect_ratio[1])

#Notes:Transfer functionality from python stuff below to more functions within the class.

#-------------------------------------------------------------------------------------------------------------------------------------------
#Calling an object from Class, any other python stuff
#-------------------------------------------------------------------------------------------------------------------------------------------

TrialLattice=Lattice(width=None,
                     length=None,
                     node_number=25,
                     connection_shape="triangle",
                     aspect_ratio=[3,2])

TrialLattice.specify_shape()

#Put this into a function of the class for all different node shapes
heightTriangle=(TrialLattice.node_separation*(math.sqrt(3)))/2

bot_to_mid_Triangle=heightTriangle/3

top_to_mid_Triangle=heightTriangle*(2/3)

x_midpointNodes=TrialLattice.node_separation/2





#-------------------------------------------------------------------------------------------------------------------------------------------
#Using FreeCAD
#-------------------------------------------------------------------------------------------------------------------------------------------

Gui.activateWorkbench("PartWorkbench")

App.newDocument("Lattice_Structure")

Gui.activateWorkbench("SketcherWorkbench")

App.activeDocument().addObject('Sketcher::SketchObject','Sketch')

App.activeDocument().Sketch.Placement = App.Placement(App.Vector(0.000000,0.000000,0.000000),App.Rotation(0.000000,0.000000,0.000000,1.000000))

App.activeDocument().Sketch.MapMode = "Deactivated"

Gui.activeDocument().activeView().setCamera('#Inventor V2.1 ascii \n OrthographicCamera {\n viewportMapping ADJUST_CAMERA \n position 0 0 87 \n orientation 0 0 1  0 \n nearDistance -112.88701 \n farDistance 287.28702 \n aspectRatio 1 \n focalDistance 87 \n height 143.52005 }')

Gui.activeDocument().setEdit('Sketch')

for v in range(int(TrialLattice.column_nodes)):

	for i in range(int(TrialLattice.row_nodes)):
		if (i%2==0):
			ProfileLib.RegularPolygon.makeRegularPolygon('Sketch',3,App.Vector(((v*TrialLattice.node_separation)+x_midpointNodes),((i*heightTriangle)+bot_to_mid_Triangle),0),App.Vector(((v+1)*TrialLattice.node_separation),(i*heightTriangle),0),False)		
		else:		
			ProfileLib.RegularPolygon.makeRegularPolygon('Sketch',3,App.Vector(((v*TrialLattice.node_separation)+x_midpointNodes),((i*heightTriangle)+top_to_mid_Triangle),0),App.Vector(((v+1)*TrialLattice.node_separation),((i+1)*heightTriangle),0),False)


"""
for i in range(int(TrialLattice.row_nodes)):
	if (i%2==0):
		ProfileLib.RegularPolygon.makeRegularPolygon('Sketch',3,App.Vector(x_midpointNodes,((i*heightTriangle)+bot_to_mid_Triangle),0),App.Vector(TrialLattice.node_separation,(i*heightTriangle),0),False)		
	else:		
		ProfileLib.RegularPolygon.makeRegularPolygon('Sketch',3,App.Vector(x_midpointNodes,((i*heightTriangle)+top_to_mid_Triangle),0),App.Vector(TrialLattice.node_separation,((i+1)*heightTriangle),0),False)
"""
#ProfileLib.RegularPolygon.makeRegularPolygon('Sketch',3,App.Vector(x_midpointNodes,bot_to_mid_Triangle,0),App.Vector(TrialLattice.node_separation,0,0),False)
#ProfileLib.RegularPolygon.makeRegularPolygon('Sketch',3,App.Vector(x_midpointNodes,(heightTriangle+top_to_mid_Triangle),0),App.Vector(TrialLattice.node_separation,(2*heightTriangle),0),False)