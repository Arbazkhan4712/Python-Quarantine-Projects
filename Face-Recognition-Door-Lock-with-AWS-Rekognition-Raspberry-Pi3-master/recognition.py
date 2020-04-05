from picamera import PiCamera
import time
import boto3

directory = '' #folder name on your raspberry pi

P=PiCamera()
P.resolution= (800,600)
P.start_preview()
collectionId='' #collection name

rek_client=boto3.client('rekognition',
                        aws_access_key_id='',# add the aws access key
                        aws_secret_access_key='',# add the aws secret access key
                        region_name='ap-south-1',)# add the region here

if __name__ == "__main__":

        #camera warm-up time
        time.sleep(2)
        
        milli = int(round(time.time() * 1000))
        image = '{}/image_{}.jpg'.format(directory,milli)
        P.capture(image) #capture an image
        print('captured '+image)
        with open(image, 'rb') as image:
            try: #match the captured imges against the indexed faces
                match_response = rek_client.search_faces_by_image(CollectionId=collectionId, Image={'Bytes': image.read()}, MaxFaces=1, FaceMatchThreshold=85)
                if match_response['FaceMatches']:
                    print('Hello, ',match_response['FaceMatches'][0]['Face']['ExternalImageId'])
                    print('Similarity: ',match_response['FaceMatches'][0]['Similarity'])
                    print('Confidence: ',match_response['FaceMatches'][0]['Face']['Confidence'])
    
                else:
                    print('No faces matched')
            except:
                print('No face detected')
            

        time.sleep(1)       
