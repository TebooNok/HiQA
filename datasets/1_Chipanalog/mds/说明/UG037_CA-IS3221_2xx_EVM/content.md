 # CA-IS3221x, CA-IS3222x 双通道栅极驱动器EVM 使用说明
 

#  1.描述
本文档主要描述了 CA-IS322x 评估板相关的使用说明, 其中包含产品介绍、原理图、PCB 布线图、物
料清单以及部分关键波形和数据等。该评估板可以用来简单评估 CA-IS3221xW、CA-IS3221xK、CA￾IS3221xN、CA-IS3222xW、CA-IS3222xK、CA-IS3222xN 的基本性能参数。


# 2.芯片简介
CA-IS322x 系列产品为双通道、隔离型栅极驱动器，可提供 6A 峰值灌电流、5A 峰值拉电流驱动。
这些器件支持高速切换，结合器件的超低传输延时(56ns，典型值)、超低脉宽失真等优势，使其成为
MOSFET、IGBT、SiC 等大功率晶体管驱动的理想选择，工作频率可达 5MHz，适用于各种逆变器、隔离
电源、电机驱动等应用。
所有器件采用川土特有的电容隔离技术，在内部集成数字隔离器。输入侧与驱动器输出侧通过二氧
化硅(SiO2)电容绝缘栅隔离，提供高达 3.75kVRMS (窄体 SOIC 封装)或 5.7kVRMS (宽体 SOIC 封装)的隔离耐
压(UL1577 认证),以及最小 100V/ns 的共模瞬态抗扰度(CMTI)。此外，内部电路在二次侧(输出侧)的驱动
器 A 与驱动器 B 之间提供功能隔离，可承受 1500V DC 工作电压。
CA-IS322x 系列栅极驱动器可以配置为双通道低边驱动、双通道高边驱动和半桥驱动，提供可编程
死区时间。使能控制(CA-IS3222 的 EN 引脚)和禁止控制(CA-IS3221 的 DIS 引脚)允许将驱动器 A 和驱动器
B 的输出快速拉至低电平，关断外部功率晶体管。另外，当输入侧或输出侧电源未上电或开路、或低于
UVLO 门限时，或当器件处于禁用状态时，驱动器输出置于默认状态：低电平；当输入信号开路时，驱
动器输出同样置于默认状态：低电平，关断外部功率管。
CA-IS322x 输入侧电源 VCCI 可接受 3V to 18V 供电范围，输出侧电源 VDD_可接受高达 25V 的供电电
压。该系列一共包含三个封装, CA-IS3221xW 和 CA-IS3222xW 为 SOIC16-WB 封装; CA-IS3221xK 和 CA￾IS3222xK 为 SOIC14-WB 封装; CA-IS3221xN 和 CA-IS3222xN 为 SOIC16-NB 封装; 客户可根据方案需求选择不
同封装类型的芯片。


