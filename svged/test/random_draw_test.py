##
# This test shall simply spawn random shapes and print them to a svg file.
##


from svged import shapes

def run():
  print(shapes.writeHeader())
  print(shapes.line(10,10,200,200))
  print(shapes.writeEnd())
