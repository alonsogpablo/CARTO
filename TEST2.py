from cartodb import CartoDBAPIKey, CartoDBException

API_KEY ='a89973f57166ad09cc6f1b6004962dbbc0076c0c'
cartodb_domain = 'palonso0vf'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)
#try:


#except CartoDBException as e:
#   print("some error ocurred", e)

#Peticion SQL
petition = ("""SELECT
    sum(ST_Area(ST_Intersection(lte_plus_100_109_112_nacional_31032016.the_geom, ign_spanish_adm3_municipalities.the_geom::geography)))/1000000 area,
    lte_plus_100_109_112_nacional_31032016.threshold
FROM lte_plus_100_109_112_nacional_31032016, ign_spanish_adm3_municipalities
WHERE ST_Intersects(lte_plus_100_109_112_nacional_31032016.the_geom, ign_spanish_adm3_municipalities.the_geom) and ign_spanish_adm3_municipalities.nameunit like '%alladolid%'
GROUP BY lte_plus_100_109_112_nacional_31032016.threshold;""")


catch = (cl.sql(petition))
for f in catch['rows']:
    print f
