from database.DB_connect import DBConnect


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

