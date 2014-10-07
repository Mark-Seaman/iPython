# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Data Files
# 
# Create a data file with and without column headers.

# <codecell>

%%file with_header.csv
id,name,age,height,weight
1,Alice,20,62,120.6
2,Freddie,21,74,190.6
3,Bob,17,68,120.0

# <codecell>

!cat with_header.csv

# <codecell>

%%file no_header.csv
1,Alice,20,62,120.6
2,Freddie,21,74,190.6
3,Bob,17,68,120.0

# <codecell>

!cat no_header.csv

# <markdowncell>

# # Read with headers
# 
# Use a CSV reader to parse data with headers.  Print out the dictionary entries that are parsed.

# <codecell>

import csv
input_file = csv.DictReader(open("with_header.csv"))
for row in input_file:
    print row

# <codecell>

import csv
input_file = csv.DictReader(open("no_header.csv"))
for row in input_file:
    print row

# <markdowncell>

# # Access the columns using the header
# 
# Note that this will only work if the data file provides the correct header names.  
# 
# Otherwise there will be a mismatch for the column names.  This will cause an exception.

# <codecell>

input_file = csv.DictReader(open("with_header.csv"))
for row in input_file:
    print ','.join([ row['name'], row['age'] ])

# <markdowncell>

# # Read the first line to see if it contains the names
# 
# The first line should contain all of the required names of the columns.

# <codecell>

first_line = open('with_header.csv').read().split('\n')
columns = first_line[0].split(',')
names = ['name','age','weight']
for n in names:
    if not n in columns:
        print 'Bad input file', n, columns

# <markdowncell>

# # Parse the first line
# 
# Make sure that all of the required names are present.

# <codecell>

def file_ok(filename):
    first_line = open(filename).read().split('\n')
    columns = first_line[0].split(',')
    names = ['name','age','weight']
    for n in names:
        if not n in columns:
            print 'Bad input line: missing "%s"'%n, columns 
            return False
    return True

def read_file(filename):
    if file_ok(filename):
        print open(filename).read()
    else:
        print 'Bad file: %s'%filename

read_file('with_header.csv')
read_file('no_header.csv')

# <codecell>


