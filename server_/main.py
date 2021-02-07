import socket
import ctypes
import inspect
import tkinter as tk
import sys
import threading
import time
from tkinter import *

massage = ''  # 报文
swith_stat = '关'  # 开关状态
resistance = ''  # 阻值
resis = 0  # 阻值滑块
ledcode = ''  # 灯泡亮灭个数
ledcode1 = '0'  # 上1
ledcode2 = '1'  # 上2
ledcode3 = '1'  # 上3
ledcode4 = '1'  # 上4

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(("127.0.0.1", 502))
sk.listen(128)
print('准备完毕----------')


"""***********************电阻滑块***********************************"""


def R_s(self):
    global resistance
    R_size = scale.get()
    resistance = R_size
    zu.set(R_size)


""""**********************开关*******************************"""


class i_helper:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.img = Label(self.master, width=50, height=31)
        src = PhotoImage(file='off.png')
        self.img.x = src
        self.img['image'] = src
        self.img.state = "on"
        self.img.bind('<Button-1>', self.switch_change)
        self.img.pack()

    def switch_change(self, event):
        global swith_stat  # 开关状态
        if self.img.state == "on":
            self.switch_off(event)
        else:
            self.switch_on(event)

    def switch_on(self, event):
        global swith_stat  # 开关状态
        src = PhotoImage(file='on.png')
        self.img.x = src
        self.img['image'] = src
        self.img.pack()
        self.img.state = "on"
        var.set("开")
        swith_stat = "开"

    def switch_off(self, event):
        global swith_stat  # 开关状态
        src = PhotoImage(file='off.png')
        self.img.x = src
        self.img['image'] = src
        self.img.pack()
        self.img.state = "off"
        var.set("关")
        swith_stat = "关"


"""*******************主机窗口******************************"""
win = tk.Tk()  # 创建窗口
win.title("钟大炮的主机")
win.geometry("500x300")
"""****************监听状态标签**************************"""
txt = tk.StringVar()
txt.set("请先启动......")
l1 = tk.Label(win, textvariable=txt)
l1.pack()
"""****************开关**************************"""
l2 = tk.Label(win, text="线圈状态切换:")
l2.place(x=10, y=50)
var = tk.StringVar()
var.set("关")
lstate = tk.Label(win, textvariable=var)
lstate.place(x=90, y=50)
farm = Frame(win)
farm.place(x=15, y=75)
i_helper(farm)
"""****************滑动变阻器**************************"""
l_R = tk.Label(win, text="电阻值:")
l_R.place(x=150, y=50)
zu = tk.StringVar()
zu.set("0")
l_r = tk.Label(win, textvariable=zu)
l_r.place(x=235, y=50)
scale = tk.Scale(win, from_=0, to=15, orient=tk.HORIZONTAL, command=R_s, showvalue='False', sliderrelief='ridge')
scale.set(resis)  # 设置电阻初始值为0
scale.place(x=150, y=80)
"""****************灯泡**************************"""
l_led = tk.Label(win, text="灯泡:")
l_led.place(x=290, y=50)
imageoff = PhotoImage(file="led_off.png")
imageon = PhotoImage(file="led_on.png")

"""****************接受数据区***********************************"""
# 标签区
l3 = tk.Label(win, text="主机数据接收区:")
l3.place(x=10, y=200)
# 文本区
t = tk.Text(win, width=45, height=4, bg="white")
t.place(x=10, y=230)
"""****************开始监听按钮*****************"""


