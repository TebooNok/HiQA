 # CA-IF1042Lx 具有正负40V 故障保护的 CAN 收发器
 
 # 1. 产品特性
• 符合 ISO 11898-2:2016 和 ISO 11898-5:2007 物理层
标准
• 所有器件均支持经典 CAN 和 5Mbps CAN FD（灵活
数据速率）
• I/O 电压范围支持 3.3V 和 5V 微控制器 (MCU)
• 未上电时的理想无源特性
- 总线和逻辑引脚处于高阻态（无负载）
- 上电和掉电时总线和 RXD 输出上无毛刺脉冲
• 保护特性
- 总线故障保护：±40V
- VCC 和 VIO （仅限 CA-IF1042LVS-Q1）电源引脚
上具有欠压保护
- 驱动器显性超时 (TXD DTO) – 最低数据速率低
至 4kbps
- 热关断保护 (TSD)
• 接收器共模输入电压：±30V
• 典型环回延迟：155ns
• 结温范围：-55°C 至 150°C
• 可提供 SOIC8 封装
• AEC Q100 Grade 1 认证中


# 2. 应用
• 汽车及交通运输行业
• 工业控制
• 建筑自动化
• 供热通风及空调系统（HVAC）


# 3. 概述
CA-IF1042Lx CAN 收发器系列符合 ISO 11898-2 (2016) 高
速 CAN（控制器局域网络）物理层标准。所有器件均设
计用于数据速率高达 5Mbps（兆位每秒）的 CAN FD 网
络。部件号包含“V”后缀的器件配有用于 I/O 电平转
换的辅助电源输入（用于设置输入引脚阈值和 RXD 输
出电平）。该系列器件具有低功耗待机模式及远程唤醒
请求特性。此外，所有器件均包含多种保护功能， 以
提高器件和 CAN 网络的稳定性。
器件信息
---table begin---
Table tile:CA-IF1042L 器件信息表
| 零件号 (Part Number) | 封装 (Package) | 封装尺寸 (Package Dimensions - Nominal) |
|----------------------|----------------|----------------------------------------|
| CA-IF1042LS-Q1       | SOIC8          | 4.9mm x 3.9mm                           |
| CA-IF1042LVS-Q1      |  SOIC8    | 4.9mm x 3.9mm                             |
---table end---

# 5. 引脚功能描述
表 5-1 CA-IF1042Lx 引脚功能描述
---table begin---
Table tile:CA-IF1042Lx 引脚图表
| 引脚名称 | 引脚编号 CA-IF1042LS | 引脚编号 CA-IF1042LVS | 类型   | 描述 |
|-------|-------------------|--------------------|------|-----|
| TXD   | 1                 | 1                  | 输入 | 传输数据输入。将 TXD 置高以使总线处于隐态，将 TXD 置低以使总线处于显态。TXD 内部有一个上拉电阻连接到 VIO。|
| GND   | 2                 | 2                  | 地   | 电源地。|
| VCC   | 3                 | 3                  | 电源 | 总线侧电源输入。在 VCC和 GND 之间接入一个 0.1μF 电容，尽量的靠近器件。|
| RXD   | 4                 | 4                  | 输出 | 接收器输出。当 CANH 和 CANL 处于隐态时，RXD 为高电平。当 CANH 和 CANL 处于显态时，RXD 为低电平。RXD 的参考电源为 VIO。|
| NC    | 5                 | -                  | NC   | 没有连接。|
| VIO   | -                 | 5                  | 电源 | I/O 侧电源输入。|
| CANL  | 6                 | 6                  | 输入输出 | 低电平 CAN 总线。CANL 是收发器输入输出的低端。|
| CANH  | 7                 | 7                  | 输入输出 | 高电平 CAN 总线。CANH 是收发器输入输出的高端。|
| STB   | 8                 | 8                  | 输入 | STB=1，低功耗待机模式；STB=0，正常工作模式。|
---table end---


# 6. 产品规格
# 6.1. 绝对最大额定值 1
---table begin---
Table tile:CA-IF1042L 绝对最大额定值 1表
参数                       最小值         最大值         单位
VCC 5-V 总线电源电压       -0.3          7               V
VIO IO 侧电平转换电源电压  -0.3          7               V
VBUS CAN 总线 IO 电压    -40           40              V
V(DIFF) CANH 和 CANL 间的最大差分电压   -40  40         V
V(Logic_Input) 逻辑侧端口输入电压（TXD，STB）  -0.3 +7 and < VIO+0.3 V
V(Logic_Output) 逻辑侧端口输出电压（RXD）  -0.3 +7 and < VIO+0.3 V
IO（RXD） RXD 接收器输出电流  -8             8               mA
TJ 结温                         -55           150           ℃
TSTG 存储温度                -65           150           ℃

