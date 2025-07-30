from typing import Optional
import requests
from datetime import datetime, timedelta
import logging

from config import SyncConfig

class AuthenticationManager:
    _client: Optional[str] = None
    _secret: Optional[str] = None
    _expiresDate: Optional[datetime] = None
    _token: Optional[str] = None

    def __init__(self, client, secret):
        self._client = client
        self._secret = secret

    def __set_expires_date(self, timeInMinutes):
        currentTime = datetime.now()
        self._expiresDate = (currentTime + timedelta(minutes=timeInMinutes))

    def get_token(self) -> Optional[str]:
        return self._token

    def requestAccess(self):
        if self._token != None and not self.isExpired():
            return self._token
        else:
            url = 'https://api.qargo.com/v1/auth/token'
            headers = {'Content-type': 'application/json'}
            auth = (str(self._client), str(self._secret))

            request = requests.post(url, headers, auth=auth)
            logging.info(f"Requesting access with client {self._client}")
            accessToken, expiresIn = request.json()['access_token'], request.json()['expires_in']

            self._token = accessToken
            self.__set_expires_date(expiresIn)
            return accessToken

    def isExpired(self):
        if self._expiresDate is not None:
            return self._expiresDate >= datetime.now()


_config = SyncConfig()
externalAuthentication = AuthenticationManager(
    client = _config.masterClient,
    secret = _config.masterSecret
)

# problem?
targetAuthentication = AuthenticationManager(
    client = _config.targetClient,
    secret = _config.targetSecret
)
