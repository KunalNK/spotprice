import boto3
import boto3, json
import pprint
import urllib.request, json
import csv
from datetime import datetime
client=boto3.client('ec2',region_name='ap-south-1')
now = datetime.utcnow()
prices=client.describe_spot_price_history(StartTime=now,EndTime=now,MaxResults=10,ProductDescriptions=['Linux/UNIX (Amazon VPC)'],AvailabilityZone='ap-south-1a')
# mydata = json.dumps(prices.read())
# pprint.pprint(prices['SpotPriceHistory'][:10]) 

dic=prices['SpotPriceHistory']

# az=(dic[1]['AvailabilityZone'])
# spotprice=(dic[1]['SpotPrice'])
# instaname=(dic[1]['InstanceType'])

# print(az)
# print(spotprice)
# print(instaname)

with open('azwise1.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Instancename','Availabilityzone1a(USD)','Availabilityzone1b(USD)','Availabilityzone1c(USD)','LowestPrice(USD)'])
    for elements in dic:
        instaname=elements['InstanceType']
        #az=elements['AvailabilityZone']
        spotprice1a=elements['SpotPrice']
        

        # thewriter.writerow([instaname,spotprice1a])

prices=client.describe_spot_price_history(StartTime=now,EndTime=now,MaxResults=10,ProductDescriptions=['Linux/UNIX (Amazon VPC)'],AvailabilityZone='ap-south-1b')
# mydata = json.dumps(prices.read())
# pprint.pprint(prices['SpotPriceHistory'][:10]) 

dic=prices['SpotPriceHistory']

with open('azwise1.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Instancename','Availabilityzone1a(USD)','Availabilityzone1b(USD)','Availabilityzone1c(USD)','LowestPrice(USD)'])
    for elements in dic:
        instaname=elements['InstanceType']
        #az=elements['AvailabilityZone']
        spotprice1b=elements['SpotPrice']


prices=client.describe_spot_price_history(StartTime=now,EndTime=now,MaxResults=10,ProductDescriptions=['Linux/UNIX (Amazon VPC)'],AvailabilityZone='ap-south-1c')
# mydata = json.dumps(prices.read())
# pprint.pprint(prices['SpotPriceHistory'][:10]) 

dic=prices['SpotPriceHistory']

with open('azwise1.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Instancename','Availabilityzone1a(USD)','Availabilityzone1b(USD)','Availabilityzone1c(USD)','LowestPrice(USD)'])
    for elements in dic:
        instaname=elements['InstanceType']
        #az=elements['AvailabilityZone']
        spotprice1c=elements['SpotPrice']

        data=[spotprice1a,spotprice1b,spotprice1c]
        print(data)
        lowestprice = min(float(sub) for sub in data) 
        

        thewriter.writerow([instaname,spotprice1a,spotprice1b,spotprice1c,lowestprice])


