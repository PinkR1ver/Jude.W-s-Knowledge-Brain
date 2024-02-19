---
title: 关于压疮（pressure injury）相关的文献阅读
tags:
  - papers
  - pressure-injury
---


## A Comprehensive and Improved Definition for Hospital-Acquired Pressure Injury Classification Based on Electronic Health Records: Comparative Study

### DOI

http://dx.doi.org/10.2196/40672

### Publication Date

2023.02.23

### Abstract

* Hospitial-acquired pressure injuries(HAPI)是一个重要的护理指标(Nursing Metric)，是医院中最常见的可预防事件。
* 文章想要通过电子健康纪录(electronic health records, EHRs)，构建机器学习模型来识别和预测HAPI。
* 目前存在的问题是，
	* 准确的模型依赖于高质量的HAPI数据标签，然而，**EHR中的不同数据源可能会提供有关于患者发生HAPI的矛盾信息**。
	* 现有的 HAPI 定义彼此不一致，即使在同一患者群体中也是如此。不一致的标准使得无法对机器学习方法进行**基准测试**来预测 HAPI。
* 该文章有着三个目标：
	* 识别EHR中HAPI来源的差异
	* 使用所有 EHR 来源的数据制定 HAPI 分类的全面定义
	* 说明改进 HAPI 定义的重要性
* 该文章使用的方法：评估了MIMIC-III数据库中的临床记录、诊断代码、程序代码和图表事件中记录的 HAPI 事件之间的一致性。我们分析了 3 个现有 HAPI 定义所使用w的标准及其对监管指南的遵守情况。提出了Emory HAPI（EHAPI），这是一个改进的、更全面的HAPI定义。然后，我们使用基于树的顺序神经网络分类器评估了标签在训练 HAPI 分类模型中的重要性。
* 最终，文章说明了定义 HAPI 的复杂性，<13% 的住院患者在 4 个数据源中记录了至少 3 个 PI 指征。尽管图表事件是最常见的指标，但它是超过 49% 的停留时间的唯一 PI 文档。我们证明现有 HAPI 定义和 EHAPI 之间缺乏一致性，只有 219 个具有一致的正面标签。我们的分析强调了改进的 HAPI 定义的重要性，使用我们的标签训练的分类器优于护士标注和consensus set(既存在任何PI证据都会标注为阳性)

> [!abstract] 
> 因为HAPI的定义不统一，文章通过使用大量不同EHR来源的数据重现制定HAPI分类的定义并提出EHAPI。通过EHAPI训练分类器会具有更好的性能 。


### Tech Detail

