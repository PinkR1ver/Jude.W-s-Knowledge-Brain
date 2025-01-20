---
title: ANOVA, Analysis of Variance & F-test
tags:
  - significance_test
  - math
  - statistics
  - advanced
date: 2025-01-09
---
## Basic

ANOVA（Analysis of Variance）是一种用于分析因变量与自变量之间关系的统计方法，它可以用来分析多个因素同时对因变量的影响。ANOVA的基本思想是将总方差分解为各个因素之间的方差和因变量之间的方差。通过分析这些方差，我们可以判断哪些因素对因变量产生了影响。

### Conditions

ANOVA的主要假设包括：

1. 自变量之间独立性假设：不同的自变量之间是独立的，即改变一个自变量不会影响另一个自变量的取值。
2. 因变量的正态分布假设：在各个组间，因变量的分布遵循正态分布。
3. 同方差假设：各个组间的方差是相同的。

当这些假设满足时，ANOVA可以用来分析多个自变量对因变量的影响。

## ANOVA algorithm theory

### Step

#### 1. 计算总方差

$$
\text{Total Variance} = \sum_{i=1}^n (y_i - \bar{y})^2
$$

#### 2. 计算因素方差

因素方差是各个组间的方差，用于衡量各个组间的差异程度

$$
\text{Factor Variance} = \sum_{j=1}^k \frac{(\bar{y_j} - \bar{y})^2}{n_j}
$$
#### 3. 计算误差方差

误差方差是各个组内观测值与组平均值之间的差的平方和，用于衡量各个组内的差异程度

$$
\text{Error Variance} = \sum_{i=1}^n\sum_{j=1}^k (y_{ij} - \bar{y_j})^2
$$

#### 4 进行F检验

通过计算F统计量，我们可以判断各个因素是否对因变量产生了影响，

$$
F = \frac{\text{Factor Variance}}{\text{Error Variance}}
$$
如果F统计量大于F阈值，则可以接受零假设，即各个因素对因变量的影像不大；否则，可以拒绝零假设，即各个因素对因变量的影响是明显的。


## Code Practise

```python

```

## Reference

* https://juejin.cn/post/7318083908603084826
* https://www.youtube.com/watch?v=oOuu8IBd-yo
* https://www.youtube.com/watch?v=ZQaWSQjm7kI