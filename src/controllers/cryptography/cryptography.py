import bcrypt


def hash_passwd(passwd):
    salt = bcrypt.gensalt()
    hashed: bytes = bcrypt.hashpw(bytes(passwd, 'utf-8'), salt)

    return hashed
