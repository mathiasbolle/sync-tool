from services.dto.resource import ResourceDto, ResourceItemDto, UnavailableResourceDto
from services.external.materDataSource import MasterDataSource

class MasterDataRepository():
    _resourceItems = []

    def getResourceItems(self) -> ResourceDto:
        resource = MasterDataSource().getAllResources()
        dtoResult=ResourceDto(items = [ResourceItemDto(resourceItem['id']) for resourceItem in resource['items']])
        cursor = resource['next_cursor']

        while (cursor != None):
            resource = MasterDataSource().getAllResources(cursor = cursor)
            dtoResult = ResourceDto(items = [ResourceItemDto(resourceItem['id']) for resourceItem in resource['items']])
            cursor = resource['next_cursor']

        self._resourceItems.append(dtoResult)
        return dtoResult

    def getUnavailalbeResourceItems(self) -> list[UnavailableResourceDto]:
        result = []

        for resourceId in self._resourceItems:
            for item in resourceId.items:
                json = MasterDataSource().getSpecificResource(item.id)

                cursor = json['next_cursor']

                if len(json['items']) != 0:
                    items = json['items'][0]
                    result.append(UnavailableResourceDto(
                        resourceId=str(items['id']),
                        externalId=str(items['external_id']),
                        startTime=str(items['start_time']),
                        endTime=str(items['start_time']),
                        reason=str(items['reason']),
                        descripton=str(items['description'])
                    ))

                    while cursor != None:
                        print("test")
                        print(cursor)

                        json = MasterDataSource().getSpecificResource(item.id, cursor)

                        cursor = json['next_cursor']

                        if len(json['items']) != 0:
                            items = json['items'][0]
                            result.append(UnavailableResourceDto(
                                resourceId=str(items['id']),
                                externalId=str(items['external_id']),
                                startTime=str(items['start_time']),
                                endTime=str(items['start_time']),
                                reason=str(items['reason']),
                                descripton=str(items['description'])
                            ))
        return result
