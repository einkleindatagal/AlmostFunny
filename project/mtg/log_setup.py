import logging

import structlog


def configure_logging(log_level=logging.DEBUG):
    logger = logging.getLogger()
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler()

    logger.addHandler(console_handler)

    processors = [
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(
            fmt="%Y-%m-%dT%H:%M:%S", utc=False, key="timestamp"
        ),
        structlog.dev.ConsoleRenderer(pad_level=False),
    ]
    structlog.configure(processors=processors, cache_logger_on_first_use=True)


configure_logging()
log = structlog.get_logger()
