import pandas as pd
import pymysql
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder
ssh_host = '1.2.3.4'
ssh_username = 'root'
database_username = 'bob_smith'
database_password = 'SecretDBPassword'
database_name = 'ecommerce'
localhost = '127.0.0.1'
home = expanduser('~')
mypkey = paramiko.RSAKey.from_private_key_file(home + pkeyfilepath)

text_file = open("db.sql", "r")
open_ssh_tunnel()
mysql_connect()
df = run_query("SELECT * FROM orders ORDER BY id DESC LIMIT 100")
df.head()

mysql_disconnect()
close_ssh_tunnel()


def open_ssh_tunnel(verbose=False):
    """Open an SSH tunnel and connect using a username and password.
    
    :param verbose: Set to True to show logging
    :return tunnel: Global SSH tunnel connection
    """
    
    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
    
    global tunnel
    tunnel = SSHTunnelForwarder(
        (ssh_host, 22),
        ssh_username = ssh_username,
        ssh_pkey=mypkey,
        remote_bind_address = ('127.0.0.1', 3306)
    )
    
    tunnel.start()


def mysql_connect():
    """Connect to a MySQL server using the SSH tunnel connection
    
    :return connection: Global MySQL database connection
    """
    
    global connection
    
    connection = pymysql.connect(
        host='127.0.0.1',
        user=database_username,
        passwd=database_password,
        db=database_name,
        port=tunnel.local_bind_port
    )


def run_query(sql):
    """Runs a given SQL query via the global database connection.
    
    :param sql: MySQL query
    :return: Pandas dataframe containing results
    """
    
    return pd.read_sql_query(sql, connection)

def mysql_disconnect():
    """Closes the MySQL database connection.
    """
    
    connection.close()


def close_ssh_tunnel():
    """Closes the SSH tunnel connection.
    """
    
    tunnel.close
