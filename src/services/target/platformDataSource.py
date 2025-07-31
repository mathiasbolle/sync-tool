from config import SyncConfig
from services.dto.resource import UnavailableResourceDto
from services.quargoService import QuargoService
from services.target.targetDataSource import TargetDataSource
from services.servicesUtil import targetAuthentication


class PlatformDataSource(TargetDataSource):
    _quargoService: QuargoService

    def __init__(self):
        config = SyncConfig()
        self._quargoService = QuargoService(
            auth=targetAuthentication,
            config= config
        )

    def getSpecificUnavailableResource(self, resourceId):
        return self._quargoService.getSpecificUnavailableResource(resourceId)

    def createUnavailableResource(self, unavailableResourceDto: UnavailableResourceDto):
        return self._quargoService.createUnavailableResource(unavailableResourceDto=unavailableResourceDto)

    def updateSpecificUnavailableResource(self, resourceId: str,
        unavailableResourceDto: UnavailableResourceDto):
            return self._quargoService.updateSpecificUnavailableResource(
                resourceId,
                unavailableResourceDto
            )
