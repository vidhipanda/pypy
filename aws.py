# Author: Vidhi Panda <vidhimpanda@gmail.com>
# Deleting aws instance using boto3 in python3


import boto3
ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        ids = ["abc"]
        if instance["InstanceId"] == "abc":
            print(instance["PrivateDnsName"])
            ec2resource = boto3.resource('ec2')
            ec2resource.instances.filter(InstanceIds=ids).stop()
