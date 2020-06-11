import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
logging.info('A new request arrived')
try:
    x=int(input('enter some number'))
    y=int(input('enter second number'))
    print(x/y)

except ZeroDivisionError as msg:
    print('cant divide a number by 0')
    logging.exception(msg)
except ValueError as msg:
    print('cant divide by other than int/float datatypes')
    logging.exception(msg)
logging.info("request executded successfully")
