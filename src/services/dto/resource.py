from dataclasses import dataclass

@dataclass
class ResourceItemDto:
    id: str

@dataclass
class ResourceDto:
    items: list[ResourceItemDto]

@dataclass(unsafe_hash=True)
class UnavailableResourceDto:
    resourceId: str
    externalId: str
    startTime: str
    endTime: str
    reason: str
    descripton: str

    def __post_init__(self):
        if self.startTime is None:
            self.startTime = ''
        if self.endTime is None:
            self.endTime = ''

    def convert_dict(self):
        data = {
            "external_id": self.externalId,
            "start_time": self.startTime,
            "end_time": self.endTime,
            "reason": self.reason,
            "description": self.descripton
        }
        return data

    def __str__(self):
        return f"{self.resourceId} - {self.reason}"
