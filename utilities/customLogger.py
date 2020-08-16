# import logging
#
# def logGen():
#
#     logging.basicConfig(filename="./Logs//automation.log",
#                         format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#
#     logger = logging.getLogger()
#     logger.setLevel(logging.INFO)
#     return logger


import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="//Users//sumitshivhare//My_Workspace//SDET//nopCommerceApp//Logs//automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger