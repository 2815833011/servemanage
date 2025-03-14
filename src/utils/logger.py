from loguru import logger
import traceback
'''
        +----------------------+------------------------+------------------------+
        | Level name           | Severity value         | Logger method          |
        +======================+========================+========================+
        | ``TRACE``            | 5                      | |logger.trace|         |
        +----------------------+------------------------+------------------------+
        | ``DEBUG``            | 10                     | |logger.debug|         |
        +----------------------+------------------------+------------------------+
        | ``INFO``             | 20                     | |logger.info|          |
        +----------------------+------------------------+------------------------+
        | ``SUCCESS``          | 25                     | |logger.success|       |
        +----------------------+------------------------+------------------------+
        | ``WARNING``          | 30                     | |logger.warning|       |
        +----------------------+------------------------+------------------------+
        | ``ERROR``            | 40                     | |logger.error|         |
        +----------------------+------------------------+------------------------+
        | ``CRITICAL``         | 50                     | |logger.critical|      |
        +----------------------+------------------------+------------------------+
'''
# logger.info("输出信息")
# logger.error("报错")
# logger.warning("警告")
# logger.success("成功")
# logger.critical("严重报错")
# logger.add(r"log/debug.info")

class Logger:
    __instance=None
    __path=None
    def __new__(cls):  #单例模式让log对象只会生成一次 
        if not cls.__instance :
            cls.__path=r"log/test.log"
            cls.__instance=super().__new__(cls)

        return cls.__instance

    def __init__(self):
        self.__log =logger
        if self.__path:
            self.__log.add(self.__path)
    
    def info(self,msg):
        '''
        输出信息
        '''
        self.__log.info(msg)

    def error(self,msg):
        '''
        报错
        '''
        self.__log.error(msg)

    def warning(self,msg):
        '''
        警告
        '''
        self.__log.warning(msg)

    def success(self,msg):
        '''
        成功
        '''
        self.__log.success(msg)

    def critical(self,msg):
        '''
        严重报错
        '''
        self.__log.critical(msg)

log2=Logger()

def log(func):
    out_func=["get_screenshot_as_png"]
    def log_action(*args,**kwargs):
        msg=f"执行函数：{func.__name__}"
        if args:
            msg+=f"执行参数：{args[1::]}"
        if kwargs:
            msg+=f"关键字参数：{kwargs}"
        log2.info(msg)
        try:

            retval=None
            retval=func(*args,**kwargs)
        except :
            exemsg= traceback.format_exc()
            log2.info(f"执行出错{exemsg}")
            raise 
        if  func.__name__ not in out_func:
            log2.info(f"执行结果为：{retval}")
      
        return retval        
    return log_action