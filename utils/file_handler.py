"""
获取文件的md5值,保证同样的消息不会重复存入数据库
"""
import hashlib
import os
from utils.logger_handler import logger
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader


def get_file_md5_hex(filepath: str):     # 获取文件的md5的十六进制字符串

    if not os.path.exists(filepath):
        logger.error(f"[get_file_md5_hex]文件{filepath}不存在")
        return

    if not os.path.isfile(filepath):
        logger.error(f"[get_file_md5_hex]路径{filepath}不是文件")
        return

    hash_md5 = hashlib.md5()

    chunk_size = 4096       # 4KB分片，避免爆内存

    try:
        with open(filepath, "rb") as f:     # 必须二进制数
            while chunk := f.read(chunk_size):
                hash_md5.update(chunk)      # 将片段内容存入hash

        md5_hex = hash_md5.hexdigest()      # 获得完整的md5十六进制数
        return md5_hex

    except Exception as e:
        logger.error(f"[get_file_md5_hex]计算文件{filepath}md5失败,{str(e)}")
        return None


def listdir_with_allowed_type(path: str, allowed_types: tuple[str]):        # 返回文件夹的文件列表(允许的文件后缀)
    files = []

    if not os.path.isdir(path):
        logger.error(f"[listdir_with_allowed_type]{path}不是文件夹")
        return allowed_types

    for f in os.listdir(path):
        if f.endswith(allowed_types):       # 允许的文件类型才能被处理
            files.append(os.path.join(path, f))

    return tuple(files)


def pdf_loader(file_path: str, passwd=None) -> list[Document]:       # 加载pdf的文档
    return PyPDFLoader(file_path, passwd).load()


def txt_loader(file_path) -> list[Document]:       # 加载txt的文档
    return TextLoader(file_path, encoding="utf-8").load()


