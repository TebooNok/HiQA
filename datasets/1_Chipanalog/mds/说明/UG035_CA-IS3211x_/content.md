 # CA-IS3211x 光耦兼容型单通道栅极驱动器EVM 使用说明


# 1.描述
本文档主要描述了 CA-IS3211x 评估板相关的使用说明, 其中包含产品介绍、原理图、PCB 布线图、
物料清单以及部分关键波形和数据等。该评估板可以用来简单评估 CA-IS3211x 的基本性能参数。


# 2.芯片简介
CA-IS3211x 是一款光耦兼容的单通道隔离式栅极驱动器, 可用于驱动 MOSFET、IGBT 和 SiC 器件。隔
离等级达到 5.7kVRMS, 芯片可提供 5A 拉、6A 灌输出峰值电流能力。高达 30V 的电源电压范围允许使用
双极性电源来有效驱动 IGBT 和 SiC 功率 FET。该芯片的性能亮点包括：高共模瞬态抗扰度（CMTI）、低
传输延迟、低脉冲宽度失真。严格的工艺控制使得芯片一致性较好。输入级是模拟二极管, 与传统的光
耦隔离栅极驱动器的 LED 相比, 具有更好的长期可靠性和老化特性。高性能和高可靠性使得该芯片适用
于工业电源、光伏逆变器、车载充电器、直流电机控制以及汽车空调与加热系统。CA-IS3211x 可以驱动
高压侧及低压侧的功率管, 既能够完全兼容传统的光耦栅极驱动器, 又显著提高了驱动的性能。
CA-IS3211x系列一共包含三个封装, IS3211VxJ为SOIC6-WB封装（Single Output）, IS3211VxG为SOIC8-
WB 封装（Single Output）, IS3211SxG 为 SOIC8-WB 封装（Split Output）, IS3211VCU 为 DUB8 封装（Single
Output）, 客户可根据方案需求选择不同封装类型的芯片。


# 3.BOM 清单
---table begin---
Table tile:UG035_CA-IS3211xBOM 清单表
| Items | Designator | Description | Footprint | Quantity | Vendor PN |
|-------|------------|-------------|-----------|----------|-----------|
| 1     | C1, C4, C6, C7, C13 | 0.1uF/50V,X7R,0805,MLCC | C0805 | 5 | SAMSUNG CL21B104KBCNNNC |
| 2     | C2, C3     | 2.2uF/50V,X7R,0805,MLCC | C0805 | 2 | TDK CGA4J3X7R1H225KT000N |
| 3     | C5, C12    | 1uF/50V,X7R,0805,MLCC | C0805 | 2 | YAGEO CC0805KKX7R9BB105 |
| 4     | C10        | 1nF/50V,X7R,0805,MLCC | C0805 | 1 | muRata GCM216R71H102KA37D |
| 5     | C11        | 220nF/50V,X7R,0805,MLCC | C0805 | 1 | KEMET C0805C224K5RAC7800 |
| 6     | J1, J2     | 2 Pin Jumper, Pitch 2.54mm | HDR2.54-LI-2P | 2 | - |
| 7     | J3, J4, J5, J6, J7 | 2 Pin Jumper, Pitch 2.54mm | HDR2.54-LI-2P | 5 | - |
| 8     | P1, P2     | 5.08mm, Terminal Block | 5.08mm, Terminal Block | 2 | - |
| 9     | R1, R5     | 0Ω, 0805 | R0805 | 2 | UNI-ROYAL 0805W8J0000T5E |
| 10    | R3, R4     | 130Ω, 0805 | R0805 | 2 | UNI-ROYAL 0805W8F1300T5E |
| 11    | TP1, TP2, TP3 | Test Point | tpt,keystone-5000 | 3 | Keystone 5000 |
| 12    | TP4, TP5, TP6, TP7, TP9 | Test Point | tpt,keystone-5002 | 5 | Keystone 5002 |
| 13    | TP8, TP10, TP11, TP12, TP13, TP14, TP15 | Test Point | tpt,keystone-5001 | 7 | Keystone 5001 |
| 14    | U1         | LDO 5V 1A | SOT-223 | 1 | PUOLOP AMS1117-5.0 |
| 15    | U2         | 2 CHANNEL BUFFER 50mA | SOT-23-6 | 1 | Texas Instruments SN74LVC2G17DBVR |
| 16    | U3         | SINGLE CHANNEL ISOLATION GATE DRIVER | SOIC6-WB Package | 1 | Chipanalog CA-IS3211VxJ |
---table end---


