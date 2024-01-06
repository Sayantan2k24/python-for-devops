import sys

instance_type = sys.argv[1]

if instance_type == "t2.micro":
    print("it will charge you 2 dollars a day")
elif instance_type == "t2.medium":
    print("it will charge you 4 dollars a day")
elif instance_type == "t2.xlarge":
    print("it will charge you 8 dollars a day")
else:
    print("Please provide a valid instance type")


'''
$ python test2.py t2.micro
it will charge you 2 dollars a day


$ python test2.py t2.medium
it will charge you 4 dollars a day


$ python test2.py t2.xlarge
it will charge you 8 dollars a day


$ python test2.py t2.ultimate
Please provide a valid instance type

'''