备注:
1. 等于或超出上述绝对最大额定值可能会导致产品永久性损坏。这只是额定最值，并不能以这些条件或者在任何其它超出本技术规
范操作章节中所示规格的条件下，推断产品能否正常工作。长期在超出最大额定值条件下工作会影响产品的可靠性。  
---table end---


# 6.2. ESD 额定值
---table begin---
Table tile:CA-IF1042L ESD 额定值表
| 测试项目 (Test Item) | 测试条件 (Test Conditions) | 数值 (Value) | 单位 (Unit) |
|----------------------|----------------------------|--------------|------------|
| HBM ESD              | 所有管脚 (All Pins)         | ±6000       | V          |
|                      | CAN 总线端口（CANH，CANL）到 GND | ±6000       | V          |
| CDM ESD              | 所有管脚 (All Pins)         | ±2000       | V          |
| System Level ESD     | CAN 总线端口 (CANH，CANL) 到 GND<br>IEC 61000-4-2 : 不上电接触放电 | ±6000^2^ | V |
备注 (Notes):
1. JEDEC 文件 JEP155 规定 500V HBM 可通过标准 ESD 控制过程实现安全制造；
2. 系统板级测试。

---table end---


# 6.3. 建议工作条件
---table begin---
| 参数 (Parameter) | 描述 (Description)          | 最小值 (Min Value) | 最大值 (Max Value) | 单位 (Unit) |
|------------------|-----------------------------|--------------------|--------------------|------------|
| VCC              | 5-V 总线电源电压 (5-V Bus Power Supply Voltage) | 4.5                | 5.5                | V          |
| VIO              | IO 侧电平转换电源电压 (IO Side Level Conversion Power Supply Voltage) | 3.0                | 5.5                | V          |
| IOH(RXD)         | RXD 端口高电平输出电流 (High Level Output Current at RXD Port)  | -2                 | -                  | mA         |
| IOL(RXD)         | RXD 端口低电平输出电流 (Low Level Output Current at RXD Port)   | -                  | 2                  | mA         |
---table end---


# 6.4. 热量信息
---table begin---
Table tile:CA-IF1042L 热量信息表
热量表 SOIC8 单位
RθJA IC 结至环境的热阻 170 °C/W
RθJC(top) IC 结到壳（顶部）热阻 40 °C/W
---table end---


# 6.5. 电气特性
建议工作条件下，环境温度 TA=-40℃到 125℃。
参数 测试条件 最小值 典型值 最大值 单位
电源特性
Icc 5V 电源电流
TXD=0V, RL=60 Ohm, CL=open, RCM=open,
STB=0V,Typical Bus Load,如图 7-1
45 70 mA
TXD=0V, RL=50 Ohm, CL=open, RCM=open,
STB=0V,High Bus Load,如图 7-1
50 80 mA
TXD=0V, STB=0V, CANH=-12V, RL=open, 
CL=open, RCM=open, 如图 7-1
110 mA
TXD=VCC or VIO, RL=50 Ohm, RCM =open, 
CL=open ,
STB=0V, CL=open, RCM=open, 如图 7-1
1.3 2.5 mA
TXD=STB=VIO（待机模式, CA-IF1042LVS-Q1）,
RL=50 Ohm, CL=open, RCM=open, 如图 7-1
0.5 5 uA
TXD=STB=VCC（待机模式, CA-IF1042LS-Q1）, 
RL=50 Ohm,如图 7-1
14 22 uA
IIO I/O 供电电流 TXD=0V,STB=0V, RXD 悬空 70 300 uA
TXD= VIO,STB= VIO, RXD 悬空 11 17 uA
UVVCC VCC UVLO 电压 上升 4.1 4.45 V
UVVCC VCC UVLO 电压 下降 3.7 3.9 4.25 V
VHYS(UVVCC) VCC UVLO 电压 迟滞电压 200 mV
UVVIO/
Vuv_vcc_sd
VIO UVLO 电压(CA-IF1042LVS-Q1)
/VCC_sd UVLO 电压(CA-IF1042LSQ1)
上升
2.35 2.75
V
UVVIO/
Vuv_vcc_sd
VIO UVLO 电压(CA-IF1042LVS-Q1)
/VCC_sd UVLO 电压(CA-IF1042LSQ1)
下降
1.3 2.2 2.6
V
VUV_IO_hys
Vuv_vcc_sd _hys
VIO UVLO 电压(CA-IF1042LVS-Q1)
/VCC_sd UVLO 电压(CA-IF1042LSQ1)
迟滞电压
150
mV
逻辑接口(STB 选择输入)
VIH 输入高电平 0.7*VCC1 V
VIL 输入低电平 0.3*VCC1 V
IIH 输入高电平漏电流 STB=VCC=VIO 5.5V -2 2 uA
IIL 输入低电平漏电流 STB=0V,VCC=VIO = 5.5V -20 -2 uA
Ilek(off) 未上电时漏电流 STB=5.5V, VCC=VIO =0V -1 1 uA
逻辑接口(TXD 输入端口)
VIH 输入高电平 0.7*VCC1 V
VIL 输入低电平 0.3*VCC1 V
IIH 输入高电平漏电流 TXD=VCC=VIO = 5.5V -2.5 0 1 uA
IIL 输入低电平漏电流 TXD=0V,VCC=VIO = 5.5V -100 -50 -7 uA
Ilek(off) 未上电时漏电流 TXD=5.5V,VCC=VIO = 0V -1 0 1 uA
Ci 输入电容 VIN=0.4*sin(4E6*π*t)+2.5V 5 pF
逻辑接口(RXD 输出端口)
VOH 输出高电平 Io=-2mA 0.8*VCC1 V
VOL 输出低电平 Io=+2mA 0.2*VCC1 V
Ilek(off) 未上电时漏电流 STB=5.5V, V

