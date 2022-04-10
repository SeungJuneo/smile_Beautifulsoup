from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x = 30
y = 60
z = 10

mc.player.setTilePos(x, y, z)

time.sleep(10)

mc.player.setTilePos(x + 1, y + 20, z+ 1)
