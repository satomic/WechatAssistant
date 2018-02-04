# coding=utf-8
import logging
import sys,os,time,socket,getpass
from common.log.MyLogger import MyLogger
import traceback


mylogger = MyLogger()

old_logging_info = logging.info
old_logging_warn = logging.warn
old_logging_error = logging.error
old_logging_debug = logging.debug

def my_info(msg,*args,**kwargs):
    mylogger.logger.info(addModule(msg),*args,**kwargs)

def my_warn(msg,*args,**kwargs):
    mylogger.logger.warn(addModule(msg),*args,**kwargs)

def my_error(msg,*args,**kwargs):
    mylogger.logger.error(addModule(msg),*args,**kwargs)
    type,value,tb = sys.exc_info()
    traceback.print_tb(tb)

def my_debug(msg,*args,**kwargs):
    mylogger.logger.debug(addModule(msg),*args,**kwargs)

logging.info = my_info
logging.warn = my_warn
logging.error = my_error
logging.debug = my_debug

# copy from logging
# next bit filched from 1.5.2's inspect.py
def currentframe():
    # return the frame object for the caller's stack frame
    try:
        raise Exception
    except:
        return sys.exc_info()[2].tb_frame.f_back

if hasattr(sys,'_getframe'):
    currentframe = lambda:sys._getframe(3)
# done filching

# _srcfile is used when walking the stack to check when we've got the first caller stack frame
_srcfile = os.path.normcase(currentframe.__code__.co_filename)
# print '_srcfile:',_srcfile

def addModule(msg):
    filename,line_number,function_name = findCaller()
    data_str = "[%s(%s) -> %s]" % (os.path.basename(filename),line_number,function_name)
    return data_str + str(msg)

def findCaller():
    '''
    find the stack frame of the caller so that we can note the source file name,line number and function name
    :return: 
    '''
    f = currentframe()
    # on some versions of IronPython, currentframe() returns None if IronPython isn't run with X:Frames
    rv = "(unknow file)",0,"(unknow function)"
    while hasattr(f,'f_code'):
        co = f.f_code
        filename = os.path.normcase(co.co_filename)
        if filename == _srcfile:
            f = f.f_back
            continue
        rv = (co.co_filename,f.f_lineno,co.co_name)
        break
    return rv