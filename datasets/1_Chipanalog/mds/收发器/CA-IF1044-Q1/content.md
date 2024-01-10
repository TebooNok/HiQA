# CA-IF1044-Q1 具有待机模式的汽车级 CAN 收发器

# 1. 产品特性
• 符合 ISO 11898-2:2016 和 ISO 11898-5:2007 物理层
标准
• 所有器件均支持经典 CAN 和 5Mbps CAN FD（灵活
数据速率）
• 工作模式
- 常规模式
- 低功耗待机模式，支持远程唤醒请求
• 未上电时的理想无源特性
- 总线和逻辑引脚处于高阻态（无负载）
- 上电和掉电时总线和 RXD 输出上无毛刺脉冲
• VIO 支持 3.0V 到 5.5V
• 保护 特性
- 总线故障保护：±58 V
- VCC 和 VIO 电源引脚上具有欠压保护
- 驱动器显性超时 (TXD DTO) - 数据速率低至
4kbps
- 热关断保护 (TSD)
• 接收器共模输入电压：±30 V
• 典型循环延迟：160ns
• 结温范围：-55°C 至 150°C
• 可提供 SOIC8 封装和无引线 DFN8 封装(3.0mm x
3.0mm)
• 通过 AEC-Q100 车规认证：
- 工作环境温度范围 Grade 1：-40℃~125℃


# 2. 应用
• 车身控制模块
• 汽车网关
• 高级驾驶辅助系统(ADAS)
• 信息娱乐系统


# 3. 概述
该 CAN 收发器系列符合 ISO11898-2 (2016) 高速 CAN（控
制器局域网络）物理层标准。所有器件均设计用于数据
速率高达 5Mbps（兆位每秒）的 CAN FD 网络。CAIF1044 收发器具有低功耗待机模式，支持 ISO 11898-
2:2016 定义的唤醒序列。CA-IF1044V 包含 VIO 电压，其
内部的逻辑电平转换支持收发器接口直接连接 3.3V 或
者 5V 逻辑电平。该器件支持总线故障保护电压±58V，
包含许多保护功能，如热关断，TXD 显性超时保护和电
源欠压保护，以提高器件和 CAN 的稳定性。
表 3-1 器件信息
零件号、封装和封装尺寸
---table begin---
Table tile:CA-IF1044-Q1零件号、封装和封装尺寸表
| 零件号            | 封装        | 封装尺寸(标称值) |
| ----------------- | ----------- | --------------- |
| CA-IF1044S-Q1     | SOIC8       | 4.9mm x 3.9mm   |
| CA-IF1044VS-Q1    | SOIC8       | 4.9mm x 3.9mm   |
| CA-IF1044D-Q1     | DFN8        | 3.0mm x 3.0mm   |
| CA-IF1044VD-Q1    | DFN8        | 3.0mm x 3.0mm   |
---table end---



# 4. 订购指南
表 4-1 有效订购零件编号
型号、封装和封装尺寸
---table begin---
Table tile:CA-IF1044-Q1有效订购零件编号表
| 型号            | 封装        | 封装尺寸       |
| --------------- | ----------- | -------------- |
| CA-IF1044S-Q1   | SOIC8       | 4.9mm x 3.9mm  |
| CA-IF1044VS-Q1  | SOIC8       | 4.9mm x 3.9mm  |
| CA-IF1044D-Q1   | DFN8        | 3.0mm x 3.0mm  |
| CA-IF1044VD-Q1  | DFN8        | 3.0mm x 3.0mm  |
---table end---



# 5. 引脚功能描述
表 5-1 CA-IF1044-Q1 引脚功能描述
---table begin---
Table tile:CA-IF1044-Q1引脚功能描述表
| 引脚名称 | 引脚编号 | 类型     | 描述 |
|---------|--------|---------|-----|
| TXD     | 1      | 输入   | 传输数据输入。TXD 为高 CAN 总线输出为隐性态，TXD 为低 CAN 总线输出为显性态。内部具有上拉电阻。|
| GND     | 2      | 地     | 参考地。|
| VCC     | 3      | 电源   | 电源输入。在 VCC和 GND 之间接入一个 0.1uF 电容尽量的靠近器件。|
| RXD     | 4      | 输出   | 接收器数据输出。当 CAN 总线处于隐性态时，RXD 为高电平。当 CAN 总线处于显性态时，RXD 为低电平。RXD 的参考电源为 VIO。|
| NC(CA-IF1044) | 5 | NC     | NC |
| VIO(CA-IF1044V) | 5 | 电源 | 逻辑电平侧电源 |
| CANL     | 6      | 输入输出 | 低电平 CAN 总线。|
| CANH     | 7      | 输入输出 | 高电平 CAN 总线。|
| STB      | 8      | 输入   | 待机模式控制管脚。STB 为高，待机模式；STB 为低，常规模式。内部具有上拉电阻。|
---table end---

