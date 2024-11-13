---
title: iPhone ARKit Framework VOG角度矫正实验
tags:
  - FYP
  - pHINTS
  - calibration
  - math
date: 2024-11-13
---

## 实验背景

眼球运动异常可在多种神经系统疾病中观察到，尤其在头晕和眩晕患者中，床边的HINTS试验（头脉冲试验，眼震试验，偏斜试验）比MRI更为敏感。尽管在临床环境中做HINTS实验有诸多好处，如何测量眼动信号存在障碍。传统的床边的HINTS试验（cHINTS，clinical-HINTS 即通过专业人员操作进行人眼观察），需要专业人员操作和用专业知识进行解释，同时因为缺乏定量的眼动信号测量方法，对于一部分患者无法得出有意义的临床结论甚至漏判[1]，使用专业设备VOG目镜进行眼动信号定量测量的vHINT（video-HINTS）试验在准确度、敏感性和特异性上都有着较大的提升，Athanasia Korda[2]通过评估46名AVS(acute vestibular syndrome, 急性前庭综合症状)患者，得到了cHINT和vHINT试验在临床检测效果的对比，如Table 1所示。

<center>Table 1. cHINT vs. vHINT</center>

<table class="tg"><thead>
  <tr>
    <th class="tg-0pky">Exp Type</th>
    <th class="tg-0pky">Accuracy</th>
    <th class="tg-0pky">Sensitivity</th>
    <th class="tg-0pky">Specificity</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0pky">cHINT</td>
    <td class="tg-0pky">88.3%</td>
    <td class="tg-0pky">90.9%</td>
    <td class="tg-0pky">85.7%</td>
  </tr>
  <tr>
    <td class="tg-0pky">vHINT</td>
    <td class="tg-0pky">94.2%</td>
    <td class="tg-0pky">100%</td>
    <td class="tg-0pky">88.9%</td>
  </tr>
</tbody>
</table>

vHINT试验在准确度和敏感性上相较于传统的cHINT都有较大的提升。但是由于高昂的成本，配置的要求复杂等原因，商用眼动分析仪，即VOG目镜并没有在各种临床环境中普及，尤其是急症室和初级保健室。

随着苹果发布ARKit、一款通过前置深度摄像头追踪和头动和眼动的框架，使用智能手机代替VOG目镜进行HINTS试验的方案进入研究视野。

我们以HINTS试验中的头脉冲试验（HIT，Head Impulse Test）为例。HIT试验的主要目的在于识别患者是否发生扫视，同时可以计算“前庭眼反射增益”这个指标来辅助判断。如，Georgios Mantokoudis[3]的研究表明前庭眼反射增益在临床指标中可以帮助医生做出判断，包括区分小脑后下动脉中风和前庭神经炎，区分正常人和前庭受损患者等应用。同样的，HINTS试验中的眼震试验中，也需要计算眼震速度，眼震增益来指导医生进行临床诊断[4]。

目前进行vHIT试验的商用设备使用的VOG算法为2D feature mapping，其准确度据A.J. Larrazabal统计，根据具体使用的方法不同，在0.38°-5°之间[1]。

T. Maxwell Parker[5]通过12名正常人的眼动测量试验评估过手机进行眼动角度测量的准确度，平均误差在23%，精度在1.3°，且在25°测量时，误差达到了10°，但是结果具备重复性并且与临床的商用设备测量的数据之间具有一致性。同时，T.Maxwell Parker[6]还通过11名患者进行手机测量的HIT试验，得到了其中10名患者的手机算出来的增益数据和商用设备测算的增益数据具备高度相关性（Pearson’s r = 0.9, p = 0.0000001）

T.Maxwell Parker的研究目前还停留在手机眼动数据有效性的验证上，没有建立起来关于手机测算HINTS试验的临床指标和商用设备临床指标之间的关系转化，因此是不可用的。我们的实验目的是找到iPhone ARKit Framework测算眼动数据向真实值进行校准的校准曲线，为后续开展手机测量HINTS实验中临床指标的计算打下基础。

## 实验设置

实验中，为了确定用户的眼动角度，将被试在距离该目标1m外的椅子上，让用户保持头部面向中中心不动，眼睛注视目标红点。红点开始时在中间，而后会在5s后发出一声“滴”提醒后，向右面开始移动，5 度（8.75 厘米）、10 度（17.5 厘米）、15 度（26.25 厘米）和 25 度（43.75 厘米），然后回到中间，紧急着会向左移动5度，10度，15度和25度，每次红点变换都会发出一声“滴”进行提醒。