CAN 总线驱动
VO(DOM) 单端输出电压（显性）
TXD=低, STB=0V, RL=50-65Ohm, CL=open, 
RCM=open, CANH 端口, 如图 7-1
2.75 4.5 V
TXD=低, STB=0V, RL=50-65Ohm, CL=open, 
RCM=open, CANL 端口, 如图 7-1
0.5 2.25 V
VO(REC) 单端输出电压（隐性） TXD=VCC or VIO, VCC=VIO STB=0V, RL=open, 
RCM=open, CANH 端口/CANL 端口, 如图 7-1
2 0.5xVCC 3 V
VO(STB) 待机模式总线电压
STB=VIO, RL open, RCM open, CANH -0.1 0.1 V
STB= VIO, RL open, RCM open, CANL -0.1 0.1 V
STB= VIO, RL open, RCM open, CANH-CANL -0.2 0.2 V
V OD(DOM) 差分输出电压（显性）
TXD=低, STB=0V, RL=45-50 Ohm , RCM open, 如
图 7-1
1.4 3.0 V
TXD=低, STB=0V, RL=50-65 Ohm , RCM open, 如
图 7-1
1.5 3.0 V
TXD=低, STB=0V, RL=2240 Ohm , RCM open, 如
图 7-1
1.5 5.0 V
VOD(REC) 差分输出电压（隐性）
TXD=高, STB=0V, RL =60 Ohm, CL=open, 
RCM=open, CANH-CANL 如图 7-1
-120 12 mV
TXD=高, STB=0V, RL =open, CL=open, 
RCM=open, CANH-CANL 如图 7-1
-50 50 mV
VSYM 瞬态对称性(显性和隐性)
RL=60 Ohm, STB=0V, Csplit=4.7nF, RCM open , 
Txd=250kHz, 1MHz, 2.5M Hz,如图 7-1
0.9 1.1 V/V
VSYM_DC DC 对称性(显性和隐性) RL=60 Ohm, STB=0V, RCM open, 如图 7-1 -0.4 0.4 V
IOS(SS_DOM) 短路电流(显性)
TXD=低, STB=0V ,CANL 开路, CANH 从-5V 到
40V, 如图 7-7
-100 mA
TXD=低, STB=0V ,CANH 开路, CANL 从-5V 到
40V, 如图 7-7
100 mA
IOS(SS_rec) 短路电流(隐性)
TXD=高, STB=0V ,VBSU=CANH=CANL 从-27V 到
32V, 如图 7-7
-5 5 mA
VCM 共模输入范围 常规模式和待机模式, RXD 输出有效,如图 7-2 -30 30 V
VIT 常规模式输入阈值电压 STB=0V, Vcm 从 -20V 到 20V, 如图 7-2 500 900 mV
STB=0V, Vcm 从 -30V 到 30V, 如图 7-2 400 1000 mV
VHYS 常规模式输入阈值迟滞电压 STB=0V 120 mV
VIT(STB) 待机模式输入阈值电压 STB=高, Vcm 从 -20V 到 20V(3≤VIO≤5.5V),如图
7-2
400 1150 mV
VIT(STB) 待机模式输入阈值电压 STB=


