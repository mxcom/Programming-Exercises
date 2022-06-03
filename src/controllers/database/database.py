from sshtunnel import SSHTunnelForwarder
from mysql import connector


def connection(ssh_pw, db_pw):
    ssh_tunnel = SSHTunnelForwarder(
        ('185.237.96.134', 22),
        ssh_password=ssh_pw,
        ssh_username='root',
        remote_bind_address=('127.0.0.1', 3306)
    )

    ssh_tunnel.start()

    db = connector.MySQLConnection(
        user='root',
        password=db_pw,
        host='127.0.0.1',
        port=ssh_tunnel.local_bind_port,
        database='progex',
        autocommit=True
    )

    return db
