from config import SyncConfig
from services.external.masterDataRepository import MasterDataRepository
from services.target.targetDataRepository import ExternalDataRepository
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler
import asyncio
import logging

def sync_data():
    masterRepository = MasterDataRepository()
    masterRepository.getResourceItems()
    unavailableResources = masterRepository.getUnavailalbeResourceItems()

    externalRepository = ExternalDataRepository()

    for unavailableResource in unavailableResources:
        result = externalRepository.getUnavailalbeResourceItem(
            resourceId=unavailableResource.resourceId
        )

        if unavailableResource not in result:
            externalRepository.createUnavailableResourceItem(unavailableResource)
        else:
            externalRepository.updateUnavailableResourceItem(
                unavailableResource.resourceId,
                unavailableResource
            )


class SyncScheduler():
    _scheduler: BackgroundScheduler

    def __init__(self):
        self._scheduler = BackgroundScheduler()
        # Add a job to the scheduler
        trigger = CronTrigger.from_crontab(SyncConfig().cron)
        self._scheduler.add_job(sync_data, trigger)
        logging.info(f"Created a cron schedule with value {SyncConfig().cron}")

        # Start the scheduler
        self._scheduler.start()

    def run(self):
        try:
            asyncio.get_event_loop().run_forever()
        except KeyboardInterrupt:
            self._scheduler.shutdown()


def main():
    logging.info("📦Cargo integration tool has started!📦")
    scheduler = SyncScheduler()
    scheduler.run()

if __name__ == '__main__':
    main()
