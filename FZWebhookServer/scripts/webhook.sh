#!/usr/bin/env bash

echo "========= BEGIN webhook =========="


git pull

# 需要到各个文件夹下去npm install
cd ../FZServer
npm install

cd ../FZSocketServer
npm install

pm2 restart all



echo "======== END webhook =========="
