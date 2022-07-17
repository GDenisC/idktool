
from idktools import *

xml = XML('test')

layer = Layer(1)
layer.addColor(ColorRGBA(array=(255, 255, 255)))
layer.addMaterial(Materials.Tarmac)
layer.addIsErase(True)
layer.addIsMirrored(True)
layer.addRotation(-21.241215125122123125)
layer.addPosition(1.2512521521, -1.5215251512)
layer.addSize(1.125125125125, 0.7125165246)
xml.add(layer.compile())

layer = Layer(2)
layer.addColor(ColorRGBA(array=(0, 0, 0)))
layer.addMaterial(Materials.Tarmac_damaged)
layer.addIsErase(False)
layer.addIsMirrored(True)
layer.addRotation(0)
layer.addPosition(1, -1)
layer.addSize(1, 2)
xml.add(layer.compile())

xml.create()
