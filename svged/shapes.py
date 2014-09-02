##
# svgEd, a very(!) basic svg creation library.
##

# some global variables, that may make life easier
svgWidth = '400'
svgHeight = '300'
svgViewBox = '0 0 %s %s' %(svgWidth, svgHeight)

strokeWidth='2px'
strokeColor='black'
fillColor='white'

myDoc = ''


# some manipulation stuff ...
def addShape(stuff):
  global myDoc
  myDoc += '\n' + stuff

# set view box
def setViewBox(x, y, width, height):
  global svgViewBox
  svgViewBox = '%s %s %s %s' %(x,y,width,height)

# setting up the header
def writeHeader():
  xmltag = '<?xml version="1.0" encoding="UTF-8"?>'
  svgtag = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" baseProfile="full" width="%s" height="%s" viewBox="%s">' %(svgWidth, svgHeight, svgViewBox)
  output = xmltag + '\n' + svgtag
  addShape(output)
  return output

# set up the end of the document
def writeEnd():
  output = '\n</svg>'
  addShape(output)
  return output



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



# methods for drawing shapes ...

# circle
def circle(cx, cy, r):
  output = '<circle cx="%s" cy="%s" r="%s"/>' %(cx, cy, r)
  addShape(output)
  return output

# ellipse
def ellipse(cx, cy, rx, ry):
  output = '<ellipse cx="%s" cy="%s" rx="%s" ry="%s"/>' %(cx, cy, rx, ry)
  addShape(output)
  return output

# line
def line(x1, y1, x2, y2):
  output = '<line x1="%s" y1="%s" x2="%s" y2="%s" />' %(x1, y1, x2, y2) # removed stroke and fill .. is that OK?
  addShape(output)
  return output

# polygon (input = coordinates of the poligon edges: x1,y1 x2,y2 .. xn,yn)
def polygon(points):
  output = '<polygon points="%s" />' %(points)
#  for i in range(len(points)):
#    output += points[i]
  addShape(output)
  return output

# polyline (input = coordinates of the poligon edges: x1,y1 x2,y2 .. xn,yn)
def polyline(points):
  output = '<polyline points="%s" />' %s(points)
  addShape(output)
  return output

# rectangle
def rectangle(x, y, width, height):
  output = '<rect x="%s" y="%s" width="%s" height="%s"/>' %(x, y, width, height) # removeed stroke and fill .. is that OK?
  addShape(output)
  return output

# something missing? 





