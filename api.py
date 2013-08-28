import requests
import json
from base64 import b64encode

## https://github.com/bensnyde/py-cpanel-api/blob/master/cpanel.py
## Referencia

class cPanel(object):
    def __init__(self, url, username, password):
        self.url = url
        self.auth = {"Authorization":
                     "Basic " + b64encode(username + ":" + password)}
        self.account = Account(self.url, self.auth)

class cPanelObjects(object):
    def __init__(self, url, auth):
        self.url = url
        self.auth = auth

    def query(self, queryString):
        response = requests.get(self.url + 'json-api/'+ queryString, headers=self.auth)
        return json.loads(response.text)

class Queue(cPanelObjects):
    def __init__(self, url, auth, username=None):
        super(Queue, self).__init__(url, auth)
        raise NotImplemented('Falta implementar')


class Backup(cPanelObjects):
    def __init__(self, url, auth, username=None):
        super(Backup, self).__init__(url, auth)
        raise NotImplemented('Falta implementar')


class Account(cPanelObjects):
    def __init__(self, url, auth, username=None):
        super(Account, self).__init__(url, auth)
        self.username = username

    def list(self):
        return self.query('listaccts')

    def listSuspended(self):
        return self.query('listsuspended')

    def modify(self, username):
        return self.query('modifyacct?user='+username)

    def create(self, username, domain):
        return self.query('createacct?username='+username+'&domain='+domain)

    def changePassword(self, username, password, update_db_password=True):
        return self.query('passwd?user='+username+'&pass='+password+'&db_pass_update='+str(int(update_db_password)))

    def getSummary(self, username):
        return self.query('accountsummary?user='+username)

    def suspend(self, username, reason=''):
        return self.query('suspendacct?user='+username+'&reason='+reason)

    def remove(self, username, keep_dns=False):
        return self.query('removeacct?user='+username+'&keep_dns='+str(int(keep_dns)))

    def changeDiskQuota(self, username, quota):
        return self.query('editquota?user='+username+'&quota='+str(quota))

    def limitBandwidth(self, username, bwlimit):
        return self.query('limitbw?user='+username+'&bwlimit='+bwlimit)

    def unsuspend(self, username):
        return self.query('unsuspendacct?user='+username)


if __name__ == '__main__':
    c = cPanel()
    #print c.account.create('prueba', 'prueba.com.ar')
    #print c.account.changeDiskQuota('prueba', 100)
