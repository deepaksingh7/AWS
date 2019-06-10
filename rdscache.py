import mysql.connector
import pickle
import redis

# Example elasiccache

redis_host = 'flipcache.weuur9.ng.0001.usw2.cache.amazonaws.com'
db_host = 'flipbasket.cihbxyzcwmv9.us-west-2.rds.amazonaws.com'

db_username = 'root';
db_password = 'password'
database = 'world'

class City:
    def __init__(self, id, name, countrycode, district, population):
        self.id = id
        self.name = name
        self.countrycode = countrycode
        self.district = district
        self.population = population
        self.tostring()
    def tostring(self):
        print "City is {0} {1} {2} {3} {4}".format(self.id,self.name,self.countrycode,self.district,self.population)

def getAllCity():
    print "\n Getting All City Details \n"
    print "\n -------------------------- -------------------------- \n "
    conn = mysql.connector.connect(host=db_host, user=db_username, passwd=db_password, db=database)
    cur = conn.cursor()
    cur.execute("SELECT ID, Name, CountryCode, District, Population from city where ID=4011")
    for id, name, countrycode, district, population in cur.fetchall() :
        city_obj = City(id, name, countrycode, district, population)
    cur.close()
    conn.close()

def getCity(city_id):
    print "\n Getting the City Details: ", city_id
    print "\n -------------------------- -------------------------- \n "
    red = redis.StrictRedis(host=redis_host, port=6379, db=0)
    red_obj = red.get(city_id)
    if red_obj != None:
        print "Object found in cache, not looking in DB"
        # Deserialize the oject coming from redis
        city_obj = pickle.loads(red_obj)
        city_obj.tostring()
    else:
        print "No key found in redis, going to database to take a look"
        conn = mysql.connector.connect(host=db_host, user=db_username, passwd=db_password, db=database)
        cur = conn.cursor()
        cur.execute("SELECT ID, Name, CountryCode, District, Population from city where ID='%s'" % (city_id))
        for id, name, countrycode, district, population in cur :
            city_obj = City(id, name, countrycode, district, population)
            # Serialize the object
            ser_obj = pickle.dumps(city_obj)
            red.set(city_id,ser_obj)
            print "Order fetched from DBa nd pushed to redis"
        cur.close()
        conn.close()

def main():
     getAllCity()
     getCity(4011)

main()
