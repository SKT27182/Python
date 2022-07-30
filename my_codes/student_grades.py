#!/usr/bin/env python3


###########################################################################################################################################################
"""
Store the record of the student in the form of csv file named as "student_grade_info.csv" in same folder as the python file.
The csv file should have the following columns:
Student ID, Student Name, Subject, Final Marks, Interim Grade, Grade Point

"""
###########################################################################################################################################################



############################################################
# import modules
############################################################

import pandas as pd
import numpy as np
import os


#############################################################
# Define DataFrame
#############################################################

if ("student_grade_info.csv" in os.listdir("data/")):
    data_frame = pd.read_csv("student_grade_info.csv")
else:
    data_frame = pd.DataFrame(columns=['Student_ID','Student_Name','University','Final_Marks','Final_Grade_Letter','Grade_Point'])


#############################################################
# Final Marks Calculations
#############################################################

def final_marks(assessment_marks):
    return (assessment_marks[0] * 0.2) + (assessment_marks[1] *0.4) + ( assessment_marks[2] *0.4) 



#############################################################
# Interim Grade for BIT Calculations
#############################################################

def bit_interim_grade(assessment_marks):
    final_marks_ = final_marks(assessment_marks)
    if final_marks_ >= 85:
        return "HD" , final_marks_
    elif final_marks_ >= 75:
        return "D" , final_marks_
    elif final_marks_ >= 65:
        return "C" , final_marks_
    elif final_marks_ >= 50:
        return "P" , final_marks_
    elif final_marks_ >= 45:
        if (sum(1 for i in assessment_marks if i == 0) ==0) & (sum(1 for j in assessment_marks if j < 50) ==1):
            if assessment_marks[0] < 50: 
                return check_sa_se(assessment_marks ,"SA",0)
            elif  assessment_marks[1] < 50 :
                return check_sa_se(assessment_marks , "SA",1)
            else :
                return check_sa_se(assessment_marks , "SE",2)
        else:
            return "F" , final_marks_
        
    else:
        if sum(1 for i in assessment_marks if i == 0) > 1:
            return "AF" , final_marks_
        else:
            return "F" , final_marks_



def check_sa_se(marks,grade,subject):
    if grade == "SA":
        new_marks = float(input("Enter student assessment marks: "))
        
    else:
        new_marks = float(input("What is this student’s supplementary exam mark: "))

    marks[subject] = new_marks
    final_marks_ = final_marks(marks)

    return bit_interim_grade(marks)


#############################################################
# BIT Grade Point Calculations
#############################################################


def bit_final_grade_letter(bit_interim_grade):
    if bit_interim_grade == "HD":
        return 4.0
    elif bit_interim_grade == "D":
        return 3.0
    elif bit_interim_grade == "C": 
        return 2.0
    elif bit_interim_grade == "P":
        return 1.0
    elif bit_interim_grade == "SP":
        return 0.5
    else:
        return 0.0
    

#############################################################
# Interim Grade for DIT Calculations
#############################################################


def dit_interim_grade(assessment_marks):
    final_marks_ = final_marks(assessment_marks)
    if final_marks_ >= 50:
        return "CP",final_marks_
    else:
        return check_nyc()


def check_nyc():
    resub_marks = list(map(int , (input("What is this student’s resubmission marks (separated by comma): ")).split(',')))
    return dit_interim_grade(resub_marks)


#############################################################
# DIT Grade Point Calculations
#############################################################


def dit_final_grade_letter(dit_interim_grade):
    dic_grade_point = {}
    if dit_interim_grade == "CP":
        return 4.0
    else:
        return 0.0


#############################################################
# Common Input
#############################################################

def common_input():
    student_id =   input("Enter student ID: ")
    student_name =   input("Enter student name: ")
    assessment_marks = list(map(int , (input("Enter student assessment marks (separated by comma): ")).split(',')))
    return student_id,student_name,assessment_marks


#############################################################
# BIT Input
#############################################################

def bit_input():
    student_id,student_name,assessment_marks =common_input()
    
    bit_interim_grade_, final_marks_ = bit_interim_grade(assessment_marks)
    grade_point = bit_final_grade_letter(bit_interim_grade_)
    data_frame.loc[len(data_frame)] = [student_id,student_name,"BIT",final_marks_, bit_interim_grade_,grade_point]


