#!/usr/bin/python
# -*- coding:utf-8 -*-
# By Jinda Han @ April Fool day on 2016
# take some sample and and located at each class folder, 
# then checking the random folder compare with all the icons in classes' folder, 
# if similar smaller than [value], then move (or copy) the icons to each class's folder

import json
import itertools
import os, sys
# from classify_nn import Classifying
# from database import Database
# from shutil import copyfile
# import pypuzzle
# import pydeep
# puzzle = pypuzzle.Puzzle()

main_folder = "training/"
sub_folder1 = "classes/"
sub_folder2 = "random/"



if __name__ == '__main__':
	print main_folder
	print sub_folder1
	
	# random folder
	random_folder = os.listdir(main_folder + sub_folder2)
	# iter each image in random folder
	for each_icon in random_folder:
		if each_icon == ".DS_Store":
			continue
		print "Compared icon: " + each_icon

		# search each classes folder
		classes_folder = os.listdir(main_folder + sub_folder1)
		for each_class in classes_folder:
			if each_class == ".DS_Store":
				continue
			#print "Class: " + each_class
			each_class_folder = os.listdir(main_folder + sub_folder1 + each_class + "/out_testing_all/")

			# iter each folder and compare the hash value using pypuzzle
			for each_class_icon in each_class_folder:
				if each_class_icon == ".DS_Store":
					continue
				#print "Compare with: " + each_class_icon + "  Class: " + each_class + "  Value: "
				# if the value larger than 0.23, 
				

				#then mv it to the exactly class folder






