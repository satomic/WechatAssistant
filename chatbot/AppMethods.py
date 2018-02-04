# coding=utf-8
from Environment import environment
import os


def get_pkls_path(nickname, work_dir):
    '''
    :param nickname: 输入的昵称
        在work_dir中创建pkls文件夹
        并在其中创建nickname文件夹
    :return: 
    '''
    pkls_dir = os.path.join(work_dir, "pkls")

    # 如果没有pkls文件夹，则创建
    if not os.path.exists(pkls_dir):
        os.makedirs(pkls_dir)

    # 创建存储当前用户的pkls的文件夹
    nickname_dir = os.path.join(pkls_dir, nickname)
    if not os.path.exists(nickname_dir):
        os.makedirs(nickname_dir)
    login_pkl = os.path.join(nickname_dir, "wxpy.pkl")
    puid_pkl = os.path.join(nickname_dir, "wxpy_puid.pkl")
    return login_pkl, puid_pkl
