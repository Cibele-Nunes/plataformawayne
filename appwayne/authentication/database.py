#import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_security import Security

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
security = Security()
migrate = Migrate()



# con = mysql.connector.connect(
#     buffered=True,
#     host = 'localhost',
#     user = 'root',
#     password = '_belmysql41'
# )

# if con.is_connected():
#     db_info = con.get_server_info()
#     print('Conectado ao servidor MySQL versão', db_info)
# try:
#     with con.cursor() as cursor:
#         cursor.execute('CREATE DATABASE IF NOT EXISTS waynedatabase')
#         cursor.execute('SHOW DATABASES')
#         con.commit()

# finally:
#     cursor.close()
#     con.close()
