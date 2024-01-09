numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        print("Skipping 3!")
        continue
    print("Current number:", number)

print("Loop finished!")



'''
In this code, the for loop iterates through the `numbers` list. 
When it encounters the value `3`, the `continue` statement is executed, 
and it skips the rest of the code inside the loop for that particular iteration. 
The message "Skipping 3!" is printed, and then the loop continues with the next iteration. 
The final message "Loop finished!" is printed outside the loop.

'''