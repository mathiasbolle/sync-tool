from services.dto.resource import UnavailableResourceDto
from services.target.platformDataSource import PlatformDataSource

class ExternalDataRepository():
    def getUnavailalbeResourceItem(self, resourceId: str) -> list[UnavailableResourceDto]:
        return PlatformDataSource().getSpecificUnavailableResource(
            resourceId=resourceId
        )

    def createUnavailableResourceItem(self, unavailableResourceDto: UnavailableResourceDto):
        PlatformDataSource().createUnavailableResource(
            unavailableResourceDto=unavailableResourceDto
        )

    def updateUnavailableResourceItem(self, resourceId,
        unavailableResourceDto: UnavailableResourceDto):
        PlatformDataSource().updateSpecificUnavailableResource
        pass
