import boto3
import boto3, json
import pprint
import urllib.request, json
import csv

client=boto3.client('ec2',region_name='ap-south-1')

prices=client.describe_spot_price_history(MaxResults=500,ProductDescriptions=['Linux/UNIX (Amazon VPC)'])
# mydata = json.dumps(prices.read())
# pprint.pprint(prices['SpotPriceHistory'][:10]) 

dic=prices['SpotPriceHistory']

# az=(dic[1]['AvailabilityZone'])
# spotprice=(dic[1]['SpotPrice'])
# instaname=(dic[1]['InstanceType'])

# print(az)
# print(spotprice)
# print(instaname)

with open('price.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Availabilityzone','Instancename','Spotprice'])
    for elements in dic:
        instaname=elements['InstanceType']
        az=elements['AvailabilityZone']
        spotprice=elements['SpotPrice']
        

        thewriter.writerow([az,spotprice,instaname])



# print(mydata)
# s
# for price in mydata['AvailabilityZone']:
#     insta=price['AvailabilityZone']
#     print(insta)

# print(prices['SpotPriceHistory'][0])
# print(type(prices))

# for price in mydata['SpotPrice']:
#     Instance_name=price['InstanceType']
#     print(Instance_name)