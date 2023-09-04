---
title: Support Vector Machine
tags:
  - machine-learning
date: 14-04-2023
---

# Hyper Parameters

## Kernel Function

* Linear
* Polynomial
* RBF
	* $\gamma$: The gamma parameter **defines the influence of each training example on the decision boundary**. A higher gamma value gives more weight to the closer points, while a lower value allows points further away to have a significant impact. Higher values of gamma can lead to overfitting, especially in datasets with noise.
## C Parameter

The C parameter, also known as the regularization parameter, controls the trade-off between maximizing the margin and minimizing the classification error. **A smaller C value allows for a larger margin but may lead to misclassification of some training examples, while a larger C value focuses on classifying all training examples correctly but might result in a narrower margin**
## [Training Method](https://wadhwatanya1234.medium.com/multi-class-classification-one-vs-all-one-vs-one-993dd23ae7ca)

* One-vs-All
* One-vs-One

# Reference

* [“华为开发者论坛.” _Huawei_, https://developer.huawei.com/consumer/cn/forum/topic/41598169. Accessed 4 Sept. 2023.](https://developer.huawei.com/consumer/cn/forum/topic/41598169)
* [Multi-class Classification — One-vs-All & One-vs-One](https://wadhwatanya1234.medium.com/multi-class-classification-one-vs-all-one-vs-one-993dd23ae7ca)