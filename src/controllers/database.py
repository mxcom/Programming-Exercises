from sshtunnel import SSHTunnelForwarder
from mysql import connector

def connection(sshp, dbup):
    ssh_tunnel = SSHTunnelForwarder(
        ('185.237.96.134', 22),
        ssh_password=sshp,
        ssh_username='root',
        remote_bind_address=('127.0.0.1', 3306)
    )

    ssh_tunnel.start()

    db = connector.MySQLConnection(
        user='root',
        password=dbup,
        host='127.0.0.1',
        port=ssh_tunnel.local_bind_port,
        database='progex',
        autocommit=True
    )

    return db
