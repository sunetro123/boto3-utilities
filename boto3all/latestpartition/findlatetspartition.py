import boto3
from datetime import timedelta, date

"""
Assuming  you are running for today (2018-APR-18), 'Latest' partition will always be one day behind (2018-APR-17) 
if the Pipeline Batch Run has not Failed .
From My old utility, I just changed path and assume you are only looking for 'DWH' tables data/env/dev/output/dwh/
XX --> actual bucket name
"""

client = boto3.client("s3")
deeper_levels = "".join(list(map(lambda t: 'batch_year=' + t[1] if t[0] == 0 else '/batch_month=' + t[1] if t[0] == 1 \
    else '/batch_day=' \
         + t[1], [(i, x) for i, x in enumerate((date.today() - timedelta(days=1)).strftime("%Y-%m-%d").split("-"))]))) + \
                '/batch_version=1/'
for x in client.list_objects_v2(Bucket='XX', Prefix='data/env/dev/output/dwh/', Delimiter='/')[
    'CommonPrefixes']:
    try:
        print(" There is a Key :--> {} \n".format( \
            client.list_objects_v2(Bucket='XX', \
                                   MaxKeys=1, Prefix=x['Prefix'] + deeper_levels, Delimiter='/') \
                ['Contents'][0]['Key']))
        # METHOD TO READ PARQUET THRU SPARK  CAN BE CALLED HERE

    except KeyError as e:
        print("\n ***IT's Sad, So Sad But There AIN't NO --> \"{}\" <--Around ****** \n".format(
            x['Prefix'] + deeper_levels))
    else:
        continue