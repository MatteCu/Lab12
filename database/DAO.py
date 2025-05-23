from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.sold_same_product import SoldTheSame

class DAO():
    def __init__(self):
        pass
    @staticmethod
    def get_all_nations():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """select distinct Country 
from go_retailers gr    """

        cursor.execute(query)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_years():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """select distinct year(gds.`Date`)
from go_daily_sales gds   """

        cursor.execute(query)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_retailers_fromcnt(country):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
FROM go_retailers gr 
where gr.Country = %s  """

        cursor.execute(query, (country,))

        for row in cursor:
            result.append(Retailer(**row))

        cursor.close()
        conn.close()
        return result

    def get_items_sold_by_retailer(country, year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
SELECT  gds.Retailer_code as R1 , gds2.Retailer_code as R2, gds.Product_number as P
from go_daily_sales gds, go_daily_sales gds2  , go_retailers gr 
where gds.Retailer_code = gr.Retailer_code AND gr.Country = %s and YEAR(gds.date)= %s and gds.Retailer_code <> gds2.Retailer_code AND gds.Product_number = gds2.Product_number
"""

        cursor.execute(query, (country,year))
        index=0

        for row in cursor:
            #print(f"AAAAAAAAAAAAAAAAA{row}")
            result.append(SoldTheSame(index, row["R1"], row["R2"], row["P"]))
            index+=1

        cursor.close()
        conn.close()
        return result

