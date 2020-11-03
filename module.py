import logging

logger = logging.getLogger(__name__)

def do_stuff(*paths):
    logger.info(paths)

    raise NotImplementedError("Do Stuff")
