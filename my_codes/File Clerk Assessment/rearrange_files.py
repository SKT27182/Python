#!/usr/bin/python3

import os
import re
import shutil


subject_pattern = r'[A-Z]{2}[\d]{2}'
full_unit_pattern = r'[\[\d\.\d\]]{5}'
topic_pattern = r"(-[\w\s].*)-"   # round bracket allows us to search only inside that brackets also
file_extension_pattern = r"[.][a-z]{3,4}"

files_to_move = os.listdir("Files to Move")


for file in files_to_move:

	sub = re.search(subject_pattern, file)[0] # extract the subject code
	subject_dic = {"PS34":"Psychology","MM34":"Methods","CH34":"Chemistry","PH34":"Physics"}
	subject_name = subject_dic[sub] # get the subject name with the help of subject code

	unit = re.search(full_unit_pattern, file)[0] # extract the unit code with big square bracket

	extension = re.search(file_extension_pattern, file)[0] # extract the extension of a file

	src_folder = os.path.join("Files to Move",file)

	if os.path.isdir(file):
		continue
	else:
		if "video" not in file.lower():
			
			
			topic = re.search(topic_pattern, file)[1] # extract the topic name
			
			new_name =  unit.strip() +" "+ topic.strip() + extension.strip()

			# for the destination folder
			unit_num_pattern = r"\[(\d{1})"
			unit_num = re.search(unit_num_pattern, unit)[1]

			# get the unit_folder name
			unit_folder = ""
			if unit_num in ["1","2","3"]:
				unit_folder = "Unit 3"
			elif unit_num  in ["4","5","6"]:
				unit_folder = "Unit 4"
			elif unit_num =="7":
				unit_folder = "Exam Revision"


			

			destinantion_folder = os.path.join("Contour Database",subject_name,unit_folder,new_name)

			print(f"moving {file} to {destinantion_folder}")
			shutil.move(src_folder,destinantion_folder)

		elif "video" in file.lower():
			with open(src_folder, 'r') as f:

				for line in f:
					if "location" in line.lower():
						location = line.split(":")[1].strip()
						#print(location)
					elif "day" in line.lower():
						day = line.split(":")[1].strip()
						#print(day)
					elif "time" in line.lower():
						time = line.split(":")[1].strip()
						#print(time)

			new_name =  location.strip() + " " + subject_name.strip() + " - "+ day.strip() + " " + time.strip() + " - "+ unit.strip() + " Recording" +extension.strip()
			
			destinantion_folder = os.path.join("Files to Move",new_name)

			print(f"renaming {file} to {new_name}")
			shutil.move(src_folder,destinantion_folder)