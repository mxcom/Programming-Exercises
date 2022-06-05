import bcrypt


def hash_passwd(passwd):
    salt = bcrypt.gensalt()
    hashed: bytes = bcrypt.hashpw(bytes(passwd, 'utf-8'), salt)

    return hashed


def compare_passwd(passwd, hash):
    if bcrypt.checkpw(bytes(passwd, 'utf-8'), bytes(hash, 'utf-8')):
        return True
    else:
        return False
