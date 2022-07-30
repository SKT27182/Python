#!/usr/bin/env python3
import csv
import re
file_path = 'data/courses_offered.csv'
#make a dictionary of Course Name as key and Current Strength as value	
def course_strength(file_path):
	with open(file_path) as f:
	#DictReader reads line by line and map the info in the form of Dictionary
		reader = csv.DictReader(f)
		#Created an empty Dictionary to store required field
		course_dic = {}
		for r in reader:
			if re.search("\d",r["Vacancy"]):
				v = int(r["Vacancy"])
				c = int(r["Current Strength"])
				course_dic[r["Course Name"]] = v - c
				#course_dic[r["Course Name"]] =(int(r["Vacancy"]) - int(r["Current Strength"]))
		return course_dic

#Contains all The Course Name and their Vacancy in the form of Dictionary
dictionary = course_strength(file_path)
#print(dictionary)
#Create a updated Dictionary by Refining the Course Name as per required
def refine_course_name(dictionary):
	#empty dictionary to store updated data
	updated_dic = {}
	for course_name, vacancy in dictionary.items():
		#Adds only the  Required part of Course Name as keys of a Dic.
		if re.search(r"(?=[A-Z]{3,3}\d{3})\w+",course_name):
			updated_dic[(re.search(r"(?=[A-Z]{3,3}\d{3})\w+",course_name)[0])] = vacancy
		else:
			pass
	return updated_dic

#Contains only the Required part of Course name and their Vacancy
updated_dictionary = refine_course_name(dictionary)
#print(updated_dictionary)


def show_vaccancy(updated_data):
	'''Enter the Required Subject Abbrivation'''
	key_word = input("Enter the keyWord: ")
	vacant_seats = input("Enter the no. of seats you are searching: ")
	for key, value in updated_dictionary.items():
		#Passes only if both Course Name and Vacancy is given
		if (key.startswith(key_word)) and key_word != '' and vacant_seats !='' and value == int(vacant_seats):
			print("{} has {} vaccany left".format(key,value))
		#Passes if Vacancy is given and Course Name is blank
		elif vacant_seats != '' and value == int(vacant_seats) and key_word == '':
			print("{} has {} vaccany left".format(key,value))
		#Passes if Course Name is given and Vacancy is blank
		elif (key.startswith(key_word)) and key_word != '' and vacant_seats =='':
			print("{} has {} vaccany left".format(key,value))
		#Passes if both are blank
		elif vacant_seats == '' and key_word=='':
			print("{} has {} vaccany left".format(key,value))
		else:
			pass



show_vaccancy(updated_dictionary)