# 4. 测试仪器
DC 直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、6.5 位多功能万用表安捷伦 34465A、高频信
号发生器等。


# 5.硬件连接
1. 将 DC 直流电压源连接到 VCC 和 VEE, VCC=15V/0.1A；
2. 信号发生器输出一定频率、占空比和幅值的信号连接输入端；
3. 通过示波器测量输出端 OUT 信号。


# 6.关键参数测试
下面是以 CA-IS3211VxJ（SOIC6-WB）为例, 测试一些典型波形, 包括输出上升&下降时间、传输延
时、输出峰值电流、信号传输、双轨电源输出、输入互锁功能等等。（除非特殊说明, Ta=25℃, VCC=15V, 
VEE=0V, REXT=130Ω, CVCC=10uF||100nF, Cload=1nF/50V）
1、输出上升时间&下降时间
关键参数测试
下面是以 CA-IS3211VxJ（SOIC6-WB）为例, 测试一些典型波形, 包括输出上升&下降时间、传输延
时、输出峰值电流、信号传输、双轨电源输出、输入互锁功能等等。（除非特殊说明, Ta=25℃, VCC=15V, 
VEE=0V, REXT=130Ω, CVCC=10uF||100nF, Cload=1nF/50V）
1、输出上升时间&下降时间
注：(1) 波形通道设置 CH2: OUT. 
(2) 上升&下降时间取输出边沿的 20%-80%.
2、传输延时
注：(1) 波形通道设置 CH1: Input, CH2: OUT.
(2) 传输延时取输入沿 50% 至输出沿 50%.
3、输出峰值电流
注：(1) 波形通道设置 CH1: Input, CH2: OUT.
(2) IOH or IOL=Cload*△V/△t.
4、信号传输
注：(1) 波形通道设置 CH1: Input, CH2: OUT
 5、双轨电源输出
注：(1) 波形通道设置 CH1: Input, CH3: OUT.
(2) VCC=15V, VEE=-5V.
6、输入互锁功能
注：(1) 波形通道设置 CH1: Input_HSON, CH2: Input_LSON, CH3: VOUT1, CH4: VOUT2.


# 7.PCB 布线建议
为了达到 CA-IS3211x 的最优性能, PCB 布局时需要遵循以下原则：
• 为了保证电源为稳定性和低噪声, VCC 到 VEE 的旁路电容需要尽可能近的靠近芯片 VCC 和 VEE 引脚, 
并推荐使用 10uF/50V 并联 100nF/50V 的低 ESR 和低 ESL 的 MLCC 电容.
• 当芯片驱动功率管时, VOUT 存在非常高的 di/dt, VOUT 环路 PCB 走线寄生电感会导致 EMI 和电压振
荡问题, 故在设计 PCB 时, 芯片应尽可能靠近功率管位置, VOUT 走线尽可能宽, 环路走线尽可能短, 
以降低环路寄生电感。
• 为确保原边侧和副边侧之间的隔离性能, 请避免在芯片下方放在任何的 PCB 走线、覆铜、焊盘和过
孔。也可以采用 PCB 开槽工艺, 以防止影响隔离性能。
• 当负载较重或开关频率较高时, 芯片的损耗也会增加, 可以通过适当 PCB 布局将热量传导到 PCB 板上, 
以达到减小芯片的温度。建议适当地增加 VCC 和 VEE 引脚的 PCB 覆铜, 优先最大程度地增加 VEE 的
连接。
• 如果系统有多层板设计, 建议在 VCC 和 VEE 层放置大量过孔连接, 以减小寄生参数。


# 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。
 http://www.chipanalog.com
