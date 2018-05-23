# -*- coding:utf-8 -*-

"""
description:
    customize several logger to use at different situation

functions:
    alpha

"""
# compatible with logging
try:
    import colorlog as logging
except:
    import logging

__all__ = ['__version__', 'alpha']

__version__ = '0.0.0.1'

def alpha():
    """
    description:
        logger to console

    Returns:
        A logger which prints on terminal window with out time info
    """
    try:
        formatter = logging.ColoredFormatter\
            ('%(log_color)s[%(levelname)s]: %(message)s')
    except:
        formatter = logging.Formatter('[%(levelname)s]: %(message)s')

    handler2con = logging.StreamHandler()
    handler2con.setFormatter(formatter)
    handler2con.setLevel('DEBUG')

    logger = logging.getLogger('alpha')
    logger.addHandler(handler2con)
    logger.setLevel('DEBUG')

    return logger


def main():
    logger = alpha()

    logger.error('test %d',5)
    logger.info('test')
    logger.debug('test')
    logger.warning('test')


if __name__ == '__main__':
    main()
