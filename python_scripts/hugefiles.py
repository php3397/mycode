#!/usr/bin/env python

import os

def get_file_paths(directory):
  file_paths = [] # list to store all of the full file-paths

  for root, directories, files in os.walk(directory):
   for filename in files:
    # join the two strings in order to form the full file_path
    file_path = os.path.join(root, filename)
    file_paths.append(file_path) # add it to the list

  return file_paths


def dir_find_large_size(directory, max_size):
 	full_file_paths = get_file_paths(directory)
 	size_mb = 0

 	for file_path in full_file_paths:
  	 if os.path.isfile(file_path):
   	  size_mb = ((os.path.getsize(file_path)) / 1024) / 1024
   	  if size_mb > max_size:
    	   print (file_path)
    	   print ('size: {0} mb'.format(size_mb))
  	  else:
   	   print ('Can not read file:')
   	   print (file_path)
 	return size_mb


def main():
 	root_dir = '/Users/aarna/tmp/tmp2'
 	result_size = 0
 	# get list of sub-directories one level under root_dir
 	dir_list = os.walk(os.path.join(root_dir, '.')).next()[1]
	print ("here",dir_list)
 	print (root_dir)
 	print ('-------------------------------')
 	for cur_dir in dir_list:
  	# print directory name
  	 print ('processing: {0} | ...'.format(cur_dir))
  	# find files bigger than 1000 mb
  	 result_size = dir_find_large_size(root_dir + '\\' + cur_dir, 1)
 	 print ('-------------------------------')

 	print (result_size)

if __name__ == "__main__": main()
