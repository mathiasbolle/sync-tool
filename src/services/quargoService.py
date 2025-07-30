from config import SyncConfig
from services.external.externalDataSource import ExternalDataSource
from services.servicesUtil import AuthenticationManager
from services.target.targetDataSource import TargetDataSource
import logging
import requests
from services.dto.resource import UnavailableResourceDto

class QuargoService(TargetDataSource, ExternalDataSource):
    """
    Responsible for the requests of the Quargo service (this is both the target and the master)
    """
    _authenticationManager: AuthenticationManager
    _config: SyncConfig

    def __init__(self, auth: AuthenticationManager, config: SyncConfig):
        self._authenticationManager = auth
        self._config = config
        self._authenticationManager.requestAccess()

    def createUnavailableResource(self, unavailableResourceDto: UnavailableResourceDto):
        logging.info("test")
        bearerToken = self._authenticationManager.get_token() # request access token
        endpoint = 'resources/resource'
        logging.error(f"{unavailableResourceDto.__str__()}")
        logging.error(f"{unavailableResourceDto.resourceId}")
        url = f"{self._config.baseUrl}/{endpoint}/{unavailableResourceDto.resourceId}/unavailability"
        headers = {"Authorization": f"Bearer {bearerToken}"}

        data = unavailableResourceDto.convert_dict()
        logging.info(f"Data for the POST request {data}")

        requests.post(url=url, headers=headers, data=data)

    def getAllResources(self,cursor = None):
        bearerToken = self._authenticationManager.get_token() # request access token
        endpoint = 'resources/resource'
        url = f"{self._config.baseUrl}/{endpoint}" + ("" if cursor is None else f"?cursor={cursor}")
        headers = {"Authorization": f"Bearer {bearerToken}"}
        logging.info(url)

        resourcesResponse = requests.get(url, headers=headers)

        if resourcesResponse.status_code != 200:
            logging.error(f"failed to make a request to URL {url} - HTTP status code {str(resourcesResponse.status_code)}")

            match resourcesResponse.status_code:
                case 401:
                    logging.error(f"cause: {resourcesResponse.json()["message"]}")
                case _:
                    pass
            exit()
        else:
            return resourcesResponse.json()

    def getSpecificUnavailableResource(self, resourceId: int, cursor = None):
        bearerToken = self._authenticationManager.get_token() # request access token
        url = f"{self._config.baseUrl}/{str(self.__endpoint(resourceId, '', ''))}"
        headers = {"Authorization": f"Bearer {bearerToken}"}
        unavailableResourcesResponse = requests.get(url, headers=headers)

        if cursor is None:
            url = f"{self._config.baseUrl}/{str(self.__endpoint(resourceId, '', ''))}"
        else:
            url = f"{self._config.baseUrl}/{str(self.__endpoint(resourceId, '', ''))}?cursor={cursor}"

        if unavailableResourcesResponse.status_code != 200:
            logging.error(url) # this is the problem!
            logging.error("test") # this is the problem!
            logging.error(f"failed to make a request to URL {url} - HTTP status code {str(unavailableResourcesResponse.status_code)}")

            match unavailableResourcesResponse.status_code:
                case 401:
                    logging.error(f"cause: {unavailableResourcesResponse.json()["message"]}")
                case _:
                    pass
            exit()
        else:
            return unavailableResourcesResponse.json()

    def __endpoint(self, id, startTime, endTime):
        return f'resources/resource/{id}/unavailability'


    def updateSpecificUnavailableResource(self, resourceId: str,
        unavailableResourceDto: UnavailableResourceDto, cursor = None):
            bearerToken = self._authenticationManager.get_token() # request access token
            url = f"{self._config.baseUrl}/{str(self.__endpoint(resourceId, '', ''))}" + f"/{unavailableResourceDto.externalId}"
            headers = {"Authorization": f"Bearer {bearerToken}"}
            updatedUnavailableResource = requests.put(url, headers=headers)

            if updatedUnavailableResource.status_code != 200:
                logging.error(url) # this is the problem!
                logging.error("test") # this is the problem!
                logging.error(f"failed to make a request to URL {url} - HTTP status code {str(updatedUnavailableResource.status_code)}")

                match updatedUnavailableResource.status_code:
                    case 401:
                        logging.error(f"cause: {updatedUnavailableResource.json()["message"]}")
                    case _:
                        pass
                exit()
            else:
                return updatedUnavailableResource.json()

    def __hasAccess(self):
        if self._authenticationManager.isExpired():
            logging.error("authentication failed.")
            logging.info("request access")
            self._authenticationManager.requestAccess()
