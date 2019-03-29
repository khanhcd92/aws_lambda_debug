from __future__ import print_function
import os

def handler(event, context):
    print('event:', event)
    region = os.environ['REGION']
    print('region: ', region)
