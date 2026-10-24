import logging

logger = logging.getLogger(__name__)

class NetworkDevice:
    def __init__(self, hostname, ip, type):
        self.hostname = hostname
        self.ip = ip
        self.type = type

    def summarize(self) -> str:
        summary_msg = f"[DEVICE_SUMMARY]: {self.hostname} ({self.type}) - {self.ip}"

        logger.info(summary_msg)

        print(summary_msg)

        return summary_msg