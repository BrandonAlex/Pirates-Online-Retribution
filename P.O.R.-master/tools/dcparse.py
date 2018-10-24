from panda3d.core import *
from panda3d.direct import *
dc = DCFile()
dc.read(Filename.fromOsSpecific('..\astron\dclass\otp.dc'))
dc.read(Filename.fromOsSpecific('..\astron\dclass\pirates.dc'))
print(hex(dc.getHash()))