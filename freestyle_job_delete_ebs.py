import json
import boto3
import time
regions = ['us-east-1','us-east-2','ap-south-1']
def delete_ebs_vols():
    for reg in regions:
        unattachedvols = []
        client = boto3.client('ec2',region_name=reg)
        resp = client.describe_volumes().get('Volumes',[])
        for vol in resp:
          if len(vol['Attachments']) == 0:
             volid = vol['VolumeId']
             print(f"Volume {volid} is not attached in region {reg} and will be deleted.")
             unattachedvols.append(vol['VolumeId'])
          else:
             volid = vol['VolumeId']
             """print(f"Volume {volid} is attached")"""   
        ec2_resource = boto3.resource('ec2', region_name=reg)
        if  len(unattachedvols) != 0:
            print(f"The Volumes which are not attached and will be deleted are {unattachedvols} in region {reg}.")
            for vol in unattachedvols:
              volume = ec2_resource.Volume(vol)
              volume.delete()
        else:
            print(f'NO UNATTACHED VOLUME TO DELETE IN REGION {reg}')
            
delete_ebs_vols()
