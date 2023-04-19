import pyvisa as visa
import matplotlib.pyplot as plt
import matplotlib
import time
matplotlib.rc("font", family='YouYuan')

rm = visa.ResourceManager()
res = rm.list_resources()
print(res)
mydev = rm.open_resource(res[0])
print(mydev.query('*IDN?'))

print(mydev.query(":MEAS:ALL? CH1"))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

curr = []
i = []
n = 0
plt.figure(figsize=(10, 5))
plt.grid(linestyle='-.')
plt.title('电压显示')
plt.xlabel('点数')
plt.ylabel('电压-V')
while 1:
    n = n+1
    cur_val = float(mydev.query(":MEAS:ALL? CH1").split(',')[0])
    curr.append(cur_val)
    i.append(n)
    plt.clf()  # 清除之前画的图
    plt.grid(linestyle='-.')
    plt.title('电压显示')
    plt.xlabel('点数') 
    plt.ylabel('电压-V')
    plt.plot(i,curr)
    plt.pause(0.5)