from mpython import *
from tinywebio import appserver, appclient

MYSSID = ''  # 请在''中输入你的WiFi热点名称
MYPWD = ''  # 请在''中输入你的WiFi热点密码

mywifi = wifi()
mywifi.connectWiFi(MYSSID, MYPWD)

oled.fill(0)
oled.DispChar('联网成功, IP为: ', 0, 0)
oled.DispChar(str(mywifi.sta.ifconfig()[0]), 0, 16)
oled.show()

appserver.start()

# 可根据实际情况和自身需要修改以下设定，其中：
# 1）第一项参数为TinyWebDB服务器地址
# 2）第二项参数为向服务器发布的数据项(逗号分隔)
# 3）第三项参数为从服务器读取的数据项(逗号分隔)
# 4）第四项参数为存取服务器的时间间隔
appclient.setup(
    'tinywebdb.17coding.net',
    'light,sound,accelerometer',
    'rgb0,rgb1,rgb2,display,buzz,music',
    1000)
# 可利用本地服务接口手动启停
# appclient.start()