#############################################################
# DIT Input
#############################################################

def dit_input():
    student_id,student_name,assessment_marks =common_input()

    dit_interim_grade_, final_marks_ = dit_interim_grade(assessment_marks)
    grade_point = dit_final_grade_letter(dit_interim_grade_)
    data_frame.loc[len(data_frame)] = [student_id,student_name,"DIT",final_marks_, dit_interim_grade_,grade_point]



#############################################################
# one point menu
#############################################################


def ono_point_menu():
            option_1 = float(input("Choose one of the following options:\n1.1 - Enter a BIT student information\n1.2 - Enter a DIT student information\n1.3 - Go back to the main menu\n"))
            if option_1 == 1.1:
                bit_input()
                ono_point_menu()
            elif option_1 == 1.2:
                dit_input()
                ono_point_menu()
            elif option_1 == 1.3:
                main_menu()
            else:
                print("Invalid option")
                ono_point_menu()


#############################################################
# two point menu
#############################################################

def two_menu():
    option_2 = float(input("Choose one of the following options:\n2.1 – Print all student grade information ascendingly by final mark\n2.2 – Print all student grade information descendingly by final mark\n2.3 – Go back to the main menu\n"))
    if option_2 == 2.1:
        print(data_frame.sort_values(by=['Final_Marks'],ascending=True)[['Student_ID','Student_Name','University','Final_Marks','Final_Grade_Letter']])
        two_menu()
    elif option_2 == 2.2:
        print(data_frame.sort_values(by=['Final_Marks'],ascending=False)[['Student_ID','Student_Name','University','Final_Marks','Final_Grade_Letter']])
        two_menu()
    elif option_2 == 2.3:
        main_menu()
    else :
        print("Invalid option")
        two_menu()


#############################################################
# three point menu
#############################################################

def three_menu():
    print("Number of students: "+str(data_frame.shape[0]))
    print("Number of BIT students: "+str(data_frame[data_frame['University'] == 'BIT'].shape[0]))
    print("Number of DIT students: "+str(data_frame[data_frame['University'] == 'DIT'].shape[0]))
    hd = data_frame[data_frame['Final_Grade_Letter'] == 'HD'].shape[0]
    d = data_frame[data_frame['Final_Grade_Letter'] == 'D'].shape[0]
    c = data_frame[data_frame['Final_Grade_Letter'] == 'C'].shape[0]
    p = data_frame[data_frame['Final_Grade_Letter'] == 'P'].shape[0]
    SP = data_frame[data_frame['Final_Grade_Letter'] == 'SP'].shape[0]
    CP = data_frame[data_frame['Final_Grade_Letter'] == 'CP'].shape[0]
    students = data_frame.shape[0]
    student_pass_rate = (hd + d + c + p + SP + CP)/students
    print("Student pass rate: "+str(student_pass_rate))
    AF = data_frame[data_frame['Final_Grade_Letter'] == 'AF'].shape[0]
    student_pass_rate_adj = (hd + d + c + p + SP + CP )/(students - AF)
    print("Student pass rate adjusted: "+str(student_pass_rate_adj))
    print("Average Final Mark: "+str(data_frame['Final_Marks'].mean()))
    print("Average grade point: "+str(data_frame['Grade_Point'].mean()))
    print("Number of HDs: "+ str(hd))
    print("Number of Ds: "+ str(d))
    print("Number of Cs: "+ str(c))
    print("Number of Ps: "+ str(p))
    print("Number of SPs: "+ str(SP))
    print("Number of CPs: "+ str(CP))
    F = data_frame[data_frame['Final_Grade_Letter'] == 'F'].shape[0]
    print("Number of Fs: "+ str(F))
    main_menu()




#############################################################
# Main Menu
#############################################################

def main_menu():

    menu = int(input("Choose one of the following options \n1 - Enter student grade information\n2 - Print all student grade information\n3 - Print class performance statistics\n4 - Exit\n"))
    if menu == 1:     
        ono_point_menu()
    elif menu == 2:
        two_menu()
    elif menu == 3:
        three_menu()
    elif menu == 4:
        data_frame.to_csv("student_grade_info.csv",index=False)
        exit()
    else:
        print("Invalid option")
        main_menu()


main_menu()
