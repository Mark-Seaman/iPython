# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Time Master
# 
# Ideas and code snippets to build a time management tool.

# <codecell>

print 'Time Master'

# <codecell>

from PIL import Image
from random import choice

def make_image():
    colors = [(255,255,0),(255,0,0),(0,255,0), (0,0,255),(0,225,255)]
    data = [choice(colors) for i in range(98)] #randomly generated
    image = Image.new('RGB', (10,10))  # 10x10 pixels
    image.putdata(data)  # data loaded will wrap every 'width' pixels    
    return image

imshow(make_image(), interpolation='nearest')  #without nearest you get a fuzzy render of your tiny image data

# <codecell>

week = '''gwwwwwwwwwwfff
gwwwwwwwwwwccp
gwwwwwwwwwffff
gwwwwwwwwwwfff
gwwwwwwwwwpppp
ggccccpppfffff
ccccppgggfffff'''.split('\n')

len(week) 
for d in week:
    print [ h for h in d ]

# <codecell>

colormap = { 'g': (255,255,0), 'w':(255,0,0), 'p': (0,255,0), 'f': (0,0,255), 'c':(0,225,255) }
colormap['f']

# <codecell>

for d in week:
    print [ colormap[h] for h in d ]

# <codecell>

data = []
for d in week:
    data += [ colormap[h] for h in d ] 
data

# <codecell>


def make_image(data):
    image = Image.new('RGB', (14,7)) # 14 hours x 7 days
    image.putdata(data)  # data loaded will wrap every 'width' pixels    
    return image

imshow(make_image(data), interpolation='nearest') 

# <codecell>

from pylab import *
A = rand(7,14)
figure(1)
imshow(A, interpolation='nearest')
grid(True)

show()
figsize(20,20)