# 6.6. 开关特性
建议工作条件下，环境温度 TA=-40℃到 125℃。
表 6-1 开关特性表
---table begin---
Table tile:CA-IF1042L开关特性表
参数 测试条件 最小值 典型值 最大值 单位
驱动器开关特性
tONTXD TXD 延迟(隐形到显性) STB=0V, RL=60 Ohm, CL=100pF, 如图 7-1 55 ns
tOFFTXD TXD 延迟(显形到隐性) STB=0V, RL=60 Ohm, CL=100pF, 如图 7-1 75 ns
tDTO TXD 显性超时 RL=60 Ohm, CL open,如图 7-5 2.5 6.8 10 ms
接收器开关特性
tONRXD RXD 延迟(隐形到显性) STB=0V ,CL=15pF, 如图 7-2 90 ns
tOFFRXD RXD 延迟(显形到隐性) STB=0V ,CL=15pF, 如图 7-2 100 ns
器件开关特性
tloop1 环回延迟时间 隐性到显性, RL=60 Ohm, CL=100pF, 如图 7-3 125 255 ns
tloop2 环回延迟时间 显性到隐性, RL=60 Ohm, CL=100pF, 如图 7-3 155 255 ns
tONTXD 模式转换时间 从待机态到常态或者从常态到待机态, 如图 7-4 12 45 μs
Twk_FILTER 有效唤醒的滤波时间 如图 9-4 0.5 1.8 μs
TWK_FILTEROUT 总线唤醒超时 如图 9-4 0.8 10 ms
FD TIMING 特性
Tbit（bus） bit 时间 STB=0V ,总线侧 RL=60 Ohm, CLD=100pF, CL=15pF, CAN 
FD 2Mbps, 如图 7-6
435 530 ns
Tbit（bus） bit 时间 STB=0V ,总线侧 RL=60 Ohm, CLD=100pF, CL=15pF, CAN 
FD 5Mbps , 如图 7-6
155 210 ns
Tbit（rxd） bit 时间 STB=0V ,接收侧 RL=60 Ohm, CLD=100pF, CL=15pF, CAN 
FD 2Mbps, 如图 7-6
400 550 ns
Tbit（rxd） bit 时间 STB=0V ,接收侧 RL=60 Ohm, CLD=100pF, CL=15pF, CAN 
FD 5Mbps, 如图 7-6
120 220 ns
Trec 脉冲偏差 STB=0V ,接收侧 RL=60 Ohm, CLD=100pF, CL=15pF, CAN 
FD 2Mbps, 如图 7-6
-65 40 ns
Trec 脉冲偏差 STB=0V ,接收侧 RL=60 Ohm, CLD=100pF, CL=15pF, CAN 
FD 5Mbps , 如图 7-6
-45 15 ns
---table end---



# 9. 详细说明
# 9.1. 概述
CA-IF1042Lx 是一款具有低功耗待机模式的 CAN 收发器芯片，适用于汽车，卡车，公交车，工程车、工业网络控
制等领域，支持 5Mbps 的 CAN FD 灵活数据速率，符合 ISO 11898-2:2016 和 ISO 11898-5:2007 物理层标准。
# 9.2. CAN 总线状态
常规模式下 CAN 总线有两种工作状态：显性和隐性，如图 9- 1 和图 9- 2。显性态时，TXD 为低，总线差分输出，
RXD 输出为低。隐性态时，TXD 为高，总线被内部电阻偏置到 Vcc/2，RXD 输出为高。
当 STB 置高，芯片会进入低功耗待机模式，这时，总线会被内部电阻偏置到地，如图 9- 1 和图 9- 2。
# 9.3.     发射端显性超时功能
在常规模式显性状态下， 若 CAN 控制器发生错误时候，会将 TXD 一直拉低，总线就会被钳位在显性状态，显性  超时功能则会避免这一状态。显性超时保护被 TXD 的下降沿所触发，当 TXD 处于显性的时间超过 tDTO 时候， 发射器会 被关闭，以释放总线到隐性状态。在出现显性超时故障后，发射器可以被 TXD 的上升沿重新使能。发射器的显性超时 功能限制了可能的最低传输速率为 4kbps。
# 9.4.     欠压保护
VCC 和 VIO  电源具有欠压保护功能。
在 CA-IF1042LS-Q1 中， 当 VCC 低于 Vuv_vcc_sd 时，不管 STB 管脚状态如何，芯片进入到保护态。 当 VCC 高于 Vuv_vcc_sd 但低于 Vuv_vcc 值时， 若 STB=GND；保护态，STB=VCC ，待机模式。当 VCC 高于 Vuv_vcc 值时， 若 STB=GND，正常模式；
STB=Vcc，待机模式。详细参考表 9-1。
在 CA-IF1042LVS-Q1 中， 如果 VIO  电源低于 VUV_IO ，收发器处于保护态。如果 VIO  电源正常而 VCC 欠压， 芯片则进入 低功耗待机模式或者保护态。详细参考表 9-2。
---table begin---
Table tile:CA-IF1042L 耗待机模式或者保护态。详细参考表

