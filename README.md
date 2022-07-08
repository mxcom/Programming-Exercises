# Programming Exercises

### Execution

To use the class `Database`, the ssh and database logins are required. Run the following commands replacing `ssh_username`, `ssh_password`, `db_username`, `db_password` with the appropriate information

```
$ python
>>> import keyring
>>> keyring.set_password(service_name="ssh_login", username="ssh_username", password="ssh_password")
>>> keyring.set_password(service_name="db_login", username="db_username", password="db_password")
>>> keyring.set_password(service_name="email_login", username="email_username", password="email_password")
```
