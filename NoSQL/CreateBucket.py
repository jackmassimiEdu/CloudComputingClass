import boto3
import csv

bucketName = 'jackmassimihw3bucket'

s3 = boto3.resource('s3',
                    aws_access_key_id='AKIA6CZA42XJ6O25H5VP',
                    aws_secret_access_key='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')
try:
    s3.create_bucket(Bucket=bucketName, CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
except Exception as e:
    print(e)

bucket = s3.Bucket(bucketName)
bucket.Acl().put(ACL='public-read')
s3.Object(bucketName, 'test.jpg').put(
    Body=open('C:/Users/JVMas/Desktop/test.jpg', 'rb'))
s3.Object(bucketName, 'test.jpg').Acl().put(ACL='public-read')


# ------------------------------------------------------------------------------------------------------

dyndb = boto3.resource('dynamodb',
                       aws_access_key_id='AKIA6CZA42XJ6O25H5VP',
                       aws_secret_access_key='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',
                       region_name='us-east-2')
try:
    table = dyndb.create_table(
        TableName='DataTable',
        KeySchema=[
            {'AttributeName': 'PartitionKey', 'KeyType': 'HASH'},
            {'AttributeName': 'RowKey', 'KeyType': 'RANGE'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'PartitionKey', 'AttributeType': 'S'},
            {'AttributeName': 'RowKey', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

except Exception as e:
    print(e)
    table = dyndb.Table("DataTable")

table.meta.client.get_waiter('table_exists').wait(TableName='DataTable')

print(table.item_count)

# ------------------------------------------------------------------------------------------------------

urlbase = "https://s3-us-west-2.amazonaws.com/" + bucketName + "/"

with open('C:/Users/JVMas/OneDrive/School/CS1660/Project3CSVfiles/experiments.csv', 'rt') as csvfile:
    csvf = csv.reader(csvfile, delimiter=',', quotechar='|')
    for item in csvf:
        print(item)

        try:
            body = open('C:/Users/JVMas/OneDrive/School/CS1660/Project3CSVfiles/' + item[4], 'rb')
            s3.Object(bucketName, item[4]).put(Body=body)
            md = s3.Object(bucketName, item[4]).Acl().put(ACL='public-read')
        except Exception as e:
            print("Failed in first try/catch")
            print(e)

        try:
            url = " https://s3-us-west-2.amazonaws.com/" + bucketName + "/" + item[4]
            metadata_item = {'PartitionKey': item[0], 'RowKey': item[1],
                             'conductivity': item[2], 'concentration': item[3], 'url': url}
        except Exception as e:
            print("Failed in second try/catch")
            print(e)

        try:
            table.put_item(Item=metadata_item)
        except:
            print("item may already be there or another failure")

response = table.scan()
print(response)