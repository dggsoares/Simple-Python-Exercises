import logging
import coloredlogs
import sys

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG',
                    logger=logger,
                    fmt='%(asctime)s %(hostname)s %(name)s[%(process)d] %(levelname)s %(message)s',
                    datefmt='%d-%m-%y %H:%M:%S',
                    stream=sys.stdout
                    )
