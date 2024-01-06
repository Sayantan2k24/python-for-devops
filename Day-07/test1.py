import sys

instance_type = sys.argv[1]

if instance_type == "t2.micro":
    print("ok, we will create the instance for you")
else:
    print("your input is not t2.micro, so we cannot create")


'''

$ python test1.py t2.micro
ok, we will create the instance for you 

$ python test1.py t2.medium
your input is not t2.micro, so we cannot create

'''