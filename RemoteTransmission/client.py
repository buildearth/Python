from socket import *
import os
import json
import struct

client = socket(AF_INET, SOCK_STREAM)

client.connect(('39.105.1.192', 8888))

while True:
    file_path = input('请输入上传文件的路径:').strip()
    if not os.path.exists(file_path):
        print('文件不存在，请重新输入！')
        continue

    # 1.构造数据头
    header_dict = {}.fromkeys(['file_name', 'total_size', 'md5'])
    # 1.1将文件名字和文件大小传入到header_dict
    header_dict['file_name'] = os.path.basename(file_path)
    header_dict['total_size'] = os.path.getsize(file_path)
    # 1.2数据头转换成Bytes类型
    header_json = json.dumps(header_dict)
    header_bytes = header_json.encode('utf-8')
    # 1.2获取文件头数据大小，发送到服务端
    header_size = struct.pack('i', len(header_bytes))
    client.send(header_size)
    # 1.3发送header数据
    client.send(header_bytes)

    # 2.发生真实数据
    with open(file_path, mode = 'rb') as f:
        for line in f:
            client.send(line)

    print('文件传输完成，文件名字：{}，文件大小：{}'.format(
        header_dict['file_name'], header_dict['total_size']))

client.close()
from socket import *
import os
import json
import struct

ip_addr = input('请输入ip:').strip()

client = socket(AF_INET, SOCK_STREAM)

client.connect((ip, 8888))

while True:
    file_path = input('请输入上传文件的路径:').strip()
    if not os.path.exists(file_path):
        print('文件不存在，请重新输入！')
        continue

    # 1.构造数据头
    header_dict = {}.fromkeys(['file_name', 'total_size', 'md5'])
    # 1.1将文件名字和文件大小传入到header_dict
    header_dict['file_name'] = os.path.basename(file_path)
    header_dict['total_size'] = os.path.getsize(file_path)
    # 1.2数据头转换成Bytes类型
    header_json = json.dumps(header_dict)
    header_bytes = header_json.encode('utf-8')
    # 1.2获取文件头数据大小，发送到服务端
    header_size = struct.pack('i', len(header_bytes))
    client.send(header_size)
    # 1.3发送header数据
    client.send(header_bytes)

    # 2.发生真实数据
    with open(file_path, mode = 'rb') as f:
        for line in f:
            client.send(line)

    print('文件传输完成，文件名字：{}，文件大小：{}'.format(
        header_dict['file_name'], header_dict['total_size']))

client.close()
