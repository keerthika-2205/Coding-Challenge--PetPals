import mysql.connector
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnUtil.connection is None:
            conn_string = DBPropertyUtil.get_property_string("C:/Users/ADMIN/Desktop/PetPals/db.properties")
            config = {
                'host': conn_string.split('@')[1].split(':')[0],
                'user': conn_string.split('://')[1].split(':')[0],
                'password': conn_string.split(':')[2].split('@')[0],
                'database': conn_string.split('/')[3],
                'port': int(conn_string.split(':')[3].split('/')[0])
            }
            DBConnUtil.connection = mysql.connector.connect(**config)
        return DBConnUtil.connection