# S3 - Simple Storage Service

Some basic concepts about S3:

- S3 was made to store objects
- FIles size can go from 0 Bytes to 5 TB
- There is not size limit on S3's disk
- S3's URL is composed like this '[region].amazonaws.com/[nom]'
- When you uplod an file to S3 you recieve an 200 http status code
- By default S3's and his files are set to private
- S3's access to buckets are managed by ACL or Bucket Policies

Consistency Model of S3:

- When you insert something into S3, it's possible to use it immediately
- When you delete or update a file there is an delay to propagate the changes

S3's Objects

- Key <- Stands for the name of the file
- Value <- Stands for the bytes of the file
- Version ID <- Used to manage the versioning of the file
- Metadata <- Data about the file

Storage Tiers/Classes

- S3 - 99.99% availability, durability, stored in diferent places
- SS3 - IA (Infrequently Acessed) - Files that are accessed sporadically, but require speed in the retrieving
- Reduced Redundancy Storage - It's an S3 for an year. If you make the commitment of using it for an Year, you get some discount
- Glacier - It's an S3 used to retrieve archical files, files store on Glacier can take hours to be retrieved

Charged For

- Storaging
- Requests
- Storage Management Princing
- Data transfer

`{bucket-name}s3-website-{region}.amazonaws.com`
