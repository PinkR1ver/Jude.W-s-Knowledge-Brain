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

![](synthetic_aperture_radar_imaging/attachments/Pasted%20image%2020230419111635.png)

![](synthetic_aperture_radar_imaging/attachments/Pasted%20image%2020230418165114.png)

如图，针对红点目标，SAR从A点开始照射到P点最接近目标，直到B点离开红点离开。

假设平台$t$时刻飞行到红点位置，雷达发射脉冲信号$s(\tau)$，此时接收的回波信号信息为：


$$
r(\tau,t) = \sigma(R_0, A_0) s(\tau - \frac{2R(t)}{c})\omega_a(\frac{t - t_p}{T_{syn}})
$$


* $\sigma(R_0, A_0)$表示$(R_0, A_0)$处目标的散射面积
* $T_{syn}$表示合成孔径的时长
* $\omega_a(\cdot)$理想情况可以认为是矩性窗，实际上是由实孔径天线的方向图构成；考虑到信号往返，$\omega_a(\cdot)$函数为天线方向图的平方。

同时，有：

$$
R(t) = \sqrt{R_0^2 + v^2(t-t_p)^2}
$$

从图示不难发现，与红点目标相比，距离向等距的黑点目标多普勒历程一致，只是对应的方位向时延不一样，反映在表达式上，即距离目标最短的时刻$t_p$不同。对接收的回波信号进一步化简可得：

$$
r(\tau, t) = \{s(\tau)w_a(\frac{t}{T_{syn}})\} \bigotimes h(\tau, t)
$$

$$
h(\tau, t) = \sigma(R_0, A_0)\delta(\tau-\frac{2R(t)}{c}, t-t_p)
$$

将SAR（信号发射到接收的过程）看成一个系统，$h(\tau, t)$为对应的系统函数，系统函数包含目标位置处散射面积$\sigma(R_0, A_0)$和重建函数$\delta(\tau-\frac{2R(t)}{c}, t-t_p)$。

SAR成像问题等效为：根据发射信号从回波信号中反卷积出系统函数$h(\tau, t)$

同时，系统函数$h(\tau, t)$中的重建函数$\delta(\tau-\frac{2R(t)}{c}, t-t_p)$的快时间维存在慢时间维的耦合项，为此SAR成像算法一个关键的步骤是去除这个耦合项，称为距离徙动校正，将重建函数矫正为$\delta(\tau-\frac{2R}{c}, t-t_p)$，这时候可以分别对快时间维$\tau$和慢时间维$t$的信号做脉冲压缩处理，得到SAR图像

上述是SAR回波信号模型的建立过程以及对所得回波信号模型的简单分析，在建立信号模型的过程中，运用了雷达领域经常用到了两个概念，*慢时间是对脉冲间时间的标记*，即慢时间表示发射的是第几个脉冲信号，所以慢时间本身是离散的，离散间隔为脉冲重复周期；*快时间是对脉冲内时间的标记*，即快时间显示的是任意一个脉冲内的时刻，相比慢时间，快时间是连续的，需要通过信号的采样来离散。


### 信号模型的四域表示



# Range-Doppler Algorithm (RDA)

Range-Doppler Algorithm是SAR成像的第一个算法，在1970年代被developed出来，用来生成stripmap的SAR。Range-Doppler Algorithm利用block-processing处理，在距离和方位角中使用频域运算。

步骤如下：

![](synthetic_aperture_radar_imaging/attachments/Pasted%20image%2020230417110036.png)

## Range Compression

![](synthetic_aperture_radar_imaging/attachments/Pasted%20image%2020230418102226.png)

距离参考函数是一系列复数，表示天线发射的原始啁啾信号(original [chirp](synthetic_aperture_radar_imaging/Chirp.md))。

天线发射的原始线性调频信号（**linear-frequency chirp**）是一种线性调频连续波信号，它的频率随着时间线性变化，形成一种锯齿状的波形。这种信号可以用数学公式表示为：

$$ s(t) = \cos\left(2\pi\left(f_c t + \frac{B}{T} t^2\right)\right) $$

其中，$f_c$是信号的中心频率，$B$是信号的带宽，$T$是信号的持续时间。这种信号可以用一个本地振荡器（LO）来生成，然后通过一个功率放大器来放大，并从天线发射出去。

## Azimuth Compression

![](synthetic_aperture_radar_imaging/attachments/Pasted%20image%2020230418162216.png)



# Reference

* [A Review of Synthetic-Aperture Radar Image Formation Algorithms and Implementations: A Computational Perspective]([Remote Sensing | Free Full-Text | A Review of Synthetic-Aperture Radar Image Formation Algorithms and Implementations: A Computational Perspective (mdpi.com)](https://www.mdpi.com/2072-4292/14/5/1258))
* [Range Doppler Algorithm - University of Kansas](https://people.eecs.ku.edu/~callen58/826/826_SAR_Processing_Algorithms_Overview-F15.pptx)
* [距离多普勒算法（RDA）-SAR成像算法系列（三）-【杨（_> <_)】的博客-CSDN博客 🚧这个人的博客讲的真不错🚧](https://blog.csdn.net/yjh_2019/article/details/123772486?spm=1001.2014.3001.5502)

