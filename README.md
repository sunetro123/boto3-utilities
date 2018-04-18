# boto3-utilities
A Repo for boto3 utilities very much used
## USECASE 1:
Requirement is to check if any Key exists for latest partition. Partition is defined as `year=xxxx/month=yy/date=zz/version=1`. A batch run will be always one day behind from today.
#### Learning :
      - use of timedelta
      - map always works on iterable, so  a string split shall become a list
      - How to use if-else-if-else in single line
      -Most important --> Syntax of boto3.client('s3).list_objects_v2 ( How to use delimiter)
      -How to use try-except-else in For loop

