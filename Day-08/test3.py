students_name = ["Sayantan", "Ram", "John", "Tom"]

students_name.append("Pop") #append
print(students_name)

students_name.remove("Pop")  #remove 
print(students_name)

subset = students_name[1:4] #slicing elements from index 1 to 3 , exclude 4 
print(subset) 

test_list =  students_name + [5, 6]  #concatenating
print(test_list)

is_present = 'Sayantan' in test_list #checking 
print(is_present)