def recv():
    global massage, swith_stat, resistance, resis, ledcode1, ledcode2, ledcode3, ledcode4
    conn, address = sk.accept()
    print('客户端连接成功')
    while 1:
        data = conn.recv(1024)  # 接受数据
        recv_data = data.decode()
        if recv_data != '连接成功':
            t.insert("insert", "收到报文:" + recv_data, tk.INSERT, '\n')
            recv_data_new = recv_data[14]
            if recv_data_new == "1":
                # massage = "读"
                # dealread_swith(swith_stat)  # 开关状态
                conn.send(swith_stat.encode())  # 发送数据
                t.insert("insert", "读开关状态", tk.INSERT, '\n')
            elif recv_data_new == "2":
                # resistance_rec(resistance)  # 电阻值
                resistance = str(resistance)
                conn.send(resistance.encode('utf-8'))  # 发送数据
                # t.insert("insert", "读电阻值请求，需要手动调节电阻值", tk.INSERT, '\n')
            elif recv_data_new == "3":  # 改变电阻值
                resistance = recv_data[15:19]
                print("电阻值", resistance)
                resistance = int(resistance, 2)
                print("十进制", resistance)
                t.insert("insert", "收到报文:" + recv_data, tk.INSERT, '\n')
                t.insert("insert", "写电阻值" + str(resistance), tk.INSERT, '\n')
                resis = resistance
                zu.set(resistance)
            elif recv_data_new == "4":
                lcd = recv_data[19:]
                ledcode1 = recv_data[19]
                ledcode2 = recv_data[20]
                ledcode3 = recv_data[21]
                ledcode4 = recv_data[22]
                print('灯泡', lcd)
                if ledcode1 == '1':
                    l_image1 = tk.Label(win, image=imageon)
                    l_image1.place(x=330, y=50)
                else:
                    l_image1 = tk.Label(win, image=imageoff)
                    l_image1.place(x=330, y=50)
                    # 2
                if ledcode2 == '1':
                    l_image2 = tk.Label(win, image=imageon)
                    l_image2.place(x=390, y=50)
                else:
                    l_image2 = tk.Label(win, image=imageoff)
                    l_image2.place(x=390, y=50)
                    # 3
                if ledcode3 == '1':
                    l_image3 = tk.Label(win, image=imageon)
                    l_image3.place(x=330, y=110)
                else:
                    l_image3 = tk.Label(win, image=imageoff)
                    l_image3.place(x=330, y=110)
                if ledcode4 == '1':
                    l_image4 = tk.Label(win, image=imageon)
                    l_image4.place(x=390, y=110)
                else:
                    l_image4 = tk.Label(win, image=imageoff)
                    l_image4.place(x=390, y=110)

"""
def lcd():
    global ledcode1, ledcode2, ledcode3, ledcode4
    if ledcode1 == '1':
        l_image1 = tk.Label(win, image=imageon)
        l_image1.place(x=330, y=50)
    else:
        l_image1 = tk.Label(win, image=imageoff)
        l_image1.place(x=330, y=50)

    # 2
    if ledcode2 == '1':
        l_image2 = tk.Label(win, image=imageon)
        l_image2.place(x=390, y=50)
    else:
        l_image2 = tk.Label(win, image=imageoff)
        l_image2.place(x=390, y=50)
    # 3
    if ledcode3 == '1':
        l_image3 = tk.Label(win, image=imageon)
        l_image3.place(x=330, y=110)
    else:
        l_image3 = tk.Label(win, image=imageoff)
        l_image3.place(x=330, y=110)
    if ledcode4 == '1':
        l_image4 = tk.Label(win, image=imageon)
        l_image4.place(x=390, y=110)
    else:
        l_image4 = tk.Label(win, image=imageoff)
        l_image4.place(x=390, y=110)
"""

# 返回开关状态
"""
def dealread_swith(swith_stat):
    global massage
    conn.send(swith_stat.encode())  # 发送数据


# 返回电阻值
def resistance_rec(resistance):
    print("电阻值", resistance)
    resistance = str(resistance)
    conn.send(resistance.encode('utf-8'))  # 发送数据
"""

thin = threading.Thread(target=recv)  # 监听线程
thin.start()
"""
thout = threading.Thread(target=dealread_swith(swith_stat))  # 发送开关状态数据线程
thout.start()
thr = threading.Thread(target=resistance_rec(resistance))  # 发送电阻值数据线程
thr.start()
"""

win.mainloop()

# conn.close()
sk.close()
