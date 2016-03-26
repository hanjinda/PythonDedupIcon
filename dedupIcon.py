# -*- coding:utf-8 -*-
# 1 reach all the class and in each class compare all the object with each other
import json
import itertools
import compare_icon
import remove_dup_icon

with open("training_elements_by_session.json") as json_file1:
    training_elements_by_session = json.load(json_file1)
    #print(training_elements_by_session)

with open("testing_elements_by_session.json") as json_file2:
    testing_elements_by_session = json.load(json_file2)
    #print(testing_elements_by_session)

# save training to list to compare
list_training = []
for session in training_elements_by_session:
	list_training.append(session)

for session in list_training:
	#print ssn
	session = str(session)
	# print all the element in the array
	print len(training_elements_by_session[session])

	# compare each icon element by
	for x,y in itertools.combinations(training_elements_by_session[session], 2):
		print x, y


# save testing to list to compare
list_testing = []
for session in training_elements_by_session:
	list_testing.append(session)






