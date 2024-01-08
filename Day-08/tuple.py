#tuple # immutable

s3_buckets_list =("sayantan_demo_bucket", "aj_demo_bucket", "jim_demo_bucket","john_demo_bucket")

# s3_buckets_list.append("tom_new_bucket")


print(type(s3_buckets_list))
print(s3_buckets_list)

'''

s3_buckets_list.append("tom_new_bucket" 

it will cause this error -->
output: 

     s3_buckets_list.append("tom_new_bucket")
AttributeError: 'tuple' object has no attribute 'append'

'''



'''
<class 'tuple'>
('sayantan_demo_bucket', 'aj_demo_bucket', 'jim_demo_bucket', 'john_demo_bucket')

'''