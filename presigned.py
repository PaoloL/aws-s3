import urllib2
import time

from boto.s3.connection import S3Connection
from boto.s3.key import Key

#configure
my_s3_bucket = 'training.xpeppers.com'
my_file_to_upload = '/Users/paololatella/Desktop/340963-sepik.jpg'
expires_in = 30

#start connection to Simple Storage Server
connection = S3Connection()
bucket = connection.get_bucket(my_s3_bucket)
k = Key(bucket)
k.key = 'presignedurl-file.jpg'
#upload file
print "Uploading a file ..."
k.set_contents_from_filename(my_file_to_upload)
#generate presigned url
print "Generating presigned url ..."
presignedurl = k.generate_url(expires_in, method='GET', headers=None, force_http=False, response_headers=None, expires_in_absolute=False)
print "Presigned url is: " + presignedurl
print "This url expire in " + str(expires_in) + " seconds"

count = 0;
#test the exprire in
while True:
	print count*10
	try:
		response = urllib2.urlopen(presignedurl)
		time.sleep(10) 
		count+=1
	except urllib2.HTTPError as e:
	    if e.code == 403:
	    	print 'Url expired'
		break
