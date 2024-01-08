#lists

s3_buckets_list = ["sayantan_demo_bucket", "aj_demo_bucket", "jim_demo_bucket","john_demo_bucket"]
print(s3_buckets_list)

print(len(s3_buckets_list))

s3_buckets_list.append("tom_new_bucket")
print(s3_buckets_list)
print(len(s3_buckets_list))

s3_buckets_list.remove("sayantan_demo_bucket")
s3_buckets_list.remove("aj_demo_bucket")
print(s3_buckets_list)
print(len(s3_buckets_list))


 