import sys
import urllib
import urllib2
import json
import requests

def cartoBatchQuery(username, api_key, sql):
    r = requests.post('http://%s.cartodb.com/api/v2/sql/job?api_key=%s' %(username,api_key),
                headers={'content-type':'application/json'},
                #params={'query': urllib.quote_plus(sql)}
                params={'query':sql}
                )
    return r.json()

def cartoBatchStatus(username, api_key, job_id):
    r = requests.get('https://%s.cartodb.com/api/v2/sql/job/%s?api_key=%s' % (username,job_id,api_key))
    return r.content #.json()



username = 'palonso0vf'
api_key = ''

sql="SELECT * INTO TEST FROM es WHERE name='Valladolid'"


print sql

job = cartoBatchQuery(username,api_key,sql)

print job


status = cartoBatchStatus(username, api_key, job["job_id"])

print status
