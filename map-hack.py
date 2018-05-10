from memorpy import *
mw=MemWorker(name="Warcraft II BNE.exe")
a=mw.Address(0x004AD98C)
a.write(1, 'uint')
