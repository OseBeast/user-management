import argparse
from minio import Minio
from minio.error import S3Error


def main():
   parser=argparse.ArgumentParser(description="Minio Uploader Arguments")
   parser.add_argument('-n','--name',help='name assigned to uploaded pic',required=True) #access args.name based on user input
   parser.add_argument('-f','--file',help='path to file to be uploaded',required=True)  #access args.file based on user input
   args=parser.parse_args()
   # Create a client with the MinIO server playground, its access key
   # and secret key.
   client = Minio(
       "localhost:9001",
       access_key="nmE8QGxw5VOZQ24g60gB",
       secret_key="VFNje93OrTWyy9YoTebLfUryHL8OUA8MiIejvTfo",
       secure=False,
   )

   # Make 'profile-pics' bucket if not exist.
   found = client.bucket_exists("profile-pics")
   if not found:
       client.make_bucket("profile-pics")
   else:
       print("Bucket 'profile-pics' already exists")

   # Upload 'minio.jpg' as object name
   # 'minio.jpg' to bucket 'profile-pics'.
   client.fput_object(
       "profile-pics", #Name of bucket to put pic in, on minio
       args.name,     #name that i will assign to the pic - this needs to be a varible of the usersname
       args.file   #API endpoint to where the User uploaded image gets sent (filepath)
   )
   print(
       f"{args.file} is successfully uploaded as {args.name} "
       f"object {args.file} to bucket 'profile-pics'."
   )


if __name__ == "__main__":
   try:
       main()
   except S3Error as exc:
       print("error occurred.", exc)