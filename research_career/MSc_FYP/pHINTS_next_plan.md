---
title: 构建pHINTS系统工作计划 - Update
tags:
  - plan
date: 2024-11-14
---
## 背景

在上一期的工作中，我们针对vHINTS试验前需要校准的需求制作了一套用于校准的方案，用于校准我们的pHINTS试验。

## 计划

pHINTS试验的工作内容主要分为3个部分，pHIT，pNystagmus和p-Test of Skew。我们接下来的计划是一步步攻克使用iPhone ARKit Framework进行这三项试验的难点。

### pHIT

在HIT试验中，其工作任务被分为识别扫视(saccades)和计算增益(gain)。

#### 识别扫视

在HIT试验中，试验人员知道患者将目光集中在目标上，如果响应头部冲击的VOR运动不足以将目光集中在目标上，即增益减少，则将激活眼球运动通路以将眼睛正确地放置在精确位置。扫视机制就是进行这种矫正的主要眼球活动，同时因为扫视运动需要更高水平的大脑活动，因此扫视运动的开始往往需要延迟80-100ms。

这种扫视又分为两种

![](research_career/MSc_FYP/attachments/Pasted%20image%2020241114103632.png)
<center>Fig 1. 显性扫视</center>

如Fig 1所示，如果从头部运动开始算起，扫视的延迟时间很长，在250ms及以上，这类扫视的发生的时候，头部已经完成了运动，被称为显性扫视。

![](research_career/MSc_FYP/attachments/Pasted%20image%2020241114103921.png)
<center>Fig 2. 隐形扫视</center>

如果患者能够预测眼睛将无法看到目标，他们可能会决定在头部停止前开始扫视。因此，扫视可能发生在头部运动期间，这被称为隐性扫视。这种扫视从头部运动开始计算的话，通常延迟小于200ms。同时，隐形扫视会伴随小范围的显性扫视，这些显性扫视太小，较难被检测到。

触发隐形扫视的机制尚不完全清楚，但是隐形扫视往往表示患者症状有所减轻。

显性扫视检查隐形扫视在pHINTS中更为重要，因为隐形扫视在cHINT中难以被检测出来。

#### 增益计算

通过VOR增益可以量化眼球和头部运动之间的关系，其计算为VOR眼球运动和头部运动的比率。目前，使用哪些头部和眼球运动的测量值来计算VOR增益仍然存在分歧。

目前常采用的方法有三种，

* 基于瞬时速度的方法，VOR 增益通常在头部冲击开始后以固定间隔（40、60 或 80 毫秒）计算
	* Pros: 不会被隐形扫视影响（计算增益时要去除隐形扫视的影响）
	* Cons: 容易受到类似于测试目镜滑落等的伪影影响
* 基于头部和眼球曲线下面积计算VOR增益
	* Cons: 必须先移除隐性扫视
* 使用脉冲前100ms眼部和头部的速度进行回归拟合，然后通过拟合线的斜率计算增益
	* Pros: 在基于瞬时速度的基础上，增益计算更稳健，对目镜运动敏感度更低


针对这两个任务，我们首先参考Jorge[1]在2015年对vHIT测试数据的处理，将vHIT的技术迁移到pHIT的数据上，如Fig 3。

![](research_career/MSc_FYP/attachments/7a24a52ac4cecf113ee8328a7d624b4c.png)
<center>Fig 3. HITCal, a software to analysis saccade in vHIT exam</center>


### pNystagmus

针对眼震环节，目前我们想针对凝视性眼震(Gaze-evoked nystagmus, GEN)。在GEN中，患者跟随注意点，眼睛慢慢转向右侧，然后转向左侧，在特定的角度停留，我们可以通过ARKit Framework去计算每个注视位置的眼球震颤的慢相速度(slow-phase velocity, SPV)[2]。

![](research_career/MSc_FYP/attachments/Pasted%20image%2020241114153125.png)
<center>Fig 4. 在手机和VOG目镜上，不同水平角度注视时，测量得到的凝视眼动数据</center>

如Fig 4所示，蓝色为眼球震颤的慢相，红色为眼球震颤的快相。

### p-Test of Skew

暂无

## Reference

[1] Rey-Martinez, Jorge, et al. “HITCal: A Software Tool for Analysis of Video Head Impulse Test Responses.” _Acta Oto-Laryngologica_, vol. 135, no. 9, Sept. 2015, pp. 886–94. _DOI.org (Crossref)_, https://doi.org/10.3109/00016489.2015.1035401.

[2] Lee, Dong-Han, et al. “Objective Measurement of HINTS (Head Impulse, Nystagmus, Test of Skew) in Peripheral Vestibulopathy.” _Auris Nasus Larynx_, vol. 49, no. 6, Dec. 2022, pp. 938–49. _DOI.org (Crossref)_, https://doi.org/10.1016/j.anl.2022.03.003.