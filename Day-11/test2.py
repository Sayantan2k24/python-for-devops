ec2_instances_info = [
    {
        "id" : "instance-001",
        "type" : "t2.micro"
    },
    {
        "id" : "instance-002",
        "type" : "t2.medium"
    },
    {
        "id" : "instance-003",
        "type" : "t2.xlarge"
    }
]


print(range(len(ec2_instances_info))) 
print(ec2_instances_info)
print(ec2_instances_info[1])
print(ec2_instances_info[1]["type"])


'''
$ python test2.py 
range(0, 3)
[{'id': 'instance-001', 'type': 't2.micro'}, {'id': 'instance-002', 'type': 't2.medium'}, {'id': 'instance-003', 'type': 't2.xlarge'}]
{'id': 'instance-002', 'type': 't2.medium'}
t2.medium

'''