# 3.BOM 清单
---table begin---
Table tile:UG037_CA-IS3221_2xx_EVMBOM 清单表
| Items | Designator | Description | Footprint | Quantity | Vendor |
|-------|------------|-------------|-----------|----------|--------|
| 1     | U1         | IC, CA-IS322x (SOIC16-WB, SOIC14-WB, SOIC16-NB) | SOIC16-WB/SOIC16-NB | 1 | Chipanalog |
| 2     | TP22, TP24, TP25, TP13, TP10, TP3, TP1 | INAR,INBR,SW,DT,DIS,INB,INA,TEST POINT YELLOW | tpt,keystone-5002 | 7 | Keystone |
| 3     | TP21, TP5, TP9, TP19 | HVDC,VCCI,OUTB,OUTA,TEST POINT RED | tpt,keystone-5000 | 4 | Keystone |
| 4     | TP11, TP16, TP23, TP2, TP6, TP12, TP14, TP26, TP27, TP7, TP15 | VSSA,VSSB,GND,TEST POINT BLK | tpt,keystone-5001 | 11 | Keystone |
| 5     | R25        | 100k/0805   | R0805_M  | 1 | - |
| 6     | R24        | 82k/0805    | R0805_M  | 1 | - |
| 7     | R23        | 62k/0805    | R0805_M  | 1 | - |
| 8     | R22        | 39k/0805    | R0805_M  | 1 | - |
| 9     | R21        | 20k/0805    | R0805_M  | 1 | - |
| 10    | R20        | 10k/0805    | R0805_M  | 1 | - |
| 11    | R8, R9, R12 | 0R/0805    | R0805_M  | 3 | - |
| 12    | R2, R6, R7, R14, R15, R32, R33 | NC         | R0805_M  | 7 | - |
| 13    | R1, R5     | 51R/0805   | R0805_M  | 2 | - |
| 14    | Q1_1, Q2_1 | MOSFET, N-FET, Single,TO220 | FET, TH, TO-220 | 2 | - |
| 15    | Q1, Q2     | IGB, single,TO247 | IGBT,THT,TO-247 | 2 | - |
| 16    | JP1, JP2   | Connector, Jumper, 2.54, 2p | con,jmp,254-2p | 2 | - |
| 17    | J14, J3, J4, J7, J12, J13 | VDDB,GND,VSSB,VCC,VSSA,VDDA | tpt,keystone-5019-SMD | 6 | Keystone |
| 18    | J6, J9     | Header, Unshrouded , 2.54, Male, 3P | con,hdr,254-3p | 2 | - |
| 19    | J5         | Header, Unshrouded , 2.54, Male, 6X2P | con,hdr,254-6X2P | 1 | - |
| 20    | J2, J10, J11 | Connector, Screw Terminal, 5.08, 2P | con,tbk,508-2p | 3 | - |
| 21    | J1         | Header, Unshrouded , 2.54, Male, 3x2P | con,hdr,254-3X2p | 1 | - |
| 22    | INB        | SMA interface' TPT,SMA-V- 5Pin | 1 | - |
| 23    | INA        | SMA interface' TPT,SMA-V- 5Pin | 1 | - |
| 24    | H1, H2, H3, H4 | A,B,C,D, 'MACHINE SCREW PAN PHILLIPS 4-40 | scw,NYPMS4400025PH | 4 | - |
| 25    | D2, D3     | Schottky, 30V/1A, SOD123 | DIODE,SOD-123 | 2 | - |
| 26    | C21, C22   | 180nF/50V/0805 | C0805_M | 2 | SAMSUNG |
| 27    | C16, C18   | 2.2uF/50V/0805 | C0805_M | 2 | SAMSUNG |
| 28    | C15        | 2.2nF/50V/0805 | C0805_M | 1 | SAMSUNG |
| 29    | C9, C14    | 1uF50V/0805 | C0805_M | 2 | SAMSUNG |
| 30    | C8, C17, C19 | 0.1uF/50V/0805 | C0805_M | 3 | SAMSUNG |
| 31    | C7, C20    |
---table end---


# 4.测试仪器
固纬电子 GPD-3303S 线性直流电源、500MHz 带宽示波器安捷伦 DSO6054A、61/2 位多功能数字万用
表 KEYSIGHT-34465A、SIGLENT-SDG1062X 高频信号发生器等。


#  5.硬件连接
1. 将 DC 直流电压源连接到 VCC 和 GND, VCC=3.3V/0.1A；VDDA-VSSA, VDDA=15V/0.1A；VDDB-VSSB,
VDDB=15V/0.1A；
2. 信号发生器输出一定频率、占空比和幅值的信号连接输入端 INA 和 INB；
3. 通过示波器测量输出端 OUTA 和 OUTB 信号。
图 10 展示了 SOIC16-WB 和 SOIC14-WB 封装的 EVM 硬件连接方式。图 11 展示了 SOIC16-NB 封装的 EVM
硬件连接方式。



