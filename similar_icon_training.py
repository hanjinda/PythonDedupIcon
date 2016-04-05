#!/usr/bin/python
# -*- coding:utf-8 -*-
# By Jinda Han @ April Fool day on 2016
# take some sample and and located at each class folder, 
# then checking the random folder compare with all the icons in classes' folder, 
# if similar smaller than [value], then move (or copy) the icons to each class's folder

import json
import itertools
import os, sys
import shutil
# from classify_nn import Classifying
# from database import Database
# from shutil import copyfile
import pypuzzle
# import pydeep
puzzle = pypuzzle.Puzzle()

main_folder = "training/"
main_folder2 = "testing/"
sub_folder1 = "classes/"
sub_folder2 = "random/"



if __name__ == '__main__':
	#print main_folder
	#print sub_folder1
	
	# random folder
	random_folder = os.listdir(main_folder + sub_folder2)
	# iter each image in random folder
	image_num = 0
	for each_icon in random_folder:
		if not os.path.isfile(main_folder + sub_folder2 + each_icon):
			continue
		image_num += 1
		if each_icon == ".DS_Store":
			continue
		finish_percentage =  (float(image_num) / float(len(random_folder)) ) * 100
		print str(finish_percentage) + "%  Icon " + str(image_num) + ": " + each_icon

		# search each classes folder
		classes_folder = os.listdir(main_folder + sub_folder1)
		for each_class in classes_folder:
			if each_class == ".DS_Store":
				continue
			
			#for testing in one folder: shopping cart
			if each_class != "shoppingcart":
				continue

			#print "Class: " + each_class
			each_class_folder = os.listdir(main_folder + sub_folder1 + each_class + "/out_testing_all/")

			# iter each folder and compare the hash value using pypuzzle
			for each_class_icon in each_class_folder:
				if each_class_icon == ".DS_Store":
					continue
				icon_orign = main_folder + sub_folder2 + each_icon
				#if img not exist
				if not os.path.isfile(icon_orign):
					continue
				icon_new = main_folder + sub_folder1 + each_class + "/out_testing_all/" + each_class_icon
				dis = puzzle.get_distance_from_file(icon_orign, icon_new)
				#print dis
				if dis <= 0.23:
					to_class_goal_folder = main_folder + sub_folder1 + each_class + "/manual/"
					print "Random: " + icon_orign + " \nCompare with: " + icon_new + "\n Value: " + str(dis)
					#back check
					# shutil.copy(icon_orign, "my_train_output")
					# shutil.move(icon_orign, to_class_goal_folder)

					# (final) if not too much left, then final round using move to output folder instead of  move to manual
					shutil.move(icon_orign, "my_train_output")

			#after compare with out_test_all, then compare with manual and keep adding
			each_class_folder = os.listdir(main_folder + sub_folder1 + each_class + "/manual/")

			# iter each folder and compare the hash value using pypuzzle
			for each_class_icon in each_class_folder:
				if each_class_icon == ".DS_Store":
					continue
				icon_orign = main_folder + sub_folder2 + each_icon
				#if img not exist
				if not os.path.isfile(icon_orign):
					continue
				icon_new = main_folder + sub_folder1 + each_class + "/manual/" + each_class_icon
				dis = puzzle.get_distance_from_file(icon_orign, icon_new)
				#print dis
				if dis <= 0.23:
					to_class_goal_folder = main_folder + sub_folder1 + each_class + "/manual/"
					print "Random: " + icon_orign + " \nCompare with: " + icon_new + "\nValue: " + str(dis)
					# (initial) back check
					# shutil.copy(icon_orign, "my_train_output")
					# shutil.move(icon_orign, to_class_goal_folder)
					
					# (final) if not too much left, then final round using move to output folder instead of  move to manual
					shutil.move(icon_orign, "my_train_output")
					
					#shutil.move(icon_new,"my_test/")
					#reak
				#print "Compare with: " + each_class_icon + "  Class: " + each_class + "  Value: "
				# if the value larger than 0.23, 
				

				#then mv it to the exactly class folder






