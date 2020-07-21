from socket import *
import json
import struct
import threading
# 多线程处理
class RequestHandleThread(threading.Thread):
    def __init__(self, conn, client_addr):
        super().__init__()
        self.conn = conn
        self.client_addr = client_addr

    def anlys_header(self):
        recv_data = self.conn.recv(4)
        if len(recv_data) == 0:
            raise Exception('客户端异常退出')
        header_size = struct.unpack('i', recv_data)[0]
        recv_header = self.conn.recv(header_size)
        header_json = recv_header.decode('utf-8')
        header = json.loads(header_json)

        return header

    def run(self):
        while True:
            try:
                # 和客户端交互
                header_dict = self.anlys_header()
                print(header_dict)
                file_name = header_dict['file_name']
                total_size = header_dict['total_size']
                recv_size = 0

                with open('{}.back'.format(file_name), mode = 'wb') as f:
                    while recv_size < total_size:
                        data = self.conn.recv(1024)
                        recv_size += len(data)
                        f.write(data)
                    print('文件{}保存成功，文件大小为:{}'.format('{}.back'.format(file_name), total_size))
            except Exception as e:
                print('客户端{}断开链接,异常信息：{}'.format(self.client_addr, e))
                break
        self.conn.close()


server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1',3378))
server.listen(5)

while True:
    conn, client_addr = server.accept()
    thr = RequestHandleThread(conn, client_addr)
    thr.start()
