# Dockerfile

## 创建服务端
sudo docker build -t soone/pyinotify-server .

## 创建客户端
mv Dockerfile Dockerfile_server
mv Dockerfile_client Dockerfile
sudo docker build -t soone/pyinotify-client .

## 在需要服务器端的地方执行以下代码 
sudo docker run -d -P --name rsync-server soone/pyinotify-server

## 查看server对应的端口
sudo docker ps

## 挂载到你要开启的容器里，如： 
sudo docker run -t -i --volumes-from rsync-server soone/centos bash

## 在对应的客户端执行以下代码
sudo docker run -d -P --name rsync-client soone/pyinotify-server 192.168.x.x 49156

## 挂载到你要开启的容器里，如： 
sudo docker run -t -i --volumes-from rsync-client soone/centos bash