红点的控制由一个动画程序控制，可以调节点的显示时间，点的大小和上下位置和目标视线平视。

![](research_career/MSc_FYP/attachments/image-20241104161106546.png)

![](research_career/MSc_FYP/attachments/image-20241104161112064.png)

<center>Fig 1. 一个控制红点的程序</center>

![](research_career/MSc_FYP/attachments/d399e5d96059d6549ca881aee779dc7f.png)

<center>Fig 2. 红点距离和角度的关系</center>



在被试前15cm-25cm处，我们使用一个在 iPhone 12 mini上运行的 ARKit 应用程序，使用红外和自然光摄像头和传感器的前置组合，以每秒 60 个样本的速度连续记录眼睛和头部位置。



## 实验过程

我们收集了12名健康被试参与实验，被试年龄在20-30岁之间，每人重复该实验三次。

## 实验数据与处理

每个人实验重复三次，得到的数据如下类似：

![](research_career/MSc_FYP/attachments/image-20241104162911680.png)

<center>Fig 3. 收集目标角度的信号序列</center>

实验信号阶段状，眼动的目标角度从0° -> 5° -> 10° -> 15° -> 25° -> 0° -> -5° -> -10° -> -15° -> -25°。第一步我们通过选择起始索引和结束索引不同的角度的阶段的信号范围并记录下来，

以角度25°为例，信号有异常值波动和锯齿状眼震，我们使用IQR法进行数据清洗，即通过计算上下四分位数Q1，Q2计算四分位距IQR定义可接受的数据范围为[Q1 - 0.2× IQR, Q3 + 0.2 × IQR]。

![](research_career/MSc_FYP/attachments/image-20241104163053875.png)

<center>Fig 4. 某个被试眼动角度为25°时的信号</center>



数据清洗后，我们再计算该数据段的平均值、中位数、最大值、最小值、上下四分位数等统计学数据，从而我们利用这些统计学数据，我们可以得到在某个角度时，多次实验下在该角度的箱型图。

![](research_career/MSc_FYP/attachments/image-20241104164424018.png)

<center>Fig 5. 被试SL在三次实验中在注视-25°时得到的实际测量到的角度值</center>



### 实验可重复性分析



为了验证Apple ARKit Framework测量眼动信号的可重复性，我们引入了变异系数这个参数，
$$
CV = (\frac{SD}{\bar{x}}) \times 100\%
$$
即标准差除以平均数。变异系数越大，表示数据的稳定性越差；变异系数越小，表示数据的稳定性越好，即该实验的可重复性好。

我们将每次实验目标角度收集到的信号序列的平均值或中值为这个目标角度下我们实际测得的角度，每个人我们进行了3次实验，其中一名wdy被试进行了10次实验。我们可以得到一张关于不同实验被试在不同角度实验下该系统的变异系数热值图，该热图中我们使用平均值表示目标角度时我们实际测量得到的角度


![](research_career/MSc_FYP/attachments/User_Stability_Mean.png)

<center>Fig 6. 不同实验患者不同角度测量时系统的稳定性评估热图，使用平均值</center>

变异系数在15%以下一般认为数据是稳定的，我们将相同角度下每个人的变异系数做平均，得到每个角度下该系统的稳定性评估。

![](research_career/MSc_FYP/attachments/platform_cv_comparison.png)

<center>Fig 7. 不同角度下变异系数</center>

结合个体的变异系数热图和不同角度的变异系数，我们可以得出，该系统在角度 > 10的时候的稳定性良好，具备矫正的条件，在低角度时，有的实验个体展现了很强的不确定性。

### 眼动角度校准

校准方法我们使用回归拟合，尝试使用线性拟合和多项式拟合，并对个体进行个性化校准和对全体进行校准，得到的结果如下：

![](research_career/MSc_FYP/attachments/polynomial_comparison.png)

<center>Fig 8. 针对单个人个性化校准的结果</center>



从左到右，从上到下，前四张为线性和二次、三次及四次多项式的校准曲线，第五张为校准前后的error，第六张为Bland-Altman Plot，表明校准值和实际值之间具有一致性。

