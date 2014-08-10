# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Data Analyst

# <markdowncell>

# **Pipe scan business needs**
# 
# Develop quanifiable flaw detector
# 
# Create data analysis tools
# 
# Graphical display of flaws for PRS operators
# 
# Better sample reduction algorithm
# 
# Peak detector
# 
# Control settings for detection algorithm
# 
# Capture and analyze known defects
# 
# Reproducible calibration process
# 
# Dimensional calibration of defects
# 
# Performance monitoring metrics

# <headingcell level=2>

# Technical Tricks

# <markdowncell>

# Read CSV data to table
# 
# List table
# 
# Write table to CSV
# 
# Group data into chunks (20/50 samples per chunk)
# 
# Reduce each chunk to average value
# 
# Calculate cells using min/max/avg
# 
# Scan data for peaks
# 
# Calculate std dev for each cell
# 
# Moving average over data
# 
# Explore group deviations
# 
# Explore modes within cell
# 
# Explore cell size
# 
# Explore memory footprint
# 
# Explore performance tradeoffs
# 

# <codecell>

import pandas as pd

from pandas import rolling_min,rolling_max

# <codecell>

from   pandas       import read_csv

filename = '/home/seaman/Projects/ipython/doc/sensors.csv'
scan = read_csv(filename)
scan [:5]

# <codecell>

# Read sensor data from a file
def read_sensors(path):
    return read_csv(path, header=None, names=None)

filename = '/home/seaman/Projects/ipython/doc/sensors.csv'
scan = read_sensors(filename)
scan [:5]

# <codecell>

# Write sensor data to a file
def write_sensors(path, data):
    data.to_csv(path, header=False, index=False, float_format='%.0f',)

filename = '/home/seaman/Projects/ipython/doc/xsensors.csv'
    
write_sensors(filename, scan)
scan = read_sensors(filename)
scan [:5]

# <codecell>

from pandas       import DataFrame


# Create some imaginary data to work with
def create_data(num_rows=10, num_columns=10):
    return [ [ 0+c+row*100 for c in range(num_columns) ]+[ row+87845 ] for row in range(num_rows) ]

# Generate a fake data frame that matches the number of sensors
def fake_data():
    return DataFrame(create_data(20,12))

# Generate a fake data frame that matches the number of sensors
def real_data():
    filename = '/home/seaman/Projects/ipython/doc/socket'
    scan = read_sensors(filename)
    return DataFrame(scan)

scan = real_data()
#scan = fake_data()

# <codecell>

wall_columns = ["Wall" +str(x) for x in range(1,4+1)]
flaw_columns = ["Flaw" +str(x) for x in range(1,8+1)]

def name_columns(scan):
    n_extra = len(scan.columns) - 13
    extra_columns = ["Extra" +str(x) for x in range(1,n_extra+1)]
    scan.columns = extra_columns + wall_columns + flaw_columns + ["Timestamp"]
    scan.set_index('Timestamp',inplace=True)

# <codecell>

#-----------------------------------------------------------------------------
# Calculate a series

# Combine wall and flaw sensors for each row
def average_sensors(scan,columns,label='averages'):
    scan[label] = scan[columns].mean(axis=1)
    return scan

# Minimum of wall and flaw sensors for each row
def sensor_spread (scan,columns,label=""):
    row_means = scan[columns].mean(axis=1)
    scan[label+'min'] = pd.rolling_min(row_means,window=5,center=True)
    scan[label+'max'] = pd.rolling_max(row_means,window=5,center=True)
    scan[label+'spread'] = scan[label+'max'] - scan[label+'min']
    return scan
     
# Eliminate ten row
def eliminate_rows(scan,nrows):
    return scan.drop(scan.index[:nrows])

# Perform all tests    
def data_pipeline(scan):
    name_columns(scan)    
    
    sensor_spread (scan, wall_columns,'wall ')
    average_sensors(scan,flaw_columns,'flaw averages')

    return scan[['wall spread','wall min','wall max','flaw averages']]


#data_pipeline(fake_data())

# <codecell>


# Generate a fake data frame that matches the number of sensors
def real_data(path):
    scan = read_sensors(path)
    return DataFrame(scan)

# Perform all tests    
def test_this():
    filename = '/home/seaman/Projects/pipescan/pipedata/2014/CompanyName/07-15/2014-07-15_122027/socket'
    scan = real_data(filename)
    return data_pipeline(scan)


scan = test_this()
scan[100:120]

scan['time'] = scan['Timestamp']/10

# <codecell>

scan['t'] = scan.index/100
sensor_table = scan.groupby('t').max()
sensor_table

# <codecell>

from matplotlib import gridspec
from matplotlib.pyplot import subplot
gs = gridspec.GridSpec(2,1)

fig1 = scan[['flaw averages']].plot(ax=subplot(gs[0]), figsize=(12,6), color='red')
fig2 = scan[['wall spread',]].plot(ax=subplot(gs[1]), figsize=(12,6))

# <codecell>


# <markdowncell>


# <headingcell level=1>

# Outputting an Image

# <codecell>

from matplotlib.pylab import savefig
import glob
figure = scan.plot()
savefig('recent.png')
print(glob.glob("*"))

# <codecell>

from PIL import Image
from random import choice

def make_image():
    colors = [(255,255,0),(255,0,0),(0,255,0), (0,0,255)]
    data = [choice(colors) for i in range(67)] #randomly generated
    image = Image.new('RGB', (10,10))  # 10x10 pixels
    image.putdata(data)  # data loaded will wrap every 'width' pixels
    return image

imshow(make_image(), interpolation='nearest')  #without nearest you get a fuzzy render of your tiny image data

# <codecell>

from PIL import Image
from random import choice
from matplotlib import gridspec
from matplotlib.pyplot import subplot

gs = gridspec.GridSpec(3,1)

fig1 = scan[['flaw averages']].plot(ax=subplot(gs[0]), figsize=(12,6), color='red')
fig2 = scan[['wall spread',]].plot(ax=subplot(gs[1]), figsize=(12,6))
fig3 = subplot(gs[2]).imshow(make_image(), interpolation='nearest')

savefig('composite.png')


