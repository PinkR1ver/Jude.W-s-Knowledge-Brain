---
title: pHINTS系统设计
tags:
  - plan
date: 2024-11-14
---
## HINTS临床试验背景


HINTS（Head Impulse, Nystagmus, Test of Skew）临床试验是一种针对急性前庭综合症（Acute Vestibular Syndrome, AVS）患者的诊断方法，旨在通过床旁测试区分中枢性和周围性眩晕的病因，尤其是快速准确地识别**中枢性眩晕**。

HINTS试验的核心组成为：

- 头部冲击试验（Head Impulse Test, HIT）
- 眼震检查（Nystagmus）
- 倾斜试验（Test of Skew）

HINTS试验的主要目的：
1. 鉴别中枢性眩晕与外周性眩晕
    - 外周眩晕（如前庭神经炎）通常无严重的神经系统危害，但中枢性眩晕（如后循环卒中）可能会导致严重后果，需紧急治疗。
2. 提高床旁诊断的敏感性和特异性
    - HINTS试验在床旁诊断中枢性眩晕的敏感性高于传统影像学（如头部CT扫描），尤其在卒中早期表现不明显时。
3. 减少不必要的影像学检查
    - 准确的床旁诊断可以减少对影像学的依赖，降低医疗成本，并加速对患者的干预。
4. 优化急性眩晕的分诊和治疗
    - 及时识别高危患者，有助于快速启动卒中或中枢性疾病的治疗。


HINTS试验可以通过简单的临床医生观察来进行，被称为cHINTS（clinic HINTS），也可以通过高帧率目镜捕捉眼动视频来进行，被称为vHINTS（video HINTS）。cHINTS在诊断的敏感性和特异性上相较于vHINTS有较大的差异，会造成患者假阴性的误判。vHINTS通常需要复杂的部署和昂贵的设备，在大多数临床场景中无法普及。

因此，我们通过手机设计pHINTS（phone HINTS），通过iPhone前置摄像头的ARKit框架捕捉头动和眼动信号来弥补cHINTS的不足，并在一些临床场景中代替vHINTS的作用。

## 系统设计框图

![](research_career/MSc_FYP/attachments/HINTS.svg)

<center>Fig 1. 系统设计框图</center>



## pHIT, 基于手机的头脉冲试验


头脉冲试验中，我们有两个主要任务，捕捉扫视波和计算前庭眼反射（VOR）增益。

### 识别扫视波

在HIT试验中，试验人员知道患者将目光集中在目标上，如果响应头部冲击的VOR运动不足以将目光集中在目标上，则将激活眼球运动通路以将眼睛正确地放置在精确位置。扫视机制就是进行这种矫正的主要眼球活动，同时因为扫视运动需要更高水平的大脑活动，因此扫视运动的开始往往需要延迟80-100ms。

![](research_career/MSc_FYP/attachments/Pasted%20image%2020241122170739.png)
<center>Fig 2. 头脉冲试验</center>



这种扫视又分为两种

![](research_career/MSc_FYP/attachments/Figure_1.png)
<center>Fig 3. 显性扫视</center>

如Fig 3所示，如果从头部运动开始算起，扫视的延迟时间很长，在250ms及以上，这类扫视的发生的时候，头部已经完成了运动，被称为显性扫视。

![](research_career/MSc_FYP/attachments/Figure_2.png)
<center>Fig 4. 隐形扫视</center>

如果患者能够预测眼睛将无法看到目标，他们可能会决定在头部停止前开始扫视。因此，扫视可能发生在头部运动期间，这被称为隐性扫视。这种扫视从头部运动开始计算的话，通常延迟小于200ms。同时，隐形扫视会伴随小范围的显性扫视，这些显性扫视太小，较难被检测到。

显性扫视检查隐形扫视在pHINTS中更为重要，因为隐形扫视在cHINT中难以被检测出来。

我们准备采用的检查方法为通过峰的数量和出现时间进行模式识别。

### 增益计算

通过VOR增益可以量化眼球和头部运动之间的关系，其计算为VOR眼球运动和头部运动的比率。目前，使用哪些头部和眼球运动的测量值来计算VOR增益仍然存在分歧。

目前常采用的方法有三种，

