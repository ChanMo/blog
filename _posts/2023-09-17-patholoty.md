---
layout: post
title: 数字病理, 医学影像相关开源技术框架
description: 数字病理, 医学影像相关开源技术框架
keywords: 数字病理, 医学影像, patholoty
tags: patholoty, opensource
---

数字病理, 医学影像相关开源技术框架

## OME开放显微镜环境

<https://www.openmicroscopy.org/omero/>

From the microscope to publication, OMERO handles all your images in a
secure central repository. You can view, organize, analyze and share
your data from anywhere you have internet access. Work with your images
from a desktop app (Windows, Mac or Linux), from the web or from 3rd
party software. Over 150 image file formats supported, including all
major microscope formats.

## ImageJ

![](./img/ImageJ.jpeg)

ImageJ是一个基于java的公共的图像处理软件，它是由National Institutes of
Health开发的。 可运行于Microsoft Windows，Mac OS，Mac OS
X，Linux，和Sharp Zaurus等多种平台。
其基于java的特点，使得它编写的程序能以applet等方式分发。

ImageJ能够显示，编辑，分析，处理，保存，打印8位，16位，32位的图片，
支持TIFF, PNG, GIF, JPEG, BMP, DICOM, FITS等多种格式。
ImageJ支持图像栈功能，即在一个窗口里以多线程的形式层叠多个图像，
并行处理。
只要内存允许，ImageJ能打开任意多的图像进行处理。除了基本的图像操作，
比如缩放，旋转， 扭曲， 平滑处理外，ImageJ还能进行图片的区域和像素统计，
间距，角度计算， 能创建柱状图和剖面图，进行傅里叶变换。

ImageJ是一个开放结构的软件， 支持用户自定义插件和宏。

ImageJ自带编辑器， 并且导入了java的编译器，实现了简单的IDE功能，
用户可直接基于ImageJ进行图像处理。

ImageJ的源代码提供免费下载 （页面存档备份，存于互联网档案馆）。

<https://github.com/imagej/ImageJ>

## DICOM医疗数位影像传输协议

医疗数位影像传输协定（DICOM，Digital Imaging and Communications in
Medicine）
是一组通用的标准协定，在对于医学影像的处理、储存、打印、传输上。
它包含了档案格式的定义及网络通信协定。DICOM是以TCP/IP为基础的应用协定，
并以TCP/IP联系各个系统。两个能接受DICOM格式的医疗仪器间，
可借由DICOM格式的档案，来接收与交换影像及病人资料。

DICOM可以整合不同厂商的医疗影像仪器、服务器、工作站、打印机和网络设备，
使它们都能整合在PACS系统中。许多不同厂商的仪器、服务器、工作站都根据DICOM的标准，
来制造支援DICOM机器。DICOM已经广泛地被医院所采用，并且在牙医和一般的诊所中获得小规模的运用。

[wikipedia](https://zh.wikipedia.org/zh-cn/DICOM)

## PACS医疗影像存档与通信系统

在影像诊断学中，医学影像存档与通信系统（英语：Picture archiving and
communication
system，PACS）是一种专门用来存储、获取、发送与展示医疗影像的电脑或网络系统，
PACS一词由Andre Duerinckx博士提出。

[wikipedia](https://zh.wikipedia.org/zh-cn/%E9%86%AB%E7%99%82%E5%BD%B1%E5%83%8F%E5%84%B2%E5%82%B3%E7%B3%BB%E7%B5%B1)
