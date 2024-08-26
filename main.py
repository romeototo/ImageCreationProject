from PIL import Image, ImageDraw

# สร้างภาพขนาด 200x200 พิกเซล
img = Image.new('RGB', (200, 200), color = 'white')

# วาดวงกลมสีแดงตรงกลาง
d = ImageDraw.Draw(img)
d.ellipse([50, 50, 150, 150], fill=(255, 0, 0))

# บันทึกภาพ
img.save('output.png')


