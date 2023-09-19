---
title: Random Signal Basic
tags:
  - signal-processing
  - math
---

# What is Random Signals

- 随机信号(Random Signals)在任何时间的取值都是不能先验确定的随机变量

- 虽然随机信号的取值不能先验确定，但这些取值却服从某种统计规律，换言之，随机信号或过程可以用概率分布特性统计地描述

- 随机变量 $X=x(t)$，离散状态为随机序列 $x(n)$,$x_k(n)$是随机序列$x(n)$的一个样本序列

# 统计量

$$
\mu_x(n)=E\{x(n)\}=\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{k=1}^N x_k(n)
$$

$$
E\{x^2(n)\}=\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{k=1}^N x^2_k(n)
$$
  

$$
\sigma^2_x(n)=E\{[x(n)-\mu_x(n)]^2\}=\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{k=1}^N[x_k(n)-\mu_x(n)]^2
$$
  

$$
\sigma^2_x(n)=E\{x^2(n)\}-\mu^2_x(n)
$$

$$
R_x(n_1,n_2)=E\{x(n_1)x(n_2)\}=\lim_{N\rightarrow\infty}\frac{1}{N}\sum_{k=1}^N x_k(n_1)x_k(n_2)
$$


## Wide Sense Stationary Process 宽平稳过程

**平稳随机信号**——其统计特性与时间无关。

1. $\mu_x(n)=\mu_x$ - 均值与n无关，即于哪次观察信号无关

2. $R_x(n,n+m)=R_x(m)$ - 自相关函数与时间n无关，之与时移m有关

> [!tip] 
> 💡 在实际工作中，我们往往把所研究的随机信号视为平稳的，这可使问题大大简化。实际上，自然界中的绝大部分随机信号在一定条件、一定范围内可以认为是平稳的。 

**非平稳随机信号**——其统计特性与时间有关，使用Wigner-Ville分布分析

## Ergodicity 各态历经


对于平稳随机信号，虽然它的统计特性与**时间无关**，但在计算各特征时采用的是**集合平均**，就需要$x_k(n)$的无穷多个样本，即$k=1,2,\cdots,\infty$

这在实际工作中显然是不现实的，实际上我们只能得到若干个样本函数，有些情况下甚至只能得到一个，比如地震波；

那能否用**一次试验记录（或一个样本函数）来计算均值、自相关函数等这些统计特征？**

如果一平稳随机信号$x(n)$在**集合平均**意义上的均值和自相关函数与单一样本函数在**时间平均**意义上的均值和自相关函数相同，则称$x(n)$为**各态历经**信号(**Ergodicity**)。
  

> [!tip] 
> Watch this video: [_What Is Ergodicity? - Alex Adamou_. _www.youtube.com_, https://www.youtube.com/watch?v=VCb2AMN87cg. Accessed 19 Sept. 2023.](https://www.youtube.com/watch?v=VCb2AMN87cg) 
  

对于拥有Ergodicity的信号，可以用时间平均代替集合平均，即

![](signal_processing/attachments/Screenshot_from_2022-10-18_10-53-17.png)
  

$$
\mu_x=E\{x(n)\}=\lim_{M\rightarrow\infty}\frac{1}{2M+1}\sum_{n=-M}^Mx(n)
$$

$$
R_x(m)=E\{x(n)x(n+m)\}=\lim_{M\rightarrow\infty}\frac{1}{2M+1}\sum_{n=-M}^M x(n)x(n+m)
$$