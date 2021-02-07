import socket
import tkinter as tk
from tkinter import ttk
import time
import threading

massage = '连接成功'
resistance = ''  # 阻值

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('准备连接服务器')
sk.connect(('127.0.0.1', 502))
print('连接成功')
"""*******************客机窗口******************************"""
win = tk.Tk()  # 创建窗口
win.title("钟大炮的客机")
win.geometry("500x300")
"""****************监听状态标签**************************"""
txt = tk.StringVar()
txt.set("准备连接......")
l1 = tk.Label(win, textvariable=txt)
l1.pack()
"""****************报文设置区**************************"""
# 传输标识符设置区
l3 = tk.Label(win, text="报文设置区:")
l3.place(x=10, y=20)
# 1
l6 = tk.Label(win, text="传输标识符:")
l6.place(x=45, y=45)
t1 = tk.Text(win, width=4, height=1, bg="white")
t1.place(x=10, y=70)
t1.insert("insert", "127")
l4 = tk.Label(win, text="—")
l4.place(x=40, y=66)
# 2
t2 = tk.Text(win, width=4, height=1, bg="white")
t2.place(x=60, y=70)
t2.insert("insert", "0")
l5 = tk.Label(win, text="—")
l5.place(x=90, y=66)
# 3
t3 = tk.Text(win, width=4, height=1, bg="white")
t3.place(x=110, y=70)
t3.insert("insert", "0")
l5 = tk.Label(win, text="—")
l5.place(x=140, y=66)
# 4
t4 = tk.Text(win, width=4, height=1, bg="white")
t4.place(x=160, y=70)
t4.insert("insert", "1")

# 数据长度设置区
l_len = tk.Label(win, text="数据长度:")
l_len.place(x=220, y=45)
t_len1 = tk.Text(win, width=4, height=1, bg="white")
t_len1.place(x=293, y=47)
t_len1.insert("insert", '00')
l_len1 = tk.Label(win, text="—")
l_len1.place(x=323, y=43)
t_len2 = tk.Text(win, width=4, height=1, bg="white")
t_len2.place(x=343, y=47)
t_len2.insert("insert", '06')

# 单元标识符设置区
l_dan = tk.Label(win, text="单元标识符:")
l_dan.place(x=220, y=70)
t_dan = tk.Text(win, width=4, height=1, bg="white")
t_dan.place(x=293, y=72)
t_dan.insert("insert", "502")

# 功能选择区
l_cmb = tk.Label(win, text="功能选择:")
l_cmb.place(x=220, y=95)
cmb = ttk.Combobox(win)  # 下拉框
cmb.place(x=293, y=97)
cmb['value'] = ('01读线圈状态', '02读电阻值', '03写电阻值', '04写灯泡')
cmb.current(0)  # 默认第一

# 寄存器地址
l_j = tk.Label(win, text="电阻阻值:")
l_j.place(x=220, y=122)
t_j = tk.Text(win, width=4, height=1, bg="white")
t_j.place(x=293, y=126)
t_j.insert('insert', "00")
l_j1 = tk.Label(win, text="—")
l_j1.place(x=323, y=123)
t_j2 = tk.Text(win, width=4, height=1, bg="white")
t_j2.place(x=343, y=126)
t_j2.insert('insert', "00")

# 寄存器个数
l_j_num = tk.Label(win, text="灯泡亮灭:")
l_j_num.place(x=220, y=151)
t_j_num = tk.Text(win, width=4, height=1, bg="white")
t_j_num.place(x=293, y=155)
t_j_num.insert("insert", "00")
l_j_num1 = tk.Label(win, text="—")
l_j_num1.place(x=323, y=152)
t_j_num2 = tk.Text(win, width=4, height=1, bg="white")
t_j_num2.place(x=343, y=155)
t_j_num2.insert("insert", "00")


# 发送按钮
def dealin():
    global massage
    # 传输标识符
    data1 = (t1.get('0.0', 'end').replace("\n", ""))
    data2 = (t2.get('0.0', 'end').replace("\n", ""))
    data3 = (t3.get('0.0', 'end').replace("\n", ""))
    data4 = (t4.get('0.0', 'end').replace("\n", ""))
    # 数据长度
    data5 = (t_len1.get('0.0', 'end').replace("\n", ""))
    data6 = (t_len2.get('0.0', 'end').replace("\n", ""))
    # 单元标识符
    data7 = (t_dan.get('0.0', 'end').replace("\n", ""))
    # 功能选择
    data8 = cmb.get()[0:2]
    # 电阻值
    data9 = (t_j.get('0.0', 'end').replace("\n", ""))
    data10 = (t_j2.get('0.0', 'end').replace("\n", ""))
    # 灯泡个数
    data11 = (t_j_num.get('0.0', 'end').replace("\n", ""))
    data12 = (t_j_num2.get('0.0', 'end').replace("\n", ""))
    data_all = ''
    # data = data_all.join(data8).join(data7).join(data6).join(data5).join(data4).join(data3).join(data2).join(data1)
    # data = data_all.join(data7).join(data6).join(data5).join(data4).join(data3).join(data2).join(data1) + data8
    data = str(data1)+str(data2)+str(data3)+str(data4)+str(data5)+str(data6)+str(data7)+data8+data9+data10+data11+data12
    t0.insert("end", "发送报文:" + data, tk.INSERT, '\n')
    massage = data
    print("massage:", data)
    dealout()  # 发送数据


def conncet_sever():
    print("连接按钮")


send = tk.Button(win, text="发送", command=dealin, width=10, height=1)
send.place(x=400, y=250)
"""****************接受数据区***********************************"""
# 标签区
l2 = tk.Label(win, text="客机数据接收区:")
l2.place(x=10, y=180)
# 文本区
t0 = tk.Text(win, width=45, height=6, bg="white", wrap='word')
t0.place(x=10, y=210)
"""****************链接按钮*****************"""
# b = tk.Button(win, text="链接", command=conncet_sever, width=10, height=1)
# b.place(x=400, y=250)  # 放置按钮，place可以设置位置


def rev():
    while 1:
        data = sk.recv(1024)  # 监听返回数据
        recv_data = "返回数据" + data.decode('utf-8')
        if data.decode('utf-8') == '开':
            t0.insert("insert", "返回报文:12700100065020100000000", tk.INSERT, '\n')
            t0.insert("insert", "开关状态为:开", tk.INSERT, '\n')
        elif data.decode('utf-8') == '关':
            t0.insert("insert", "返回报文：12700100065020000000000", tk.INSERT, '\n')
            t0.insert("insert", "开关状态为:关", tk.INSERT, '\n')
        elif recv_data[0:4] == '返回数据':
            # t0.insert("insert", "返回报文:127001000650202", tk.INSERT, '\n')
            resistance = int(data.decode('utf-8') or 0)
            resistance = '{:04b}'.format(resistance)  # 转换成四位二进制
            print(resistance)
            t0.insert("insert", "返回报文:127001000650202"+resistance+"0000", tk.INSERT, '\n')
            t0.insert("insert", "电阻值"+data.decode('utf-8'), tk.INSERT, '\n')
        print(recv_data[0:4])

def dealout():
    global massage, resistance
    sk.send(massage.encode())  # 发送数据


thin = threading.Thread(target=rev)  # 接受数据线程
thin.start()
thout = threading.Thread(target=dealout)  # 发送数据线程
thout.start()

win.mainloop()

sk.close()
