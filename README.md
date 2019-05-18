# TinyWebIO实验版

## 说明
为App Inventor应用提供远程控制接口的掌控板工具包。
TinyWebIO由roadlabs开发，原地址为：
https://gitee.com/roadlabs/TinyWebIO

## 安装
可通过以下任一方法进行安装。
1. 将项目中的`tinywebio.py`烧录到掌控板上
2. 在掌控板REPL界面中，使用upip安装，步骤如下：
    * 导入upip模块，执行`import upip`
    * 安装tinywebio，执行`upip.install('mpython-tinywebio')`

## 启动

1. 前提条件：掌控板已登录到本地WiFi网络或已启用AP模式
2. 导入tinywebio模块，执行`from tinywebio import appserver`
3. 启动服务，执行`appserver.start()`或`appserver.start_foreground()`，其中前者为以守护进程(Daemon)方式运行。默认服务端口为8888，如需改变端口运行，可以`appserver.start(<端口号>)`或`appserver.start_foreground(<端口号>)`方式执行。



**参考代码**

(建议文件名为main.py)

```python
from mpython import *
from tinywebio import appserver, appclient

MYSSID = ''  # 请在''中输入你的WiFi热点名称
MYPWD = ''  # 请在''中输入你的WiFi热点密码

mywifi=wifi()
mywifi.connectWiFi(MYSSID, MYPWD)

oled.fill(0)
oled.DispChar('联网成功,IP为：',0,0)
oled.DispChar(str(mywifi.sta.ifconfig()[0]),0,16)
oled.show()

appserver.start()
# 可根据实际情况和自身需要修改以下设定，其中：
# 第一项参数为TinyWebDB服务器地址
# 第二项参数为向服务器发布的数据项(逗号分隔)
# 第三项参数为从服务器读取的数据项(逗号分隔)
# 第四项参数为存取服务器的时间间隔
appclient.setup('tinywebdb.17coding.net', 'light,sound,accelerometer,time', 'rgb0,rgb1,rgb2,display,buzz,music', 1000)
# 可利用本地服务接口手动启停
# appclient.start()
```

## 测试

安装完成并重启掌控板后，可利用网络浏览器访问掌控板的IP地址及端口号，测试相关功能。

## 接口

采用App Inventor网络数据库(TinyWebDB)组件的接口协议存取和控制掌控板系统资源，其中，tag表示要访问的资源名称，value表示与控制功能相关的参数，具体类别如下：

| tag值         | 对应资源     | 功能                      | value值                                                      |
| ------------- | ------------ | ------------------------- | ------------------------------------------------------------ |
| buttona       | A键          | 读取状态                  | 无                                                           |
| buttonb       | B键          | 读取状态                  | 无                                                           |
| touchpadp     | 触摸按键P    | 读取数值                  | 无                                                           |
| touchpady     | 触摸按键Y    | 读取数值                  | 无                                                           |
| touchpadt     | 触摸按键T    | 读取数值                  | 无                                                           |
| touchpadh     | 触摸按键H    | 读取数值                  | 无                                                           |
| touchpado     | 触摸按键O    | 读取数值                  | 无                                                           |
| touchpadn     | 触摸按键N    | 读取数值                  | 无                                                           |
| light         | 光线传感器   | 读取数值                  | 无                                                           |
| sound         | 麦克风       | 读取数值                  | 无                                                           |
| accelerometer | 加速度传感器 | 读取三轴数值              | 无                                                           |
| id | 标识 | 读取掌控板标识 | 无 |
| time | 时间戳 | 读取事件戳 | 无 |
| rgb`<n>`      | RGB LED灯珠  | 点亮由灯珠n，n取值为0,1,2 | 逗点分隔红绿蓝颜色亮度值，如`255,0,0`                        |
| display或oled | OLED显示屏   | 显示文本或清空屏幕        | 显示文本为`show:<文本>,<x>,<y>`，清空屏幕为`fill:1`或`fill:0`，默认为在0,0处显示指定文本 |
| buzz          | 蜂鸣器       | 播放声音或停止            | 播放为`on`或`on:<频率值>`，停止为`off`，默认为播放指定频率   |
| music         | 音乐         | 播放乐谱或非音符音调      | 播放乐谱为内置或逗号分隔自编乐谱，音调为pitch:<频率>,<时长>  |
| servo`<n>`      | 舵机         | 设置舵机脉冲宽度或角度    | 角度值 |
| pind`<n>`     | 数字IO引脚   | 输入输出数据              | 输入不用设置数值，输出时需设置目标值                         |
| pina`<n>`     | 模拟IO引脚   | 输入输出数据              | 输入不同设置数值，输出时需设置目标值                         |
| client | 远程访问 | 存取TinyWebDB服务器 | 开启为start，为stop |

注：

* 表中出现的`<n>`为相应资源编号，编写时需替换为具体数值，如0、1、2等，注意不要带入`<`和`>`符号
* 如果以页面方式提交数据(GET或POST)，需另外增加一个参数`fmt`，其值应为`html`

## 演示

demo目录中分别包括AppInventor、HTML页面、Postman和Python等演示或测试项目代码。注意，**测试或执行应用时，应确保测试设备与掌控板处于同一WiFi网络中**。