| VCC            | Device State           | BUS Output   | RXD            |
|----------------|------------------------|--------------|----------------|
| 大于 Vuv_vcc   | STB=VCC ，待机模式      | 偏置到地     | 根据唤醒状态  |
|                | STB=GND，正常模式       | 根据 TXD    | 根据总线       |
| 小于 Vuv_vcc   | 并且大于 Vuv_vcc_sd    | STB=VCC ，待机模式 | 偏置到地    | 根据唤醒状态  |
|                | STB=GND ，保护态        | 偏置到地     | 隐形          |
| 小于 Vuv_vcc_sd| 保护态                  | 高阻         | 高阻          |

| VCC           | VIO           | Device State          | BUS Output   | RXD             |
|---------------|---------------|-----------------------|--------------|-----------------|
| 大于 Vuv_vcc   | 大于 VUV_IO   | STB=VCC ，待机模式     | 偏置到地     | 根据唤醒状态    |
|               |               | STB=GND，正常模式      | 根据 TXD    | 根据总线         |
| 小于 Vuv_vcc   | 大于 VUV_IO   | STB=VIO ，待机模式     | 偏置到地     | 根据唤醒状态    |
|               |               | STB=GND ，保护态       | 偏置到地     | 隐性             |
| X1            | 小于 VUV_IO   | 保护态                 | 高阻         | 高阻             |
注： 1.X 表示 VCC  电压无论是大于还是小于 Vuv_vcc。
---table end---


# 9.6.     接收端
接收端读取总线(CANH,CANL)上的差分输入数据并将其转化为单端输出(RXD)到 CAN 控制器。其内部包含一个比较 器，比较器读取差分电压 VDIFF=(CANH-CANL)，同内部的 0.7V 阈值电压进行比较。如果 VDIFF>0.9V,输出低电平到 RXD ， 如果 VDIFF<0.5V,输出高电平到 RXD。
总线 CANH 和 CANL 的共模电压范围为±30V。当 CANH 和 CANL 发生短路， 断路或者悬空时，RXD 输出高电平。
---table begin---
Table tile:CA-IF1042L 接收端表
| Device Mode  | VID=VCANH-VCANL | BUS state            | RXD              |
|--------------|-----------------|----------------------|------------------|
| 常规模式      | VID>0.9V        | 显性                 | 低               |
|              | 0.5V<VID<0.9V   | 未知                 | 未知             |
|              | VID<0.5V        | 隐性                 | 高               |
| 待机模式      | VID>1.15V       | 显性                 | 唤醒后根据总线状态 |
|              | 0.4V<VID<1.15V  | 未知                 |                  |
|              | VID<0.4V        | 隐性                 |                  |
| 任何情况      | OPEN(VID=0V)    | OPEN                 | 高               |
---table end---


# 9.7.     过温保护
当结温超过过温保护阈值时，驱动端会关断。在过温时， CANH 和 CANL 处于高阻态，而接收端一直工作。当结温 回退至正常工作温度范围内，驱动端回到正常的工作模式。
# 9.8.     非上电状态
当没有上电时候，总线端处于高阻态，小的漏电流允许总线上挂更多的器件。
# 9.9.     悬空端口状态
当 TXD 端口悬空时候， 内部上拉至电源， 使得总线输出处于隐性状态。当 STB 端口悬空时候， 内部上拉至电源， 器件处于待机模式以节省功耗。
# 9.10.  VIO  电源
在 CA-IF1042LVS-Q1 中带有 VIO  电源，芯片逻辑端口可以直接和微控制器相连接，芯片内部会将逻辑电平转换为 5V 电压域。该版本支持 3V 到 5.5V 的逻辑输入。在 3V~5.5V 电源时， 待机模式下支持±20V 的总线唤醒共模电压。
# 9.11.   工作模式
CA-IF1042LS-Q1 和 CA-IF1042LVS-Q1 有两种工作模式:常规模式和待机模式。模式选择由 STB 管脚来控制。
表 9-5 工作模式表
---table begin---
Table tile:CA-IF1042L 工作模式表
| STB | Mode      | Driver   | Receiver             | RXD              |
|-----|-----------|----------|----------------------|------------------|
| 高  | 待机模式   | 关闭     | 低功耗接收器工作     | 唤醒后根据总线   |
| 低  | 常规模式   | 工作     | 工作                 | 根据总线         |
---table end---