# 6. 产品规格
# 6.1. 绝对最大额定值
表 6-1 绝对最大额定值
参数范围
---table begin---
Table tile:CA-IF1044-Q1绝对最大额定值表
| 参数              | 最小值 | 最大值 | 单位 |
| ----------------- | ------ | ------ | ---- |
| VCC               | -0.3   | 7      | V    |
| VIO               | -0.3   | 7      | V    |
| VBUS              | -58    | 58     | V    |
| V(DIFF)           | -58    | 58     | V    |
| V(Logic_Input)    | -0.3   | +7     | V    |
| V(Logic_Output)   | -0.3   | +7     | V    |
| IO (RXD)          | -8     | 8      | mA   |
| TJ                | -55    | 150    | ℃    |
| TSTG              | -65    | 150    | ℃    |
备注：
1. 等于或超出上述绝对最大额定值可能会导致产品永久性损坏。这只是额定最值，并不能以这些条件或者在任何其它超出本技术规范操作章节中所示规格的条件下，推断产品能否正常工作。长期在超出最大额定值条件下工作会影响产品的可靠性。
---table end---


# 6.2. ESD 额定值
表 6-2 ESD 额定值
 测试项目与条件
---table begin---
Table tile:CA-IF1044-Q1测试项目与条件表
| 测试项目                | 测试条件                                                  | 数值   | 单位 |
| ----------------------- | --------------------------------------------------------- | ------ | ---- |
| CA-IF1044S，CA-IF1044D   |                                                           |        |      |
| HBM1 ESD                | 人体模型 (HBM)，所有引脚，根据 AEC-Q100-0021 HBM ESD 认证标准 3A | ±6000  | V    |
| 人体模型 (HBM)，CAN 总线端口 (CANH，CANL)到 GND，根据 AEC-Q100-0021 HBM ESD 认证标准 3B | ±8000  | V    |
| CDM ESD                 | 组件充电模式(CDM)，所有管脚，根据 AEC-Q100-011 CDM ESD 认证标准 C3 | ±2000  | V    |
| System Level ESD        | CAN 总线端口（CANH，CANL）到 GND IEC 61000-4-2 : 不上电接触放电 | ±60002 | V    |
备注:
1. AEC Q100-002 规定 HBM 应力应符合 ANSI/ESDA/JEDEC JS-001 规范;
2. 系统板级测试；
---table end---


# 6.3. 建议工作条件
表 6-3 建议工作条件
参数范围
---table begin---
Table tile:CA-IF1044-Q1建议工作条件表
| 参数              | 最小值 | 最大值 | 单位 |
| ----------------- | ------ | ------ | ---- |
| VCC               | 4.5    | 5.5    | V    |
| VIO               | 3.0    | 5.5    | V    |
| IOH (RXD)         | -      | -2     | mA   |
| IOL (RXD)         | 2      | -      | mA   |
---table end---


# 6.4. 热量信息
表 6-4 热量表
 热量表
---table begin---
Table tile:CA-IF1044-Q1热量表
| 封装   | RθJA    | 单位   |
| ------ | ------- | ------ |
| DFN8   | 40      | °C/W   |
| SOIC8  | 170     | °C/W   |
---table end---


