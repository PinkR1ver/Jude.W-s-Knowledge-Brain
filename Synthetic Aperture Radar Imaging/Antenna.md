---
title: Antenna
tags:
- SAR
- physic
- basic
---

# Theorem

## 谐振电路 (Resonant circuit) - RLC for example

### 什么是谐振

电路中电容器$L$、电感器$C$两组件之能量相等，当能量由电路中某一电抗组件释出时，且另一电抗组件必吸收相同之能量，即此两电抗组件间会产生一能量脉动。

### 两种简单的谐振电路

![](Synthetic%20Aperture%20Radar%20Imaging/attachments/Pasted%20image%2020230330160535.png)


#### *Resonant Frequency*

电容，电阻的[电抗](Circuit/Basic/Electric_units.md#Electrical%20impedance)相同时发生谐振

$$
|X_C| = |\frac{1}{j2\pi fC}| = |X_L| = |j2\pi fL|
$$
Rearranging,

$$
f^2 =  \frac{1}{(2\pi)^2 C L}
$$

$$
f = \frac{1}{2\pi \sqrt{LC}}
$$