# 9.11.2.  待机模式
当 STB 端口拉高或者悬空时候， 器件处于待机模式。在此模式下， 驱动器和主接收器都被关闭， 不支持双向通
信。低功耗接收器工作， 以接受总线的唤醒请求。唤醒序列如图 9- 4 所示， 控制器检测 RXD 从高跳低后将 STB 管脚拉 低以使器件回到常规模式。
在待机模式下， 总线被偏置到地以节省功耗。
# 9.11.3.  远程唤醒
总线上的一个特定的唤醒序列可以将芯片从待机模式唤醒（根据 ISO 11898-2:2016）。
唤醒序列包含:
•      显性态至少持续 Twk_FILTER,然后
•       隐性态至少持续 Twk_FILTER,然后
•      显性态至少持续 Twk_FILTER
上述中的显性或者隐性位宽若小于 Twk_FILTER 和 Twk_FILTER 将会被忽略。
该完整的显性- 隐性-显性序列必须小于 Twk_FILTEROUT  以被有效识别（图 9- 4），否则，内部的唤醒逻辑会被重置， 必 须等待下一个完整的唤醒序列来触发唤醒行为。在有效唤醒前，RXD 管脚一直为高电平。
再检测到完整的唤醒序列后，芯片仍处于待机模式下,RXD 管脚输出总线的信号。总线的信号若小于 TWK_FILTER 时 间，将不会被低功耗接收器识别并输出到 RXD 管脚上。
在有效唤醒后， 若发生以下行为，RXD 管脚仍将不会显示唤醒行为：
•      芯片切换到常规模式；
•      在 Twk_FILTEROUT 时间内， 完整的唤醒序列没有被接受到；
•      VIO 发生欠压 (VIO< UVVIO)；


# 10.  应用信息
图 10- 1 给出了 CA-IF1042LS-Q1 版本的典型应用图，VCC  电源与 MCU 的电源连接在一起。
图 10- 2 给出了 CA-IF1042LVS-Q1 版本的典型应用图，VIO  电源与 MCU  的电源连接在一起。
在多节点 CAN 总线网络中，保持线路阻抗均匀非常重要， 由此需要提供适当的终端匹配。网络拓扑不能使用星形、 树形或环形拓扑，在网络相距最远的两个端点之间挂接任何一个节点都会产生一个“接头”，而高速信号在这些电缆   “接头”上将产生信号反射，在总线上引入干扰。设计中，需要使用尽可能短的电缆挂接每个节点，尤其是对于高速  传输网络。图 10- 3 给出了 CAN 总线的典型拓扑， 在总线的两个端点可采用单个 120Ω电阻(RT)匹配总线，其中，120Ω	 为电缆的特征阻抗；如果需要增加共模滤波， 也可以将其分隔成两个 60Ω的电阻进行终端匹配。


# 11.  封装信息
SOIC8 封装尺寸图和建议焊盘尺寸图, 尺寸以毫米为单位。

 
# 12.   焊接信息
---table begin---
Table tile:CA-IF1042L焊接信息表
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


# 13.   编带信息

 
# 14.   重要声明
上述资料仅供参考使用， 用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知的情况下， 保 留因技术革新而改变上述资料的权利。
Chipanalog 产品全部经过出厂测试。 针对具体的实际应用，客户需负责自行评估， 并确定是否适用。 Chipanalog 对客户使用所述资源的授权仅限于开发所涉及 Chipanalog 产品的相关应用。 除此之外不得复制或展示所述资源， 如 因使用所述资源而产生任何索赔、 赔偿、 成本、 损失及债务等， Chipanalog 对此概不负责。


#  商标信息
Chipanalog Inc.® 、Chipanalog®为 Chipanalog 的注册商标。