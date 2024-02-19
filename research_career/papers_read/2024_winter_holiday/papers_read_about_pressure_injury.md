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
* 该文章使用的方法：评估了MIMIC-III数据库中的临床记录、诊断代码(diagnosis code)、程序代码和图表事件中记录的 HAPI 事件之间的一致性。我们分析了 3 个现有 HAPI 定义所使用w的标准及其对监管指南的遵守情况。提出了Emory HAPI（EHAPI），这是一个改进的、更全面的HAPI定义。然后，我们使用基于树的顺序神经网络分类器评估了标签在训练 HAPI 分类模型中的重要性。
* 最终，文章说明了定义 HAPI 的复杂性，<13% 的住院患者在 4 个数据源中记录了至少 3 个 PI 指征。尽管图表事件是最常见的指标，但它是超过 49% 的停留时间的唯一 PI 文档。我们证明现有 HAPI 定义和 EHAPI 之间缺乏一致性，只有 219 个具有一致的正面标签。我们的分析强调了改进的 HAPI 定义的重要性，使用我们的标签训练的分类器优于护士标注和consensus set(既存在任何PI证据都会标注为阳性)

> [!abstract] 
> 因为HAPI的定义不统一，文章通过使用大量不同EHR来源的数据重现制定HAPI分类的定义并提出EHAPI。通过EHAPI训练分类器会具有更好的性能 。


### Tech Detail

* Center for Medicare and Medicaid(CMS) and Healthcare Research and Quality(AHRQ)认为 HAPI 是“绝不会发生的事件”，即对医疗服务提供者造成严重经济处罚的事件。
* 国家压力性损伤咨询小组 (National Pressure Injury Advisory Panel, NPIAP) 参考指南将设施获得率(facility-acquired)定义为“入院时未发生压力性损伤但在机构逗留期间发生压力性损伤的个体的百分比”。
* Data Sources for PI in Hospital Stays
	* **Chart Events**
		* "chart events"（图表事件）是指医疗记录中的时间序列数据，用于描述患者在医院期间的各种观测值、监测值和测量值。
		* "chart events"包括了多个类别的数据，如生理参数（如血压、心率、体温等）、实验室检查结果（如血液、尿液、生化检验、血药浓度等）、药物治疗（如药物剂量、给药途径等）等等。这些数据通过定期或不定期的观测、监测和测量获得，以在医疗记录中反映患者的病情和生理状态。
	* **Notes**
		* "notes"（笔记）是指医疗记录中的文字描述，其中包含了医生、护士或其他医疗专业人员对患者的病情、治疗方案、手术过程、医嘱等进行详细记录的文本。
		* MIMIC-III数据库中的"notes"包括了各种类型的文本记录，如护理记录、病历摘要、手术报告、放射学报告、心电图诊断、社交史、家族史、既往史等。这些文本记录可提供丰富的信息，包括患者病情发展、诊断过程、治疗决策以及诊疗方案的执行情况等。
	* **Diagnosis Codes**
		* "diagnosis codes"（诊断代码）用于描述患者的疾病诊断，并提供了一种标准化的分类方法。诊断代码通常使用国际分类系统（如ICD-9-CM或ICD-10-CM）提供，并用于追踪、记录和统计患者的诊断信息。
		* MIMIC-III数据库中的诊断代码包括了多种类型的诊断，如主要诊断、次要诊断、手术前诊断等。这些诊断代码能够提供对患者诊断情况的细致描述，包括疾病的类型、严重程度以及可能的并发症等。
	* **Procedure Codes**
		* Procedure Codes（手术代码）是用于描述患者接受的医疗过程或手术的分类标识符。这些代码用于记录患者在医疗过程中所接受的各种医疗和外科手术。手术代码通常由医学编码系统（比如ICD-9-CM或ICD-10-PCS）提供，并用于追踪和统计特定类型的医疗操作。
		* 在MIMIC-III数据库中，Procedure Codes可用于分析和研究多个方面，例如手术类型、手术风险、手术后并发症等。
* Ideal HAPI Criteria Based on Guidelines
	* CMS provides several inclusion and exclusion criteria for HAPI
		* 一项纳入标准是与入院相比，出院时存在一项或多项新的或恶化的 PI。
		* 一项纳入标准是，unstageable PI -> staged
		* 出院评估中缺少新的或恶化的 2、3 和 4 期或不可分期压疮（包括深部组织损伤）的数据，则为exclusion
		* 患者死亡也被记为exclusion
* Existing MIMIC-III HAPI Case Definitions and Their Limitations
	
| Existing Methods for Definitions | Limitations | Reference |
| ---- | ---- | ---- |
| Recurrent additive network for temporal risk prediction(CANTRIP), 专注于预测 HAPI 首次出现 之前 48 至 96 小时或事件日期 (data of event, **DOE**) ,既入院后 48 小时以上首次在带时间戳的医院记录中提及 PI 相关关键词或 PI 分期图事件（≥ 1 期）。没有DOE的数据会被当做对照组 | 该研究中包括已故患者和治愈和改善的患者 | 10.1093/jamia/ocaa004 |
| Cramer 等人试图利用前 24 小时的数据开发一种 PI 筛查工具。他们仅**使用入院 24 小时后发生的 PI 分期图事件来识别 HAPI 病例**。 | 它排除了 1 期 PI 以及“无法分期”和深部组织损伤 PI。与 CANTRIP 类似，Cramer 病例定义包括已故患者和治愈或改善的 PI。 | 10.5334/egems.307 |
| Sotoodeh 等人探索了对临床文本使用否定预处理来检测 PI。病例患者是**使用国际疾病分类 (ICD)-9 代码或临床记录中 PI 特定关键字**来定义的。 | 死亡、治愈或改善的 PI 包含在病例定义;同时，没有考虑PI staging chart events | https://europepmc.org/abstract/MED/33936492 |
| ... | ... | ... |
* **EHAPI Case Definition in MIMIC-III** *Paper's Key Section*
	* 