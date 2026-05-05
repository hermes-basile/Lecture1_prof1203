import pathlib

import mysql.connector

class DBConnect:
    _mypool = None

    def __init__(self):
        #per implementare il pattern singletone ed impedire al chiamante di creare istanza di classe.
        raise RuntimeError("Attenzione! non devi creare un'istanza di questa classe. Usa i metodi di classe.")

    @classmethod
    def getConnection(cls):
        if cls._mypool is None:
            try:
                # cnx = mysql.connector.connect(
                #     user = "root",
                #     password = "rootroot",
                #     host = "127.0.0.1",
                #     database = "sw_gestionale"
                # )
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(
                    # user = "root",
                    # password = "rootroot",
                    # host = "127.0.0.1",
                    # database="sw_gestionale",
                    pool_size = 3,
                    pool_name = "myPool",
                    option_files = f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"
                )
                return cls._myPool.get_connection()

            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None
        else:
            #allora il pool già esiste, e quindi restituisco direttamente la connessione
            return cls._myPool.get_connection()



