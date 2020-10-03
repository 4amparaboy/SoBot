import psycopg2


class Controller(object):

    def __init__(self, dbname, user, password, host):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def add_so(self, user, so):
        self.cursor.execute('INSERT INTO user_so (id, so) VALUES(%s, %s)', (
            user, so))
        self.conn.commit()

    def get_so(self, user):
        try:
            self.cursor.execute('SELECT DISTINCT so FROM user_so WHERE id =' + str(user))
            return self.cursor.fetchall()
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
            return [[]]

    def delete_so(self, user):
        self.cursor.execute('DELETE FROM user_so WHERE id =' + str(user))
        self.conn.commit()


    def get_soinfo(self, so):
        try:
            self.cursor.execute('SELECT information FROM so_info WHERE number =' + str(so))
            return self.cursor.fetchall()
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
            return [[]]
    def get_soinfo_fromuser(self, user):
        try:
            self.cursor.execute(
                'SELECT information FROM so_info WHERE so in (SELECT DISTINCT so FROM user_so WHERE id = %s)', ([user]))
            return self.cursor.fetchall()
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
            return [[]]
    def normalization(self):
        self.cursor.execute('UPDATE user_so SET so = REPLACE(so,\'*\',\'\')', )
        self.conn.commit()
