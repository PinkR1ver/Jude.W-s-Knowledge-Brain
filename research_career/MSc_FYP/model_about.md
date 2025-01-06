---
title: 基于238例来自神经内科STANDING检查流程患者的脑卒中和前庭炎分类研究
tags:
  - algorithm
  - classification
date: 2025-01-06
---
## 数据来源和分布


该数据收录了总共235名具有影像学金标准的急性眩晕患者，按照症状分为前庭炎患者和中风患者，同时所有纳入患者均接受了头部冲击试验（HIT）、自发眼震试验、凝视诱发眼震试验，并进行了站立能力评估。这三项试验被叫做STANDING流程，是近些年来新提出的临床检测中枢性急性眩晕的结构化算法，在一些研究中表现出较高的灵敏度[1]。

![](research_career/MSc_FYP/attachments/label_distribution.png)
<center>Fig 1. 患者诊断结果分布</center>


235例急性眩晕患者中，前庭炎占比192例(81.7%)，脑卒中占比43例(18.3%)。

## 使用STANDING流程对235例患者进行外周性或中枢性检测


### STANDING流程


![](research_career/MSc_FYP/attachments/STANDING.drawio.svg)
<center>Fig 2. STANDIN流程图，根据我们数据的改版</center>

根据STANDING流程我们设计了针对我们数据来源的STANDING流程改版，首先，进行眼震检查，分为两个项目，SN（Spontaneous Nystagmus 自发性眼震）和GEN（Gaze-evoked Nystagmus 凝视诱发性眼震）;可以得到的眼震模式分为 H-SN，UD-GEN，V-SN，D-GEN或者没有眼震（Absent）；
这些眼震模式的含义如下所示：

* H: Horizonal 水平方向
* V: Vertical 垂直方向
* D: Direction 方向性 (眼震的快相方向与注视方向一致，注视向右时，眼震的快相向右；注视向左时，眼震的快相向左)
* UD: Uni-Direction 单一方向性 (凝视性眼震中，眼震快相方向与注视方向无关，保持一致)

其中H-SN和UD-GEN眼震模式可能是由于外周性或中枢性原因导致，需要通过头脉冲试验进一步确认；如果头脉冲试验阳性则表明患者由于外周性原因导致的眩晕，常常因为前庭炎，头脉冲阴性则指向中枢性眩晕原因，通常为中风。

如果出现V-SN或D-GEN模式，则患者大概率为中枢性眩晕；

没有眼震的患者需要进行站立评估，如果共济失调评估等级在2级以上，则指向中枢性眩晕原因

### 眼震模式分布


![](research_career/MSc_FYP/attachments/Nystagmus_pattern_with_label.png)
<center>Fig 3. 眼震模式分布</center>


![](research_career/MSc_FYP/attachments/HIT_distribution_with_pattern.png)
<center>Fig 4. 不同眼震模式下</center>


按照眼震模式区分，235例患者大部分表现为水平性自发性眼震和单一方向性的凝视性眼震。可以看到按照流程走，在眼震模式下具备中枢性特征的D-GEN，V-SN都被检测到卒中，敏感度达到100%。STANDING流程主要在


## Reference

[1] Vanni, S., et al. “STANDING, a Four-Step Bedside Algorithm for Differential Diagnosis of Acute Vertigo in the Emergency Department.” _Acta Otorhinolaryngologica Italica: Organo Ufficiale Della Societa Italiana Di Otorinolaringologia E Chirurgia Cervico-Facciale_, vol. 34, no. 6, Dec. 2014, pp. 419–26.