# 6.关键参数测试
下面是以 CA-IS3221xW 为例, 测试一些典型波形, 包括输出上升&下降时间、传输延时、输出峰值电
流、信号传输、驱动 IGBT、死区控制功能等等。（除非特殊说明, Ta=25℃, VCC=3.3V 或 5V, VDDA=15V,
VDDB=15V, CVCC=1uF||100nF, CVDD=10uF||100nF, Cload=100pF/50V）
1、输出上升时间&下降时间
用户在测试前需要在 EVM 上短接 C4 和 C13 负载电容的 Pad，确保 1.8nF 负载电容的正确连接。
图 12 和图 13 展示了 OUTA 上升和下降时间波形。图 14 和图 15 展示了 OUTB 上升和下降时间波形。
注：(1) 波形通道设置 CH1:INA, CH2:INB, CH3:OUTA, CH4:OUTB.
(2) 上升&下降时间取输出边沿的 20%-80%.
2、传输延时
用户在测试前需确保负载电容没有连接。图 16 和图 17 展示了输入与输出之间的传输延时。
注：(1) 波形通道设置 CH1:INA, CH2:INB, CH3:OUTA, CH4:OUTB.
(2) tPDLH 传输延时取输入信号 IN 上升沿 50% 至输出信号 OUT 上升沿的 10%；tPDHL 传输延时取输
入信号 IN 下降沿 50% 至输出信号 OUT 下降沿的 90%；
3、输出峰值电流
用户在测试前需要在 EVM 上通过 JP1 和 JP2 跳冒连接 C21 和 C22 负载电容，确保 180nF 负载电容的正
确连接。通过测试输出上升或下降边沿的 dV/dt，计算出输出峰值电流 IOH 和 IOL。值得注意的是，当
用户测量 dV/dt 时，需要取刚开始上升或下降后 100ns 左右的时间开始计算。因为这个时刻芯片给负载
电容充电的电流最大。测试波形参考图 18-21,。计算公式如下：IOH or IOL=Cload*△V/△t.
注：(1) 波形通道设置 CH1:INA, CH2:INB, CH3:OUTA, CH4:OUTB.
4、信号传输
测试条件：VCC=5V，VDD-VSS=15V，INA=INB=100kHz 方波，INA 与 INB 的相位差 180 度，RDT=20kΩ，
无负载电容条件。下图 22 展示了 100kHz 信号传输过程波形。
注：(1) 波形通道设置 CH1:INA, CH2:INB, CH3:OUTA, CH4:OUTB.
5、驱动 IGBT
测试条件：VCC=5V，VDD-VSS=15V，fPWM=10kHz，驱动英飞凌 IGBT 管子(型号 K40MCS7)，
Ron/off=0ohm，Probe 直接测试 IGBT 的 G 和 E 的 lead。
图 23 展示了 VGE 驱动波形上升沿波形。图 24 展示了 VGE 驱动波形下降沿波形。
注：(1) 波形通道设置 CH1:IN, CH2:VGE
6、死区时间控制
• DT Pin 接 VCCI：
CA-IS322x 内置了死区时间控制，当 DT 接 VCC 时，输入与输出同相，允许两个通道之间输出交叠。如
下图 25 显示了 OUTA 和 OUTB 输出相位相同的波形。

注：(1) 波形通道设置 CH1:INA,CH2:OUTA,CH3:INB,CH4:OUTB
• DT 接 RDT 电阻（RDT=20 kΩ, RDT 接 R21）：
两个通道输出之间的死区时间根据以下条件设置：tDT（ns） = 10 × RDT （kΩ）。为了更好的实现抗噪性
和两个通道之间的死区时间匹配，我们建议在 RDT 电阻上并联一个（2.2nF 或以上）旁路电容。EVM 板
上已安装 2.2nF/50V 电容。图 26 显示了 OUTA 和 OUTB 之间有死区时间的输出波形。
注：(1) 波形通道设置 CH1:INA,CH2:OUTA,CH3:INB,CH4:OUTB


# 7.PCB 布线建议
为了达到 CA-IS322x 的最优性能，PCB 布局时需要遵循以下原则：
• 为了保证电源为稳定性和低噪声，低 ESR 和低 ESL 电容器必须靠近器件连接在 VCCI 和 GND 引脚之
间以及 VDD 和 VSS 引脚之间，以便在接通外部电源时支持高峰值电流。
• 为避免开关节点 VSSA 引脚上出现较大的负瞬变，需最小化上管的源极和下管的源极的走线，以减
小寄生电感效应。
• 当 MCU 与驱动芯片距离较远时，推荐尽可能靠近 EN 或 DIS 引脚处放置旁路电容，以减小噪声干
扰。
• 为确保初级侧和次级侧之间的隔离性能，应避免在芯片下方放置任何 PCB 走线、覆铜、焊盘和过
孔。建议使用 PCB 切口以防止污染该芯片的隔离性能。
• 用于半桥或高边/低边配置，通道 A 和通道 B 驱动器可以在高达 1500 VDC 的直流母线电压下工作，
应尝试增加 PCB 的爬电距离，即高压侧和低压侧 PCB 走线之间的布局。
• 当芯片驱动功率管时，OUT 存在非常高的 di/dt，OUT 环路 PCB 走线寄生电感会导致 EMI 和电压振
荡问题，故在设计 PCB 时，芯片应尽可能靠近功率管位置，OUT 走线尽可能宽，环路走线尽可能
短，以降低环路寄生电感。
• 当负载较重或开关频率较高时，芯片的损耗也会增加，可以通过适当 PCB 布局将热量传导到 PCB 板
上，以达到减小芯片的温度。建议适当地增加 VDD 和 VSS 引脚的 PCB 覆铜，优先最大程度地增加
VSS 的连接。
• 如果系统有多层板设计，建议在 VDD 和 VSS 层放置大量过孔连接，以减小寄生参数。


# 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。
 http://www.chipanalog.com
