import enum
from PIL import Image

img = Image.new('L', (1920, 1112))
with open('./forensic/citra/chall.csv', 'r') as f:
    lines = f.readlines()
    for i,line in enumerate(lines):
        for j,value in enumerate(line.split(',')):
            img.putpixel((j,i), int(float(value)))

img.show()

# didapat dari gambar
string = '''46696E6449544354467B59345F4E64346B5F5461755F4B306B5F4E64344B5F54346E79415F4D34737433725F39393939393939393939397D
'''
print(bytes.fromhex(string))
