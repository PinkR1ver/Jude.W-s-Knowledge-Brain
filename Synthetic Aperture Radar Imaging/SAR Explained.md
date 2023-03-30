---
title: Synthetic Aperture Radar (SAR) Explained
tags:
- SAR
- basic
---

# Radar Basic Concepts

## Down Looking vs. Side Looking

![Pasted image 20230320150424](Synthetic%20Aperture%20Radar%20Imaging/attachments/Pasted%20image%2020230320150424.png)

Down Looking不能区分距离一样的a，b点，一般只用于monitoring of air and naval traffic

## Simplified explanation of Radar working & What is SAR
The radar consists fundamentally of *a transmitter*, *a receiver*, *an antenna* and *an electronic system* to process and record the data.

The transmitter generates successive short bursts or pulses of microwave at regular intervals which are focused by the antenna into a beam. Radar beam illuminates the surface **obliquely** at a right angle to the motion of the platform. The antenna receives a portion of the transmitted energy reflected or it's known as backscattered from various objects within the illuminated beam by  measuring this time delay between the transmission of a pulse and the reception of the backscattered echo from different  targets. Their distance from the radar and therefore their location can be determined as the sensor platform *moves forward* recording and processing of the backscattered signals builds up a 2-dimensional image of the surface.


> [!important] 
> Important<br>
> The along track **resolution** is determined by the beam width which is *inversely proportional to the antenna length*, also known as the **aperture**, which means that longer antenna or a longer aperture will produce a narrow beam and a finer resolution. <br>
> Long antenna $\leftrightarrow$ Small beam $\leftrightarrow$ Long aperture $\leftrightarrow$ Better image resolution

### Detail geometry

![](Synthetic%20Aperture%20Radar%20Imaging/attachments/Pasted%20image%2020230330153450.png)
**Fig** *Geometry of a side-looking real aperture radar. (SLAR)*

side-looking的雷达被分为two types —— real aperture radar(*SLAR or SLR*, SL for side-looking)和synthetic aperture radar(SAR)

如上图所示，雷达发出的pulse被[antenna聚焦](Synthetic%20Aperture%20Radar%20Imaging/Antenna.md)在一个narrow的area里，然后scatter后在不同和的时间再被receiver接收


### Why SAR
介于实际情况下的物理空间中，雷达天线的大小是限的，可以通过雷达的移动去模拟长天线情况下的雷达，也就是活得更大的aperture，这项被叫做SAR。目的是在于使用*comparatively small physical antennas*去获得*high resolution images*


## Review of Radar Image Formation

![660](Synthetic%20Aperture%20Radar%20Imaging/attachments/Pasted%20image%2020230320163240.png)

* Radar can measure *amplitude* and *phase*
* Radar can only measure part of echoes.
* The strength of the reflected echo is the backscattering coefficient ([sigma nought](Synthetic%20Aperture%20Radar%20Imaging/Radiometric%20Calibration.md)）and is expressed in [decibels(dB)](Signal%20Processing/What%20is%20dB.md)

## Radar Resolution



## Radar Key Parameters
* Wave Length
* Polarization
* Incidence Angle

### Wave Length

![](Synthetic%20Aperture%20Radar%20Imaging/attachments/Pasted%20image%2020230330153007.png)

雷达数据的空间分辨率与传感器波长与传感器天线长度之比直接相关。 对于给定的波长，天线越长，空间分辨率越高。 对于以大约 5 cm 波长运行的太空卫星（C 波段雷达），为了获得 10 m 的空间分辨率，您需要一个大约 4,250 m 长的雷达天线。 （超过 47 个足球场！）


# Reference

* [Theory of Synthetic Aperture Radar (uzh.ch)](https://www.geo.uzh.ch/~fpaul/sar_theory.html)

* ***Sentinel-1** is a famous SAR, you can find almost every *definitions* of SAR in this page:
[User Guides - Sentinel-1 SAR - Definitions - Sentinel Online - Sentinel Online (esa.int)](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-1-sar/definitions)

* [SAR(Synthetic Aperture Radar)基础(一) - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/98053986)