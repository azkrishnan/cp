from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def putnum(inp, num, outp):
	num = str(num);
	img = Image.open(inp);
	font = ImageFont.truetype("font.ttf", 14)
	draw = ImageDraw.Draw(img);
	draw.text((14-(8*len(num))/2, 4), num, font=font, fill="#000000")
#	draw = ImageDraw.Draw(img)
	img.save(outp)


for i in xrange(2, 1500):
	print i;
	putnum("found2.png", i, "numicons/marker"+str(i)+".png");
