from services.servicesUtil import externalAuthentication
from config import SyncConfig
from services.quargoService import QuargoService

class MasterDataSource():
    _quargoService: QuargoService

    def __init__(self):
        config = SyncConfig()
        self._quargoService = QuargoService(
            auth=externalAuthentication,
            config=config
        )

    def getAllResources(self, cursor = None):
        return self._quargoService.getAllResources(cursor=cursor)

    def endpoint(self, id, startTime, endTime):
        return f'resources/resource/{id}/unavailability'

    def getSpecificResource(self, resourceId, cursor = None):
        return self._quargoService.getSpecificUnavailableResource(
            resourceId=resourceId,
            cursor=cursor
        )
