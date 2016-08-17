import sys
import urllib
import urllib2
import json
import requests

username = 'palonso0vf'
api_key = ''


#RUNTIME QUERY
from cartodb import CartoDBAPIKey, CartoDBException
cl = CartoDBAPIKey(api_key, username)

#BATCH QUERY

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





rtsql='SELECT * FROM TEEST3'
catch = (cl.sql(rtsql))
for f in catch['rows']:
    sql = """
    INSERT INTO TEST1708b
    SELECT
          ST_Area(
            ST_Intersection(l.the_geom::geography, m.the_geom::geography))/1000000 area,
        l.threshold,
        m.nameunit
    FROM lte_plus_100_109_112_nacional_31032016 l, ign_spanish_adm3_municipalities m
    WHERE l.the_geom && m.the_geom
    AND nameunit like '%s'
    """ % f['nameunit']
    job = cartoBatchQuery(username,api_key,sql)
    status = cartoBatchStatus(username, api_key, job["job_id"])
    print status
