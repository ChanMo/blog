---
layout: post
title: 使用树莓派定制智能电视系统
excerpt: 使用树莓派定制家庭影音中心
tags: raspberry kodi jellyfin
---

## 2022/04/16

Pi3B播放H264没问题, H265会卡顿, 只有音频, 无视频 Pi4B可正常播放H264,
H265

## KODI

### Install

    $ sudo apt install kodi

### 修复中文字符无法显示

Goto Kodi home screen Select menu: System \| Interface settings Select:
Skin Select: Fonts Select: Arial based

### 开机启动

    $ sudo sed -i "1i @kodi" /etc/xdg/lxsession/LXDE-pi/autostart

## Jellyfin

### Install

    $ sudo apt install apt-transport-https
    $ curl https://repo.jellyfin.org/debian/jellyfin_team.gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/jellyfin-archive-keyring.gpg >/dev/null
    $ echo "deb [signed-by=/usr/share/keyrings/jellyfin-archive-keyring.gpg arch=$( dpkg --print-architecture )] https://repo.jellyfin.org/debian $( lsb_release -c -s ) main" | sudo tee /etc/apt/sources.list.d/jellyfin.list
    $ sudo apt update
    $ sudo apt install jellyfin
