#AWS S3 bucket text search

# Requirements

Install: 
`python3`
`boto3`

Insert your aws credentials in the script or use standart AWS env variables.
```
AWS_ACCESS_KEY_ID - The access key for your AWS account.
AWS_SECRET_ACCESS_KEY - The secret key for your AWS account.
AWS_SESSION_TOKEN - The session key for your AWS account.
```
launch the script.

```
./s3_search --bucket-name myAwesomebucket --string findMeIfYouCan
```
Enjoy :)
