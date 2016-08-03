from cartodb import CartoDBAPIKey, CartoDBException

API_KEY ='a89973f57166ad09cc6f1b6004962dbbc0076c0c'
cartodb_domain = 'palonso0vf'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)
#try:


#except CartoDBException as e:
#   print("some error ocurred", e)

#Peticion SQL
petition = ("""SELECT * FROM job_result""")


catch = (cl.sql(petition))
for f in catch['rows']:
    print f
