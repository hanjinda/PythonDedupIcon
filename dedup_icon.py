#!/usr/bin/python
# -*- coding:utf-8 -*-
# 1 reach all the class and in each class compare all the object with each other
import json
import itertools
import os, sys
from classify_nn import Classifying
from database import Database
from shutil import copyfile
import pypuzzle
import pydeep
puzzle = pypuzzle.Puzzle()

crawler_path = os.path.abspath(os.path.join(os.path.realpath(__file__),"..","..","exploration"))
print crawler_path
sys.path.append(crawler_path)

from utilities.utilities import create_folder, read_json, write_json

if __name__ == '__main__':
	print "hello"
	training_elements_by_session = read_json("./training_elements_by_session.json")
	testing_elements_by_session = read_json("./testing_elements_by_session.json")

	config = read_json("./config.json")
	input_folder = os.path.join(config['elements_folder'], "image", "processed_icon", "resized", "gray", "50")
	training_folder = os.path.join(config['training_folder'], "all/")
	# print training_folder
	testing_folder = os.path.join(config['testing_folder'], "all/")
	training_dedup_folder = os.path.join(config['training_folder'], "dedup/")
	testing_dedup_folder = os.path.join(config['testing_folder'], "dedup/")

	training_test_folder = os.path.join(config['training_folder'], "test/")
	testing_test_folder = os.path.join(config['testing_folder'], "test/")	

	db = Database()

	# db.set_same_as_helper() # only run once

	num1 = 1 # output file number of training 
	num2 = 1 # output file number of testing
	rounds1 = 1 #training session numbers to stop
	rounds2 = 1 #testing session numbers to stop
	# save training to list to compare
	list_training = []
	for session in training_elements_by_session:
		list_training.append(session)

	ltr_length = len(list_training)

	for session in list_training:
		#print ssn
		session = str(session)

		# compare each icon element by
		for x,y in itertools.combinations(training_elements_by_session[session], 2):
			
			file_name1 = x + ".png"
			file_name2 = y + ".png"
			#output file name in the /test folder
			file_num1 = str(num1) + "a_" + file_name1 #output image1
			file_num2 = str(num1) + "b_" + file_name2 #output image2
			# Get distance between two image files
			if os.path.isfile(training_folder + file_name1) & os.path.isfile(training_folder + file_name2): #training_dedup_folder
				# print x + " vs " + y
				dis = puzzle.get_distance_from_file(training_folder + file_name1, training_folder + file_name2)
				# print dis

				# save db the element feature
				libpuzzle_features1 = puzzle.get_cvec_from_file(training_folder + file_name1)
				lf_compress1 = puzzle.compress_cvec(libpuzzle_features1)
				libpuzzle_features2 = puzzle.get_cvec_from_file(training_folder + file_name2)
				lf_compress2 = puzzle.compress_cvec(libpuzzle_features2)

				db.set_libpuzzle_features(x,lf_compress1)
				db.set_libpuzzle_features(y,lf_compress2)

				if (dis <= 0.23): #add the compare here
					print "[Pic"+str(num1)+ "] "+ x + " and " + y + "are similar"

					db.set_same_as(y, x)
					num1 += 1
					
					try:
						# print "!!!!!!! YES REMOVED !!!!!!"
						if os.path.isfile(training_dedup_folder + file_name2):
							os.remove(training_dedup_folder + file_name2)
						#copy two image to test folders
						# copyfile(os.path.join(training_folder, file_name1), os.path.join(training_test_folder, file_num1))
						# copyfile(os.path.join(training_folder, file_name2), os.path.join(training_test_folder, file_num2))
					except Exception, e:
						print e
						continue
				else:
					# save the same as parents as null if different 
					db.set_same_as(y, "null")

			else:
				# in case save db the element as null if there is no pic
				# db.set_libpuzzle_features(x,"null")
				# db.set_libpuzzle_features(y,"null")
				continue

			# rounds1 -= 1
			# if rounds1 <= 0:
			# 	break # compare each, reamove after test

	# save testing to list to compare
	list_testing = []
	for session in testing_elements_by_session:
		list_testing.append(session)

	lte_length = len(list_testing)

	for session in list_testing:
		#print ssn
		session = str(session)

		# compare each icon element by
		for x,y in itertools.combinations(testing_elements_by_session[session], 2):	
			file_name1 = x + ".png"
			file_name2 = y + ".png"
			file_num1 = str(num2) + "a_" + file_name1 #output image1
			file_num2 = str(num2) + "b_" + file_name2 #output image2

			# if two image exits, then 
			if os.path.isfile(testing_folder + file_name1) & os.path.isfile(testing_folder + file_name2): #testing_dedup_folder
				# print x + " vs " + y
				# Get distance between two image files
				dis = puzzle.get_distance_from_file(testing_folder + file_name1, testing_folder + file_name2)
				print dis

				# save db the element feature
				libpuzzle_features1 = puzzle.get_cvec_from_file(testing_folder + file_name1)
				lf_compress1 = puzzle.compress_cvec(libpuzzle_features1)
				libpuzzle_features2 = puzzle.get_cvec_from_file(testing_folder + file_name2)
				lf_compress2 = puzzle.compress_cvec(libpuzzle_features2)
				# print lf_compress1, lf_compress2
				db.set_libpuzzle_features(x,lf_compress1)
				db.set_libpuzzle_features(y,lf_compress2)

				if (dis <= 0.23): #add the compare here
					print "[Pic"+str(num2)+ "] "+ x + " and " + y + "are similar"
					
					db.set_same_as(y, x)
					num2 += 1
					
					try:
						print "!!!!!!! YES REMOVED !!!!!!"
						if os.path.isfile(testing_dedup_folder + file_name2):
							os.remove(testing_dedup_folder + file_name2)
						#copy two image to test folders
						# copyfile(os.path.join(testing_folder, file_name1), os.path.join(testing_test_folder, file_num1))
						# copyfile(os.path.join(testing_folder, file_name2), os.path.join(testing_test_folder, file_num2))
					except Exception, e:
						print e
						continue
				else:
					# save the same as parents as null if different 
					db.set_same_as(y, "null")

			else:
				# in case save db the element as null if there is no pic
				# db.set_libpuzzle_features(x,"null")
				# db.set_libpuzzle_features(y,"null")
				continue

			# rounds2 -= 1
			# if rounds2 <= 0:
			# 	break # compare each, reamove after test
