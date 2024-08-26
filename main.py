from PIL import Image, ImageDraw

# สร้างภาพขนาด 200x200 พิกเซล
img = Image.new('RGB', (200, 200), color = 'white')

# วาดวงกลมสีแดงตรงกลาง
d = ImageDraw.Draw(img)
d.ellipse([50, 50, 150, 150], fill=(255, 0, 0))

# บันทึกภาพ
img.save('output.png')

from PIL import Image, ImageDraw, ImageFont

def create_image(text):
    # สร้างภาพขนาด 400x200 พิกเซล
    img = Image.new('RGB', (400, 200), color='white')
    
    # วาดข้อความลงในภาพ
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((10, 10), text, fill=(0, 0, 0), font=font)

    # บันทึกภาพ
    img.save('output.png')

if __name__ == "__main__":
    user_input = input("Enter the text to display on the image: ")
    create_image(user_input)
    print("Image created successfully!")

