from abc import ABC, abstractmethod

class ExternalDataSource(ABC):

    @abstractmethod
    def getAllResources(self,cursor = None):
        pass
