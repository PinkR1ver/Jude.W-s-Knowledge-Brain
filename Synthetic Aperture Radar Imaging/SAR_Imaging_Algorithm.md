---
title: SAR Imaging Algorithm review in 2022
tags:
- SAR
- basic
- algorithm
- state-of-art
---


# Overview

* Backprojection
* Matched-filter
* Polar format
* Range-Doppler
* Chirp scaling algorithms

# What is SAR processing?

## Born approximation

SAR 处理算法将场景建模为一组离散的点目标，其分散的 EM 场不会相互影响。

* 无多次反弹
* 目标处的电场仅来自入射波，而不来自周围的散射体
* 目标模型是线性的，因为点目标 P1 和点目标 P2 的散射响应被建模为点目标 P1 本身的响应 + 点目标 P2 本身的响应
* 可以应用**叠加原理(principle of superposition)**

--- 

SAR 处理是对图像中每个像素应用匹配滤波器，其中匹配滤波器系数是来自单个孤立点目标的响应

* SAR processing is a correlation filter between a single isolated point target response and the raw data
* SAR processing is an inner product between our model of a single isolated point target and the raw data


# Range-Doppler Algorithm (RDA)

Range-Doppler Algorithm是SAR成像的第一个算法，在1970年代被developed出来，用来生成stripmap的SAR。Range-Doppler Algorithm利用block-processing处理，在距离和方位角中使用频域运算。

步骤如下：

![](Synthetic%20Aperture%20Radar%20Imaging/attachments/Pasted%20image%2020230417110036.png)

## Range Compression



# Reference

* [A Review of Synthetic-Aperture Radar Image Formation Algorithms and Implementations: A Computational Perspective]([Remote Sensing | Free Full-Text | A Review of Synthetic-Aperture Radar Image Formation Algorithms and Implementations: A Computational Perspective (mdpi.com)](https://www.mdpi.com/2072-4292/14/5/1258))
* [Range Doppler Algorithm - University of Kansas](https://people.eecs.ku.edu/~callen58/826/826_SAR_Processing_Algorithms_Overview-F15.pptx)