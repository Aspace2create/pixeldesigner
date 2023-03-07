# pixel-designer
A pixel art tool that serves as a kit basher that allows plugins and loading your own images to Create awesome new ones

## Commands
####

```

```

# PXL ToolKit Documentation


## Creating An Effect

### Example: Vignette effect
```py
import random
import numpy as np

self.functionn=lambda self,image:vignette(self,image)
def vignette(self, image):
        image = np.array(image)
        rows, cols, channels = image.shape
        center_x, center_y = int(cols / 2), int(rows / 2)
        max_dist = np.sqrt((center_x - 0) ** 2 + (center_y - 0) ** 2)
        mask = np.zeros((rows, cols, channels), dtype=np.float32)
        for i in range(rows):
            for j in range(cols):
                dist = np.sqrt((center_x - j) ** 2 + (center_y - i) ** 2)
                mask[i, j] = 1 - dist / max_dist
        image = image * mask
        return image.tolist()
```
#### Step 1: import your modules:
currently PxlToolkit only supports a few image modules, and has a few image functions built in such as:
```py
PIL, OpenCv(cv2), random, io, numpy, math, scipy, json, regex(re)

#and from "ImageCommands", our own funtions

rotatematrix,insert,patinsert,loader,colorize,
create_gradient_rectangle,circle_matrix,create_diagonal_line,
create_line,invert,nineslice,rgba_matrix_to_greyscale,
qimage_to_rgba_matrix,matrix_to_qimage,round_corners,
crop_transparent,create_Circle,create_Rect,create_RectRound
```
the first step is to create our function, a function can either output An rgba matrix like in the vignette Example, or output a Pil image, but  nothig else, as of now.

#### step 2: create your function

the next step is simple, create a function that manipulates the image however you like

```py
def myfunction(self, image):
    #do something
    pass
```

next you have to use ```lambda``` to properly output your function
```py
self.functionn=lambda self,image:vignette(self,image)
```
and with that you are done, make sure your function takes two variables, and make sure the lambda function is created by typing ```self.functionn```< with 2 n's 

ounce you create the effect put it in a zipfile and rename the ```.zip``` with ```.pakfx``` and us the pluginloader to load it into the app, or just go inside the resource folder and drop it in ```Effects```
## Creating A basic Tool
### Example: Circle Tool
```py
#define our function list the first two arent going to be used so are added first and left blank
functList=["",""]

#adding in our on release command
functList.append("""

#defining our resize command for our ShapeItm
resizeCommand='''
try:
    if self.raction:
        self.reshape(imageCommands.create_Circle(self.color,1,width=new_W,height=new_H).toqimage())
        self.updateManipulator()
    else:
        im=Image.fromqimage(self.originalim)
        imr=np.array(im)
        imr=np.tile(imr,(10,10,1))
        im=im.resize((new_W,new_H))
        im.paste(Image.fromarray(imr),(0,0))
        self.reshape(im.toqimage())
        self.updateManipulator()
except Exception as e:
    print(e)
    pass
'''
#using tool identifier to run our release function VVVV
if self.curtool=="CircleTool010":
    try:
        if event.button() == Qt.LeftButton:
            if self.rubberBand.default=="iregyx":
                new=ShapeItm(qimage=(create_Circle(self.color,1,width=widthr,height=heightr).transpose(Image.FLIP_LEFT_RIGHT).
                transpose(Image.FLIP_TOP_BOTTOM)).toqimage(), 
                parent=self,pos=self.view.mapToScene(QPoint(enrd.x(),enrd.y())),resizedir=resizeCommand,color=self.color)
            elif self.rubberBand.default=="iregxy":
                new=SimpleItm(qimage=create_Circle(self.color,1,width=widthr,height=heightr).transpose(Image.FLIP_LEFT_RIGHT).
                toqimage(), parent=self,pos=self.view.mapToScene
                (QPoint(enrd.x(),self.originpoint.y())),resizedir=resizeCommand,color=self.color)
            elif self.rubberBand.default=="ireg":
                new=ShapeItm(qimage=create_Circle(self.color,1,width=widthr,height=heightr).transpose(Image.FLIP_TOP_BOTTOM).
                transpose(Image.FLIP_LEFT_RIGHT).toqimage(), 
                parent=self,pos=self.view.mapToScene(QPoint(self.originpoint.x(),self.originpoint.y())),resizedir=resizeCommand,color=self.color)
            elif self.rubberBand.default=="reg":
                new=ShapeItm(qimage=create_Circle(self.color,1,width=widthr,height=heightr).transpose(Image.FLIP_TOP_BOTTOM).
                toqimage(), parent=self,
                pos=self.view.mapToScene(QPoint(self.originpoint.x(),enrd.y())),resizedir=resizeCommand,color=self.color)
            self.graphicsItems.append(new)
            self.scene.addItem(self.graphicsItems[-1])
            self.rubberBand.hide()
    except Exception as e:
        print(e)
        self.rubberBand.hide()""")

#vv tells the drag function to show a circle when our tool is used
self.circr.append("CircleTool010")
#uses stored icon "circle" and function returnIco to set the icon
newQaction=ToolAction(QIcon(self.returnICO("circle")), "Circle Tool", parent=self,func="self.manipbox.hide()",override=True,
funclst=functList ,name="CircleTool010",source=("Default Tool","Version 0.0.1","Move Tool"))
#vv for toggkleable tools only
newQaction.setCheckable(True)
self.DefaultTools.append(newQaction)
self.toolbar.addAction(newQaction)
self.toolbar.insertSeparator(newQaction)
#vv dont do this if action is not toggleable
self.group.addAction(newQaction)
```



### Step 1: defining our variables
every plugin has 3 parts, but not all parts are used! our first step is to define our ```functlist``` by typing ```funclist=[]``` the first part of our funclist controls our ```on_press``` event so when the user drags their clicks while our tool is active an event will happen the PxlToolkit has a variable ```self.specialtoolvars``` which is a list, note, to prevent intervention with other tools it is best to use the sample code below whenever using ```self.specialtoolvars```


```py
#adding our tool variable var to the list
self.specialtoolvars.append(("Identifier","value"))

```
and now to retrieve your stored data when necessary:

```py
#iterate through the tool variable list
for i in self.specialtoolvars:
    if i[0]="Identifier":
        myvar=i

#get index of my tool variable if necessary...

myindex=self.specialtoolvars.index(myvar)
```
most tools do not recquire an on call method but in any case that you may need such a thing, feel free to use the code above to create variables to be accessed on drag or on release methods.

the next method is on drag, the on drag method is rarely customized or used, but again you may use the code above to utilyze any stored variables.

the next method is crucial it is on release, this is when any objects are added if that is how your tool works or where you would apply an effect if that is something your tool does.
follow the circle tool example for more information on that


