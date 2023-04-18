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

<!--SAR 处理是对图像中每个像素应用匹配滤波器，其中匹配滤波器系数是来自单个孤立点目标的响应

* SAR processing is a correlation filter between a single isolated point target response and the raw data
* SAR processing is an inner product between our model of a single isolated point target and the raw data
-->

## 信号建模


SAR成像是对一个区域的散射特性进行成像，这个区域的地形一般比较复杂，区域内不同位置处的物体散射特性各不相同，最后SAR接收的是探测区域内所有物体后向散射信号的叠加，整个探测区域散射的回波信号模型非常复杂。直接构造整个探测区域的散射信号模型十分困难，也没有必要。为了简化信号模型，信号模型的建立运用了两个离散化：

* 探测区域的离散化；
* 平台飞行的离散化;

### 探测区域离散化

**将探测区域认为是若干散射点的集合**，由此对区域回波信号模型的建立转化为对这些散射点回波信号模型的建立。这样只需构建任意散射点的回波信号模型即可表示整个探测区域的回波信号模型。该离散化的准则是：离散间隔内的物体散射特性基本不变。

### 平台飞行离散化

**将平台的飞行过程认为是一个“走停”模式**，即在一个脉冲时间（脉冲重复周期）内，平台是“停”（静止）的状态，平台发射一个脉冲信号，并在该位置处接收该脉冲照射目标的回波信号；在下一个脉冲时间内，平台“走”（瞬移）到另一个位置（按照原来匀速运动应该走到的位置处），并在下一个位置重复上一个脉冲时间内平台的操作。该离散化的准则是：电磁波传播速度远大于平台速度，即SAR一次发射、接收过程中，雷达的位置基本不变。

--- 

![](Synthetic%20Aperture%20Radar%20Imaging/attachments/Pasted%20image%2020230418165114.png)

如图，针对红点目标，SAR从A点开始照射到P点最接近目标，直到B点离开红点离开。

# Range-Doppler Algorithm (RDA)

Range-Doppler Algorithm是SAR成像的第一个算法，在1970年代被developed出来，用来生成stripmap的SAR。Range-Doppler Algorithm利用block-processing处理，在距离和方位角中使用频域运算。

步骤如下：

![](Synthetic%20Aperture%20Radar%20Imaging/attachments/Pasted%20image%2020230417110036.png)

## Range Compression

![](Synthetic%20Aperture%20Radar%20Imaging/attachments/Pasted%20image%2020230418102226.png)

距离参考函数是一系列复数，表示天线发射的原始啁啾信号(original [chirp](Synthetic%20Aperture%20Radar%20Imaging/Chirp.md))。

天线发射的原始线性调频信号（**linear-frequency chirp**）是一种线性调频连续波信号，它的频率随着时间线性变化，形成一种锯齿状的波形。这种信号可以用数学公式表示为：

$$ s(t) = \cos\left(2\pi\left(f_c t + \frac{B}{T} t^2\right)\right) $$

其中，$f_c$是信号的中心频率，$B$是信号的带宽，$T$是信号的持续时间。这种信号可以用一个本地振荡器（LO）来生成，然后通过一个功率放大器来放大，并从天线发射出去。

## Azimuth Compression

![](Synthetic%20Aperture%20Radar%20Imaging/attachments/Pasted%20image%2020230418162216.png)



# Reference

* [A Review of Synthetic-Aperture Radar Image Formation Algorithms and Implementations: A Computational Perspective]([Remote Sensing | Free Full-Text | A Review of Synthetic-Aperture Radar Image Formation Algorithms and Implementations: A Computational Perspective (mdpi.com)](https://www.mdpi.com/2072-4292/14/5/1258))
* [Range Doppler Algorithm - University of Kansas](https://people.eecs.ku.edu/~callen58/826/826_SAR_Processing_Algorithms_Overview-F15.pptx)
* [距离多普勒算法（RDA）-SAR成像算法系列（三）-【杨（_> <_)】的博客-CSDN博客 🚧这个人的博客讲的真不错🚧](https://blog.csdn.net/yjh_2019/article/details/123772486?spm=1001.2014.3001.5502)