针对所有人的校准误差分析我们使用五折交叉验证，结果如下图和表：

![](research_career/MSc_FYP/attachments/cv_fold_3.png)

<center>Fig 9. 五折交叉验证下不同阶数的校准拟合曲线结果</center>

<center>Table 2. 校准前后训练集和测试集误差</center>

<table>
    <thead>
        <tr>
            <th>多项式阶数</th>
            <th>训练集误差</th>
            <th>测试集误差</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>原始误差</td>
            <td>5.86° ± 3.17°</td>
            <td>5.54° ± 3.25°</td>
        </tr>
        <tr>
            <td>一阶多项式</td>
            <td>2.33° ± 1.81°</td>
            <td>2.62° ± 1.87°</td>
        </tr>
        <tr>
            <td>二阶多项式</td>
            <td>2.33° ± 1.81°</td>
            <td>2.62° ± 1.87°</td>
        </tr>
        <tr>
            <td>三阶多项式</td>
            <td>1.92° ± 1.51°</td>
            <td>1.91° ± 1.67°</td>
        </tr>
        <tr>
            <td>四阶多项式</td>
            <td>1.92° ± 1.50°</td>
            <td>1.90° ± 1.65°</td>
        </tr>
    </tbody>
</table>



## 讨论

我们的实验中，Apple ARKit Framework测量眼动角度的平均误差在5.54° ± 3.25°，即准确度在5.54度，精度在3.25度，不符合计算临床指标的标准。在校准后，在针对所有人的误差进行统一校准的算法中，平均误差可以达到1.90° ± 1.65°，即准确度在1.90°，进度在1.65°，达到目前商用设备的中后段的性能。针对个人进行个性化校准更符合目前手机端的眼动算法[1]，其误差范围在1.07°±0.82°，准确度为1.07°，精度为0.82°，其性能达到商用设备的前半段水平。

<center>Table 3. 准确度和精度比较</center>

| 临床指标计算需要的准确度和精度 | 商用设备的准确度 | iPhone准确度和精度(校准前) | iPhone准确度和精度(整体校准) | iPhone准确度和精度(个性化校准) |
| ------------------------------ | ---------------- | -------------------------- | ---------------------------- | ------------------------------ |
| ×                              | 0.32°-5°         | 5.86° ± 3.17°              | 1.90° ± 1.65°                | 1.07°± 0.82°                   |



## Reference

[1] Larrazabal, A. J., et al. “Video-Oculography Eye Tracking towards Clinical Applications: A Review.” *Computers in Biology and Medicine*, vol. 108, May 2019, pp. 57–66. *DOI.org (Crossref)*, https://doi.org/10.1016/j.compbiomed.2019.03.025.

[2] Korda, Athanasia, et al. “Videooculography ‘HINTS’ in Acute Vestibular Syndrome: A Prospective Study.” *Frontiers in Neurology*, vol. 13, July 2022, p. 920357. *DOI.org (Crossref)*, https://doi.org/10.3389/fneur.2022.920357.

[3] Mantokoudis, Georgios, et al. “Impact of Artifacts on VOR Gain Measures by Video-Oculography in the Acute Vestibular Syndrome.” *Journal of Vestibular Research: Equilibrium & Orientation*, vol. 26, no. 4, Nov. 2016, pp. 375–85. *PubMed*, https://doi.org/10.3233/VES-160587.

[4] Lee, Dong-Han, et al. “Objective Measurement of HINTS (Head Impulse, Nystagmus, Test of Skew) in Peripheral Vestibulopathy.” *Auris Nasus Larynx*, vol. 49, no. 6, Dec. 2022, pp. 938–49. *ScienceDirect*, https://doi.org/10.1016/j.anl.2022.03.003.

[5] Parker, T. Maxwell, et al. “Eye and Head Movement Recordings Using Smartphones for Telemedicine Applications: Measurements of Accuracy and Precision.” *Frontiers in Neurology*, vol. 13, Mar. 2022, p. 789581. *DOI.org (Crossref)*, https://doi.org/10.3389/fneur.2022.789581.

[6] Parker, T. Maxwell, et al. “Proof of Concept for an ‘eyePhone’ App to Measure Video Head Impulses.” *Digital Biomarkers*, vol. 5, no. 1, Dec. 2020, pp. 1–8. *DOI.org (Crossref)*, https://doi.org/10.1159/000511287.