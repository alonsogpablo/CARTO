from cartodb import CartoDBAPIKey, CartoDBException

API_KEY =''
cartodb_domain = 'palonso0vf'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)
#try:


#except CartoDBException as e:
#   print("some error ocurred", e)

#Peticion SQL
petition = ("""SELECT nameunit, ST_Area(the_geom::geography)/1000000 area FROM ign_spanish_adm3_municipalities where nameunit like '%Valladolid%';""")


catch = (cl.sql(petition))
for f in catch['rows']:
    print f
