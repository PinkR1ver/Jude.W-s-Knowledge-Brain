---
title: How to run paperless-ngx in windows
tags:
  - tool
date: 2024-10-23
---
## Step 1. Install WSL (Windows Sub Linux)

因为paperless-ngx是运行在linux容器里，所以windows下必须下载WSL。

安装WSL的方法是通过PowerShell，
1.  使用`wsl -l` 检查计算机是否启用wsl功能，如果没有启用，用管理员权限打开PowerShell进入步骤2；如果有输出，则进入步骤3

2. 运行下面这个指令：

```PowerShell
# 开启 windows 子系统
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
# 开启虚拟机特性
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

该指令的目的是启用wsl功能

3. 查看可以下载的Linux Distribution并下载：

```PowerShell
wsl --list --online
```

得到下面的输出：

```
The following is a list of valid distributions that can be installed.
Install using 'wsl.exe --install <Distro>'.

NAME                            FRIENDLY NAME
Ubuntu                          Ubuntu
Debian                          Debian GNU/Linux
kali-linux                      Kali Linux Rolling
Ubuntu-18.04                    Ubuntu 18.04 LTS
Ubuntu-20.04                    Ubuntu 20.04 LTS
Ubuntu-22.04                    Ubuntu 22.04 LTS
Ubuntu-24.04                    Ubuntu 24.04 LTS
OracleLinux_7_9                 Oracle Linux 7.9
OracleLinux_8_7                 Oracle Linux 8.7
OracleLinux_9_1                 Oracle Linux 9.1
openSUSE-Leap-15.6              openSUSE Leap 15.6
SUSE-Linux-Enterprise-15-SP5    SUSE Linux Enterprise 15 SP5
SUSE-Linux-Enterprise-15-SP6    SUSE Linux Enterprise 15 SP6
openSUSE-Tumbleweed             openSUSE Tumbleweed
```

选择`Ubuntu-22.04`下载，

```
wsl --install Ubuntu-22.04
```


## Step 2. Download Docker Desktop 

下载Docker Desktop，在官网下载即可；

然后打开docker desktop


## Step 3. Configure the docker file

git clone paperless-ngx这个项目，我们需要的是其`docker\compose\`下的三个文件

```
docker-compose.sqlite-tika.yml
docker-compose.env
.env
```

把他们打包到一个文件夹下，然后更改docker-compose.sqlite-tika.yml名字到doker-compose.yml;

同时新建文件夹 `data` `consume` `export` `media`

现在，这个文件夹就是paperless工作的根目录了；

如图所示：

![](toolkit/paperless_ngx/attachments/Pasted%20image%2020241223110555.png)


其中，`docker-compose.yml`里面的一些配置要相应改变

![](toolkit/paperless_ngx/attachments/Pasted%20image%2020241223110707.png)

49行到53行，将前面的路径改成我们相应的路径，格式是这样的：

```
{our_data_path}:/usr/src/paperless/data
{our_media_path}:/usr/src/paperless/media
{our_export_path}:/usr/src/paperless/export
{our_consume_path}:/usr/src/paperless/consume
```


## Step 4. Docker compose

进入到我们的paperless 文件夹下

运行：

```
docker-compose pull
```

pull完之后，然后运行，

```
docker-compose run -rm webserver createsuperuser
```

然后运行

```
docker-compose up -d
```



## Step 5. Run paperless-ngx in Docker Desktop

做完以上这些，应该要在docker desktop里发现这个paperless容器，打开它

![](toolkit/paperless_ngx/attachments/Pasted%20image%2020241223111325.png)


![](toolkit/paperless_ngx/attachments/Pasted%20image%2020241223111353.png)

run起来后，打开[http://localhost:8000/](http://localhost:8000/)就可以看到paperless运行起来了

![](toolkit/paperless_ngx/attachments/Pasted%20image%2020241223111501.png)


## Reference

* https://www.youtube.com/watch?v=UfhqronSKAo