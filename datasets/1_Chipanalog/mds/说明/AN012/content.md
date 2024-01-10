# 基于 CA-IS3211x 的 100W 半桥降压转换器


# 1. Introduction 简介
CA-IS3211x 是一款光耦兼容型的单通道增强型隔离式栅极驱动器，可用于驱动 MOSFET、IGBT 和 SiC 器件。隔离等级达
到 5.7kVRMS，芯片可提供 5A 拉、6A 灌输出峰值电流能力。高达 30V 的电源电压范围允许使用双极性电源来有效驱动
IGBT 和 SiC 功率 FET。该芯片的性能亮点包括：高共模瞬态抗扰度（CMTI >150kV/us）、低传输延迟（Typ. 70ns）、低
脉冲宽度失真（Max.35ns）。严格的工艺控制使得芯片一致性较好。输入级是模拟二极管，与传统的光耦隔离栅极驱
动器的 LED 相比，具有更好的长期可靠性和老化特性。高性能和高可靠性使得该芯片适用于工业电源、光伏逆变器、
车载充电器、直流电机控制以及汽车空调与加热系统。CA-IS3211x 可以驱动高压侧及低压侧的功率管和支持输入互锁
配置，既能够完全兼容传统的光耦栅极驱动器，又显著提高了驱动的性能。
基于这款产品应用，我们设计一款 100W 半桥降压型转换器应用参考方案，采用两颗 CA-IS3211x 芯片分别驱动主开关
IGBT 和同步整流 IGBT，通过 MCU 控制高边和低边控制器的占空比和死区时间，既可调整占空比和频率，同时也保证
高低边功率管不会同时导通。


#  2. DEMO 实物图


# 3. Basic Configuration 基础配置
---table begin---
Table tile:AN0012基础配置表
HVDC Input  400V/0.3A
VCC Input  15V/0.3A
Output  48V/2A
Switching frequency 20kHz
PWM Duty cycle  12%
---table end---


# 4. Schematic 原理图


# 5 .PCB 版图文件


# 6. BOM 原料表
---table begin---
Table tile:AN0012原料表
-| Designator | Comment | Description | Footprint | Quantity |
|------------|---------|-------------|-----------|----------|
| A, B, C, D | M3 MACHINE SCREW | M3 Machine Screw | - | 4 |
| C1, C5, C28, C30, C32 | 10uF | 10uF/50V, MLCC | C0805_L | 5 |
| C2, C4, C6, C12, C14, C17, C22, C29, C33 | 0.1uF | 0.1uF/50V, MLCC | C0805_L | 9 |
| C3 | 10uF | 10uF/50V, MLCC | C0805_L | 1 |
| C8 | 2.2uF | 2.2uF/50V, MLCC | C0805_L | 1 |
| C9, C31 | 0.1uF | 0.1uF/50V, MLCC | C0805_L | 2 |
| C10 | 10nF | 10nF/500V, MLCC | C1206_L | 1 |
| C11, C13, C16, C21 | 1uF | 1uF/50V, MLCC | C0805_L | 4 |
| C15, C23 | NC | Capacitor | C0805_L | 2 |
| C20 | 0.1uF | 0.1uF/50V, MLCC | C1206_L | 1 |
| C24, C27 | 100nF | 100nF/50V, MLCC | C0805_L | 2 |
| C25, C26 | 1uF | 1uF/50V, MLCC | C0805_L | 2 |
| CE1 | 10uF | Electronic capacitor, 10uF/500V | WCAP-ATG5_13x20x5 | 1 |
| CE2, CE3, CE4 | 47uF | Electronic capacitor, 47uF/100V | WCAP-ATG5_13x20x5 | 3 |
| D1, D3 | NC | Diode, General | DIODE,SOD-123FL | 2 |
| D2, D4 | NC | Diode, TVS, SMAJ16CA | DIODE,SMA | 2 |
| J1, J2, J5 | - | Connector, Screw Terminal, 5.08, 2P | con,tbk,508-2p,molex￾0395443002 | 3 |
| J3, J10 | MCU | Header, Unshrouded, 2.54, Male, 8P | con,hdr,254-8p | 2 |
| J4, J6, J7, J8, J9 | - | Header, Unshrouded, 2.54, Male, 3P | con,hdr,254-3p | 5 |
| L1 | L1=2mH | Inductor, 2mH/10A | L, Vertical_27x56mm | 1 |
| Q1, Q3 | IKW40N120CS7 | IGBT, IKW40N120CS7, 80A/1200V | IGBT,THT,TO-247 | 2 |
| Q2, Q4 | 2N7002KW | NMOSFET, 2N7002KW, 300mA/60V | MFET,SMD,SOT23-3 | 2 |
| R1, R3, R7, R9 | 130R | 130R/0805, Resistor | R0805_L | 4 |
| R2, R8 | 10R | 10R/0805, Resistor | R0805_L | 2 |
| R4, R5, R10, R11 | NC | Resistor | R0805_L | 4 |
| R6 | 24K | 24k/1206, Resistor | R1206_L | 1 |
| R12, R13, R14 | 10k | 10k/0805, Resistor | R0805_L | 3 |
| TP1, TP4, TP6, TP8, TP9, TP12, TP13, TP16 | - | TEST POINT PC MINI .040"D BLK | tpt,keystone-5001 | 8 |
| TP2, TP3, TP5, TP7, TP10, TP11, TP14, TP15, TP17, TP18 | - | TEST POINT PC MINI .040"D RED | tpt,keystone-5000 | 10 |
| U1, U5 | QA151M1_1 | Double rail power resource +15V/-5V | QA151M1 | 2 |
| U2, U3 | IC, CA-IS3211x | IC, CA-IS3211VxJ, SOIC6-WB | SOIC6-WB | 2 |
| U4 | IC, AMS1117-5 | IC, 5V LDO | SOT223 | 1 |

---table end---



# 7. Key Parameters 关键参数测试
 驱动波形测试


# 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知的情况下，保
留因技术革新而改变上述资料的权利。
Chipanalog 产品全部经过出厂测试。 针对具体的实际应用，客户需负责自行评估，并确定是否适用。Chipanalog
对客户使用所述资源的授权仅限于开发所涉及 Chipanalog 产品的相关应用。 除此之外不得复制或展示所述资源， 如
因使用所述资源而产生任何索赔、 赔偿、 成本、 损失及债务等， Chipanalog 对此概不负责。


# 商标信息
Chipanalog Inc.®、Chipanalog®为 Chipanalog 的注册商标。



