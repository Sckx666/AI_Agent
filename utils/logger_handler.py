"""
运行日志
"""
import os
import logging
from utils.path_tool import get_abs_path
from datetime import datetime

# 日志保存的根目录
Log_Root = get_abs_path("logs")

# 确保日志的目录存在
os.makedirs(Log_Root, exist_ok=True)

# 日志的格式配置
Default_Log_Format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s -%(filename)s:%(lineno)d - %(message)s'
)


def get_logger(
        name: str = "agent",
        console_level: int = logging.INFO,
        file_level: int = logging.DEBUG,
        log_file = None,
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 避免添加重复的Handler
    if logger.handlers:
        return logger

    # 控制台Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(Default_Log_Format)

    # 添加到Handler中
    logger.addHandler(console_handler)

    # 文件Handler
    if not log_file:
        # 文件存放目录
        log_file = os.path.join(Log_Root, f"{name}_{datetime.now().strftime('%Y-%m-%d')}.log")

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(file_level)
    file_handler.setFormatter(Default_Log_Format)

    # 添加到Handler中
    logger.addHandler(file_handler)

    return logger


# 快捷获取日志管理器
logger = get_logger()

if __name__ == '__main__':
    logger.info("信息日志")
    logger.error("错误日志")
    logger.warning("警告日志")
    logger.debug("调试日志")
