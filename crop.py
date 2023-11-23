
# Improting Image class from PIL module 
from PIL import Image 
  
# Opens a image in RGB mode 
im = Image.open("001.jpg") 
  
# Setting the points for cropped image 
left = 500
top = 350
right = 1200
bottom = 1080
  
# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 
  
# Shows the image in image viewer 
im1.save("crop.png")