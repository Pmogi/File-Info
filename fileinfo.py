'''
Patrick Mogianesi
June 13 2016
fileinfo script

This program will get the information of a chosen file:
The size of the file.
The Name of file.
How old the file is.
'''
#the user inputs the path for the file

#os.path allows for paths to be understood by the computer
import os, os.path

def main():
	print "CTRL-C to exit"
	#input for user
	path = raw_input("Input path of file > ")
	
	#this list takes 3 functions, and finds values for them
	#basename = name of file
	#getsize = size of file
	#getntime = age of file
	x = [os.path.basename(path), os.path.getsize(path), os.path.getmtime(path)]
	
	#Simply prints out the info calling for information from the list.
	print "The files name is %r." % x[0]
	
	print "The program is %r bytes big." % x[1]

	print "The file is %r seconds old." % x[2]
	
	#sends user back start of the script
	main()
	

#starts script by calling main function
main()
