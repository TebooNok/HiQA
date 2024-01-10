# AEC-Q100 可靠性认证报告
产品名称： CA-IF1051XX-Q1
版 本： A1 
参考标准： AEC-Q100-REV-H


# 1. 概述
川土微电子产品的质量与可靠性测试是一个风险缓解过程，旨在确保设备在客户应用中的使用寿命。半导体
晶圆制造工艺和封装级可靠性的评估方法多种多样，可能包括加速环境试验条件，随后降低到实际使用条
件。芯片的可制造性评估包括验证稳健的装配流程，产品生产的连续性，确保供货能力。根据汽车电子委员
会（AEC）标准和程序，川土微电子的产品评估符合行业标准测试方法。


# 2 .系列群族产品料号表
群族系列 CA-IF1051XX
封装类型 SOIC8-NB(S)
产品料号 CA-IF1051S-Q1/CA-IF1051VS-Q1
备注：根据 AEC-Q100 附录 1 规范, 相同 Fab 工厂、Fab 工艺、相同的封装工厂、封装工艺生产的料号可以
使用相似的通用数据进行认证。


# 3. 产品信息表
# 3.1. 产品 Fab 基本信息
晶圆工厂 DH HiTek
晶圆名称 Saturn
晶圆工艺 BCDXXX

# 3.2. 产品封装基本信息
封装厂 UNIMOS
测试厂 UNIMOS
封装形式 SOIC8 (S)
Lead Frame Cu
Bond wire 20um Au
湿敏等级 MSL3
工作温度等级 Grade 1 (-40℃ - 125℃)


# 4. 产品可靠性认证计划
 Test Group A – Accelerated Environment Stress Tests
A1** PC J-STD-020
JESD22-A113
Preconditioning:** (Test @ Rm)
SMD only; Moisture Preconditioning for 
THB/HAST, AC/UHST, TC, &PTC; Peak Reflow 
Temp =260℃
Min. MSL = 3
A2** THB/BHAST JESD22-A101
JESD22-A110
THB:** 85℃, 85%RH 1000hrs. (Test @ 
Rm/Hot)
BHAST:** 130℃, 85%RH 96hrs. (Test @ 
Rm/Hot)
3*77pcs

A3** AC/TH/UHAST
JESD22-A102
JESD22-A118
JESD22-A101
TH:** 85℃, 85%RH 1000hrs. (Test @ Rm)
UHAST:** 130℃, 85%RH 96hrs. (Test @ Rm)
3*77pcs

A4** TC JESD22-A104
TC:** -65℃-150℃, 500cycles (Test @Rm/ Hot)
3*77pcs

A5** PTC JESD22-A105
PTC:** -65℃-125℃, 1000cycles (Test @ 
Rm/Hot)
NA Not Applicable

A6** HTSL JESD22-A103
HTSL:** Ta=150℃, 1000hrs (Test @ Rm/Hot)
1*45pcs

Test Group B – Accelerated Lifetime Simulation Tests

B1** HTOL JESD22-A108
HTOL:** Ta=125℃, Vcc=5V, 1000hrs (Test @ 
Rm/Cold/Hot)
3*77pcs

B2** ELFR AEC-Q100-008
ELFR:** Ta=125℃, Vcc=5V, 48hrs (Test @ 
Rm/Hot)
3*800pcs

B3** EDR AEC-Q100-005
EDR:** (Test @ Rm/Hot)
NA Not Applicable

 Group C – Package Assembly Integrity Tests

C1** WBS AEC-Q100-001
AEC-Q003 Wire Bond Shear Test: (Cpk > 1.67) 30wire from 5pcs

C2** WBP MIL-STD883
AEC-Q003 Wire Bond Pull: (Cpk > 1.67); Each bonder 
used 30wire from 5pcs

C3** SD JESD22-B102
JSTD-002D Solderability: (>95% coverage) 8hr steam 
aging prior to testing 1*15pcs

C4** PD JESD22-B100
JESD22-B108 AEC-Q003 Physical Dimensions: (Cpk > 1.67) 3*10pcs

C5** SBS AEC-Q100-010 
AEC-Q003 Solder Ball Shear: (Cpk > 1.67); 5
balls from min. of 10 devices NA Not Applicable

C6** LI JESD22 B105
Lead Integrity: (No lead cracking or 
breaking); Through-hole only; 10 leads from 
each of 5 devices
NA Not Applicable

Test Group D – Die Fabrication Reliability Tests

D1** EM JESD61 Electromigration

D2** TDDB JESD35 Time Dependent Dielectric Breakdown

D3** HCI JESD60 & 28 Hot Carrier Injection

D4** NBTI JESD90 Negative Bias Temperature Instability

D5** SM JESD61, 87, & 202 Stress Migration

Group E- Electrical Verification

E1** TEST per datasheet Pre and Post Stress Electrical Test: all

E2** HBM AEC Q100-002
HBM:** 500V, 1KV, 2KV, 6KV (Test @ Rm/Hot); 3pcs/voltage 
level

