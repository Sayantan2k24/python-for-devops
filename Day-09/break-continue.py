numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        print("Found 3! Breaking out of the loop.")
        break
    elif number == 2:
        print("Skipping 2!")
        continue
    print("Current number:", number)

print("Loop finished!")


'''
When the loop encounters the value 3, the break statement is executed, and the loop is terminated.
When the loop encounters the value 2, the continue statement is executed, 
and it skips the rest of the code inside the loop for that iteration.
For other values, it prints "Current number: [value]" to show the progress of the loop.
The final message "Loop finished!" is printed outside the loop.

'''
