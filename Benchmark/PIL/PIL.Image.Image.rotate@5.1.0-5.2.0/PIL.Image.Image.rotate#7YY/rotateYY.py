from PIL import Image
img = Image.open('example.jpg')
rotated_img = img.rotate(45,  Image.BICUBIC, expand=True)