E3** CDM AEC-Q100-011
CDM:** 250V, 500V, 750V, 1KV, 2KV (Test @ Rm/Hot); 
3pcs/voltage 
level

E4** LU AEC-Q100-004
Latch-Up:** (Test @ Rm/Hot) 1*6pcs

E9** EMC SAE J1752/3
Electromagnetic Compatibility (Radiated 
Emissions) 1*1pcs


# 5. 产品可靠性测试结果
 Test Group A – Accelerated Environment Stress Tests

A1** PC MSL 3 Min. MSL = 3
- DUC12151E Pass
- DUC12152E Pass
- DUC12153E Pass

A2** BHAST 130℃, 85%RH 96hrs. Vcc=5V 3*77pcs
- DUC12151E Pass
- DUC12152E Pass
- DUC12153E Pass

A3** UHAST 130℃, 85%RH 96hrs. 3*77pcs
- DUC12151E Pass
- DUC12152E Pass
- DUC12153E Pass

A4** TC -65℃-150℃, 500cycles 3*77pcs
- DUC12151E Pass
- DUC12152E Pass
- DUC12153E Pass

A6** HTSL Ta=150℃, 1000hrs 1*45pcs
- DUC12151E Pass

Test Group B – Accelerated Lifetime Simulation Tests

B1** HTOL Ta=125℃, 1000hrs, Vcc=5V, TTL 信号输入, F=100KHZ. 3*77pcs
- DUC12151E Pass
- DUC12152E Pass
- DUC12153E Pass

B2** ELFR ELFR: Ta=125℃, Vcc=5V, 48hrs (Test @ Rm/Hot) 3*800pcs
- DUC12151E Pass
- DUC12152E Pass
- DUC12153E Pass

##Group C – Package Assembly Integrity Tests

C1** WBS Wire Bond Shear Test: (Cpk > 1.67) 30wire from 5pcs
- DUC12151E Pass, CPK=2.71

C2** WBP Wire Bond Pull: (Cpk > 1.67); Each bonder used 30wire from 5pcs
- DUC12151E Pass, CPK=3.16

C3** SD Solderability: (>95% coverage) 8hr steam aging prior to testing 1*15pcs
- DUC12151E Pass

C4** PD Physical Dimensions: (Cpk > 1.67) 3*10pcs
- DUC12151E Pass
- DUC12152E Pass
- DUC12153E Pass

TEST GROUP D – Die Fabrication Reliability Tests

D1** EM Electromigration
- The Die Fabrication Reliability Tests are carried out for every fabrication site. The data, test method, calculations and internal criterial is available to the customer upon request.

D2** TDDB Time Dependant Dielectric Breakdown

D3** HCI Hot Carrier Injection

D4** NBTI Negative Bias Temperature Instability
D5** SM Stress Migration

Group E- Electrical Verification

E1** TEST Pre and Post Stress Electrical Test: all all Pass

E2** HBM HBM: 500V,1KV,2KV,6KV (Test @ Rm/Hot); 3pcs/voltage level
- DUC12151E Pass 6KV class 3A

E3** CDM CDM: 250V,500V,750V,1KV,2KV(Test @ Rm/Hot); 3pcs/voltage level
- DUC12151E Pass 2KV class C6

E4** LU Latch-Up: (Test @ Rm/Hot) 1*6pcs
- DUC12151E Pass, classⅡA

E9** EMC Electromagnetic Compatibility (Radiated Emissions) 1*1pcs
- DUC12151E 参考附录 1


# 6. MTBF&FIT
 支撑数据
---table begin---
Table tile:CA-IF1051XX-Q1支撑数据表
| MTBF(Hrs.) | FIT | 实验温度 | 实验电压 | 实验时间 | 样本数量 | 故障数量 | 使用温度 | 使用电压 | 活化能（eV) | 置信度 |
|------------|-----|----------|---------|----------|----------|---------|----------|----------|-------------|--------|
| 1.61E+08   | 6.20 | 125℃ | 5V | 1000hrs | 231 | 0 | 55℃ | 3.3V | 0.7 | 60% |
|            |      | 125℃ | 5V | 48hrs | 2400 | 0 | 55℃ | 3.3V | 0.7 | 60% |
---table end---



# 7. 结论
以上测试项目遵循 AEC-Q100 测试规范，CA-IF1051XX 系列产品满足所有相关可靠性测试要求，结果全部通
过，满足可靠性测试认证要求。


# 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知的情况下，保
留因技术革新而改变上述资料的权利。
Chipanalog 产品全部经过出厂测试。针对具体的实际应用，客户需负责自行评估，并确定是否适用。Chipanalog
对客户使用所述资源的授权仅限于开发所涉及 Chipanalog 产品的相关应用。 除此之外不得复制或展示所述资源，
如因使用所述资源而产生任何索赔、赔偿、成本、损失及债务等，Chipanalog 对此概不负责。


# 商标信息
Chipanalog Inc.®、Chipanalog®为 Chipanalog 的注册商标。


# 附录 1 ：EMC 测试结果
