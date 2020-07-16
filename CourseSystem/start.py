import os
import sys
# python解释器环境变量的添加
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core import src
if __name__ == '__main__':
    # 程序入口
    src.run()
