numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        print("Found 3! Breaking out of the loop.")
        break
    print("Current number:", number)

print("Loop finished!")

'''
In this code, the for loop iterates through the numbers list. 
When it encounters the value 3, the break statement is executed, and the loop is terminated. 
The message "Found 3! Breaking out of the loop." is printed, 
and then "Loop finished!" is printed outside the loop.

'''