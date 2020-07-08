# 程序入口

# 解释器环境变量导入
import sys
import os

from core import src
pro_path = print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pro_path)


if __name__ == '__main__':
    src.run()
