# 0x00 前言

项目的思路是看文章抄来的（别问为什么，因为I'm vegetable dog），价值不大就当往自己github灌水

文章中没有直接给出可以用的源码，所以自己敲了一下...然后把工具跑起来



# 0x01 准备工作

（1）首先下载一个xray：https://github.com/chaitin/xray/releases

（2）然后下载rad：https://github.com/chaitin/rad  将两者安装在同一目录下。

（3）在该目录下创建url.txt，里面存放要扫描的域名。

（4）burp安装自己想要的漏洞检测插件，如：

**ShiroScan**

https://github.com/amad3u4/ShiroScanner/

**J2EEScan**

https://github.com/PortSwigger/j2ee-scan

**Struts RCE 1.0**

https://github.com/prakharathreya/Struts2-RCE

**FastjsonScan**

https://github.com/p1g3/Fastjson-Scanner

（4）设置burp：

burp设置监听端口8080：

![image-20201223113724341](E:\Desktop\资料\blog\rad+xray自动化扫描\image-20201223113724341.png)

burp起个upstream代理，然后让rad的流量从burp转出

![image-20201223113815656](E:\Desktop\资料\blog\rad+xray自动化扫描\image-20201223113815656.png)



# 0x02 开始扫描

（1）burp在user options中设置upstream 127.0.0.1 7777，同时开启burp监听8080端口

（2）命令行运行脚本批量进行

```
python3 8080scan.py
```

（3）命令行运行xray，xray监听由burp转发过来的流量，进行漏洞检测

```
xray.exe webscan --listen 127.0.0.1:7777 --html-output xxx.html
```



# 0x03 结果

![image-20201223115115034](E:\Desktop\资料\blog\rad+xray自动化扫描\image-20201223115115034.png)

burpsuite中也有插件进行漏洞检测，这里懒得放了



#  0x04 抄袭(划掉)参考

**原文：**https://mp.weixin.qq.com/s/UoZZv2SG-oCqOzr7NnwDPw

