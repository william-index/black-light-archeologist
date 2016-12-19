# @TODO  creates and returns a canvas
# @TODO  Limbs are drawn positive for both axis
# @TODO  All limbs start exactly in top left
# @TODO  limbs have N segments
# @TODO  (p3) different segment bone types
# @TODO  each segment may branch to M other segments,
#           but only the "top" segments continue


# Taken from old method fo drawing bone
# def drawBone(self, boneWidth, thickness):
#     canvas = (boneWidth+thickness, int(thickness*1.75))
#     boneScene = Image.new('RGBA', canvas, (255,100,100,0))
#     draw = ImageDraw.Draw(boneScene)
#
#     for capsX in [0, boneWidth]:
#         draw.ellipse((0+capsX, 0, thickness+capsX, thickness), fill = (255,255,0,255))
#         draw.ellipse((0+capsX, thickness*.75, thickness+capsX, thickness*.75 + thickness), fill = (255,255,0,255))
#     draw.line(
#         (thickness/2, thickness*.75, thickness/2+boneWidth, thickness*.75),
#         fill = (255,255,0,255),
#         width = thickness
#     )
#
#     return boneScene
