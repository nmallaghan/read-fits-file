from astropy.io import fits
import pandas
from astropy.table import Table
import numpy as np

#insert your own file into here to open the right fits file
hdu = fits.open("/Users/niamhmallaghan/Documents/Dusty Object NGTS/dustyobjectinorion/data/HARPS_data/ESO_data/10_02_20/reduced/2020-02-09/HARPS.2020-02-10T01:07:54.402_s1d_A.fits")

#info basically tells you how many sections are in the fits file, what kind of data they hold, how many data points etc. 
# This will print automatically from this command
info = hdu.info()

#This grabs the header for the file, where all of the important info is placed
hdr = hdu[0].header

#This grabs the data from whichever section you want it from
section_no = 0
data = hdu[section_no].data

# I've added this so that when you print the data it comes out in a nice table format instead of the usual format
table_data = Table(data)

#This is good for if the header file is really big and it's more difficult to read in the terminal
# you can open the file instead to read it
"""
text_file = open("/Users/niamhmallaghan/Documents/Output.txt", "w")

text_file.write(str(hdr))

text_file.close()
"""

#then use this to print whatever you want - the first command is used is it starts truncating your values
#np.set_printoptions(threshold=np.inf)
print(hdr)