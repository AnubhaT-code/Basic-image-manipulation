
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys

n_input = sys.argv[1]
image = Image.open(n_input)
#plt.imshow(image)

copied_image = image.copy()
size = (500,500)

crop_image1 = image.crop((0,0,190,200))

crop_image1.convert('RGB')
width, height = crop_image1.size
for x in range(0, width):
    for y in range(0, height):
        r, g, b = crop_image1.getpixel((x,y))
        value = (r,b,g)
        crop_image1.putpixel((x, y), value)
    
crop_image1.thumbnail(size)
copied_image.paste(crop_image1,(0,200))


crop_image2 = image.crop((515,150,700,330))

transpose_image2 = crop_image2.transpose(Image.FLIP_LEFT_RIGHT)
transpose_image2.thumbnail(size) # preserves aspect ratio
copied_image.paste(transpose_image2,(515,150))

crop_image3 = image.crop((0,200,190,410))

transpose_image3 = crop_image3.transpose(Image.FLIP_TOP_BOTTOM)
transpose_image3.thumbnail(size)
copied_image.paste(transpose_image3,(0,0))

crop_image4 = image.crop((370,371,797,421))

transpose_image4 = crop_image4.transpose(Image.FLIP_TOP_BOTTOM)
transpose_image4.thumbnail(size) # preserves aspect ratio
copied_image.paste(transpose_image4,(370,371))

crop_image5 = copied_image.crop((0,410,190,415))

transpose_image5 = crop_image5.transpose(Image.FLIP_TOP_BOTTOM)
transpose_image5.thumbnail(size) # preserves aspect ratio

copied_image.paste(transpose_image5,(0,405))

crop_image6 = copied_image.crop((0,395,190,400))

transpose_image6 = crop_image6.transpose(Image.FLIP_TOP_BOTTOM)
transpose_image6.thumbnail(size) # preserves aspect ratio

copied_image.paste(transpose_image6,(0,400))
copied_image.save("jigsolved.jpg")
#plt.imshow(copied_image)


