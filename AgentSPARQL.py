__author__ = 'bejar'

from SPARQLWrapper import SPARQLWrapper, JSON

from SPARQLPoints import OPENLINK, DBPEDIA


sparql = SPARQLWrapper(DBPEDIA)


# sparql.setQuery("""
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#
#     SELECT  ?val,  ?label
#     WHERE { ?val  <http://yago-knowledge.org/resource/isConnectedTo>   <http://yago-knowledge.org/resource/Barcelona>.
#             ?val  <http://yago-knowledge.org/resource/isLocatedIn> ?label}
# """)

#f = open('/home/javier/DBAirports.csv', 'w')

#sparql.setQuery("""
#    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#    PREFIX dbpedia2: <http://dbpedia.org/property/>
#    SELECT  DISTINCT *
#    WHERE { ?subject rdf:type <http://dbpedia.org/ontology/Airport>.
#            ?subject <http://dbpedia.org/ontology/iataLocationIdentifier> ?IATA.
#            ?subject <http://dbpedia.org/property/cityServed> ?city.
#            ?subject <http://dbpedia.org/property/name> ?name.
#            ?subject <http://www.w3.org/2003/01/geo/wgs84_pos#long> ?long.
#            ?subject <http://www.w3.org/2003/01/geo/wgs84_pos#lat> ?lat.
#            FILTER (lang(?name) = "en" or lang(?name) = "" )
#          }
#""")

sparql.setQuery("""
 Prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
 Prefix ogc: <http://www.opengis.net/ont/geosparql#>
 Prefix geom: <http://geovocab.org/geometry#>
 Prefix lgdo: <http://linkedgeodata.org/ontology/>
 Prefix dbp: <http://dbpedia.org/ontology/>

Select *
   WHERE
  {
    <http://dbpedia.org/resource/New_York_metropolitan_area> dbp:populationTotal ?t .
  }
  LIMIT 200
 """)


sparql.setReturnFormat(JSON)
results = sparql.query()#.convert()

#print results

results.print_results()

#for result in results["results"]["bindings"]:
#    try:
#        f.write(result['subject']['value']+','
#                +result['name']['value']+','
#                +result['IATA']['value']+','
#                +result['city']['value']+','
#                +result['long']['value']+','
#                +result['lat']['value']
#                +'\n')
#    except UnicodeEncodeError:
#        pass

#f.close()






# sparql.setReturnFormat(JSON)
# results = sparql.query()
# print results.print_results()

# sparql.setQuery("""
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX dbpo: <http://dbpedia.org/property/>
# SELECT ?subdivision ?label
# WHERE {
#   <http://dbpedia.org/resource/Catalunya> dbpo:subdivisionName ?subdivision .
#   ?subdivision rdfs:label ?label .
# }
# """)
# sparql.setReturnFormat(JSON)
# results = sparql.query()
# results.print_results()