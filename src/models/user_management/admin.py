class Admin:

    def __init__(self, admin_id='', identifier='', password=''):
        self._admin_id = admin_id
        self._identifier = identifier
        self._password = password

    def set_admin_id(self, admin_id):
        self._admin_id = admin_id

    def set_identifier(self, identifier):
        self._identifier = identifier

    def set_password(self, password):
        self._password = password

    def get_admin_id(self):
        return self._admin_id

    def get_identifier(self):
        return self._identifier

    def get_password(self):
        return self._password
