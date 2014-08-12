
svgWidth = "400"
svgHeight = "300"
svgViewBox = "0 0 %s %s" % (svgWidth, svgHeight)

strokeWidth="2px"
strokeColor="black"
fillColor="white"

myDoc = "<!-- here comes the interesting part -->"



# setter for the stroke variables
def setStroke(color, width):
  global strokeColor 
  strokeColor = color
  global strokeWidth
  strokeWidth = width

# setter for fill variable
def setFill(color):
  global fillColor 
  fillColor = color

# set width and height of the svg image
def setSize(width, height):
  global svgWidth 
  svgWidth = width
  global svgHeight
  svgHeight = height

# set view box
def setViewBox(x, y, width, height):
  global svgViewBox
  svgViewBox = "%s %s %s %s" % (x,y,width,height)



# setting up the header
def writeHeader():
  xmltag = '<?xml version="1.0" encoding="UTF-8"?>'
  svgtag = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" baseProfile="full" width="%s" height="%s" viewBox="%s">' % (svgWidth, svgHeight, svgViewBox)
  return xmltag + "\n" + svgtag

def writeEnd():
  return "\n</svg>"



# methods for drawing things ...

# line
def line(x1,y1,x2,y2):
  return '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" />' % (x1,y1,x2,y2,strokeColor,strokeWidth)

# rectangle
def rectangle(x,y,width,height):
  return '<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="%s"/>' % (x,y,width,height,fillColor,strokeColor,strokeWidth)



# some manipulation stuff ...
def addstuff(stuff):
  global myDoc
  myDoc += "\n" + stuff



## testing ...
setSize(600,400)

addstuff(line(10,10,100,100))
addstuff(line(300,10, 400,100))
addstuff(rectangle(50,100,30,60))
setStroke("red","5px")
setFill("green")
addstuff(rectangle(50,50,100,100))

print(writeHeader() + myDoc + writeEnd())


