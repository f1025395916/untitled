from PIL import  Image,ImageFont,ImageDraw

# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

image = Image.open('0.png')
w,h =image.size
font =ImageFont.truetype('arial.ttf',50)
draw = ImageDraw.Draw(image)
draw.text((4*w/5,h/5),'5',fill=(255,10,10),font = font)
image.save('0.0.png','png')



