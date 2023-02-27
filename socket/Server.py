import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # 创建socket对象
s.bind(('127.0.0.1',4323))                                      # 绑定地址
s.listen(5)                                                     # 建立5个监听
while True:
    conn,addr= s.accept()                                       # 等待客户端连接
    print('欢迎{}'.format(addr))                              #打印访问的用户信息
    while True:
        data=conn.recv(1024)
        dt=data.decode('utf-8')                                 #接收一个1024字节的数据
        print('收到：',dt)
        aa=input('服务器发出：')
        if aa=='quit':
            conn.close()                                        #关闭来自客户端的连接
            s.close()                                           #关闭服务器端连接
        else:
            conn.send(aa.encode('utf-8'))

            '''
            分别用2个Pycharm去跑代码 
            Pycharm CE跑服务端
            Pycharm跑客户端
            
            
            '''