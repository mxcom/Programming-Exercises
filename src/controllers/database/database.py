import keyring

from sshtunnel import SSHTunnelForwarder
from mysql import connector


class Database(object):

    def __init__(self):
        try:
            self._ssh_tunnel = SSHTunnelForwarder(
                ('185.237.96.134', 22),
                ssh_password=keyring.get_credential(service_name="ssh_login", username=None).password,
                ssh_username=keyring.get_credential(service_name="ssh_login", username=None).username,
                remote_bind_address=('127.0.0.1', 3306)
            )

            self._ssh_tunnel.start()

            self._db = connector.MySQLConnection(
                user=keyring.get_credential(service_name="db_login", username=None).username,
                password=keyring.get_credential(service_name="db_login", username=None).password,
                host='127.0.0.1',
                port=self._ssh_tunnel.local_bind_port,
                database='progex',
                autocommit=True
            )

            self._db_cursor = self._db.cursor()
        except Exception as e:
            print(e)

    def get_database(self):
        return self._db

    def get_cursor(self):
        return self._db_cursor