* 基于瞬时速度的方法，VOR 增益通常在头部冲击开始后以固定间隔（40、60 或 80 毫秒）计算
	* Pros: 不会被隐形扫视影响（计算增益时要去除隐形扫视的影响）
	* Cons: 容易受到类似于测试目镜滑落等的伪影影响
* 基于头部和眼球曲线下面积计算VOR增益
	* Cons: 必须先移除隐性扫视
* 使用脉冲前100ms眼部和头部的速度进行回归拟合，然后通过拟合线的斜率计算增益
	* Pros: 在基于瞬时速度的基础上，增益计算更稳健，对目镜运动敏感度更低

这三种增益我们都会计算并和商用设备比较



## p-Nystagmus，基于手机的眼震试验

针对眼震环节，目前我们想针对自发性眼震和(Spontaneous nystagmus)和凝视性诱发眼震(Gaze-evoked nystagmus, GEN)。在自发性眼震中，患者直视前方并被观察眼震。在GEN中，患者跟随注意点，眼睛慢慢转向右侧，然后转向左侧，在特定的角度停留。

眼震实验中，我们捕捉的参数为眼震快相方向和慢相速度。

![](research_career/MSc_FYP/attachments/Pasted%20image%2020241122172637.png)

<center>Fig 5. 眼震信号，水平方位和竖直方位</center>

在Fig 5中，LH代表horizontal position of the left eye，左眼水平位置，LV代表vertical position of the left eye，右眼水平位置，即信号代表的快相方向为向左和向上。

通过眼震的快相方向，我们可以定性地判断出患者是否有中枢性病变，其逻辑在系统框图中有具体细节。简单来说，外周性前庭病变，如前庭神经炎或梅尼埃病往往是单向水平眼震，中枢性前庭病变往往会有竖直方向水平眼震，并在凝视诱发眼震中会表现出变向眼震和慢相速度不稳定等现象。

慢相速度可以用来量化眼震的强度，为医生判断病因提供辅助，具体细节见框图Fig 1。


## p-Test of Skew，基于手机的偏斜试验

偏斜试验的试验步骤如下：

- 患者固定头部，通常直立或坐着。
- 目光注视固定目标，如检查者的鼻尖。
- 检查者使用遮挡物（如手或纸片），快速遮盖患者的一个眼睛，然后立即遮盖另一个眼睛。
- 遮挡时观察眼睛的反应。
- 每次遮挡移除后，观察是否有眼球垂直方向的调整（即眼位回中或偏离的现象）。

偏斜试验（Test of Skew）是HINTS试验中的一个关键组成部分，用于识别隐匿性斜视（skew deviation），帮助判断患者的眩晕是否可能由中枢性病变引起。

偏斜试验的特异性很高，在系统中，该模块主要输出是否有偏斜出现为眼震试验提供补充。

## 系统最终输出

通过pHINTS三个模块的设计，我们可以快速判断患者健康、前庭外周病变、前庭中枢病变；并初步判断判断患者的严重程度。

最终我们会生成一份报告，提供给医生详细的参数和系统的初步判断以辅助医生临床诊断的决策。


## Reference

[1] Rey-Martinez, Jorge, et al. “HITCal: A Software Tool for Analysis of Video Head Impulse Test Responses.” _Acta Oto-Laryngologica_, vol. 135, no. 9, Sept. 2015, pp. 886–94. _DOI.org (Crossref)_, https://doi.org/10.3109/00016489.2015.1035401.

[2] Lee, Dong-Han, et al. “Objective Measurement of HINTS (Head Impulse, Nystagmus, Test of Skew) in Peripheral Vestibulopathy.” _Auris Nasus Larynx_, vol. 49, no. 6, Dec. 2022, pp. 938–49. _DOI.org (Crossref)_, https://doi.org/10.1016/j.anl.2022.03.003.

[3] Kang, Jin-Ju, et al. “Recording and Interpretation of Ocular Movements: Spontaneous and Induced Nystagmus.” _Annals of Clinical Neurophysiology_, vol. 25, no. 1, Apr. 2023, pp. 10–18. _DOI.org (Crossref)_, https://doi.org/10.14253/acn.2023.25.1.10.

