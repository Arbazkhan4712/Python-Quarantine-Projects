import boto3

s3_client = boto3.client(
    's3',
    aws_access_key_id='',# add the aws access key
    aws_secret_access_key=''# add the aws secret access key
    
)

collectionId='' #collection name

rek_client=boto3.client('rekognition',
                            aws_access_key_id='',# add the aws access key
                            aws_secret_access_key='',# add the aws secret access key
                            region_name='',)# add the region here


bucket = '' #S3 bucket name
all_objects = s3_client.list_objects(Bucket =bucket )


'''
delete existing collection if it exists
'''
list_response=rek_client.list_collections(MaxResults=2)

if collectionId in list_response['CollectionIds']:


    rek_client.delete_collection(CollectionId=collectionId)

'''
create a new collection 
'''
rek_client.create_collection(CollectionId=collectionId)

'''
add all images in current bucket to the collections
use folder names as the labels
'''

for content in all_objects['Contents']:
    collection_name,collection_image =content['Key'].split('/')
    if collection_image:
        label = collection_name
        print('indexing: ',label)
        image = content['Key']    
        index_response=rek_client.index_faces(CollectionId=collectionId,
                                Image={'S3Object':{'Bucket':bucket,'Name':image}},
                                ExternalImageId=label,
                                MaxFaces=1,
                                QualityFilter="AUTO",
                                DetectionAttributes=['ALL'])
        print('FaceId: ',index_response['FaceRecords'][0]['Face']['FaceId'])