# 6.5. 电气特性
建议工作条件下，环境温度 TA=-55℃到 125℃。
表 6-5 电气特性表
参数范围
---table begin---
Table tile:CA-IF1044-Q1参数范围表
| 参数          | 测试条件                                                     | 最小值 | 典型值 | 最大值 | 单位 |
| ------------- | ------------------------------------------------------------ | ------ | ------ | ------ | ---- |
| 电源特性       |                                                              |        |        |        |      |
| Icc           | 5V 电源电流<br>TXD=0V, STB=0V, RL=60 Ohm（显性），如图 7-1 | 45     | 70     |        | mA   |
| Icc           | 5V 电源电流<br>TXD=0V, STB=0V, RL=50 Ohm（显性），如图 7-1 | 50     | 80     |        | mA   |
| Icc           | 5V 电源电流<br>TXD=0V, STB=0V, CANH=-12V（显性），如图 7-1 |        | 130    |        | mA   |
| Icc           | 5V 电源电流<br>TXD=VCC, STB=0V, RL=50 Ohm（隐性），如图 7-1 | 4.5    | 7.5    |        | mA   |
| Icc           | 5V 电源电流<br>TXD=STB=VCC（待机模式, CA-IF1044），RL=50 Ohm，如图 7-1 | 22     | 35     |        | μA   |
| Icc           | 5V 电源电流<br>TXD=STB=VIO（待机模式, CA-IF1044V），RL=50 Ohm，如图 7-1 | 0.5    | 3      |        | μA   |
| IIO（常规模式）| VIO 电源电流（CA-IF1044V）<br>TXD=0V, STB=0V, RXD 悬空（显性） | 125    | 300    |        | μA   |
| IIO（常规模式）| VIO 电源电流（CA-IF1044V）<br>TXD=VCC, STB=0V, RXD 悬空（隐性） | 70     | 150    |        | μA   |
| IIO（待机模式）| VIO 电源电流（CA-IF1044V）<br>TXD=STB=VIO, RXD 悬空          | 20     | 33     |        | μA   |
| Vuv_vcc       | VCC UVLO 电压 上升                                        | 4.2    | 4.45   |        | V    |
| Vuv_vcc       | VCC UVLO 电压 下降                                        | 3.65   | 4.0    | 4.4    | V    |
| Vuv_vcc_sd    | VCC 保护状态电压（CA-IF1044） 上升                           | 1.56   | 1.9    |        | V    |
| Vuv_vcc_sd    | VCC 保护状态电压（CA-IF1044） 下降                           | 1.3    | 1.51   | 1.85   | V    |
| Vuv_vio       | VIO 保护状态电压（CA-IF1044V） 上升                          | 1.56   | 1.9    |        | V    |
| Vuv_vio       | VIO 保护状态电压（CA-IF1044V） 下降                          | 1.3    | 1.51   | 1.85   | V    |
| 逻辑接口(STB) | 输入高电平                                                  | 0.7*VCC |        |        | V    |
| 逻辑接口(STB) | 输入低电平                                                  | 0.3*VCC |        |        | V    |
| 逻辑接口(STB) | 输入高电平漏电流<br>STB=VCC=5.5V                             | -2     | 2      |        | μA   |
| 逻辑接口(STB) | 输入低电平漏电流<br>STB=0V, VCC=5.5V                        | -200   | -100   | -20    | μA   |
| 逻辑接口(STB) | 未上电时漏电流<br>STB=5.5V, VCC=0V                         | -1     | 1      |        | μA   |
| 逻辑接口(TXD) | 输入高电平                                                  | 0.7*VCC |        |        | V    |
| 逻辑接口(TXD) | 输入低电平                                                  | 0.3*VCC |        |        | V    |
| 逻辑接口(TXD) | 输入高电平漏电流<br>TXD=VCC=5.5V                             | -2.5   | 0      | 1      | μA   |
| 逻辑接口(TXD) | 输入低电平漏电流<br>TXD=0V, VCC=5.5V                        | -200   | -100   | -20    | μA   |
| 逻辑接口(TXD) | 未上电时漏电流<br>TXD=5.5V, VCC=0V                         | -1     | 0      | 1      | μA   |
| Ci            | 输入电流<br>Vin=0.4*sin(4E6*π*t)+2.5V                     |        |        | 5      | pF   |
| 逻辑接口(RXD) | 输出高电平<br>Io=-2mA, VIO=3.3V-5.5V                       |        |        | 0.8*VCC | V    |
| 逻辑接口(RXD) | 输出低电平<br>Io=+2mA, VIO=3.3V-5.5V                       |        |        | 0.2*VCC | V    |
| 逻辑接口(RXD) | 未上电时漏电流<br>S=5.5V, VCC=0V                           | -
---table end---


# 6.5.1. 电气特性参数范围
建议工作条件下，环境温度 TA=-55℃到 125℃。
 参数范围
