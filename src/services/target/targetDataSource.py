from abc import ABC, abstractmethod
from services.dto.resource import UnavailableResourceDto

class TargetDataSource(ABC):

    @abstractmethod
    def createUnavailableResource(self, unavailableResourceDto: UnavailableResourceDto):
        pass

    @abstractmethod
    def getSpecificUnavailableResource(self, resourceId):
        pass

    @abstractmethod
    def updateSpecificUnavailableResource(self, resourceId: str,
        unavailableResourceDto: UnavailableResourceDto):
            pass
