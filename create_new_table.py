#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import os, sys
from database import Database
from shutil import copyfile
# crawler_path = os.path.abspath(os.path.join(os.path.realpath(__file__),"..","..","exploration"))
# print crawler_path
# sys.path.append(crawler_path)

# from utilities.utilities import create_folder, read_json, write_json
# PIL not exist

db = Database()

if __name__ == '__main__':
	# config = read_json("./config.json")

	with open('./config.json') as data_file:    
		config = json.load(data_file)

	session_folder = os.path.dirname(config['processed_sessions_folder'])
	# print session_folder

	# get all the name of subdir
	subdirectories = os.listdir(session_folder)
	# print subdirectories
	for each_subdir in subdirectories:
		# print each_subdir also called session ID
		if each_subdir == ".DS_Store":
			continue

		each_subdir_folder = os.path.join(config['processed_sessions_folder'], each_subdir)
		# print each_subdir_folder

		with open(each_subdir_folder+"/status.json") as status_file:    
			status = json.load(status_file) 
		# print status["status"]

		if status["status"] == "ok":
			print "yes"
			imgdirectories = os.listdir(each_subdir_folder + "/img")
			#print imgdirectories
			img_list = []
			for each_img_name in imgdirectories:
				if each_img_name == ".DS_Store":
					continue

				#print int(each_img_name.split(".")[0])
				img_list.append(int(each_img_name.split(".")[0]))

			# print sorted(img_list)
			# save seach session + sorted img_name_list
			db.save_images_for_session(each_subdir,sorted(img_list))






