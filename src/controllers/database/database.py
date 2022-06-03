import keyring

from sshtunnel import SSHTunnelForwarder
from mysql import connector


class Database(object):

    def __init__(self):
        try:
            self.ssh_tunnel = SSHTunnelForwarder(
                ('185.237.96.134', 22),
                ssh_password=keyring.get_credential(service_name="ssh_login", username=None).password,
                ssh_username=keyring.get_credential(service_name="ssh_login", username=None).username,
                remote_bind_address=('127.0.0.1', 3306)
            )

            self.ssh_tunnel.start()

            self.db = connector.MySQLConnection(
                user=keyring.get_credential(service_name="db_login", username=None).username,
                password=keyring.get_credential(service_name="db_login", username=None).password,
                host='127.0.0.1',
                port=self.ssh_tunnel.local_bind_port,
                database='progex',
                autocommit=True
            )

            self.db_cursor = self.db.cursor()
        except Exception as e:
            print(e)

    def __del__(self):
        self.db.close()
        self.ssh_tunnel.close()