---table begin---
Table tile:CA-IF1044-Q1参数范表
| 参数        | 测试条件                                                     | 最小值 | 典型值 | 最大值 | 单位 |
| ----------- | ------------------------------------------------------------ | ------ | ------ | ------ | ---- |
| V OD(DOM)   | TXD=低，STB=0V,RL=45-70 Ohm , RCM open,如图 7-1           | 1.4    | 3.3    |        | V    |
| V OD(DOM)   | TXD=低，STB=0V,RL=50-65 Ohm , RCM open,如图 7-1           | 1.5    | 3.0    |        | V    |
| V OD(DOM)   | TXD=低，STB=0V,RL=2240 Ohm , RCM open,如图 7-1           | 1.5    | 5.0    |        | V    |
| VO(REC)     | TXD=高，STB=0V,无负载, CANH 端口,如图 7-1                | 2      | 3      |        | V    |
| VO(REC)     | TXD=高，STB=0V,无负载, CANL 端口,如图 7-1                | 2      | 3      |        | V    |
| VOD(REC)    | TXD=高，STB=0V, RL=60 Ohm,如图 7-1                      | -120   | 12     |        | mV   |
| VOD(REC)    | TXD=高，STB=0V, 无负载,如图 7-1                         | -50    | 50     |        | mV   |
| VO(STB)     | 待机模式总线电压<br>STB=VCC, RL open, CANH               | -0.1   | 0.1    |        | V    |
| VO(STB)     | 待机模式总线电压<br>STB=VCC, RL open, CANL               | -0.1   | 0.1    |        | V    |
| VO(STB)     | 待机模式总线电压<br>STB=VCC, RL open, CANH-CANL          | -0.2   | 0.2    |        | V    |
| IOS(SS_DOM) | 短路电流(显性)<br>TXD=低，STB=0V ,CANL 开路，CANH 从-15V 到 40V,如图 7-7 | -115   |        |        | mA   |
| IOS(SS_DOM) | 短路电流(显性)<br>TXD=低，STB=0V ,CANH 开路，CANL 从-15V 到 40V, 如图 7-7 | 115    |        |        | mA   |
| IOS(SS_rec) | 短路电流(隐性)<br>TXD=高，STB=0V ,VBUS 从-27V 到 32V, 如图 7-7 | -6     | 6      |        | mA   |
| Vsys        | 瞬态对称性(显性和隐性)<br>RL=60 Ohm, STB=0V, Csplit=4.7nF, RCM open , Txd=250kHz,1MHz,2.5MHz | 0.9    | 1.1    |        | V/V  |
| Vsys_dc     | DC 对称性(显性和隐性)<br>RL=60 Ohm, STB=0V, RCM open     | -0.4   | 0.4    |        | V    |
| TTSD        | 过温保护                                                     |        |        | 190    | °C   |
| TTSD_HYS    | 过温保护滞回                                                 |        |        | 10     | °C   |
| CAN 接收器   | (TXD=High，CANH/CANL 由外部驱动)                           |        |        |        |      |
| VCM         | 共模输入范围<br>常规模式，RXD 输出有效，如图 7-2           | -30    | 30     |        | V    |
| VCM         | 待机模式，RXD 输出有效，如图 7-2                           | -20    | 20     |        | V    |
| VIT         | 常规模式输入阈值电压<br>STB=0V, Vcm 从 -20V 到 20V, 如图 7-2 | 500    | 900    |        | mV   |
| VIT         | 常规模式输入阈值电压<br>STB=0V, Vcm 从 -30V 到 30V, 如图 7-2 | 400    | 1000   |        | mV   |
| VIT(ST
---table end---


#  6.6. 开关特性
建议工作条件下，环境温度 TA=-55℃到 125℃。
表 6-6 开关特性表
 参数范围
---table begin---
Table tile:CA-IF1044-Q1 参数范围表
| 参数         | 测试条件                                                     | 最小值 | 典型值 | 最大值 | 单位 |
| ------------ | ------------------------------------------------------------ | ------ | ------ | ------ | ---- |
| 驱动器开关特性 |                                                              |        |        |        |      |
| tR           | 总线驱动上升时间<br>STB=0V,RL=60 Ohm, CL=100pF ,如图 7-1   |        |        | 30     | ns   |
| tF           | 总线驱动下降时间<br>STB=0V,RL=60 Ohm, CL=100pF,如图 7-1 |        |        | 50     | ns   |
| tONTXD       | TXD 延迟(隐形到显性)<br>STB=0V,RL=60 Ohm, CL=100pF,如图 7-1 |        |        | 80     | ns   |
| tOFFTXD      | TXD 延迟(显形到隐性)<br>STB=0V,RL=60 Ohm, CL=100pF,如图 7-1 |        |        | 70     | ns   |
| Tsk(p)       | 脉冲偏差<br>STB=0V,RL=60 Ohm, CL=100pF,如图 7-1           |        |        | 20     | ns   |
| tDOM         | TXD 显性超时<br>RL=60 Ohm,CL open,如图 7-5               | 2      | 5      | 8      | ms   |
| 接收器开关特性 |                                                              |        |        |        |      |
| tONRXD       | RXD 延迟(隐形到显性)<br>STB=0V , CRXD=15pF,如图 7-2     |        |        | 65     | ns   |
| tOFFRXD      | RXD 延迟(显形到隐性)<br>STB=0V , CRXD =15pF,如图 7-2     |        |        | 90     | ns   |
| tR           | RXD 驱动上升时间<br>STB=0V , CRXD =15pF,如图 7-2        |        |        | 10     | ns   |
| tF           | RXD 驱动下降时间<br>STB=0V , CRXD =15pF,如图 7-2        |        |        | 10     | ns   |
| 器件开关特性  |                                                              |        |        |        |      |
| tloop1       | 环路延迟时间 隐性到显性<br>RL=60 Ohm,CL=100pF,如图 7-3   | 125    | 210    |        | ns   |
| tloop2       | 环路延迟时间 显性到隐性<br>RL=60 Ohm,CL=100pF,如图 7-3   | 150    | 210    |        | ns   |
| tONTXD       | 模式转换时间 从待机态到常态或者从常态到待机态,如图 7-4    |        | 20     |        | μs   |
| Twk_FILTE    | 有效唤醒的滤波时间 如图 8-4                               | 0.5    | 1.8    |        | μs   |
| TWK_FILTEROUT| 总线唤醒超时 如图 8-4                                     | 0.8    | 6      |        | ms   |
| FD TIMING    | 特性                                                         |        |        |        |      |
| Tbit（bus）  | bit 时间<br>STB=0V ,总线侧 RL=60 Ohm,CL=100pF, CRXD =15pF,如图 7-6 | 450    | 530    |        | ns   |
| Tbit（bus）  | bit 时间<br>STB=0V ,总线侧 RL=60 Ohm,CL=100pF, CRXD =15pF,高速版本 ,如图 7-6 | 155   
---table end---


# 7. 参数测量信息


# 8. 详细说明
具有低功耗待机模式的 CAN 收发器 CA-IF1044 适用于工业网络应用，其 VCC工作电源电压为 5V。CA-IF1044 具有
+/-30V 的共模输入范围，CAN 总线端口(CANH,CANL)支持高达+/-58V 的短路保护，使其能适用于恶劣的工业环境。
器件可以工作在 CAN 的最大传输速率下，允许小型网络传输 5Mbps 数率，最大的传输速率受限于电容负载和一
些其他的因素。
CA-IF1044V 具有双电源供电，其 VIO 电源可与 MCU 共用一个电源，内部电平转换器将低压侧电平转换为 5V VCC
电平。
CANH 和 CANL 具有输出短路保护功能，当过热时，内部的过温保护电路会将驱动输出设为高阻态。
# 8.1. CAN 总线状态
常规模式下 CAN 总线有两种工作状态：显性和隐性，如图 9-1 和 9-2。显性态时，TXD 为低，总线差分输出，RXD
输出为低。隐性态时，TXD 为高，总线被内部电阻偏置到 Vcc/2，RXD 输出为高。
当 STB 置高，芯片会进入低功耗待机模式，这时，总线会被内部电阻偏置到地，如图 9-1 和 9-2。
# 8.2. 发射端显性超时功能
 在常规模式显性状态下，若 CAN 控制器发生错误时候，会将 TXD 一直拉低，总线就会被钳位在显性状态，显性
超时功能则会避免这一状态。显性超时保护被 TXD 的下降沿所触发，当 TXD 处于显性的时间超过 tTXD-DTO时候，发射
器会被关闭，以释放总线到隐性状态。在出现显性超时故障后，发射器可以被 TXD 的上升沿重新使能。发射器的显性
超时功能限制了可能的最低传输速率为 4kbps。
# 8.3. 欠压保护
VCC 和 VIO 电源具有欠压保护功能。
在 CA-IF1044 中，当 VCC 低于 Vuv_vcc_sd 值时，不管 STB 管脚状态如何，芯片进入到保护态。当电源高于
Vuv_vcc_sd 但低于 Vuv_vcc 时，若 STB=GND，保护态；若 STB=VCC，待机模式。当电源高于 Vuv_vcc 时，正常态。
在 CA-IF1044V 中，如果 VIO 电源小于 VUV_VIO，收发器处于保护态。如果 VIO 电源正常而 VCC 欠压，芯片则根据
STB 的电平进入低功耗待机模式或者保护态。
表 8-1 欠压保护状态表(CA-IF1044)
---table begin---
Table tile:CA-IF1044-Q1欠压保护状态表(CA-IF1044)
| VCC          | Device State       | BUS Output  | RXD Condition                 |
|--------------|--------------------|-------------|-------------------------------|
| Greater than Vuv_vcc | Normal State      | According to TXD | According to BUS        |
| Less than Vuv_vcc and Greater than Vuv_vcc_sd | STB=VCC, Standby Mode | Ground Bias, Based on Wakeup State |
| Less than Vuv_vcc_sd | Protection State  | High Impedance, Hidden State | High Impedance           |
---table end---


## 8.3.1. 欠压保护状态表
表 8-2 欠压保护状态表(CA-IF1044V)
---table begin---
Table tile:CA-IF1044-Q1 欠压保护状态表(CA-IF1044V)
| VCC          | VIO          | Device State       | BUS Output  | RXD Condition                 |
|--------------|--------------|--------------------|-------------|-------------------------------|
| Greater than Vuv_vcc | Greater than VUV_VIO | Normal State      | According to TXD | According to BUS        |
| Less than Vuv_vcc and Greater than VUV_VIO | | STB=VIO, Standby Mode | Ground Bias, Based on Wakeup State |
| Less than Vuv_vcc and Less than VUV_VIO | | Protection State  | High Impedance, Hidden State | High Impedance           |
| Greater than Vuv_vcc | Less than VUV_VIO | Protection State  | High Impedance, Hidden State | High Impedance           |
| Less than Vuv_vcc | Less than VUV_VIO | Protection State  | High Impedance, Hidden State | High Impedance           |
---table end---


# 8.4. 驱动端
在常规工作模式下，当 TXD 输入高电平或者悬空时候，总线输出处于隐性状态，当 TXD 输入低电平时候，总线输
出处于显性状态。
表 8-3 驱动器功能表
---table begin---
Table tile:CA-IF1044-Q1驱动器功能表
| Device Mode | TXD   | CANH  | CANL  | Bus Driver State |
|-------------|-------|-------|-------|------------------|
| Normal      | Low   | High  | Low   | Dominant         |
|             | High or Floating | High-Z | High-Z | Recessive |
| Standby     | X     | High-Z | High-Z | Weak Pull-down to Ground |
---table end---



当输出端短路到高或低电平时候，CA-IF1044 通过限制驱动级电流来进行短路保护。过温保护功能进一步保护了短
路时产生的过热，当短路移除后，驱动端将回到正常工作状态。
# 8.5. 接收端
接收端读取总线(CANH,CANL)上的差分输入数据并将其转化为单端输出(RXD)到 CAN 控制器。其内部包含一个比较
器，比较器读取差分电压 VDIFF=(CANH-CANL)，同内部的 0.7V 阈值电压进行比较。如果 VDIFF>0.9V,输出低电平到 RXD，
如果 VDIFF<0.5V,输出高电平到 RXD。
总线 CANH 和 CANL 的共模电压范围为+/-20V。当 CANH 和 CANL 发生短路，断路或者悬空时，RXD 输出高电平。
表 8-4 接收器功能表
---table begin---
Table tile:CA-IF1044-Q1接收器功能表
| Device Mode | VID          | BUS State             | RXD   |
|-------------|--------------|-----------------------|-------|
| Normal      | VID > 0.9V   | Dominant (High)       | Low   |
|             | 0.5V < VID < 0.9V | Unknown           | Unknown |
|             | VID < 0.5V   | Recessive (High)      | High  |
| Standby     | VID > 1.15V  | Dominant (High)       | After Wake-up |
|             | 0.4V < VID < 1.15V | Unknown           | After Wake-up |
|             | VID < 0.4V   | Recessive            | High  |
| Any Case    | OPEN (VID=0V)| OPEN                  | High  |
---table end---


# 8.6. 过温保护
当结温超过过温保护阈值时，驱动端会关断。在过温时，CANH 和 CANL 处于高阻态，而接收端一直工作。当结温
回退至正常工作温度范围内，驱动端回到正常的工作模式。
# 8.7. 非上电状态
当没有上电时候，总线端处于高阻态，小的漏电流允许总线上挂更多的器件。
# 8.8. 悬空端口状态
当 TXD 端口悬空时候，内部上拉至电源，使得总线输出处于隐性状态。当 STB 端口悬空时候，内部上拉至电源，
器件处于待机模式以节省功耗。
# 8.9. VIO 电源
在 CA-IF1044V 中带有 VIO 电源，芯片逻辑端口可以直接和微控制器相连接，芯片内部会将逻辑电平转换为 5V 电
压域。该版本支持 3.3V 到 5.0V 的逻辑输入。在 VIO 电源大于等于 3.3V 时侯，待机模式支持+/-20V 的总线唤醒共模电
压，
# 8.10. 工作模式
CA-IF1044 有两种工作模式:常规模式和待机模式。模式选择由 STB 管脚来控制。
表 8-5 工作模式表
---table begin---
Table tile:CA-IF1044-Q1工作模式表
| STB Mode | Driver    | Receiver               | RXD                  |
|----------|-----------|------------------------|----------------------|
| High     | Standby   | Disabled               | Low Power Rx         |
| Low      | Normal    | Active                 | Active               |
---table end---


# 8.10.1. 常规模式 
当 STB 端口拉低时候，器件处于常规模式。在此模式下，收发器都正常工作并支持双向的总线通信。
 #8.10.2. 待机模式 
当 STB 端口拉高或者悬空时候，器件处于待机模式。在此模式下，驱动器和主接收器都被关闭，不支持双向通
信。低功耗接收器工作，以接受总线的唤醒请求。唤醒序列如图 9-4 所示，控制器检测 RXD 从高跳低后将 STB 管脚拉
低以使器件回到常规模式。
在待机模式下，总线被偏置到地以节省功耗。
#  8.11. 远程唤醒
总线上的一个特定的唤醒序列可以将芯片从待机模式唤醒（根据 ISO 11898-2:2016）。
唤醒序列包含:
• 显性态至少持续 Twk_FILTE,然后
# 8.10.1. 常规模式 
当 STB 端口拉低时候，器件处于常规模式。在此模式下，收发器都正常工作并支持双向的总线通信。
# 8.10.2. 待机模式 
当 STB 端口拉高或者悬空时候，器件处于待机模式。在此模式下，驱动器和主接收器都被关闭，不支持双向通
信。低功耗接收器工作，以接受总线的唤醒请求。唤醒序列如图 9-4 所示，控制器检测 RXD 从高跳低后将 STB 管脚拉
低以使器件回到常规模式。
在待机模式下，总线被偏置到地以节省功耗。
#  8.11. 远程唤醒
总线上的一个特定的唤醒序列可以将芯片从待机模式唤醒（根据 ISO 11898-2:2016）。
唤醒序列包含:
• 显性态至少持续 Twk_FILTE,然后


# 9. 应用信息
图 9-1 给出了 CA-IF1044 版本的典型应用图，VCC 电源与 MCU 的电源连接在一起。
图 9-2 给出了 CA-IF1044V 版本的典型应用图，VIO 电源与 MCU 的电源连接在一起。


# 10. 封装信息
# 10.1. SOIC8 的外形尺寸
SOIC8 封装尺寸图和建议焊盘尺寸图。尺寸以毫米为单位
#  10.2. DFN8 的外形尺寸
DFN8 的封装尺寸图，尺寸以毫米为单位。


# 11. 焊接信息


# 12. 编带信息
---table begin---
Table tile:CA-IF1044-Q1焊接信息表
| 参数                         | 值                                       |
| ---------------------------- | ---------------------------------------- |
| 温升速率（TL=217°C 至峰值 TP） | 最大 3°C/s                              |
| 预热时间 ts                 | 60~120 秒                                |
| 温度保持时间 tL             | 60~150 秒                                |
| 峰值温度 TP                 | 260°C                                   |
| 峰值温度下的时间 tP         | 最长 30 秒                              |
| 降温速率（峰值 TP 至 TL=217°C） | 最大 6°C/s                              |
| 常温 25°C 到峰值温度 TP 时间 | 最长 8 分钟                              |
---table end---


# 13. 附录
表 13-1 ISO11898-2:2016 标准参数对照表
---table begin---
Table tile:CA-IF1044-Q1IS O11898-2:2016 标准参数对照表 表
##ISO 11898-2:2016 CA-IF1044 Datasheet

| Parameter Note | Symbol | Parameter |
|----------------|--------|-----------|
| HS-PMA dominant output characteristics | Single ended voltage on CAN_H | VCAN_H |
| | VO(DOM) dominant output voltage | |
| Single ended voltage on CAN_L | VCAN_L | |
| Differential voltage on normal bus load | VDiff | |
| VOD(DOM) dominant differential output voltage | | |
| Differential voltage on effective resistance during arbitration | | |
| Optional: Differential voltage on extended bus load range | | |
| HS-PMA driver symmetry | Driver symmetry | Vsym |
| Transmitter voltage symmetry | | |
| Maximum HS-PMA driver output current | Absolute current on CAN_H | ICAN_H |
| | IOS(SS_DOM) dominant short-circuit output current | |
| Absolute current on CAN_L | ICAN_L | |
| HS-PMA recessive output characteristics, bus biasing active/inactive | Single ended output voltage on CAN_H | VCAN_H |
| | VO(REC) recessive output voltage | |
| Single ended output voltage on CAN_L | VCAN_L | |
| Differential output voltage | VDiff | |
| VOD(REC) recessive differential output voltage | | |
| Optional HS-PMA transmit dominant timeout | Transmit dominant timeout, long | tdom |
| TXD dominant time-out time | | |
| Transmit dominant timeout, short | | |
| HS-PMA static receiver input characteristics, bus biasing active/inactive | Recessive state differential input voltage range | VDiff |
| Dominant state differential input voltage range | | |
| Differential receiver threshold voltage | VIT | |
| HS-PMA receiver input resistance (matching) | Differential internal resistance | RDiff |
| Single ended internal resistance | RCAN_H | |
| | RCAN_L | |
| Input resistance | RIN | |
| Input resistance deviation | mR | |
| HS-PMA implementation loop delay requirement | Loop delay | tLoop |
| Delay time from TXD HIGH to RXD HIGH | tloop2 | |
| Delay time from TXD LOW to RXD LOW | tloop1 | |
| Optional HS-PMA implementation data signal timing requirements for use with bit rates above 1 Mbit/s up to 2 Mbit/s and above 2 Mbit/s up to 5 Mbit/s | Transmitted recessive bit width @ 2 Mbit/s / @ 5 Mbit/s | tBit(Bus) |
| Transmitted recessive bit width | tbit(BUS) | |
| Received recessive bit width | tBit(RXD) | |
| Bit time on pin RXD | tbit(RXD) | |
| Receiver timing symmetry | ∆tRec | |
| HS-PMA maximum ratings of VCAN_H, VCAN_L and VDiff | Maximum rating VDiff | V(DIFF) voltage between pin CANH and pin CANL |
| General maximum rating | VCAN_H | |
| | VCAN_L | |
| V(BUS) voltage on CANH, CANL pin | | |
| Optional: Extended maximum rating | VCAN_H and VCAN_L | |
---table end---
 


#  14. 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知的情况下，保
留因技术革新而改变上述资料的权利。
Chipanalog 产品全部经过出厂测试。 针对具体的实际应用，客户需负责自行评估，并确定是否适用。Chipanalog
对客户使用所述资源的授权仅限于开发所涉及 Chipanalog 产品的相关应用。 除此之外不得复制或展示所述资源， 如
因使用所述资源而产生任何索赔、 赔偿、 成本、 损失及债务等， Chipanalog 对此概不负责。

# 商标信息
Chipanalog Inc.®、Chipanalog®为 Chipanalog 的注册商标。