#https://github.com/Wangdikwang3210/03230104_BIA101_CAP3
#Karma Wangdi
#BBI A
# 03230104
#references
#https://www.w3schools.com/python/python_regex.asp
#https://hackernoon.com/how-to-read-text-file-in-python

# solution
# the sum of all two-digit numbers is = 477541 


import re

def extract_digits(line):# extracting all individual lines
    digits = re.findall(r'\d', line)
    if len(digits) < 2:
        return 0
    return int(digits[0] + digits[-1])# Combining the first and the last digit found to form new number

def calculate_sum_from_file(filename): # initializing the total sum to 0
    total_sum = 0
    try:
        with open(filename, 'r') as file:
            for line in file:# reading the file by each line
                number = extract_digits(line.strip())# process the line to extract two digit number 
                total_sum += number# adding the extracted numbe to the total sum
    except FileNotFoundError:
        print(f"File {filename} not found.")# print error if file is not found 
    return total_sum

filename = '104.txt'
result = calculate_sum_from_file(filename)# calculate the sum of all to digit numbers from the file
print(f"The sum of all the two-digit numbers is: {result}")# printing the output
