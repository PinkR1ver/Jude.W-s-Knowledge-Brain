---
title: Z-score
tags:
  - math
  - statistics
date: 2024-10-08
---
# What is Z-score

$$
z = \frac{X-\mu}{\sigma}
$$
* $X$: 单个数据点
* $\mu$: 总体均值
* $\sigma$: 总体标准差

通过该公式，Z-score表示一个数据点与平均值之间的标准差距离。具体来说：

- 当Z-score为0时，表示该数据点等于均值。
- 当Z-score在±1之间时，表示数据点在一个标准差范围内。
- 当Z-score超过±3时，通常被视为异常值


# Pros and Cons

Z-score的概念很直接，部署快捷。

Z-score为什么要叫做Z-score，是因为**Z的符号来源于正态分布**。在统计学中，标准正态分布是一种具有均值为0、标准差为1的特殊正态分布，通常用字母 **Z** 表示。

也是因为此，Z-score用于的数据分布常常处于正太分布，对数据正太分布有依赖性，因此对极端值敏感，使得均值和标准差容易受到极端值影响，导致误判