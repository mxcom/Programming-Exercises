import bcrypt

def hash_passwd(passwd):
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes(passwd, 'utf-8'), salt)

    return hash
