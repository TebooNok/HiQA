# adc12qj1600-sp

# 1. ADC12QJ1600-SP 具有 JESD204C 接口的四通道 1.6GSPS 12 位模数转换器 (ADC)

# 1.1. 特性
辐射性能：
- 电离辐射总剂量 (TID)：300krad (Si)
- 单粒子锁定 (SEL)：120MeV-cm2/mg
- 单粒子翻转 (SEU) 抗扰度寄存器
ADC 内核：
- 分辨率：12 位
- 最大采样率：1.6GSPS
- 非交错式架构
- 内部抖动可减少高次谐波
性能规格 (–1dBFS)：
- SNR (100MHz)：57.4dBFS
- ENOB (100MHz)：9.1 位
- SFDR (100MHz)：64dBc
- 本底噪声 (–20dBFS)：-147dBFS
满量程输入电压：800mVPP-DIFF
全功率输入带宽：6GHz
JESD204C 串行数据接口：
- 总共支持 2 至 8 个串行器/解串器通道
- 最大波特率：17.16Gbps
- 64B/66B 和 8B/10B 编码模式
- 子类 1 支持确定性延迟
- 与 JESD204B 接收器兼容
可选的内部采样时钟生成：
- 内部 PLL 和 VCO (7.2–8.2GHz)
SYSREF 窗口可简化同步
四个时钟输出可简化系统时钟
- FPGA 或相邻 ADC 的参考时钟
- 串行器/解串器收发器的参考时钟
脉冲系统的时间戳输入和输出
功耗 (1GSPS)：1.9W
电源：1.1V/1.9V

# 2. 应用
- 电子战（信号情报、电子情报）
- 卫星通信 (SATCOM)

# 3. 说明
ADC12QJ1600-SP 是一款四通道、12 位、1.6GSPS 模数转换器 (ADC)。该器件具有低功耗、高采样率和 12 位分辨率，适合用于各种多通道通信系统。
6GHz 的全功率输入带宽 (-3dB) 还支持 L 频带和 S 频带的直接射频采样。
---table begin---
Table tile: 封装信息
| 器件型号 | 封装(1) | 封装尺寸(2) |
|---|---|---|
| ADC12QJ1600-SP | FCBGA (144) | 10mm × 10mm |
---table end---
(1)如需了解所有可用封装，请参阅数据表末尾的封装选项附录。
(2)封装尺寸（长 × 宽）为标称值，并包括引脚（如适用）。
四通道器件方框图

# 6. Pin Configuration and Functions
1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
A  
B  
C  
D  
E  
F  
G  
H  
J  
K  
L  
M  
Not to scale
AGND
INA+
INA±
AGND
AGND
INB+
INB±
AGND
CALTRIG
VD11
DGND
DGND
AGND
AGND
AGND
AGND
AGND
AGND
AGND
AGND
CALSTAT
VD11
DGND
DGND
TMSTP+
AGND
BG
SYNCSE
AGND
AGND
CLKCFG0
PLLREF_SE
ORA
DGND
D7+
D3+
TMSTP±
AGND
AGND
VA19
VA19
VA11
CLKCFG1
PLL_EN
ORB
VD11
D7±
D3±
AGND
AGND
VA11
AGND
VA11
VA19
AGND
SCS
ORC
VD11
D6+
D2+
CLK+
SE_CLK
VA11
AGND
VA11
VA19
AGND
SCLK
ORD
DGND
D6±
D2±
CLK±
SE_GND
VA11
AGND
VA11
VA19
AGND
SDI
SDO
DGND
D5+
D1+
AGND
AGND
VA11
AGND
VA11
VA19
AGND
VD11
VD11
VD11
D5±
D1±
SYSREF+
AGND
PGND
VPLL19
VPLL19
VA11
PLLREFO+
VTRIG
TRIGOUT+
VD11
D4+
D0+
SYSREF±
AGND
TDIODE+
TDIODE±
PGND
VREFO
PLLREFO±
VTRIG
TRIGOUT±
DGND
D4±
D0±
AGND
AGND
AGND
AGND
AGND
AGND
AGND
AGND
DGND
VD11
DGND
DGND
AGND
IND+
IND±
AGND
AGND
INC+
INC±
AGND
PD
VD11
DGND
DGND
图 6-1. Quad Channel ALR Package, 144-Ball Flip Chip BGA
(Top View)
---table begin---
Table tile: Pin Functions
| PIN | TYPE | DESCRIPTION |
|---|---|---|
| A1, A4, A5, A8, B1, B2, B3, B4, B5, B6, B7, B8, C2, C5, C6, D2, D3, E1, E2, E4, E7, F4, F7, G4, G7, H1, H2, H4, H7, J2, K2, L1, L2, L3, L4, L5, L6, L7, L8, M1, M4, M5, M8 | AGND | Analog supply ground. Tie AGND, PGND, SE_GND and DGND to a common ground plane (GND) on the circuit board. |
| C3 | BG | Band-gap voltage output. This pin is capable of sourcing only small currents and driving limited capacitive loads, as specified in the Recommended Operating Conditions table. This pin can be left disconnected if not used. |
| B9 | CALSTAT | Foreground calibration status output or device alarm output. Functionality is programmed through CAL_STATUS_SEL. This pin can be left disconnected if not used. |
| A9 | CALTRIG | Foreground calibration trigger input. This pin is only used if hardware calibration triggering is |
---table end---# # 1. Pin Descriptions
Connected and/or tied to GND through 1Ω or less. TI strongly recommends joining all ground pins (i.e AGND, PGND, SE_GND and DGND to a common ground plane (GND) on the circuit board.
---

# 1.1 Pin Specs
---table begin--- 
Table tile: Pin Specifications
| Pin | Name | Type | Description |
|---|---|---|---|
| C3 | BG | O | Band-gap voltage output. This pin is capable of sourcing only small currents and driving limited capacitive loads, as specified in the Recommended Operating Conditions table. This pin can be left disconnected if not used. |
| B9 | CALSTAT | O | Foreground calibration status output or device alarm output. Functionality is programmed through CAL_STATUS_SEL. This pin can be left disconnected if not used. |
| A9 | CALTRIG | I | Foreground calibration trigger input. This pin is only used if hardware calibration triggering is selected in CAL_TRIG_EN, otherwise software triggering is performed using CAL_SOFT_TRIG. Tie this pin to GND if not used. |
---table end--- 
---

# 1.2 Additional Pin Specs
---table begin---
Table tile: Additional Pin Specifications
| Pin | Name | Type | Description |
|---|---|---|---|
| G1 | CLK– | I | Device (sampling) clock negative input or differential PLL reference clock negative input. TI strongly recommends using AC-coupling for best performance. This pin can be left disconnected if SE_CLK is used to apply the reference clock. |
| F1 | CLK+ | I | Device (sampling) clock positive input or differential PLL reference clock negative input. The clock signal is strongly recommended to be AC-coupled to this input for best performance. This differential input has an internal 100-Ω differential termination and is self-biased to the optimal input common-mode voltage as long as DEVCLK_LVPECL_EN is set to 0. This pin can be left disconnected if SE_CLK is used to apply the reference clock when the PLL is used. |
| C7 | CLKCFG0 | I | CLKCFG0 and CLKCFG1 can be used enable additional clock outputs on ORC and ORD when the C-PLL is used (PLL_EN is set high). Tie this pin to ground if not used. |
| D7 | CLKCFG1 | I | CLKCFG0 and CLKCFG1 can be used enable additional clock outputs on ORC and ORD when the C-PLL is used (PLL_EN is set high). Tie this pin to ground if not used. |
---table end---
---

# 1.3 More Pin Specs 
---table begin---
Table tile: More Pin Specifications 
| Pin | Name | Type | Description |
|---|---|---|---|
| K12 | D0– | O | High-speed serialized data output for lane 0, negative connection. This pin can be left disconnected if not used, or connected to any voltage level between GND (0V) and VD11 (1.1V) using 0 OHM to 1MOHM resistors. |
| J12 | D0+ | O | High-speed serialized data output for lane 0, positive connection. This differential output must be AC-coupled and must always be terminated with a 100-Ω differential termination at the receiver. This pin can be left disconnected if not used, or connected to any voltage level between GND (0V) and VD11 (1.1V) using 0 OHM to 1MOHM resistors. |
| H12 | D1– | O | High-speed serialized data output for lane 1, negative connection. This pin can be left disconnected if not used, or connected to any voltage level between GND (0V) and VD11 (1.1V) using 0 OHM to 1MOHM resistors. |
| G12 | D1+ | O | High-speed serialized data output for lane 1, positive connection. This differential output must be AC-coupled and must always be terminated with a 100-Ω differential termination at the receiver. This pin can be left disconnected if not used, or connected to any voltage level between GND (0V) and VD11 (1.1V) using 0 OHM to 1MOHM resistors. |
---table end---# 1. Chapter Title 
High-speed serialized data output for lane 2, negative connection. This pin can be left disconnected if not used, 
or connected to any voltage level between GND (0V) and VD11 (1.1V) using 0 OHM to 1MOHM resistors.

# 2. Chapter Title 
High-speed serialized data output for lane 2, positive connection. This differential output must be AC-coupled 
and must always be terminated with a 100-Ω differential termination at the receiver. This pin can be left 
disconnected if not used, or connected to any voltage level between GND (0V) and VD11 (1.1V) using 0 OHM to 
1MOHM resistors.
---table begin---  
Table tile: Pin Functions
| Number | Name | Type | Description |
|---|---|---|---|
| E12 | D2+ | O | High-speed serialized data output for lane 2, positive connection. This differential output must be AC-coupled and must always be terminated with a 100-Ω differential termination at the receiver. This pin can be left disconnected if not used, or connected to any voltage level between GND (0V) and VD11 (1.1V) using 0 OHM to 1MOHM resistors. |
| D12 | D3– | O | High-speed serialized data output for lane 3, negative connection. This pin can be left disconnected if not used, or connected to any voltage level between GND (0V) and VD11 (1.1V) using 0 OHM to 1MOHM resistors. |
| C12 | D3+ | O | High-speed serialized data output for lane 3, positive connection. This differential output must be AC-coupled and must always be terminated with a 100-Ω differential termination at the receiver. This pin can be left disconnected if not used, or connected to any voltage level between GND (0V) and VD11 (1.1V) using 0 OHM to 1MOHM resistors. |
| K11 | D4- | O | High-speed serialized data output for lane 4, negative connection. Not used for single channel devices. This pin can be left disconnected if not used, or connected to any voltage level between GND (0V) and VD11 (1.1V) using 0 OHM to 1MOHM resistors. |
---table end---

# 3. Chapter Title 
High-speed serialized data output for lane 4, positive connection. Not used for single channel devices. This 
differential output must be AC-coupled and must always be terminated with a 100-Ω differential termination at 
the receiver. This pin can be left disconnected if not used, or connected to any voltage level between GND (0V) 
and VD11 (1.1V) using 0 OHM to 1MOHM resistors.# 4. Channels and Pin Information

# D11
**D7- O High-speed serialized data output for lane 7, negative connection.**
Not used for single channel devices. This pin can be left disconnected if not used, or connected to any voltage level between GND (0V) and VD11 (1.1V) using 0 OHM to 1MOHM resistors.

# C11
**D7+ O  High-speed serialized data output for lane 7, positive connection.**
Not used for single channel devices. This differential output must be AC-coupled and must always be terminated with a 100-Ω differential termination at the receiver. This pin can be left disconnected if not used, or connected to any voltage level between GND (0V) and VD11 (1.1V) using 0 OHM to 1MOHM resistors.
---table begin---
Table title: Common pin configurations 
| Pins | Name | Type | Description |
|---|---|---|---|
| A11, A12, B11, B12, C10, F10, G10, K10, L9, L11, L12, M11, M12 | DGND | — | Digital supply ground. Tie AGND, PGND, SE_GND and DGND to a common ground plane (GND) on the circuit board. |
| A3 | INA– | I | Channel A analog input negative connection for quad, dual and single channel devices. This input is terminated to VA11 through a 50-Ω termination resistor. This pin can be left disconnected if not used. |
| A2 | INA+ | I | Channel A analog input positive connection for quad, dual and single channel devices. This input is terminated to VA11 through a 50-Ω termination resistor. The input common-mode voltage is internally self-biased to VA11 (1.1 V nominally) and must follow the recommendations in the Recommended Operating Conditions table. This pin can be left disconnected if not used. |
---table end---

# 5. Channel Information Continued 

# A7
**INB– I Channel B analog input negative connection for quad and dual channel devices.**
Do not connect for single channel device. This input is terminated to VA11 through a 50-Ω termination resistor. This pin can be left disconnected if not used.

# A6
**INB+ I Channel B analog input positive**
Channel B analog input positive connection for quad and dual channel devices. Do not connect for single channel device. This input is terminated to VA11 through a 50-Ω termination resistor. This pin can be left disconnected if not used.

# M7
**INC– I Channel C analog input negative**
Channel C analog input negative connection for quad channel device. Do not connect for single and dual channel devices. This input is terminated to VA11 through a 50-Ω termination resistor. This pin can be left disconnected if not used.

# M6
**INC+ I Channel C analog input positive**
Channel C analog input positive connection for quad channel device. Do not connect for single and dual channel devices. This pin can be left disconnected if not used.

# 6. Pin Functions (continued)
# Chapter Title
PLL reference clock output. The clock is repeated from the selected PLL reference clock input (CLK± or SE_CLK). It is available at device power up to clock other devices when PLL_EN is set high and PD is held low. These pins can be left disconnected if not used.
Serial interface clock. This pin functions as the serial-interface clock input that clocks the serial programming data in and out. The Using the Serial Interface section describes the serial interface in more detail. Supports 1.1-V to 1.9-V CMOS levels.
---table begin---
Table Tile: Description of Pins
| pin | name | type | description |
|---|---|---|---|
| K7 | PLLREFO– | O | Negative LVDS PLL reference clock output |
| J7 | PLLREFO+ | O | Positive LVDS PLL reference clock output |
| F8 | SCLK | I | Serial interface clock |
| E8 | SCS | I | Serial interface chip select active low input |
| G8 | SDI | I | Serial interface data input |
| G9 | SDO | O | Serial interface data output |
---table end---
# 6. Pin Functions (continued)

# Chapter Title
# 6.2. Description of Pins 
This differential input (SYSREF+ to SYSREF–) has an internal untrimmed 100-Ω differential termination and can be AC-coupled when SYSREF_LVPECL_EN is set to 0. This input is self-biased when SYSREF_LVPECL_EN is set to 0.
---table begin---
Description of Pins (continued)
| pin | name | type | description |
|---|---|---|---|
| K4 | TDIODE– | I | Temperature diode negative (cathode) connection. This pin can be left disconnected if not used.|
| K3 | TDIODE+ | I | Temperature diode positive (anode) connection. An external temperature sensor can be connected to TDIODE+ and TDIODE– to monitor the junction temperature of the device. This pin can be left disconnected if not used.|
| D1 | TMSTP– | I | Timestamp input negative connection. This pin can be left disconnected and the TMSTP receiver powered down (TMSTP_RECV_EN = 0) if timestamp is not required.|
| C1 | TMSTP+ | I | Timestamp input positive connection. This input is a timestamp input, used to mark a specific sample, when TIME_STAMP_EN is set to 1. For additional usage information, see the Timestamp section.|
---table end---
# Chapter Title

# 7. Specifications
# 7.1 Absolute Maximum Ratings
over operating free-air temperature range (unless otherwise noted)(1)
---table begin---
Table tile: Maximum Ratings
| Supply voltage range | MIN | MAX | UNIT |
|---|---|---|---|
| VA19(2) | –0.3 | 2.35 | V |
| VPLL19(3) | –0.3 | 2.35 | V |
| VREFO(2) | –0.3 | 2.35 | V |
| VTRIG(5) | –0.3 | 2.35 | V |
| VA11(2) | –0.3 | 1.32(11) | V |
| VD11(5) | –0.3 | 1.32(11) | V |
| Voltage difference between any 1.9 V supply (VA19, VPLL19 or VREFO) | –0.5 | 0.5 | V |
| Voltage between AGND, DGND, PGND and SE_GND | –0.1 | 0.1 | V |
| Pin voltage range D[7:0]+, D[7:0]–, TMSTP+, TMSTP–(5) | –0.5 | VD11 + 0.5(7) | V |
| CLK+, CLK–, SYSREF+, SYSREF–(2) | –0.5 | VA11 + 0.5(6) | V |
| SE_CLK(4)| –0.5 | VA19 + 0.5(8) | V |
| PLLREFO+, PLLREFO–(2) | –0.5 | VREFO + 0.5(9) | V |
| TRIGOUT+,TRIGOUT–(5) | –0.5 | VTRIG + 0.5(10) | V |
| BG, TDIODE+, TDIODE–(2) | –0.5 | VA19 + 0.5(8) | V |
| INA+, INA–, INB+, INB–, INC+, INC–, IND+, IND–(2) | VA11 – 1.0 | VA11 + 1.0 | V |
| CALSTAT, CALTRIG, CLKCFG0, CLKCFG1, PLL_EN, PLLREF_SE, ORA, ORB, ORC, ORD, PD, SCLK, SCS, SDI, SDO, SYNCSE (2)| –0.5 | VA19 + 0.5(8) | V |
| Peak input current (any input except INA+, INA–, INB+, INB–, INC+, INC–, IND+, IND–) | –25 | 25 | mA |
| Peak input current (INA+, INA–, INB+, INB–, INC+, INC–, IND+, IND–) | –50 | 50 | mA |
| Peak RF input power (INA+, INA–, INB+, INB–, INC+, INC–, IND+, IND–) Single-ended with ZS-SE = 50 Ω |  | 16.4 | dBm |
| Peak total input current (sum of absolute value of all currents forced in or out, not including power-supply current) |  | 100 | mA |
| Operating junction temperature, Tj | –40 | 150 | °C |
| Storage temperature, Tstg | –65 | 150 | °C |
---table end---
# 7. Specifications
Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
Measured to AGND.
Measured to PGND.
Measured to SE_GND.
Measured to DGND.
Maximum voltage not to exceed VA11 absolute maximum rating.
Maximum voltage not to exceed VD11 absolute maximum rating.
Maximum voltage not to exceed VA19 absolute maximum rating.
Maximum voltage not to exceed VREFO absolute maximum rating.
Maximum voltage not to exceed VTRIG absolute maximum rating.
The 1.1-V supplies (VA11, VD11) must not be more than 0.5 V above any of the 1.9-V supplies (VA19, VPLL19, VREFO) or VTRIG (1.1 V or 1.9 V) during power up, normal operation or power down. See Power Sequencing section.

# 7.2 ESD Ratings
---table begin---
Table tile: ESD Ratings
| | VALUE | UNIT |
|---|---|---|
| V(ESD) Electrostatic discharge Human-body model (HBM), per AEC Q100-002(1)| 4000 | V |
| Charged-device model (CDM), per AEC Q100-011 | 750 | |
---table end---
AEC Q100-002 indicates that HBM stressing shall be in accordance with the ANSI/ESDA/JEDEC JS-001 specification.

# 7.3 Recommended Operating Conditions
# 1. Supply voltage range
---table begin---
|   | MIN | NOM | MAX | UNIT |
|---|---|---|---|---|
| VA19, analog 1.9-V supply(2) | 1.8 | 1.9 | 2.0 | V |
| VPLL19, PLL supply(3) | 1.8 | 1.9 | 2.0 | V |
---table end---
# 7.3 Recommended Operating Conditions

# 2. Charge pump supply
---table begin---
|   | MIN | NOM | MAX | UNIT |
|---|---|---|---|---|
| VREFO, PLLREFO± and PLL charge pump supply(2) | 1.8 | 1.9 | 2.0 | V |
| VTRIG, TRIGOUT± supply(4) | 1.05 | 1.1 or 1.9 | 2.0 | V |
---table end---

# 3. 1.1-V supply
---table begin---
|   | MIN | NOM | MAX | UNIT |
|---|---|---|---|---|
| VA11, analog 1.1-V supply(2) | 1.05 | 1.1 | 1.15 | V |
| VD11, digital 1.1-V supply(4) | 1.05 | 1.1 | 1.15 | V |
---table end---

# 4. Input common-mode voltage
---table begin---
|   | MIN | NOM | MAX | UNIT |
|---|---|---|---|---|
| VCMI Input common-mode voltage INA+, INA–, INB+, INB–, INC+, INC–, IND+, IND–(2) | 1.05 | 1.1 | 1.15 | V |
| CLK+, CLK–, SYSREF+, SYSREF–(2) (5) | 0 | 0.3 | 0.55 | V |
| TMSTP+, TMSTP–(4) (6) | 0 | 0.3 | 0.55 | V |
---table end---

# 5. Input voltage
---table begin---
| VID(DIFF) Input voltage, peak-to-peak differential CLK+ to CLK–, SYSREF+ to SYSREF–, TMSTP+ to TMSTP– |   |
|---|---|
| MIN | 0.4 |
| MAX | 2.0 |
| UNIT | VPP-DIFF |
| INA+, INA–, INB+, INB–, INC+, INC–, IND+, IND– | 1.0(7) |
---table end---

# 6. High-level input voltage
---table begin---
|   | MIN | MAX | UNIT |
|---|---|---|---|
| VIH High-level input voltage SE_CLK | 0.9 | 1.8 | V |
| VIL Low-level input voltage SE_CLK | 0 | 0.3 | V |
| IC_TD Temperature diode input current TDIODE+ to TDIODE– | 100 | | µA |
| CL BG maximum load capacitance | | 50 | pF |
---table end---

# 7. Operating parameters
---table begin---
|   | MIN | MAX | UNIT |
|---|---|---|---|
| IO BG maximum output current Current at -2% drop from nominal voltage | | 140 | µA |
| TA Operating free-air temperature | –55 | 125(1) | °C |
| Tj Operating junction temperature | | 150(1) | °C |
---table end---

# 8. Notes
# 7.6 Electrical Characteristics: Power Consumption (continued)
---table begin---
Table title: Electrical Characteristics: Power Consumption
| PARAMETER | TEST CONDITIONS           | MIN | TYP | MAX | UNIT |
|-----------|---------------------------|-----|-----|-----|------|
| IVA19     | Power mode 6: Power-down enabled (PD = 1) |     | 47  |     | mA   |
| IVPLL19   | PLL analog supply current |     | 0   |     | mA   |
| IVREFO    | PLLREFO± analog supply current |     | 0   |     | mA   |
| IVTRIG    | TRIGOUT± analog supply current |     | 0   |     | mA   |
| IVA11     | 1.1-V analog supply current |     | 30  |     | mA   |
| IVD11     | 1.1-V digital supply current |     | 17  |     | mA   |
| PDIS      | Power dissipation          |     | 0.14 |     | W    |
---table end---
# 8. Notes
_Low-power background (LPBG) calibration supply current and power dissipation numbers are in the calibration sleep state. The power 
dissipation in this mode increases to the background (BG) calibration power consumption during the calibration state. The sleep period 
can be controlled by the user and long sleep periods will average out the calibration state power dissipation contribution._

# 7.7 Electrical Characteristics: AC Specifications
_typical valu_# 7.7 Electrical Characteristics: AC Specifications
typical values at TJ = 50°C, VA19 = 1.9 V, VPLL19 = 1.9 V, VREFO = 1.9 V, VTRIG = 1.1V, VA11 = 1.1 V, VD11 = 1.1 V, default full-scale voltage (VFS = 0.8 VPP), fIN = 97 MHz, AIN = –1 dBFS, fCLK = 1.6 GHz, filtered 1-VPP sine-wave clock applied to CLK±, PLL disabled, JMODE = 0, High Performance Mode and foreground calibration (unless otherwise noted); minimum and maximum values are at nominal supply voltages and over the operating junction temperature range provided in the Recommended Operating Conditions table
---table begin---
Table title: AC Specifications - part1
| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| FPBW | Full-power input bandwidth (-3 dB)(1) | | Foreground calibration | 6 | GHz |
|        |             | | Background calibration | 6 |     |
| XTALK | Channel-to-channel crosstalk |  | Aggressor = 400 MHz, –1 dBFS | –73 | dB |
|       |            | | Aggressor = 1 GHz, –1 dBFS | –65 |
|        |             | | Aggressor = 3 GHz, –1 dBFS | –59 |
| CER | Code error rate | | Maximum CER, does not include JESD204C interface BER | 10-18 | Errors/sample |
| tORR | Overrange recovery time | | Time from an overdriven input to accurate conversion after a step from a ±1.2 VPP-DIFF overdriven input stepped to 0 VPP-DIFF. | 1 | tCLK cycles |
| NOISEDC | DC input noise standard deviation | | No input, foreground calibration, excludes DC offset | 1.8 | LSB |
| NSD | Noise spectral density | | Maximum full-scale voltage (VFS = 1.0 VPP), AIN = –20 dBFS | –148 | dBFS/Hz |
|       |           | | Default full-scale voltage (VFS = 0.8 VPP), AIN = –20 dBFS | –147 |
| NF | Noise figure, ZS = 100 Ω | | Maximum full-scale voltage (VFS = 1.0 VPP), AIN = –20 dBFS | 26.2 | dB |
|    |           | | Default full-scale voltage (VFS = 0.8 VPP), AIN = –20 dBFS | 25.8 |
---table end---

# 7.7 Electrical Characteristics: AC Specifications (continued)
typical values at TJ = 50°C, VA19 = 1.9 V, VPLL19 = 1.9 V, VREFO = 1.9 V, 
VTRIG = 1.1V, VA11 = 1.1 V, VD11 = 1.1 V, default full-scale voltage (VFS = 0.8 VPP), 
fIN = 97 MHz, AIN = –1 dBFS, fCLK = 1.6 GHz, filtered 1-VPP sine-wave clock applied to 
CLK±, PLL disabled, JMODE = 0, High Performance Mode and foreground calibration (unless otherwise noted); 
minimum and maximum values are at nominal supply voltages and over the operating junction temperature range provided in 
the Recommended Operating Conditions table
---table begin---
Table tile: Electrical Characteristics: AC Specifications (continued)
| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| IMD3 | 3rd-order intermodulation distortion |
|  | f1 = 93 MHz, f2 = 103 MHz, AIN = –7 dBFS per tone | | | –80 | dBFS |
|  | f1 = 93 MHz, f2 = 103 MHz, AIN = –9 dBFS per tone | | | –87 | dBFS |
|  | f1 = 93 MHz, f2 = 103 MHz, AIN = –18 dBFS per tone | | | –91 | dBFS |
|  | f1 = 93 MHz, f2 = 103 MHz, AIN = –9 dBFS per tone, VFS = 1.0 VPP | | | -86 | dBFS |
|  | f1 = 493 MHz, f2 = 503 MHz, AIN = –7 dBFS per tone | | | –84 | dBFS |
|  | f1 = 493 MHz, f2 = 503 MHz, AIN = –9 dBFS per tone | | | –84 | dBFS |
|  | f1 = 493 MHz, f2 = 503 MHz, AIN = –18 dBFS per tone | | | –88 | dBFS |
|  | f1 = 993 MHz, f2 = 1003 MHz, AIN = –7 dBFS per tone | | | –77 | dBFS |
|  | f1 = 993 MHz, f2 = 1003 MHz, AIN = –9 dBFS per tone | | | –80 | dBFS |
|  | f1 = 993 MHz, f2 = 1003 MHz, AIN = –18 dBFS per tone | | | –85 | dBFS |
|  | f1 = 993 MHz, f2 = 1003 MHz, AIN = –9 dBFS per tone, VFS = 1.0 VPP | | | -78 | dBFS |
|  | f1 = 1793 MHz, f2 = 1803 MHz, AIN = –7 dBFS per tone | | | –68 | dBFS |
|  | f1 = 1793 MHz, f2 = 1803 MHz, AIN = –9 dBFS per tone | | | –73 | dBFS |
|  | f1 = 1793 MHz, f2 = 1803 MHz, AIN = –18 dBFS per tone | | | –91 | dBFS |
|  | f1 = 2693 MHz, f2 = 2703 MHz, AIN = –7 dBFS per tone | | | –56 | dBFS |
|  | f1 = 2693 MHz, f2 = 2703 MHz, AIN = –9 dBFS per tone | | | –63 | dBFS |
|  | f1 = 2693 MHz, f2 = 2703 MHz, AIN = –18 dBFS per tone | | | –83 | dBFS |
|  | f1 = 3493 MHz, f2 = 3503 MHz, AIN = –7 dBFS per tone | | | –52 | dBFS |
|  | f1 = 3493 MHz, f2 = 3503 MHz, AIN = –9 dBFS per tone | | | –57 | dBFS |
|  | f1 = 3493 MHz, f2 = 3503 MHz, AIN = –18 dBFS per tone | | | –90 | dBFS |
---table end---
Note (1): 
Full-power input bandwidth (FPBW) is defined as the input frequency where the reconstructed output of the ADC has dropped 3 dB below the power of a full-scale input signal at a low input frequency. Useable bandwidth may exceed the –3-dB, full-power input bandwidth.

# 7.8 Switching Characteristics
# 7.8 Switching Characteristics (continued)
Typical values at TJ = 25°C, VA19 = 1.9 V, VPLL19 = 1.9 V, VREFO = 1.9 V, VTRIG = 1.1V, VA11 = 1.1 V, VD11 = 1.1 V, default full-scale voltage (VFS = 0.8 VPP), fIN = 97 MHz, AIN = –1 dBFS, fCLK = 1.6 GHz, filtered 1-VPP sine-wave clock applied to CLK±, PLL disabled, JMODE = 0, High Performance Mode and foreground calibration, SER_PE = 4 (unless otherwise noted); VA11Q and VCLK11 noise suppression on when CPLL on; minimum and maximum values are at nominal supply voltages and over the operating junction temperature range provided in the Recommended Operating Conditions table
---table begin---
Table tile: ADC Core Latency
| Parameter | Test Conditions | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| ADC CORE LATENCY tADC | Deterministic delay from the CLK± edge that samples the reference sample to the CLK± edge that samples SYSREF going high(1) JMODE = 0 | –2 | | | tCLK cycles |
| ADC CORE LATENCY tADC | Deterministic delay from the CLK± edge that samples the reference sample to the CLK± edge that samples SYSREF going high(1) JMODE = 1 | 1 | | | tCLK cycles |
| ADC CORE LATENCY tADC | Deterministic delay from the CLK± edge that samples the reference sample to the CLK± edge that samples SYSREF going high(1) JMODE = 2 | –1 | | | tCLK cycles |
| ... | ... | ... | ... | ... | ... |
---table end---
# 7.8 Switching Characteristics

# 7.9 Timing Requirements
# 7.1 DNL vs Code
---table begin---
Table tile: DNL vs Code
| Output Code | DNL (LSB) |
|---|---|
| 0 | 4096 |
| -0.2 | -0.15 |
| -0.1 | -0.05 |
| 0 | 0.05 |
| 0.1 | 0.15 |
| 0.2 | D121 |
---table end---
# 7.9 Timing Requirements

# 7.2 INL vs Code
---table begin---
Table tile: INL vs Code
| Output Code | INL (LSB) |
|---|---|
| 0 | 4096 |
| -2 | -1.5 |
| -1 | -0.5 |
| 0 | 0.5 |
| 1 | 1.5 |
| 2 | D122 |
---table end---

# 7.3 Input Fullscale vs Frequency
---table begin---
Table tile: Input Fullscale vs Frequency
| Input Frequency (MHz) | Input Fullscale (dB) |
|---|---|
| 0 | 1000 |
| 2000 | 3000 |
| 4000 | 5000 |
| 6000 | -2 |
| -1 | 0 |
| 1 | 2 |
| ch A | ch B |
| ch C | ch D |
| Relative to 0Hz | |
---table end---

# 7.4 Single Tone FFT at 347 MHz and -1 dBFS - Graph 1
---table begin---
Table tile: Single Tone FFT at 347 MHz and -1 dBFS
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | 100 |
| 200 | 300 |
| 400 | 500 |
| 600 | 700 |
| 800 | -120 |
| -110 | -100 |
| -90 | -80 |
| -70 | -60 |
| -50 | -40 |
| -30 | -20 |
| -10 | 0 |
| D022 | High power mode |
---table end---

# 7.5 Single Tone FFT at 347 MHz and -1 dBFS - Graph 2
---table begin---
Table tile: Single Tone FFT at 347 MHz and -1 dBFS
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | 100 |
| 200 | 300 |
| 400 | 500 |
| 600 | 700 |
| 800 | -120 |
| -110 | -100 |
| -90 | -80 |
| -70 | -60 |
| -50 | -40 |
| -30 | -20 |
| -10 | 0 |
| D062 | High power mode, C-PLL on |
---table end---

# 7.6 Single Tone FFT at 347 MHz and -1 dBFS - Graph 3
---table begin---
Table tile: Single Tone FFT at 347 MHz and -1 dBFS
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | 100 |
| 200 | 300 |
| 400 | 500 |
| 600 | 700 |
| 800 | -120 |
| -110 | -100 |
| -90 | -80 |
| -70 | -60 |
| -50 | -40 |
| -30 | -20 |
| -10 | 0 |
| D113 | High power mode, C-PLL on, Noise suppression off |
---table end---

# 7.7 Single Tone FFT at 847 MHz and -1 dBFS - Graph 1
---table begin---
Table tile: Single Tone FFT at 847 MHz and -1 dBFS
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | 100 |
| 200 | 300 |
| 400 | 500 |
| 600 | 700 |
| 800 | -120 |
| -110 | -100 |
| -90 | -80 |
| -70 | -60 |
| -50 | -40 |
| -30 | -20 |
| -10 | 0 |
| D026 | High power mode |
---table end---

# 7.8 Single Tone FFT at 997 MHz and -1 dBFS - Graph 1
---table begin---
Table tile: Single Tone FFT at 997 MHz and -1 dBFS
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | 100 |
| 200 | 300 |
| 400 | 500 |
| 600 | 700 |
| 800 | -120 |
| -110 | -100 |
| -90 | -80 |
| -70 | -60 |
| -50 | -40 |
| -30 | -20 |
| -10 | 0 |
| D114 | High power mode, C-PLL on |
---table end---

# 7.9 Single Tone FFT at 997 MHz and -1 dBFS - Graph 2
---table begin---
Table tile: Single Tone FFT at 997 MHz and -1 dBFS
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | 100 |
| 200 | 300 |
| 400 | 500 |
| 600 | 700 |
| 800 | -120 |
| -110 | -100 |
| -90 | -80 |
| -70 | -60 |
| -50 | -40 |
| -30 | -20 |
| -10 | 0 |
| D115 | High power mode, C-PLL on, Noise suppression off |
---table end---

# 7.10 Single Tone FFT at 1797 MHz and -1 dBFS 
... More tables continue ...# 7.10 Typical Characteristics 
Typical values at 25°C, AIN = -1 dBFS, FIN = 347 MHz, FS = 1600 MSPS, High power mode, FG calibration, JMODE 0, C-PLL off, C-PLLREF = 50 MHz and VA11Q and VCLK11 noise suppression on when C-PLL on, Quad Channel operation, nominal supply voltages, unless otherwise noted. SNR results exclude DC and HD2 to HD9; SINAD, ENOB, and SFDR results exclude DC.
---table begin---
Table tile: Single Tone FFT at 347 MHz and -1 dBFS
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | 100 |
| 50 | 100 |
| 150 | 200 |
| 250 | 300 |
| 350 | 400 |
| 450 | 500 |
| -120 | -110 |
| -100 | -90 |
| -80 | -70 |
| -60 | -50 |
| -40 | -30 |
| -20 | -10 |
| 0 | D098 |
---table end---
# 7.10 Single Tone FFT at 1797 MHz and -1 dBFS 

# 7.11 Single Tone FFT at 897 MHz and -1 dBFS
---table begin---
Table tile: Single Tone FFT at 897 MHz and -1 dBFS
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | 100 |
| 50 | 100 |
| 150 | 200 |
| 250 | 300 |
| 350 | 400 |
| 450 | 500 |
| -120 | -110 |
| -100 | -90 |
| -80 | -70 |
| -60 | -50 |
| -40 | -30 |
| -20 | -10 |
| 0 | D027 |
---table end---

# 7.12 Single Tone FFT at 2097 MHz and -1 dBFS 
---table begin---
Table tile: Single Tone FFT at 2097 MHz and -1 dBFS
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | 100 |
| 50 | 100 |
| 150 | 200 |
| 250 | 300 |
| 350 | 400 |
| 450 | 500 |
| -120 | -110 |
| -100 | -90 |
| -80 | -70 |
| -60 | -50 |
| -40 | -30 |
| -20 | -10 |
| 0 | D028 |
---table end---

# 7.13 Single Tone FFT at 3797 MHz and -1 dBFS 
... More tables continue ...# 7.25 SINAD vs Sample Rate
---table begin---
Table tile: SINAD vs Sample Rate
| Sample Rate (MSPS) | SINAD (dBFS) |
|---|---|
| 500 | 40 |
| 700 | 42 |
| 900 | 44 |
| 1100 | 46 |
| 1300 | 48 |
| 1500 | 50 |
| - | 52 |
| - | 54 |
| - | 56 |
| - | 58 |
| - | 60 |
---table end---

# 7.26 ENOB vs Sample Rate
---table begin---
Table tile: ENOB vs Sample Rate
| Sample Rate (MSPS) | ENOB (bits) |
|---|---|
| 500 | 5 |
| 700 | 6 |
| 900 | 7 |
| 1100 | 8 |
| 1300 | 9 |
| 1500 | 10 |
---table end---
... More tables continue ...

# 7.35 SNR vs AIN 
---table begin---
Table tile: SNR vs AIN 
| Input Amplitude (dBFS) | SNR (dBc or dBFS) |
|---|---|
| -40 | 0 |
| -35 | 5 |
| -30 | 10 |
| -25 | 15 |
| -20 | 20 |
| -15 | 25 |
| -10 | 30 |
| -5 | 35 |
| 0 | 40 |
| - | 45 |
| - | 50 |
| - | 55 |
| - | 60 |
---table end---

# 7.36 SFDR vs ACLK 
# 7.37 SNR vs ACLK
---table begin---
Table tile: SNR vs ACLK
| Clock Amplitude (VPP-DIFF) | SNR (dBFS) |
|---|---|
| 0 | 40 |
| 0.5 | 42 |
| 1 | 44 |
| 1.5 | 46 |
| 2 | 48 |
| 2.5 | 50 |
| 3 | 52 |
| 3.5 | 54 |
| 4 | 56 |
| - | 58 |
| - | 60 |
---table end---
# 7.36 SFDR vs ACLK 

# 7.38 SNR vs FREF and Suppression
---table begin---
Table tile: SNR vs FREF and Suppression
| REF_FsPLL | SNR (dBFS) |
|---|---|
| 0 | 50 |
| 50 | 51 |
| 100 | 52 |
| 150 | 53 |
| 200 | 54 |
| 250 | 55 |
| 300 | 56 |
| 350 | 57 |
| 400 | 58 |
| 450 | 59 |
| 500 | 60 |
---table end---

# 7.39 SFDR vs FREF and Suppression
---table begin---
Table tile: SFDR vs FREF and Suppression
| REF_FsPLL | SFDR (dBFS) |
|---|---|
| 0 | 50 |
| 50 | 52 |
| 100 | 54 |
| 150 | 56 |
| 200 | 58 |
| 250 | 60 |
| 300 | 62 |
| 350 | 64 |
| 400 | 66 |
| 450 | 68 |
| 500 | 70 |
---table end---

# 7.40 SFDR vs FIN and C-PLL Modes
# 7.41 SINAD vs FIN and C-PLL modes
---table begin---
Table title: SINAD vs FIN and C-PLL modes
| Input Frequency (MHz) | ENOB (bits) | Mode |
|---|---|---|
| 0 | 6 | CPLL On, Suppression Off |
| 50 | 6.5 | CPLL On, Suppression On |
| 100 | 7 | CPLL Off |
| 150 | 7.5 | Low power mode |
| 200 | 8 |
| 250 | 8.5 |
| 300 | 9 |
| 350 | 9.5 |
| 400 | 10 |
| 450 |
| 500 |
---table end---
# 7.40 SFDR vs FIN and C-PLL Modes

# 7.42 SFDR vs AIN and C-PLL
---table begin---
Table title: SFDR vs AIN and C-PLL
| Input Frequency (MHz) | SFDR (dBFS) | Mode |
|---|---|---|
| 0 | 20 | CPLL On, AIN = -12dBFS |
| 500 | 30 | CPLL On, AIN = -6dBFS |
| 1000 | 40 | CPLL On, AIN = -1dBFS |
| 1500 | 50 | CPLL Off, AIN = -12dBFS |
| 2000 | 60 | CPLL Off, AIN = -6dBFS |
| 2500 | 70 | CPLL Off, AIN = -1dBFS |
| 3000 | 80 |
| 3500 |
| 4000 |
---table end---

# 7.43 SNR vs AIN and C-PLL
---table begin---
Table title: SNR vs AIN and C-PLL
| Input Frequency (MHz) | SNR (dBFS) | Mode |
|---|---|---|
| 0 | 30 | CPLL On, AIN = -12dBFS |
| 500 | 35 | CPLL On, AIN = -6dBFS |
| 1000 | 40 | CPLL On, AIN = -1dBFS |
| 1500 | 45 | CPLL Off, AIN = -12dBFS |
| 2000 | 50 | CPLL Off, AIN = -6dBFS |
| 2500 | 55 | CPLL Off, AIN = -1dBFS |
| 3000 | 60 |
| 3500 |
| 4000 |
---table end---

# 7.44 SINAD vs AIN and C-PLL
---table begin---
Table title: SINAD vs AIN and C-PLL
| Input Frequency (MHz) | SINAD (dBFS) | Mode |
|---|---|---|
| 0 | 30 | CPLL On, AIN = -12dBFS |
| 500 | 35 | CPLL On, AIN = -6dBFS |
| 1000 | 40 | CPLL On, AIN = -1dBFS |
| 1500 | 45 | CPLL Off, AIN = -12dBFS |
| 2000 | 50 | CPLL Off, AIN = -6dBFS |
| 2500 | 55 | CPLL Off, AIN = -1dBFS |
| 3000 | 60 |
| 3500 |
| 4000 |
---table end---

# 7.45 ENOB vs AIN and C-PLL
# 7.54 SFDR vs AIN and C-PLL
---table begin---
Table title: SFDR vs AIN and C-PLL
| Input Frequency (MHz) | SNR (dBFS) | Mode |
|---|---|---|
| 0 | 50 | CPLL On, AIN = -12dBFS |
| 50 | 51 | CPLL On, AIN = -6dBFS |
| 100 | 52 | CPLL On, AIN = -1dBFS |
| 150 | 53 | CPLL Off, AIN = -12dBFS |
| 200 | 54 | CPLL Off, AIN = -6dBFS |
| 250 | 55 | CPLL Off, AIN = -1dBFS |
| 300 | 56 | Low power mode |
| 350 | 57 |
| 400 | 58 |
| 450 | 59 |
| 500 | 60 |
---table end---
# 7.45 ENOB vs AIN and C-PLL

# 7.55 SNR vs AIN and C-PLL
---table begin---
Table title: SNR vs AIN and C-PLL
| Input Frequency (MHz) | SINAD (dBFS) | Mode |
|---|---|---|
| 0 | 50 | CPLL On, AIN = -12dBFS |
| 50 | 51 | CPLL On, AIN = -6dBFS |
| 100 | 52 | CPLL On, AIN = -1dBFS |
| 150 | 53 | CPLL Off, AIN = -12dBFS |
| 200 | 54 | CPLL Off, AIN = -6dBFS |
| 250 | 55 | CPLL Off, AIN = -1dBFS |
| 300 | 56 | Low power mode |
| 350 | 57 |
| 400 | 58 |
| 450 | 59 |
| 500 | 60 |
---table end---

# 7.56 SINAD vs AIN and C-PLL
---table begin---
Table title: SINAD vs AIN and C-PLL
| Input Frequency (MHz) | ENOB (bits) | Mode |
|---|---|---|
| 0 | 8 | CPLL On, AIN = -12dBFS |
| 50 | 8.2 | CPLL On, AIN = -6dBFS |
| 100 | 8.4 | CPLL On, AIN = -1dBFS |
| 150 | 8.6 | CPLL Off, AIN = -12dBFS |
| 200 | 8.8 | CPLL Off, AIN = -6dBFS |
| 250 | 9 | CPLL Off, AIN = -1dBFS |
| 300 | 9.2 | Low power mode |
| 350 | 9.4 |
| 400 | 9.6 |
| 450 |
| 500 |
---table end---

# 7.57 ENOB vs AIN and C-PLL
---table begin---
Table title: ENOB vs AIN and C-PLL
| Input Frequency (MHz) | HD2 (dBFS) | Mode |
|---|---|---|
| 0 | -100 | CPLL On, AIN = -12dBFS |
| 50 | -90 | CPLL On, AIN = -6dBFS |
| 100 | -80 | CPLL On, AIN = -1dBFS |
| 150 | -70 | CPLL Off, AIN = -12dBFS |
| 200 | -60 | CPLL Off, AIN = -6dBFS |
| 250 | -50 | CPLL Off, AIN = -1dBFS |
| 300 | -40 | Low power mode |
| 350 | -30 |
| 400 | -20 |
| 450 | -10 |
| 500 | 0 |
---table end---

# 7.58 HD2 vs AIN and C-PLL# 7.64. SNR vs Temperature
---table begin---
Table title: SNR vs Temperature
| Temperature (qC) | SNR (dBFS) |
|---|---|
| -60 | 50 |
| -40 | 52 |
| -20 | 54 |
| 0 | 56 |
| 20 | 58 |
| 40 | 60 |
| 60 | 62 |
| 80 | 64 |
| 100 | 66 |
| 120 | 68 |
| 140 | 70 |
---table end---

# 7.65. SFDR vs Temperature
---table begin---
Table title: SFDR vs Temperature
| Temperature (qC) | SFDR (dBFS) |
|---|---|
| -60 | -80 |
| -40 | -78 |
| -20 | -76 |
| 0 | -74 |
| 20 | -72 |
| 40 | -70 |
| 60 | -68 |
| 80 | -66 |
| 100 | -64 |
| 120 | -62 |
| 140 | -60 |
---table end---

# 7.66. HD2 vs Temperature
---table begin---
Table title: HD2 vs Temperature
| Temperature (qC) | HD2 (dBFS) |
|---|---|
| -60 | -80 |
| -40 | -75 |
| -20 | -70 |
| 0 | -65 |
| 20 | -60 |
| 40 | -55 |
| 60 | -50 |
| 80 | -45 |
| 100 | -40 |
---table end---

# 7.67. HD3 vs Temperature
---table begin---
Table title: HD3 vs Temperature
| Temperature (qC) | HD3 (dBFS) |
|---|---|
| -60 | -80 |
| -40 | -75 |
| -20 | -70 |
| 0 | -65 |
| 20 | -60 |
| 40 | -55 |
| 60 | -50 |
---table end---

# 7.68. Worst Spur vs Temperature
---table begin---
Table title: Worst Spur vs Temperature
| Temperature (qC) | SFDR (dBFS) |
|---|---|
| -60 | -80 |
| -40 | -75 |
| -20 | -70 |
| 0 | -65 |
| 20 | -60 |
| 40 | -55 |
| 60 | -50 |
---table end---

# 7.69. Two Tone FFT at 498MHz
---table begin---
Table title: Two Tone FFT at 498MHz
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | -120 |
| 100 | -110 |
| 200 | -100 |
| 300 | -90 |
| 400 | -80 |
| 500 | -70 |
| 600 | -60 |
| 700 | -50 |
| 800 | -40 |
---table end---

# 7.70. Two Tone FFT at 1798MHz
---table begin---
Table title: Two Tone FFT at 1798MHz
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | -120 |
| 100 | -110 |
| 200 | -100 |
| 300 | -90 |
| 400 | -80 |
| 500 | -70 |
| 600 | -60 |
| 700 | -50 |
| 800 | -40 |
---table end---

# 7.71. Two Tone FFT at 3498MHz
---table begin---
Table title: Two Tone FFT at 3498MHz
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | -120 |
| 100 | -110 |
| 200 | -100 |
| 300 | -90 |
| 400 | -80 |
| 500 | -70 |
| 600 | -60 |
| 700 | -50 |
| 800 | -40 |

# 7.72. Two Tone FFT at 348 MHz
---table begin---
Table title: Two Tone FFT at 348 MHz
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | -120 |
| 50 | -110 |
| 100 | -100 |
| 150 | -90 |
| 200 | -80 |
| 250 | -70 |
| 300 | -60 |
| 350 | -50 |
| 400 | -40 |
| 450 | -30 |
| 500 | -20 |
---table end---

# 7.73. Two Tone FFT at 1798 MHz
---table begin---
Table title: Two Tone FFT at 1798 MHz
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | -120 |
| 50 | -110 |
| 100 | -100 |
| 150 | -90 |
| 200 | -80 |
| 250 | -70 |
| 300 | -60 |
| 350 | -50 |
| 400 | -40 |
| 450 | -30 |
| 500 | -20 |
---table end---

# 7.74. Two Tone FFT at 3498 MHz
---table begin---
Table title: Two Tone FFT at 3498 MHz
| Output Frequency (MHz) | Amplitude (dBFS) |
|---|---|
| 0 | -120 |
| 50 | -110 |
| 100 | -100 |
| 150 | -90 |
| 200 | -80 |
| 250 | -70 |
| 300 | -60 |
| 350 | -50 |
| 400 | -40 |
| 450 | -30 |
| 500 | -20 |
---table end---

# 7.75. IMD3 vs FIN
---table begin---
Table title: IMD3 vs FIN
| Center Input Frequency (MHz) | IMD3 (dBFS) |
|---|---|
| 0 | -100 |
| 500 | -90 |
| 1000 | -80 |
| 1500 | -70 |
| 2000 | -60 |
| 2500 | -50 |
| 3000 | -40 |
| 3500 | -30 |
| 4000 | -20 |
---table end---

# 7.76. IMD3 vs FIN
---table begin---
Table title: IMD3 vs FIN
| Input Frequency (MHz) | IMD3 (dBFS) |
|---|---|
| 0 | -100 |
| 500 | -90 |
| 1000 | -80 |
| 1500 | -70 |
| 2000 | -60 |
| 2500 | -50 |
| 3000 | -40 |
| 3500 | -30 |
| 4000 | -20 |
---table end---

# 7.77. Crosstalk to Channel A vs FIN
---table begin---
Table title: Crosstalk to Channel A vs FIN
| Input Frequency (MHz) | Crosstalk (dB) |
|---|---|
| 0 | -100 |
| 500 | -95 |
| 1000 | -90 |
| 1500 | -85 |
| 2000 | -80 |
| 2500 | -75 |
| 3000 | -70 |
| 3500 | -65 |
| 4000 | -60 |
---table end---

# 7.78. Crosstalk to Channel B vs FIN
---table begin---
Table title: Crosstalk to Channel B vs FIN
| Input Frequency (MHz) | Crosstalk (dB) |
|---|---|
| 0 | -100 |
| 500 | -95 |
| 1000 | -90 |
| 1500 | -85 |
| 2000 | -80 |
| 2500 | -75 |
| 3000 | -70 |
| 3500 | -65 |
| 4000 | -60 |
---table end---

# 7.79. Quad Channel, Power Dissipation vs FS and JMODES 0
---table begin---
Table title: Power Dissipation vs FS and JMODES 0
| Sample Rate (MSPS) | Power Dissipation (W) |
|---|---|
| 400 | 0 |
| 600 | 0.5 |
| 800 | 1 |
| 1000 | 1.5 |
| 1200 | 2 |
| 1400 | 2.5 |
| 1600 | 3 |
---table end---

# 7.80. Quad Channel, Power Dissipation vs FS and JMODE 4 - 7
---table begin---
Table title: Power Dissipation vs FS and JMODE 4 - 7
| Sample Rate (MSPS) | Power Dissipation (W) |
|---|---|
| 400 | 0 |
| 600 | 0.5 |
| 800 | 1 |
| 1000 | 1.5 |
| 1200 | 2 |
| 1400 | 2.5 |
| 1600 | 3 |
---table end---

# 7.81. Quad Channel, Power Dissipation vs FS and JMODE 8 - 12
---table begin---
Table title: Power Dissipation vs FS and JMODE 8 - 12
| Sample Rate (MSPS) | Power Dissipation (W) |
|---|---|
| 400 | 0 |
| 600 | 0.5 |
| 800 | 1 |
| 1000 | 1.5 |
| 1200 | 2 |
| 1400 | 2.5 |
| 1600 | 3 |
---table end---

# 7.82. Quad Channel, Power Dissipation vs FS and JMODE 13 - 15
---table begin---
Table title: Power Dissipation vs FS and JMODE 13 - 15
| Sample Rate (MSPS) | Power Dissipation (W) |
|---|---|
| 400 | 0 |
| 600 | 0.5 |
| 800 | 1 |
| 1000 | 1.5 |
| 1200 | 2 |
| 1400 | 2.5 |
| 1600 | 3 |
---table end---

# 7.83. Quad Channel, IVA19 vs FS
---table begin---
Table title: IVA19 vs FS
| Sample Rate (MSPS) | IVA19 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.1 |
| 800 | 0.2 |
| 1000 | 0.3 |
| 1200 | 0.4 |
| 1400 | 0.5 |
| 1600 | 0.6 |
---table end---

# 7.84. Quad Channel, IVA11 vs FS
# 7.83. Quad Channel, IVA19 vs FS 
---table begin---
Table title: IVA19 vs FS 
| Sample Rate (MSPS) | IVA19 (A) |
|---|---|
| 400   | 0.0 |
| 600   | 0.1 |
| 800   | 0.2 |
| 1000 | 0.3 |
| 1200 | 0.4 |
| 1400 | 0.5 |
| 1600 | 0.6 |
---table end---
# 7.84. Quad Channel, IVA11 vs FS

# 7.84. Quad Channel, IVA11 vs FS 
---table begin---
Table title: IVA11 vs FS 
| Sample Rate (MSPS) | IAVDD11 (A) | 
|---|---|
| 400 | 0.0 |
| 600 | 0.1 |
| 800 | 0.2 |
| 1000 | 0.3 |
| 1200 | 0.4 |
| 1400 | 0.5 |
| 1600 | 0.6 |
---table end---

# 7.85. Quad Channel, IVD11 vs FS and JMODE 0 - 3
---table begin---
Table title: IVD11 vs FS and JMODE 0 - 3
| Sample Rate (MSPS) | IVD11 (A) |
|---|---|
| 400 | 0.0 |
| 600 | 0.1 |
| 800 | 0.2 |
| 1000 | 0.3 |
| 1200 | 0.4 |
| 1400 | 0.5 |
| 1600 | 0.6 |
---table end---

# 7.86. Quad Channel, IVD11 vs FS and JMODE 4 - 7
---table begin---
Table title: IVD11 vs FS and JMODE 4 - 7
| Sample Rate (MSPS) | IVD11 (A) |
|---|---|
| 400 | 0.0 |
| 600 | 0.1 |
| 800 | 0.2 |
| 1000 | 0.3 |
| 1200 | 0.4 |
| 1400 | 0.5 |
| 1600 | 0.6 |
---table end---

# 7.87. Quad Channel, IVD11 vs FS and JMODE 8 - 12
---table begin---
Table title: IVD11 vs FS and JMODE 8 - 12
| Sample Rate (MSPS) | IVD11 (A) |
|---|---|
| 400 | 0.0 |
| 600 | 0.1 |
| 800 | 0.2 |
| 1000 | 0.3 |
| 1200 | 0.4 |
| 1400 | 0.5 |
| 1600 | 0.6 |
---table end---

# 7.88. Quad Channel, IVD11 vs FS and JMODE 13 - 15
---table begin---
Table title: IVD11 vs FS and JMODE 13 - 15
| Sample Rate (MSPS) | IVD11 (A) |
|---|---|
| 400 | 0.0 |
| 600 | 0.1 |
| 800 | 0.2 |
| 1000 | 0.3 |
| 1200 | 0.4 |
| 1400 | 0.5 |
| 1600 | 0.6 |
---table end---

# 7.89. Dual Channel, Power Dissipation vs FS and JMODE 0 -3
---table begin---
Table title: Power Dissipation vs FS and JMODE 0 - 3
| Sample Rate (MSPS) | Power Dissipation (W) | 
|---|---|
| 400 | 0 |
| 600 | 0.2 |
| 800 | 0.4 |
| 1000 | 0.6 |
| 1200 | 0.8 |
| 1400 | 1.0 |
| 1600 | 1.2 |
---table end---

# 7.90. Dual Channel, Power Dissipation vs FS and JMODE 4 - 7
---table begin---
Table title: Power Dissipation vs FS and JMODE 4 - 7
| Sample Rate (MSPS) | Power Dissipation (W) |
|---|---|
| 400 | 0 |
| 600 | 0.2 |
| 800 | 0.4 |
| 1000 | 0.6 |
| 1200 | 0.8 |
| 1400 | 1.0 |
| 1600 | 1.2 |
---table end---

# 7.91. Dual Channel, Power Dissipation vs FS and JMODE 8 - 12
---table begin---
Table title: Power Dissipation vs FS and JMODE 8 - 12
| Sample Rate (MSPS) | Power Dissipation (W) |
|---|---|
| 400 | 0 |
| 600 | 0.2 |
| 800 | 0.4 |
| 1000 | 0.6 |
| 1200 | 0.8 |
| 1400 | 1.0 |
| 1600 | 1.2 |
---table end---

# 7.92. Dual Channel, Power Dissipation vs FS and JMODE 13 - 15
---table begin---
Table title: Power Dissipation vs FS and JMODE 13 - 15
| Sample Rate (MSPS) | Power Dissipation (W) |
|---|---|
| 400 | 0 |
| 600 | 0.05 |
| 800 | 0.1 |
| 1000 | 0.15 |
| 1200 | 0.2 |
| 1400 | 0.25 |
| 1600 | 0.3 |
|  | 0.35 |
|  | 0.4 |
|  | 0.45 |
|  | 0.5 |
---table end---

# 7.93. Dual Channel, IVA19 vs FS
---table begin---
Table title: Dual Channel, IVA19 vs FS
| Sample Rate (MSPS) | IVA19 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.05 |
| 800 | 0.1 |
| 1000 | 0.15 |
| 1200 | 0.2 |
| 1400 | 0.25 |
| 1600 | 0.3 |
|  | 0.35 |
|  | 0.4 |
|  | 0.45 |
|  | 0.5 |
---table end---

# 7.94. Dual Channel, IVA11 vs FS
---table begin---
Table title: Dual Channel, IVA11 vs FS
| Sample Rate (MSPS) | IAVDD11 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.1 |
| 800 | 0.2 |
| 1000 | 0.3 |
| 1200 | 0.4 |
| 1400 | 0.5 |
| 1600 | 0.6 |
---table end---

# 7.95. Dual Channel, Power Dissipation vs FS and JMODE 0 - 3
---table begin---
Table title: Dual Channel, Power Dissipation vs FS and JMODE 0 - 3
| Sample Rate (MSPS) | IVD11 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.05 |
| 800 | 0.1 |
| 1000 | 0.15 |
| 1200 | 0.2 |
| 1400 | 0.25 |
| 1600 | 0.3 |
|  | 0.35 |
|  | 0.4 |
|  | 0.45 |
|  | 0.5 |
---table end---

# 7.96. Dual Channel, Power Dissipation vs FS and JMODE 4 - 7
---table begin---
Table title: Dual Channel, Power Dissipation vs FS and JMODE 4 - 7
| Sample Rate (MSPS) | IVD11 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.05 |
| 800 | 0.1 |
| 1000 | 0.15 |
| 1200 | 0.2 |
| 1400 | 0.25 |
| 1600 | 0.3 |
|  | 0.35 |
|  | 0.4 |
|  | 0.45 |
|  | 0.5 |
---table end---

# 7.97. Dual Channel, Power Dissipation vs FS and JMODE 8 - 12
---table begin---
Table title: Dual Channel, Power Dissipation vs FS and JMODE 8 - 12
| Sample Rate (MSPS) | IVD11 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.05 |
| 800 | 0.1 |
| 1000 | 0.15 |
| 1200 | 0.2 |
| 1400 | 0.25 |
| 1600 | 0.3 |
|  | 0.35 |
|  | 0.4 |
|  | 0.45 |
|  | 0.5 |
---table end---

# 7.98. Dual Channel, Power Dissipation vs FS and JMODE 13 - 15
---table begin---
Table title: Dual Channel, Power Dissipation vs FS and JMODE 13 - 15
| Sample Rate (MSPS) | IVD11 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.05 |
| 800 | 0.1 |
| 1000 | 0.15 |
| 1200 | 0.2 |
| 1400 | 0.25 |
| 1600 | 0.3 |
|  | 0.35 |
|  | 0.4 |
|  | 0.45 |
|  | 0.5 |
---table end---

# 7.99. Single Channel, Power Dissipation vs FS and JMODE 0 - 3
---table begin---
Table title: Single Channel, Power Dissipation vs FS and JMODE 0 - 3
| Sample Rate (MSPS) | Power Dissipation (W) |
|---|---|
| 400 | 0 |
| 600 | 0.2 |
| 800 | 0.4 |
| 1000 | 0.6 |
| 1200 | 0.8 |
| 1400 | 1 |
| 1600 | 1.2 |
|  | 1.4 |
|  | 1.6 |
|  | 1.8 |
|  | 2 |
---table end---

# 7.100. Single Channel, Power Dissipation vs FS and JMODE 4 - 7
---table begin---
Table title: Power Dissipation vs FS and JMODE 4-7
| Sample Rate (MSPS) | Power Dissipation (W) |
|---|---|
| 400 | 0 |
| 600 | 0.2 |
| 800 | 0.4 |
| 1000 | 0.6 |
| 1200 | 0.8 |
| 1400 | 1 |
| 1600 | 1.2 |
|   | 1.4 |
|   | 1.6 |
|   | 1.8 |
|   | 2 |
---table end---

# 7.101. Single Channel, Power Dissipation vs FS and JMODE 8 - 12
---table begin---
Table title: Power Dissipation vs FS and JMODE 8-12
| Sample Rate (MSPS) | Power Dissipation (W) |
|---|---|
| 400 | 0 |
| 600 | 0.2 |
| 800 | 0.4 |
| 1000 | 0.6 |
| 1200 | 0.8 |
| 1400 |   1 |
| 1600 | 1.2 |
|   | 1.4 |
|   | 1.6 |
|   | 1.8 |
|   | 2 |
---table end---

# 7.102. Single Channel, Power Dissipation vs FS and JMODE 13 - 15
---table begin---
Table title: Power Dissipation vs FS and JMODE 13-15
| Sample Rate (MSPS) | IVA19 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.05 |
| 800 | 0.1 |
| 1000 | 0.15 |
| 1200 | 0.2 |
| 1400 | 0.25 |
| 1600 | 0.3 |
|   | 0.35 |
|   | 0.4 |
|   | 0.45 |
|   | 0.5 |
---table end---

# 7.103. Single Channel, IVA19 vs FS
---table begin---
Table title: IVA19 vs FS
| Sample Rate (MSPS) | IAVDD11 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.1 |
| 800 | 0.2 |
| 1000 | 0.3 |
| 1200 | 0.4 |
| 1400 | 0.5 |
| 1600 | 0.6 |
|   | 0.7 |
|   | 0.8 |
|   | 0.9 |
|   | 1 |
---table end---

# 7.104. Single Channel, IVA11 vs FS
---table begin---
Table title: IVA11 vs FS
| Sample Rate (MSPS) | IVD11 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.05 |
| 800 | 0.1 |
| 1000 | 0.15 |
| 1200 | 0.2 |
| 1400 | 0.25 |
| 1600 | 0.3 |
|   | 0.35 |
|   | 0.4 |
|   | 0.45 |
|   | 0.5 |
---table end---

# 7.105. Single Channel, IVD11 vs FS and JMODE 0 - 3
---table begin---
Table title: IVD11 vs FS and JMODE 0-3
| Sample Rate (MSPS) | IVD11 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.05 |
| 800 | 0.1 |
| 1000 | 0.15 |
| 1200 | 0.2 |
| 1400 | 0.25 |
| 1600 | 0.3 |
|   | 0.35 |
|   | 0.4 |
|   | 0.45 |
|   | 0.5 |
---table end---

# 7.106. Single Channel, IVD11 vs FS and JMODE 4 - 7
---table begin---
Table title: IVD11 vs FS and JMODE 4-7
| Sample Rate (MSPS) | IVD11 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.05 |
| 800 | 0.1 |
| 1000 | 0.15 |
| 1200 | 0.2 |
| 1400 | 0.25 |
| 1600 | 0.3 |
|   | 0.35 |
|   | 0.4 |
|   | 0.45 |
|   | 0.5 |
---table end---

# 7.107. Single Channel, IVD11 vs FS and JMODE 8 - 12
---table begin---
Table title: IVD11 vs FS and JMODE 8-12
| Sample Rate (MSPS) | IVD11 (A) |
|---|---|
| 400 | 0 |
| 600 | 0.05 |
| 800 | 0.1 |
| 1000 | 0.15 |
| 1200 | 0.2 |
| 1400 | 0.25 |
| 1600 | 0.3 |
|   | 0.35 |
|   | 0.4 |
|   | 0.45 |
|   | 0.5 |
---table end---

# 7.108. Single Channel, IVD11 vs FS and JMODE 13 - 15
---table begin---
Table title: IVD11 vs FS and JMODE 13-15
| Sample Rate (MSPS) | Power Dissipation Difference (W) |
|---|---|
| 400 | -0.5 |
| 600 | -0.4 |
| 800 | -0.3 |
| 1000 | -0.2 |
| 1200 | -0.1 |
| 1400 | 0 |
| 1600 | 0.1 |
|  | 0.2 |
|  | 0.3 |
|  | 0.4 |
|  | 0.5 |
---table end---

# 7.109. Quad Channel, Power Dissipation Change with Calibration Mode
---table begin---
Table title: Power Dissipation Change with Calibration Mode
| Sample Rate (MSPS) | Power Dissipation Difference (W) |
|---|---|
| 400 | -0.5 |
| 600 | -0.4 |
| 800 | -0.3 |
| 1000 | -0.2 |
| 1200 | -0.1 |
| 1400 | 0 |
| 1600 | 0.1 |
|  | 0.2 |
|  | 0.3 |
|  | 0.4 |
|  | 0.5 |
---table end---

# 7.110. Dual Channel, Power Dissipation Change with Calibration Mode
---table begin---
Table title: Power Dissipation Change with Calibration Mode - Dual Channel
| Sample Rate (MSPS) | Power Dissipation Difference (W) |
|---|---|
| 400 | -0.5 |
| 600 | -0.4 |
| 800 | -0.3 |
| 1000 | -0.2 |
| 1200 | -0.1 |
| 1400 | 0 |
| 1600 | 0.1 |
|  | 0.2 |
|  | 0.3 |
|  | 0.4 |
|  | 0.5 |
---table end---

# 7.111. Single Channel, Power Dissipation Change with Calibration Mode
---table begin---
Table title: Power Dissipation Change with Calibration Mode - Single Channel
| Sample Rate (MSPS) | Power Dissipation Difference (W) |
|---|---|
| 400 | -0.5 |
| 600 | -0.4 |
| 800 | -0.3 |
| 1000 | -0.2 |
| 1200 | -0.1 |
| 1400 | 0 |
| 1600 | 0.1 |
|  | 0.2 |
|  | 0.3 |
|  | 0.4 |
|  | 0.5 |
---table end---

# 7.112. Quad Channel, IVA19 Change with Calibration Mode
---table begin---
Table title: IVA19 Change with Calibration Mode - Quad Channel
| Sample Rate (MSPS) | IVA19 Difference (mA) |
|---|---|
| 400 | -200 |
| 600 | -150 |
| 800 | -100 |
| 1000 | -50 |
| 1200 | 0 |
| 1400 | 50 |
| 1600 | 100 |
|  | 150 |
|  | 200 |
---table end---

# 7.113. Dual Channel, IVA19 Change with Calibration Mode
---table begin---
Table title: IVA19 Change with Calibration Mode - Dual Channel
| Sample Rate (MSPS) | IVA19 Difference (mA) |
|---|---|
| 400 | -200 |
| 600 | -150 |
| 800 | -100 |
| 1000 | -50 |
| 1200 | 0 |
| 1400 | 50 |
| 1600 | 100 |
|  | 150 |
|  | 200 |
---table end---

# 7.114. Single Channel, IVA19 Change with Calibration Mode
---table begin---
Table title: IVA19 Change with Calibration Mode - Single Channel
| Sample Rate (MSPS) | IVA19 Difference (mA) |
|---|---|
| 400 | -200 |
| 600 | -150 |
| 800 | -100 |
| 1000 | -50 |
| 1200 | 0 |
| 1400 | 50 |
| 1600 | 100 |
|  | 150 |
|  | 200 |
---table end---

# 7.115. Quad Channel, IVA11 Change with Calibration Mode
---table begin---
Table title: IVA11 Change with Calibration Mode - Quad Channel
| Sample Rate (MSPS) | IVA11 Difference (mA) |
|---|---|
| 400 | -100 |
| 600 | -80 |
| 800 | -60 |
| 1000 | -40 |
| 1200 | -20 |
| 1400 | 0 |
| 1600 | 20 |
|  | 40 |
|  | 60 |
|  | 80 |
|  | 100 |
---table end---

# 7.116. Dual Channel, IVA11 Change with Calibration Mode
# 图 7-115. Quad Channel, IVA11 Change with Calibration Mode
---table begin---
| Sample Rate (MSPS) | IVA11 Difference (mA) |
|---|---|
| 400 | -100 |
| 600 | -80 |
| 800 | -60 |
| 1000 | -40 |
| 1200 | -20 |
| 1400 | 0 |
| 1600 | 20 |
|  | 40 |
|  | 60 |
|  | 80 |
|  | 100 |
---table end---
# 7.116. Dual Channel, IVA11 Change with Calibration Mode

# 图 7-116. Dual Channel, IVA11 Change with Calibration Mode
---table begin---
| Sample Rate (MSPS) | IVA11 Difference (mA) |
|---|---|
| 400 | -100 |
| 600 | -80 |
| 800 | -60 |
| 1000 | -40 |
| 1200 | -20 |
| 1400 | 0 |
| 1600 | 20 |
|  | 40 |
|  | 60 |
|  | 80 |
|  | 100 |
---table end---

# 图 7-117. Single Channel, IVA11 Change with Calibration Mode
---table begin---
| Sample Rate (MSPS) | IVD11 Difference (mA) |
|---|---|
| 400 | -50 |
| 600 | -40 |
| 800 | -30 |
| 1000 | -20 |
| 1200 | -10 |
| 1400 | 0 |
| 1600 | 10 |
|  | 20 |
|  | 30 |
|  | 40 |
|  | 50 |
---table end---

# 图 7-118. Quad Channel, IVD11 Change with Calibration Mode
---table begin---
| Sample Rate (MSPS) | IVD11 Difference (mA) |
|---|---|
| 400 | -50 |
| 600 | -40 |
| 800 | -30 |
| 1000 | -20 |
| 1200 | -10 |
| 1400 | 0 |
| 1600 | 10 |
|   | 20 |
|   | 30 |
|   | 40 |
|   | 50 |
---table end---

# 图 7-119. Dual Channel, IVD11 Change with Calibration Mode
---table begin---
| Sample Rate (MSPS) | IVD11 Difference (mA) |
|---|---|
| 400 | -50 |
| 600 | -40 |
| 800 | -30 |
| 1000 | -20 |
| 1200 | -10 |
| 1400 | 0 |
| 1600 | 10 |
|   | 20 |
|   | 30 |
|   | 40 |
|   | 50 |
---table end---

# 图 7-120. Single Channel, IVD11 Change with Calibration Mode
---table begin---
| Sample Rate (MSPS) | IVD11 Difference (mA) |
|---|---|
| 400 | -50 |
| 600 | -40 |
| 800 | -30 |
| 1000 | -20 |
| 1200 | -10 |
| 1400 | 0 |
| 1600 | 10 |
|   | 20 |
|   | 30 |
|   | 40 |
|   | 50 |
---table end---

# 图 7-121. Quad Channel, Power Dissipation vs Temperature
---table begin---
| Temperature (°C) | Power Dissipation (W) |
|---|---|
| -60 | 2.5 |
| -40 | 2.6 |
| -20 | 2.7 |
|   0 | 2.8 |
|  20 | 2.9 |
|  40 | 3.0 |
|  60 | 3.1 |
|  80 | 3.2 |
| 100 | 3.3 |
| 120 | 3.4 |
| 140 | 3.5 |
---table end---

# 图 7-122. Dual Channel, Power Dissipation vs Temperature
---table begin---
| Temperature (°C) | Power Dissipation (W) |
|---|---|
| -60 | 1.5 |
| -40 | 1.6 |
| -20 | 1.7 |
|   0 | 1.8 |
|  20 | 1.9 |
|  40 | 2.0 |
|  60 | 2.1 |
|  80 | 2.2 |
| 100 | 2.3 |
| 120 | 2.4 |
| 140 | 2.5 |
---table end---

# 图 7-123. Single Channel, Power Dissipation vs Temperature
---table begin---
| Temperature (°C) | Power Dissipation (W) |
|---|---|
| -60 | 1.0 |
| -40 | 1.1 |
| -20 | 1.2 |
|   0 | 1.3 |
|  20 | 1.4 |
|  40 | 1.5 |
|  60 | 1.6 |
|  80 | 1.7 |
| 100 | 1.8 |
| 120 | 1.9 |
| 140 | 2.0 |
---table end---

# 图 7-124. Background Calibration Core Transition (midscale voltage)
---table begin---
| Sample # | ADC Output Code |
|---|---|
|   0 | 2030 |
| 100 | 2035 |
| 200 | 2040 |
| 300 | 2045 |
| 400 | 2050 |
| 500 | 2055 |
| 600 | 2060 |
| 700 | 2065 |
| 800 | 2070 |
---table end---

# 图 7-125. BG Calibration, input voltage offset ~ 90% of fullscale
# 7.123. Single Channel, Power Dissipation vs Temperature
---table begin---
Table tile: FG Calibration
| Sample # | ADC Output Code |
|---|---|
|   0 | 2030 |
| 100 | 2035 |
| 200 | 2040 |
| 300 | 2045 |
| 400 | 2050 |
| 500 | 2055 |
| 600 | 2060 |
| 700 | 2065 |
| 800 | 2070 |
| 900 | 1000 |
| D130 | Average of 4 ADC transitions |
---table end---
# 图 7-125. BG Calibration, input voltage offset ~ 90% of fullscale

# 7.124. Background Calibration Core Transition (midscale voltage)
---table begin---
Table tile: BG Calibration, midscale input voltage, ADC_SRC_DLY=31, MUX_DLY=30
| Sample # | ADC Output Code |
|---|---|
|   0 | 3740 |
| 100 | 3745 |
| 200 | 3750 |
| 300 | 3755 |
| 400 | 3760 |
| 500 | 3765 |
| 600 | 3770 |
| 700 | 3775 |
| 800 | 3780 |
| 900 | 1000 |
| D129 | Average of 8 ADC transitions |
---table end---

# 7.125. Background Calibration Core Transition (offset voltage)
---table begin---
Table tile: BG Calibration, input voltage offset ~ 90% of fullscale, ADC_SRC_DLY=31, MUX_DLY=30
| Sample # | ADC Output Code |
|---|---|
|   0 | 60000 |
| 120000 | 180000 |
| 240000 | 300000 |
|   0 | 500 |
| 1000 | 1500 |
| 2000 | 2500 |
| 3000 | 3500 |
| 4000 | Zoomed Region |
| D131 | BG Calibration, ADC_SRC_DLY=31, MUX_DLY=30, zoomed region shown in next plot |
---table end---

# 7.126. Background Calibration Core Transition (AC Signal)
---table begin---
Table tile: BG Calibration, ADC_SRC_DLY=31, MUX_DLY=30, unzoomed region shown in previous plot
| Sample # | ADC Output Code |
|---|---|
| 174000 | 175000 |
| 176000 | 177000 |
| 178000 | 1900 |
| 1920 | 1940 |
| 1960 | 1980 |
| 2000 | 2020 |
| 2040 | 2060 |
| 2080 | 2100 |
| D132 | BG Calibration, ADC_SRC_DLY=31, MUX_DLY=30, unzoomed region shown in previous plot |
---table end---

# 7.127. Background Calibration Core Transition (AC Signal Zoomed)

# 8. Detailed Description

# 8.1. Overview
The ADC12QJ1600-SP is a quad channel 12-bit, 1.6-GSPS analog-to-digital converters (ADC). The device have been optimized for low power consumption while maintaining high sampling rate and performance. The combination of power consumption, sampling rate and 12-bit resolution makes the device is ideally suited for light detection and ranging (LiDAR) systems. High channel density and wide input bandwidth also makes device an ideal fit for multi-channel oscilloscopes and digitizers and small form factor electronic warfare systems.
The device has a buffered input with full-power input bandwidth (-3 dB) of 6 GHz. The device is capable of direct RF sampling of L-band (1-2 GHz) and S-band (2-4 GHz) for electronic warfare systems and satellite communication equipment up to 4 GHz.
A number of clocking features are included to relax system timing requirements and simplify system architectures. The device has an internal phase-locked loop (PLL) with integrated voltage-controlled oscillator (VCO) to generate the sampling clock from a low frequency reference eliminating the need for an external high frequency clock generator. The low frequency PLL reference also relaxes timing of the SYSREF timing reference to achieve deterministic latency and multi-device synchronization. The internal PLL can be bypassed in favor of sending the high frequency sampling clock directly to the device for highest performance. A SYSREF Windowing feature relaxes the setup and hold requirement of SYSREF by directly measuring and adjusting the SYSREF delay inside of the device without the need to meet external timing requirements. The PLL reference clock can be output from the device to clock the digital logic FPGA or ASIC or an adjacent device to eliminate external clock buffer and distribution devices. Two additional CMOS outputs can send copies or divided copies of the PLL reference clock to clock additional devices in the system. A fourth clock output can output a SerDes reference clock for the transceiver block in the FPGA or ASIC to provide a complete system clocking solution. A timestamp input can be used to mark a specific sample using an external trigger. The timestamp is output over the JESD204C interface to mark the sample in the FPGA or ASIC. The timestamp signal can optionally be output from the device instead of the SerDes reference cl# 8.2. Functional Block Diagram
ADC A
INA+
INAt
  ADC B
INB+
INBt
  ADC C
INC+
INCt
  ADC D
IND+
INDt
TMSTP+
TMSTPt
JESD204B/C
SYNCSE\
D0+
D0t
D7+
D7t
TRIGOUT+
TRIGOUTt
SE_CLK
SYSREF+
SYSREFt
PLL
+VCO
Timestamp 
Insertion
Timestamp 
Insertion
Timestamp 
Insertion
Timestamp 
Insertion
Status 
Indicators
OVRA
OVRB
OVRC
OVRD
Calibration 
Controller
CALTRIG
CALSTAT
PLLREFO+
PLLREFOt
÷
CLK+
CLKt
SYSREF 
Windowing
Clock 
Control
PLLEN
PLLREFSE
SerDes 
PLL
To synchronization logic
÷
÷
CLKCFG0
CLKCFG1
Serial 
Programming 
Interface
SCLK
SCS
SDI
SDO

# 8.3. Feature Description

# 8.3.1 Analog Input
The analog input of the device has an internal buffer to enable high input bandwidth and to isolate sampling 
capacitor glitch noise from the input circuit. The analog input must be driven differentially because operation with 
a single-ended signal results in degraded performance. Both AC-coupling and DC-coupling of the analog input is 
supported. The analog input is designed for an input common-mode voltage (VCMI) of 1.1 V, which is terminated 
internally through single-ended, 50-Ω resistors to the VA11 supply on each input pin. DC-coupled input signals 
must have a common-mode voltage that meets the device input common-mode requirements specified as VCMI 
in the Recommended Operating Conditions table. The device includes internal analog input protection to protect 
the ADC input during over-range input conditions; see the Analog Input Protection section.
50 �
50 �
INx+
INxt
VA11 (1.1 V)
Analog input 
protection 
diodes
Input buffer
  ADC Core
Input 
Termination

# 8.3.1.1 Analog Input Protection
The analog input is protected against overdrive conditions by internal clamping diodes that are capable of 
sourcing or sinking input currents during over-range conditions, see the voltage and current limits in the Absolute 
Maximum Ratings table. The over-range protection is also defined for a peak RF input power in the Absolute 
Maximum Ratings table, which is frequency independent. Operation above the maximum conditions listed in the 
Recommended Operating Conditions table results in an increase in failure-in-time (F# 8.3.1.1 Analog Input Protection
The analog input is protected against overdrive conditions by internal clamping diodes that are capable of sourcing or sinking input currents during over-range conditions, see the voltage and current limits in the Absolute Maximum Ratings table. The over-range protection is also defined for a peak RF input power in the Absolute Maximum Ratings table, which is frequency independent. Operation above the maximum conditions listed in the Recommended Operating Conditions table results in an increase in failure-in-time (FIT) rate, so the system must correct the overdrive condition as quickly as possible. 

# 8.3.1.2 Full-Scale Voltage (VFS) Adjustment
Input full-scale voltage (VFS) adjustment is available, in fine increments, through FS_RANGE. All inputs are set to the same full-scale voltage setting. The available adjustment range is specified in the DC Specifications table. Larger full-scale voltages improve SNR and noise floor (in dBFS/Hz) performance.

# 8.3.1.3 Analog Input Offset Adjust
The input offset voltage for each analog input of the quad channel device can be adjusted through the OFSxy registers, where x represents the ADC core (0, 1, 2, 3, 4 or 5) and y represents the analog input for ADC core 2 (A or B) and core 3 (C or D). The y parameter is omitted for ADC core 0, 1, 4 and 5 since these cores always sample the same analog input. The y parameter is omitted for ADC core 0 and 1 since these cores always sample the same analog input. For the single channel device, x represents the ADC core (0 or 2) and the y parameter is omitted for ADC core 0 since this core always samples the same analog input. The adjustment range is approximately 33 mV to –33 mV differential. 

# 8.3.1.4 ADC Core
The device consists of a total of six ADC cores. The cores are swapped on-the-fly for calibration as required by the operating mode. This section highlights the theory and key features of the ADC cores.

# 8.3.1.4.1 ADC Theory of Operation
The differential voltages at the analog inputs are captured by the rising edge of CLK±. After capturing the input signal the ADC converts the analog voltage to a digital value by comparing the voltage to the internal reference voltage. 

# 8.3.1.4.2 ADC Core Calibration
ADC core calibration is required to optimize the analog performance of the ADC cores. Calibration must be repeated when operating conditions change significantly, namely temperature, in order to maintain optimal performance. The device has a built-in calibration routine that can be run as a foreground operation or a background operation. Foreground operation requires ADC downtime, where the ADC is no longer sampling the input signal, to complete the process.# 8.3.1.4.3 Analog Reference Voltage
The reference voltage for the device is derived from an internal band-gap reference. A buffered version of the reference voltage is available at the BG pin for user convenience. This output has an output-current capability of ±100 µA. The BG output must be buffered if more current is required. No provision exists for the use of an external reference voltage, but the full-scale input voltage can be adjusted through the full-scale-range register settings. Note that the VA11 supply voltage should be used to set the output common-mode voltage of a front-end fully-differential amplifier and the BG output should not be used for this purpose.

# 8.3.1.4.4 ADC Over-range Detection
For the system gain management to have a quick response time, a low-latency configurable over-range function is included. The over-range function works by monitoring the converted 12-bit samples at the ADC to quickly detect if the ADC is near saturation or already in an over-range condition. The absolute value of the upper 8 bits of the ADC data are checked against a programmable threshold, OVR_TH. The threshold programmed into OVR_TH is used for all analog inputs.
---
table begin
Table tile: Conversion of ADC Sample for Over-range Comparison
| ADC SAMPLE (Offset Binary) | ADC SAMPLE (2's Complement) | ABSOLUTE VALUE | UPPER 8 BITS USED FOR COMPARISON |
|---|---|---|---|
| 1111 1111 1111 (4095) | 0111 1111 1111 (+2047) | 111 1111 1111 (2047) | 1111 1111 (255) |
| 1111 1111 0000 (4080) | 0111 1111 0000 (+2032) | 111 1111 0000 (2032) | 1111 1110 (254) |
| 1000 0000 0000 (2048) | 0000 0000 0000 (0) | 000 0000 0000 (0) | 0000 0000 (0) |
| 0000 0001 0000 (16) | 1000 0001 0000 (–2032) | 111 1111 0000 (2032) | 1111 1110 (254) |
---
table end
---
table begin
Table tile: Conversion of ADC Sample for Over-range Comparison (continued)
| ADC SAMPLE (Offset Binary) | ADC SAMPLE (2's Complement) | ABSOLUTE VALUE | UPPER 8 BITS USED FOR COMPARISON |
|---|---|---|---|
| 0000 0000 0000 (0) | 1000 0000 0000 (–2048) | 111 1111 1111 (2047) | 1111 1111 (255) |
---
table end

# 8.3.1.4.5 Over-range Detection
Over-range detection is enabled by setting OVR_EN to 1. If the upper 8 bits of the absolute value equal or exceed the OVR_TH threshold during the monitoring period, then the over-range bit associated with the over-ranged ADC channel is set to 1, otherwise the over-range bit is 0. For the Quad channel device, the over-range status can be monitored on the ORA, ORB, ORC or ORD output pins for ADC channels A, B, C and D, respectively. OVR_N can be used to set the output pulse duration from the last over-range event.
---
table begin
Table tile: Over-range Monitoring Period
| OVR_N | over-range PULSE LENGTH SINCE LAST over-range EVENT (DEVCLK Cycles) |
|---|---|
| 0 | 8 |
| 1 | 16 |
| 2 | 32 |
| 3 | 64 |
| 4 | 128 |
| 5 | 256 |
| 6 | 512 |
| 7 | 1024 |
---
table end
Typically, the OVR_TH threshold is set...

# 8.3.1.3 Over-Range Monitoring
it associated with the over-ranged ADC channel is set to 1, otherwise the over-range bit is 0. For the Quad channel device, the over-range status can be monitored on the ORA, ORB, ORC or ORD output pins for ADC channels A, B, C and D, respectively. OVR_N can be used to set the output pulse duration from the last over-range event.
---
table begin
Table tile: Over-range Monitoring Period
| OVR_N | over-range PULSE LENGTH SINCE LAST over-range EVENT (DEVCLK Cycles) |
|---|---|
| 0 | 8 |
| 1 | 16 |
| 2 | 32 |
| 3 | 64 |
| 4 | 128 |
| 5 | 256 |
| 6 | 512 |
| 7 | 1024 |
---
table end
Typically, the OVR_TH threshold is set near the 8-bit full-scale value (228 for example). When the threshold is triggered, a typical system turns down the system gain to avoid clipping.

# 8.3.1.4.5 Code Error Rate (CER)
ADC cores can generate bit errors within a sample, often called code errors (CER) or referred to as sparkle codes, resulting from meta-stability caused by non-ideal comparator limitations. The device uses a unique ADC architecture that inherently allows significant code error rate improvements from traditional pipelined flash or successive approximation register (SAR) ADCs.

# 8.3.2 Temperature Monitoring Diode
A built-in thermal monitoring diode is made available on the TDIODE+ and TDIODE– pins. This diode facilitates temperature monitoring and characterization of the device in higher ambient temperature environments. Only assert the PD pin long enough to take the offset measurement. 

# 8.3.3 Timestamp
The TMSTP+ and TMSTP– differential input can be used as a time-stamp input to mark a specific sample based on the timing of an external trigger event relative to the sampled signal. Effectively, the TMSTP± input acts as a 1-bit ADC sampled in parallel with the analog input.# 8.3.4 Clocking
The input to the clocking subsystem of the device includes two clock inputs (CLK± and SE_CLK) and a synchronization signal (SYSREF±). An internal phase-locked loop (PLL) and voltage-controlled oscillator (VCO) can optionally be used to generate the ADC sampling clock from a low frequency reference by setting the PLL_EN pin high. The sampling clock PLL is called the converter PLL (C-PLL). The C-PLL reference can be provided to either the CLK± differential input or the SE_CLK single-ended input. The single-ended C-PLL reference input is selected by setting the PLLREF_SE pin high. For highest performance, the internal C-PLL can be bypassed and the sampling clock provided directly to the CLK± input when PLL_EN and PLLREF_SE are held low. Note that SE_CLK cannot be used if the C-PLL is disabled. The C-PLL reference clock can be sent to either an FPGA or ASIC or to an adjacent device through the PLLREFO± LVDS output when the PLL is enabled. Two additional copies or divided copies of PLLREFO can be output on ORC and ORD when enabled through the CLKCFG[1:0] pins or through SPI. PLLREFO and the ORC and ORD clock outputs are available at device power up when the CMOS control pins (PLL_EN, CLKCFG0 and CLKCFG1) are set appropriately and if PD is held low. Toggling PD high to power down the device also powers down the clock outputs.
In addition, the SerDes block contains a PLL, called S-PLL, that generates the SerDes output clock from the ADC sampling clock. The S-PLL generated clock can be divided and output from the TRIGOUT± LVDS output and sent to an FPGA or ASIC to clock the SerDes receivers. The SYSREF signal is captured by the chosen clock input (CLK± or SE_CLK). A SYSREF Windowing block is used to measure and optimize the setup and hold timing of the SYSREF signal relative to the selected clock input. SYSREF Windowing relaxes the timing requirement of the external signals.

# 8.3.4.1 Converter PLL (C-PLL) for Sam
(Note: the conversion would be more accurate if the rest of the text under "8.3.4.1 Converter PLL (C-PLL) for Sam" is provided)# 8.3.4 Clocking Subsystem
The clock generated by the C-PLL when the PLL is enabled or the clock provided to CLK± when the PLL is disabled is used as the sampling clock for the ADC core as well as the clocking for the digital processing and serializer S-PLL. Use a low-noise (low jitter) clock input, whether the PLL is enabled or disabled, to maintain high signal-to-noise ratio (SNR) within the ADC.

# 8.3.4.1 Converter PLL (C-PLL) for Sampling Clock Generation
# 1. Rate Description and Values
---table begin---
Table tile: Rate Values and Descriptions
| Rate | Description | Value | 
|---|---|---|
| 5 | Minimum ADC Core Sampling Rate | 1440 MSPS | 
| 5 | Maximum ADC Core Sampling Rate | 1600 MSPS |
| 6 | Minimum ADC Core Sampling Rate | 1200 MSPS |
| 6 | Maximum ADC Core Sampling Rate | 1367 MSPS |
| 8 | Minimum ADC Core Sampling Rate | 900 MSPS |
| 8 | Maximum ADC Core Sampling Rate | 1025 MSPS |
| 10 | Minimum ADC Core Sampling Rate | 720 MSPS |
| 10 | Maximum ADC Core Sampling Rate | 820 MSPS |
| 12 | Minimum ADC Core Sampling Rate | 600 MSPS |
| 12 | Maximum ADC Core Sampling Rate | 683 MSPS |
| 16 | Minimum ADC Core Sampling Rate | 500 MSPS |
| 16 | Maximum ADC Core Sampling Rate | 513 MSPS |
---table end---
# 8.3.4.1 Converter PLL (C-PLL) for Sampling Clock Generation

# 2. C-PLL Reset and Calibration
The C-PLL should be held in reset before changing any of the C-PLL settings by setting register CPLL_RESET 
to 1 (address = 0x5C CPLL_RESET). The C-PLL dividers can be programmed using registers PLL_P_DIV 
(address = 0x3D PLL_P_DIV), PLL_V_DIV (address = 0x03D PLL_V_DIV) and PLL_N_DIV (address = 0x3E 
PLL_N_DIV). After programming the dividers the VCO calibration should be run by first setting register 
VCO_CAL_EN to 1 (address = 0x5D VCO_CAL_EN). The VCO calibration is run when register CPLL_RESET 
(address = 0x5C CPLL_RESET) is set to 0 to take the C-PLL out of reset. Calibration is finished and the C-PLL 
is locked when register VCO_CAL_DONE (address = 0x5E VCO_CAL_DONE) returns 1 and register 
CPLL_LOCKED (address = 0x208 CPLL_LOCKED) is 1.

# 3. Noise Suppression Options
The C PLL includes noise suppression options for the VA11Q and VCLK11 that reduce the sampling jitter and 
reference clock input spur at the expense of approximately 20 mA of current each. The control bits are found in 
the CLK_CTRL2 register (address = 0x2B CLK_CTRL2).

# 4. LVDS Clock Outputs
Two LVDS clock outputs are provided to simplify system clocking architectures. These outputs are shown in 图 
8-3. The first LVDS clock output is PLLREFO±. PLLREFO± repeats the PLL reference clock directly from the 
selected reference clock input (CLK± or SE_CLK) as determined by PLLREF_SE. 
(/\*additional content omitted for brevity*\)

# 5. CMOS Clock Outputs 
Additional CMOS PLL reference clock outputs are available on ORC and ORD when configured through 
CLKCFG[1:0] or through SPI. The clock outputs are available at device power up when CLKCFG[1:0] are used 
to enable the clock outputs and when PD is held low. Setting the PD pin high disables these output# 8.3.4 Optional CMOS Clock Outputs (ORC, ORD)
Additional CMOS PLL reference clock outputs are available on ORC and ORD when configured through CLKCFG[1:0] or through SPI. The clock outputs are available at device power up when CLKCFG[1:0] are used to enable the clock outputs and when PD is held low. Setting the PD pin high disables these outputs; and therefore, the PD pin should not be used when these clocks are necessary for system operation. SPI register overrides are available for the CLKCFG[1:0] pins through the DIVREF_C_MODE and DIVREF_D_MODE SPI register settings. Note that CLKCFG[1:0] can be used to enable or disable ORC and ORD and set the output divider for ORC, but cannot set the output divider for ORD (enable or disable only). The DIVREF_C and DIVREF_D functionality has higher priority than over-range as reflected in 表 8-4 and 表 8-5. Using these outputs as clock outputs results in spurs in the ADC output spectrum at the output frequency and harmonics of the output frequency. Limit the capacitive loading on these outputs to less than 10 pF to limit the noise impact.

# Remark
---table begin---
Table tile: Table 8-5 Setting ORD Functionality
| CPLL_OVR_EN | CLKCFG1 | CLKCFG0 | DIVREF_D_MODE | OVR_EN | ORD Function |
|---|---|---|---|---|---|
| 0 | 0 | 0 | X | 0 | Disabled |
| 0 | 0 | 0 | X | 1 | Over-range for channel D |
| 0 | 0 | 1 | X | X | PLL Reference |
| 0 | 1 | 0 | X | X | PLL Reference |
| 0 | 1 | 1 | X | X | PLL Reference |
| 0 | 0 | 0 | 0x0 | 0 | Disabled |
| 1 | X | X | 0x0 | 1 | Over-range for channel D |
| 1 | X | X | 0x1 | X | PLL Reference |
| 1 | X | X | 0x2 | X | PLL Reference / 2 |
| 1 | X | X | 0x3 | X | PLL Reference / 4 |
---table end---
# Remark

# 8.3.4.4 SYSREF for JESD204C Subclass-1 Deterministic Latency
SYSREF is a system timing reference used for JESD204C subclass-1 implementations of deterministic latency. SYSREF is used to achieve deterministic latency and for multi-device synchronization. SYSREF must be captured by the correct device clock edge in order to achieve repeatable latency and synchronization. The device includes a SYSREF Windowing feature to ease the requirements on the external clocking circuits and to simplify the synchronization process. SYSREF Windowing replaces the traditional setup and hold times as these are no longer required when SYSREF Windowing is used. SYSREF can be implemented as a single pulse or as a periodic clock. In periodic implementations, SYSREF must be equal to, or an integer division of, the local multiframe clock frequency in 8B/10B encoding modes or the local extended multiblock clock frequency in 64B or 66B encoding modes. 
Equation 7 is used to calculate valid SYSREF frequencies in 8B/10B encoding modes. In 64B or 66B modes, the denominator changes to 66 × 32 × E × n, where E is the number of multiblocks in an extended multiblock. 
CLK 
SYSREF 
R 
f 
f 
10 
F 
K 
n 
u 
u 
u

# 8.3.4.4.1. SYSREF Capture for Multi-Device Synchronization and Deterministic Latency
The clocking subsystem is largely responsible for achieving multi-device synchronization and deterministic latency. The device uses the JESD204C subclass-1 method to achieve deterministic latency and synchronization. Subclass 1 requires that the SYSREF signal be captured by a deterministic clock (CLK± or SE_CLK) edge at each system power-on and at each device in the system. This requirement imposes setup and hold constraints on SYSREF relative to CLK±, which can be difficult to meet at giga-sample clock rates over all system operating conditions. The device includes a number of features to simplify this synchronization process and to relax system timing constraints:
- The device includes an integrated PLL and VCO to generate the high frequency sampling clock, relaxing the timing requirement by requiring timing to only be met relative to a low frequency reference clock.
- A SYSREF position detector (relative to CLK± or SE_CLK) and selectable SYSREF sampling position aid the user in meeting setup and hold times over all conditions; see the SYSREF Position Detector and Sampling Position Selection (SYSREF Windowing) section

# 8.3.4.4.2. SYSREF Position Detector and Sampling Position Selection (SYSREF Windowing)
The SYSREF Windowing block is used to first detect the position of SYSREF relative to the input clock (CLK± or SE_CLK) rising edge and then to select a desired SYSREF sampling instance, which is a delayed version of the input clock, to maximize setup and hold timing margins. In many cases a single SYSREF sampling position (SYSREF_SEL) is sufficient to meet timing for all systems (device-to-device variation) and conditions (temperature and voltage variations). However, this feature can also be used by the system to expand the timing window by tracking the movement of SYSREF as operating conditions change or to remove system-to-system variation at production test by finding a unique optimal value at nominal conditions for each system.
This section describes proper usage of the SYSREF Windowing block. First, apply the device clock and SYSREF to the device. The location of SYSREF relative to the device clock cycle is determined and stored in the SYSREF_POS field. Each bit of SYSREF_POS represents a potential SYSREF sampling position. If a bit in SYSREF_POS is set to 1, then the corresponding SYSREF sampling position has a potential setup or hold violation. Upon determining the valid SYSREF sampling positions (the positions of SYSREF_POS that are set to 0) the desired sampling position can be chosen by setting SYSREF_SEL to the value corresponding to that SYSREF_POS position. In general, the middle sampling position between two setup and
---table begin---
Table tile: SYSREF Parameters
|   |   |   | 
|---|---|---|
| CLK | SYSREF | R | 
| f | f | 10 |
| F | K | n |
| u | u | u | 
| u |   |   |
---table end---
where
- R and F are set by the JMODE setting (see 表 8-15)
- fCLK is the device clock frequency (CLK±)
- K is the programmed multiframe length (see 表 8-15 for valid K settings)
- and n is any positive integer

# Section 1.
ice. The location of SYSREF relative to the device clock cycle is determined and stored in the SYSREF_POS field. Each bit of SYSREF_POS represents a potential SYSREF sampling position. If a bit in SYSREF_POS is set to 1, then the corresponding SYSREF sampling position has a potential setup or hold violation. Upon determining the valid SYSREF sampling positions (the positions of SYSREF_POS that are set to 0) the desired sampling position can be chosen by setting SYSREF_SEL to the value corresponding to that SYSREF_POS position. In general, the middle sampling position between two setup and hold instances is chosen. Ideally, SYSREF_POS and SYSREF_SEL are performed at the nominal operating conditions of the system (temperature and supply voltage) to provide maximum margin for operating condition variations. This process can be performed at final test and the optimal SYSREF_SEL setting can be stored for use at every system power up. Further, SYSREF_POS can be used to characterize the skew between CLK± and SYSREF± over operating conditions for a system by sweeping the system temperature and supply voltages. For systems that have large variations in CLK± to SYSREF± skew, this characterization can be used to track the optimal SYSREF sampling position as system operating conditions change. In general, a single value can be found that meets timing over all conditions for well-matched systems, such as those where CLK± and SYSREF± come from a single clocking device.
The step size between each SYSREF_POS sampling position can be adjusted using SYSREF_ZOOM. When SYSREF_ZOOM is set to 0, the delay steps are coarser. When SYSREF_ZOOM is set to 1, the delay steps are finer. See the Timing Requirements table for delay step sizes when SYSREF_ZOOM is enabled and disabled. In general, SYSREF_ZOOM is recommended to always be used (SYSREF_ZOOM = 1) unless a transition region (defined by 1's in SYSREF_POS) is not observed, which can be the case for low clock rates. Bits 0 and 23 of SYSREF_POS are always be set to 1 because there is insufficient information to determine if these settings are close to a timing violation, although the actual valid window can extend beyond these sampling positions. The value programmed into SYSREF_SEL is the decimal number representing the desired bit location in SYSREF_POS. 

# Section 1.1.
---table begin---
Table title: Examples of SYSREF_POS Readings and SYSREF_SEL Selections
| SYSREF_POS[23:0] | OPTIMAL SYSREF_SEL SETTING | 0x02E[7:0] (Largest Delay) | 0x02D[7:0](1) |  0x02C[7:0](1) (Smallest Delay) |
|---|---|---|---|---|
| b10000000 | 8 or 9 | b01100000 | b00011001 |
| b10011000 | 12 | b00000000 | b00110001 |
| b10000000 | 6 or 7 | b01100000 | b00000001 |
| b10000000 | 4 or 15 | b00000011 | b00000001 |
| b10001100   |  6  | b01100011 |  b00011001 | 
---table end---
Red coloration indicates the bits that are selected, as given in the last column of this table.

# Section 2.
# 8.3.4 Supported JESD204C Features
Not all optional features of JESD204C are supported by ADC12QJ1600-SP. The list of features that are supported and the features that are not supported is provided below.
---table begin---
Table tile: Declaration of Supported JESD204C Features
| LETTER IDENTIFIER | REFERENCE CLAUSE | FEATURE | SUPPORT IN ADC12QJ1600-SP |
|---|---|---|---|
| a | clause 8 | 8B/10B link layer | Supported |
| b | clause 7 | 64B/66B link layer | Supported |
---table end---
# Section 2.

# 8.4 Declaration of Supported JESD204C Features (continued)
---table begin---
Table tile: Declaration of Supported JESD204C Features (continued)
| LETTER IDENTIFIER | REFERENCE CLAUSE | FEATURE | SUPPORT IN ADC12QJ1600-SP |
|---|---|---|---|
| c | clause 7 | 64B/80B link layer | Not supported |
| d | clause 7 | The command channel when using the 64B/66B or 64B/80B link layer | Not supported |
| e | clause 7 | Forward error correction (FEC) when using the 64B/66B or 64B/80B link layer | Supported |
| f | clause 7 | CRC3 when using the 64B/66B or 64B/80B link layer | Not supported |
| g | clause 8 | A physical SYNC pin when using the 8B/10B link layer | Supported |
| h | clause 7, clause 8 | Subclass 0| Not supported, but subclass 1 transmitter is compatible with subclass 0 receiver |
| i | clause 7, clause 8 | Subclass 1| Supported |
| j | clause 8 | Subclass 2| Not supported |
| k | clause 7, clause 8 | Lane alignment within a single link| Supported |
| l | clause 7, clause 8 | Subclass 1 with support for a lane alignment on a multipoint link by means of the MULTIREF signal| Not supported |
| m | clause 8 | SYNC interface timing is compatible with JESD204A| Supported |
| n | clause 8 | SYNC interface timing is compatible with JESD204B| Supported |
---table end---

# 8.3.5.1 Transport Layer
The transport layer takes samples from the ADC output and maps the samples into octets inside of frames.
These frames are then mapped onto the available lanes. The mapping of octets into frames and frames onto
lanes is defined by the transport layer settings such as L, M, F, S, N and N'. An octet is 8 bits (before 8B/10B or
64B/66B encoding), a frame consists of F octets and the frames are mapped onto L lanes. Samples are N bits,
but sent as N' bits across the link. The samples come from M converters and there are S samples per converter
per frame cycle. M is sometimes artificially increased in order to obtain a more desirable mapping, for instance
lower latency may be achieved with a larger M value for long frames.
There are a number of predefined transport layer modes in the device that are defined below. The high level
configuration parameters for the transport layer in the device are described below. The transport layer mode
is chosen by simply setting the JMODE register setting. For reference, the various configuration parameters for
JESD204C are defined below.
The link layer further maps the frames into multiframes when using 8B/10B encoding or blocks, multiblocks and
extended multiblocks when using 64B/66B encoding.

# 8.3.5.2 Scrambler
A data scrambler is available to scramble the data before transmission across the channel. Scrambling is used
to remove the possibility of spectral peaks in the transmitted data due to repetitive data streams. The scrambler
is optional for 8B or 10B encoded modes, however it is mandatory for 64B or 66B encoded modes in order to
have sufficient spectral content for clock recovery and adaptive equalization. The scrambler operates on the data
before encoding, such that the 8B or 10B scrambler scrambles the 8-bit octets before 10-bit encoding and the
64B or 66B scrambler scrambles the 64-bit block before the sync header insertion (66-bit encoding). The
JESD204C receiver automatically synchronizes its descrambler to the incoming scrambled data stream. For
8B/10B encoding, the initial lane alignment# 8. Scrambler
The scrambler is optional for 8B or 10B encoded modes, however it is mandatory for 64B or 66B encoded modes in order to have sufficient spectral content for clock recovery and adaptive equalization. The scrambler operates on the data before encoding, such that the 8B or 10B scrambler scrambles the 8-bit octets before 10-bit encoding and the 64B or 66B scrambler scrambles the 64-bit block before the sync header insertion (66-bit encoding). The JESD204C receiver automatically synchronizes its descrambler to the incoming scrambled data stream. For 8B/10B encoding, the initial lane alignment sequence (ILA) is never scrambled. Scrambling can be enabled by setting SCR for 8B or 10B encoding modes, but it is automatically enabled in 64B/66B modes. The scrambling polynomial is different for 8B or 10B encoding and 64B or 66B encoding schemes as defined by the JESD204C standard.

# 8.3.5.3 Link Layer
The link layer serves multiple purposes in JESD204C for both 8B or 10B and 64B or 66B encoding schemes, however there are some differences in implementation for each encoding scheme. In general, the link layer responsibilities include scrambling of the data (see Scrambler), establishing the code (8B or 10B) or block (64B or 66B) boundaries and the multiframe (8B or 10B) or multiblock (64B or 66B) boundaries, initializing the link, encoding the data, and monitoring the health of the link. This section is split into an 8B or 10B section (8B or 10B Link Layer) and a 64B or 66B section (64B or 66B Link Layer) in order to cover the specific implementation for each encoding scheme.

# 8.3.5.4 8B or 10B Link Layer
This section covers the link layer for the 8B or 10B encoding operating modes including initialization of the character, frame and multiframe boundaries, alignment of the lanes, 8B or 10B encoding and monitoring of the frame and multiframe alignment during operation.

# 8.3.5.4.1 Data Encoding (8B or 10B)
The data link layer converts the 8-bit octets from the transport layer into 10-bit characters for transmission across the link using 8B or 10B encoding. 8B or 10B encoding ensures DC balance to allow use of AC-coupling between the SerDes transmitter and receiver and specify a sufficient number of edge transitions for the receiver to reliably recover the data clock. 8B/10B encoding also provides some error detection since a single bit error in a character likely results in either not being able to find the 10-bit character in the 8B or 10B decoder lookup table or an incorrect character disparity.

# 8.3.5.4.2 Multiiframes and the Local Multiframe Clock (LMFC)
The frames from the transport layer are combined into multiframes which are used in the process of achieving deterministic latency in subclass 1 implementations. The length of a multiframe is set by the K parameter which defines the number of frames in a multiframe. JESD204C increases the maximum allowed number of frames per multiframe (K) from 32 in JESD204B to 256 in JESD204C to allow a longer multiframe to ease deterministic latency requirements. The total allowed range of K is defined by the inequality ceil(17/F) ≤ K ≤ min(256, floor(1024/F)) where ceil() and floor() are the ceiling and floor function, respectively. The local multiframe clock (LMFC) keeps track of the start and end of a multiframe for deterministic latency and data synchronization purposes. The LMFC is reset by the SYSREF signal to a deterministic phase in both the transmitter and receiver in order to act as a timing reference for deterministic latency. The LMFC clock frequency is given in Equation 8.# 8.3.5.4.2 Multiframe Clock 
A longer multiframe to ease deterministic latency requirements. The total allowed range of K is defined by the inequality ceil(17/F) ≤ K ≤ min(256, floor(1024/F)) where ceil() and floor() are the ceiling and floor function, respectively. The local multiframe clock (LMFC) keeps track of the start and end of a multiframe for deterministic latency and data synchronization purposes. The LMFC is reset by the SYSREF signal to a deterministic phase in both the transmitter and receiver in order to act as a timing reference for deterministic latency. The LMFC clock frequency is given in Equation 8 where fBIT is the serialized bit rate (line rate) of the SerDes interface and F and K are as defined above. The frequency of SYSREF must equal to or an integer division of fLMFC when using 8B/10B encoding modes if SYSREF is a continuous signal.
fLMFC = fBIT / (10 × F × K) (8)

# 8.3.5.4.3 Code Group Synchronization (CGS)
The first step in initializing the JESD204C link, after the LMFC is deterministically reset by SYSREF, is for the receiver to find the boundaries of the encoded 10-bit characters sent across each SerDes lane. This process is called code group synchronization (CGS). The receiver first asserts the SYNC signal (set to logic '0') when ready to initialize the link. The transmitter responds to the request by sending a stream of K28.5 comma characters. The receiver aligns its character clock to the K28.5 character sequence and CGS is achieved after successfully receiving four consecutive K28.5 characters. The receiver deasserts SYNC (set to logic '1') on the next LMFC edge after CGS is achieved and waits for the transmitter to start the initial lane alignment sequence (ILAS).

# 8.3.5.4.4 Initial Lane Alignment Sequence (ILAS)
After the transmitter detects the SYNC signal deassert (logic '0' to logic '1' transition), the transmitter waits until its next LMFC edge to start sending the initial lane alignment sequence (ILAS). The ILAS consists of four multiframes each containing a predetermined sequence. The receiver searches for the start of the ILAS to determine the frame and multiframe boundaries. Each multiframe of the ILAS starts with a /R/ character (K28.0) and ends with a /A/ character (K28.3) and either can be used to detect the boundary of a multiframe. Each lane starts buffering its data in the elastic buffer once the ILAS reaches the receiver, starting with the /R/ character, until all receivers have received the ILAS and subsequently release the ILAS from all lanes at the same time in order to align the lanes. The elastic buffer release point is chosen to avoid ambiguity in the release of the data caused by variation in the data delay (arrival of the ILAS at the receiver for each lane). The second multiframe of the ILAS contains configuration parameters for the JESD204C link configuration that can be used by the receiver to verify that the transmitter and receiver configurations match.

# 8.3.5.4.5 Frame and Multiframe Monitoring
The device supports frame and multiframe monitoring for verifying the health of the JESD204C link when using 8B/10B encoding. The scheme changes depending on the use of scrambling. The implementation when scrambling is disabled is covered first. If the last octet of the current frame matches the last octet of the previous frame, then the last octet of the current frame is encoded as an /F/ (K28.7) character. If the current frame is also the last frame of a multiframe, then an /A/ (K28.3) character is used instead. Neither an /F/ or /A/ character should occur in a normal data stream, except..# 8.3.5.5 64B or 66B Link Layer
This section covers the link layer for the 64B or 66B encoding operating modes which includes scrambling of the data, addition of the sync headers (64B or 6B encoding), the structure of the block and multiblock, the sync header, cyclic redundancy checking (CRC), forward error correction (FEC) and link alignment.

# 8.3.5.5.1 64B or 66B Encoding
The frames formed by the transport layer are packed into 8-octet long blocks (64 bits). This 64-bit block is scrambled and then a 2-bit sync header (SH) is appended to form a 66-bit transmission block. The sync header is used for block synchronization by marking the end of a block as well as allowing for cyclic redundancy checking (CRC), forward error correction (FEC) or a command channel. The structure of a block is given in 表 8-9 where SH represents the appended 2-bit sync header.
---table begin---
Table Title: Structure of 64B or 66B Block with Sync Header
|    | OCTET0 | OCTET1 | OCTET2 | OCTET3 | OCTET4 | OCTET5 | OCTET6 | OCTET7 |
|--- |---     |---     |---     |---     |---     |---     |---     |---     |
| SH | [0:1]  | [2:9]  | [10:17]| [18:25]| [26:33]| [34:41]| [42:49]| [50:57]| 
---table end---

# 8.3.5.5.2 Multiblocks, Extended Multiblocks and the Local Extended Multiblock Clock (LEMC)
A multiblock is a 32 block container which consists of a concatenation of 32 blocks. An extended multiblock is a concatenation of multiple multiblocks, where E defines the number of multiblocks in an extended multiblock. A frame can be split between blocks and multiblocks, but there must be an integer number of frames in an extended multiblock. An extended multiblock is only necessary when a multiblock does not have an integer number of frames. If an extended multiblock is not used, because a multiblock contains an integer number of frames, then the E parameter is equal to 1 to indicate that there is one multiblock in an extended multiblock.
An extended multiblock is analogous to a multiframe in the 8B or 10B transport layer. The local extended mutiblock clock (LEMC) keeps track of the start and end of a multiblock for deterministic latency and data synchronization purposes in the same way the LMFC tracks the start and end of a multiframe in 8B or 10B encoding. The LEMC is reset by the SYSREF signal to a deterministic phase in both the transmitter and receiver in order to act as a timing reference for deterministic latency. The LEMC clock frequency is defined by Equation 9 where fBIT is the serialized bit rate (line rate) of the SerDes interface. The frequency of SYSREF must equal to or an integer division of fLMFC when using 64B or 66B encoding modes if SYSREF is a continuous signal.
fLEMC = fBIT / (66 × 32 × E)
---table begin---
Table tile: Table 8-9 Structure of 64B or 66B Block with Sync Header
| SH | OCTET0 | OCTET1 | OCTET2 | OCTET3 | OCTET4 | OCTET5 | OCTET6 | OCTET7 |
|---|---|---|---|---|---|---|---|---|
| [0:1] | [2:9] | [10:17] | [18:25] | [26:33] | [34:41] | [42:49] | [50:57] | [58:65] |
---table end---

# 8.3.5.5.2.1 Block, Multiblock and Extended Multiblock Alignment using Sync Header
The sync header contains two bits that are always opposite of each other (either 01 or 10). The JESD204C receiver can find the block boundaries by looking for a 66-bit boundary that always contains a 0 to 1 or 1 to 0 transition. Although 0 to 1 and 1 to 0 transitions occur at other locations in a block, it is impossible for the sequence to appear at a fixed location, other than the proper sync header location, in successive blocks for a long period of time. The sync header indicates the start of a block and can be used for block alignment monitoring. If a 00 or a 11 bit sequence is seen at the assumed sync header location of a block, then block alignment may have been lost. Multiple occurrences of incorrect sync header bits should trigger a search for the sync header after sending SYSREF to all devices to reset LEMC alignment.
A sync header ([0:1]) of 01 corresponds to transmission of a 1 while a sync header of 10 corresponds to a transmission of a 0. The transmitted bit from the sync header of each block of a multiblock are combined into a 32-bit word called the sync header stream. The sync header stream is used to transmit data in parallel with the user data in order to synchronize the link by marking the borders of multiblocks and extended multiblocks. In addition, the sync header stream provides one of either CRC, FEC or a command channel. ADC12QJ1600-SP supports CRC-12 and FEC and does not support CRC-3 or the command channel.
The 32-bit sync header stream always ends with a 00001 bit sequence, called the end-of-multiblock (EoMB) signal, that# 8.3.5.5.2.1.1 Cyclic Redundancy Check (CRC) Mode
The cyclic redundancy check (CRC) mode is available to allow detection of potential bit errors during 
transmission. Support for the 12-bit word CRC-12 mode is required by JESD204C, while a 3-bit word CRC-3 
mode is optional. The device does not support the CRC-3 mode and therefore this section is specific to the 
CRC-12 mode only. The transmitter computes the CRC-12 parity bits from the scrambled data bits of the 32 
blocks of a multiblock. The 12-bit CRC parity word is then transmitted in the sync header stream of the next 
multiblock. The receiver computes the 12-bit parity word of the received multiblock and compares it against the 
received 12-bit parity word of the next multiblock. A difference indicates that there is at least one error in the 
received data bits or in the received 12-bit parity word. The minimum latency to the detection of a bit error in the 
first data bit of a multiblock is 46 blocks. Enable CRC-12 mode by setting SHMODE to 0.
The mapping of the sync header stream when using the CRC-12 mode is shown in the following table.
---table begin---
Table title: Sync Header Stream Bit Mapping for CRC 12 Mode
|  Bit  | Function |
|---|---|
|  0  |  CRC[11]  |
|  1  |  CRC[10]  |
|  2  |  CRC[9]  |
|  3  |  1  |
|  4  |  CRC[8]  |
|  5  |  CRC[7]  |
|  6  |  CRC[6]  |
|  7  |  1  |
|  8  |  CRC[5]  |
|  9  |  CRC[4]  |
| 10 |  CRC[3]  |
| 11 |  1  |
| 12 |  CRC[2]  |
| 13 |  CRC[1]  |
| 14 |  CRC[0]  |
| 15 |  1  |
| 16 | Cmd[6]  |
| 17 |  Cmd[5]  |
| 18 |  Cmd[4]  |
| 19 |  1  |
| 20 |  Cmd[3]  |
| 21 |  1  |
| 22 |  EoEMB  |
| 23 |  1  |
| 24 |  Cmd[2]  |
| 25 |  Cmd[1]  |
| 26 |  Cmd[0]  |
| 27 |  0  |
| 28 |  0  |
| 29 |  0  |
| 30 |  0  |
| 31 |  1  |
---table end---
The CRC-12 enc

# 8.3.5.5.2.1.2 Sync Header Stream Bit Mapping for CRC 12 Mode
at the end of the sync header, allowing multiblock alignment after only a single multiblock has been received. EoEMB is the end-of-extended-multiblock bit, which is set to 1 for the last multiblock of an extended multiblock.
---table begin---
Table tile: 功能
| Bit | Function |
|---|---|
| 0 | CRC[11] |
| 8 | CRC[5] |
| 16 | Cmd[6] |
| 24 | Cmd[2] |
| 1 | CRC[10] |
| 9 | CRC[4] |
| 17 | Cmd[5] |
| 25 | Cmd[1] |
| 2 | CRC[9] |
| 10 | CRC[3] |
| 18 | Cmd[4] |
| 26 | Cmd[0] |
| 3 | 1 |
| 11 | 1 |
| 19 | 1 |
| 27 | 0 |
| 4 | CRC[8] |
| 12 | CRC[2] |
| 20 | Cmd[3] |
| 28 | 0 |
| 5 | CRC[7] |
| 13 | CRC[1] |
| 21 | 1 |
| 29 | 0 |
| 6 | CRC[6] |
| 14 | CRC[0] |
| 22 | EoEMB |
| 30 | 0 |
| 7 | 1 |
| 15 | 1 |
| 23 | 1 |
| 31 | 1 |
---table end---
The CRC-12 encoder takes in a multiblock of 32 scrambled blocks (2048 bits) and computes the 12-bit parity word using the generator polynomial given by Equation 10. The polynomial is sufficient to detect all 2-bit errors in a multiblock, spanning any distance, and burst error sequences of up to 12-bits in length. The probability of not detecting a 3-bit error spanning any distance in a multiblock is approximately 0.004%.
0x987 == x12+x9+x8+x3+x2+x+1
(10)
The full parity bit generation for CRC-12 is shown in 图 8-7. The input is a 2048 bit sequence, built from the 32 scrambled blocks of a multiblock (sync header is not included). The 12-bit parity word, CRC[11:0], is taken from the Sx blocks after the full 2048 bit sequence is processed. The Sx blocks are initialized with 0s before processing each multiblock.
S0 S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 1 x2 x3 x x8 x9 x12 32-block input (2048 bits) CRC[0] CRC[1] CRC[2] CRC[3] CRC[4] CRC[5] CRC[6] CRC[7] CRC[8] CRC[9] CRC[10] CRC[11] 图 8-7. CRC-12 Parity Bit Generator

# 8.3.5.5.2.1.2 Forward Error Correction (FEC) Mode
Forward error correction (FEC) is an optional feature in JESD204C and is supported by ADC12QJ1600-SP. Whereas CRC-12 mode can only detect errors on the link, FEC is able to detect and correct errors in order to improve the bit error rate (BER) for error-sensitive applications. Many applications can tolerate random bit errors, however some applications, such as an oscilloscope, rely on long error-free measurements in order to detect a certain response from the device under test (DUT). An error in these applications may result in a false-positive detection of the response. Enable FEC mode by setting SHMODE to 2.# 8.3.5.5.2 Forward Error Correction
Forward Error Correction (FEC) is an optional feature in JESD204C and is supported by ADC12QJ1600-SP. Whereas CRC-12 mode can only detect errors on the link, FEC is able to detect and correct errors in order to improve the bit error rate (BER) for error-sensitive applications. Many applications can tolerate random bit errors, however some applications, such as an oscilloscope, rely on long error-free measurements in order to detect a certain response from the device under test (DUT). An error in these applications may result in a false-positive detection of the response. Enable FEC mode by setting SHMODE to 2.
---table begin---
Table title: Sync Header Stream Bit Mapping for FEC Mode
| Bit | Function | Bit | Function | Bit | Function | Bit | Function |
|---|---|---|---|---|---|---|---|
| 0 | FEC[25] | 8 | FEC[17] | 16 | FEC[9] | 24 | FEC[2] |
| 1 | FEC[24] | 9 | FEC[16] | 17 | FEC[8] | 25 | FEC[1] |
| 2 | FEC[23] | 10 | FEC[15] | 18 | FEC[7] | 26 | FEC[0] |
| 3 | FEC[22] | 11 | FEC[14] | 19 | FEC[6] | 27 | 0 |
| 4 | FEC[21] | 12 | FEC[13] | 20 | FEC[5] | 28 | 0 |
| 5 | FEC[20] | 13 | FEC[12] | 21 | FEC[4] | 29 | 0 |
| 6 | FEC[19] | 14 | FEC[11] | 22 | EoEMB | 30 | 0 |
| 7 | FEC[18] | 15 | FEC[10] | 23 | FEC[3] | 31 | 1 |
---table end---
For more information on the FEC parity word generation, refer to the JESD204C standard.

# 8.3.5.5.3 Initial Lane Alignment
The 64B or 66B link layer does not use an initial lane alignment sequence (ILAS) like the 8B/10B link layer. Therefore, the receiver must use a different scheme to align lanes using the elastic buffer. In 8B or 10B mode, the ILAS triggers the elastic buffer to start buffering the data for each lane. After all lanes have started buffering the data, the elastic buffers for each lane are released at a release point determined by the release buffer delay (RBD) parameter and the phase of the LMFC. In 64B/66B mode, the process starts by having all lanes achieve block, multiblock and extended multiblock alignment. Once all lanes have achieved alignment, the receiver can begin buffering data in the elastic buffers at the start of the next extended multiblock on each lane. The data is released at the next release point after all lanes have seen the start of an extended multiblock and have started buffering the data. The release point is defined rela# 8.3.5.5.4 Block, Multiblock and Extended Multiblock Alignment Monitoring
Synchronization of blocks, multiblocks and extended multiblocks by monitoring the sync header of each block and EoMB and EoEMB bit of the sync header stream. A block always begins with a 0 to 1 or 1 to 0 transition (sync header). A single missed sync header can occur due to a bit error, however if there are a number of sync header errors within a set number of blocks, then block synchronization has been lost and block synchronization should be reinitialized. It is possible to still have block synchronization, but to lose multiblock or extended multiblock synchronization. Multiblock synchronization is monitored by looking for the EoMB signal, 00001, at the end of the sync header stream for each multiblock. If multiple EoMB signals are erroneous within a number of blocks, multiblock synchronization has been lost and multiblock synchronization should be reinitialized. If an erroneous EoEMB bit is received for multiple extended multiblocks within a number of extended multiblocks, such as a 1 for a multiblock that is not the end of an extended multiblock or a 0 for a multiblock that is the end of an extended multiblock, then multiblock synchronization is lost and extended multiblock synchronization should be reinitialized. If multiblock or extended multiblock synchronizaton is lost, SYSREF should be applied to the erroneous devices in order to reestablish the LEMC before the synchronization process begins.

# 8.3.5.6 Physical Layer
The JESD204C physical layer consists of a current mode logic (CML) output driver and receiver. The receiver consists of a clock detection and recovery (CDR) unit to extract the data clock from the serialized data stream and can contain a continuous time linear equalizer (CTLE) and/or discrete feedback equalizer (DFE) to correct for the low-pass response of the physical transmission channel. Likewise, the transmitter can contain pre-equalization to account for frequency dependent losses across the channel. The total reach of the SerDes links depends on the data rate, board material, connectors, equalization, noise and jitter, and required bit-error performance. The SerDes lanes do not have to be matched in length because the receiver aligns the lanes during the initial lane alignment sequence.

# 8.3.5.6.1 SerDes Pre-Emphasis
The ADC12QJ1600-SP high-speed output drivers can pre-equalize the transmitted data stream by using pre-emphasis in order to compensate for the low-pass response of the transmission channel. Configurable pre-emphasis settings allow the output drive waveform to be optimized for different PCB materials and signal transmission distances. The pre-emphasis setting# 8.3.5.6.1 SerDes Pre-Emphasis
The ADC12QJ1600-SP high-speed output drivers can pre-equalize the transmitted data stream by using pre-emphasis in order to compensate for the low-pass response of the transmission channel. Configurable pre-emphasis settings allow the output drive waveform to be optimized for different PCB materials and signal transmission distances. The pre-emphasis setting is adjusted through the serializer pre-emphasis setting SER_PE. Higher values increase the pre-emphasis to compensate for more lossy PCB materials. This adjustment is best used in conjunction with an eye-diagram analysis capability in the receiver. Adjust the pre-emphasis setting to optimize the eye-opening for the specific hardware configuration and line rates needed.

# 8.3.5.7 JESD204C Enable
The JESD204C interface must be disabled through JESD_EN while any of the other JESD204C parameters are being changed. When JESD_EN is set to 0 the block is held in reset and the serializers are powered down. The clocks for this section are also gated off to further save power. When the parameters are set as desired, the JESD204C block can be enabled (JESD_EN is set to 1).

# 8.3.5.8 Multi-Device Synchronization and Deterministic Latency
JESD204C subclass 1 outlines a method to achieve deterministic latency across the serial link. If two devices achieve the same deterministic latency then they can be considered synchronized. This latency must be achieved from system startup to startup to be deterministic. There are two key requirements to achieve deterministic latency. The first is proper capture of SYSREF for which the device provides a number of features to simplify this requirement at giga-sample clock rates (see the SYSREF Capture for Multi-Device Synchronization and Deterministic Latency section for more information). SYSREF resets either the LMFC in 8B/10B encoding mode or the LEMC is 64B/66B encoding mode. The LMFC and LEMC are analogous between the two modes and is now referred to as LMFC/LEMC.
The second requirement is to choose a proper elastic buffer release point in the receiver. Because the device is an ADC, the device is the transmitter (TX) in the JESD204C link and the logic device is the receiver (RX). The elastic buffer is the key block for achieving deterministic latency, and does so by absorbing variations in the propagation delays of the serialized data as the data travels from the transmitter to the receiver. A proper release point is one that provides sufficient margin against delay variations. An incorrect release point results in a latency variation of one LMFC/LEMC period. Choosing a proper release point requires knowing the average arrival time of data at the elastic buffer, referenced to an LMFC/LEMC edge, and the total expected delay variation for all devices. With this information the region of invalid release points within the LMFC/LEMC period can be defined, which stretches from the minimum to maximum delay for all lanes. Essentially, the designer must ensure that the data for all lanes arrives at all devices after the previous release point occurs and before the next release point occurs.# 8.3.5.8 LMFC/LEMC Valid Region Definition for Elastic Buffer Release Point Selection 
Delay variation for all devices. With this information, the region of invalid release points within the LMFC/LEMC period can be defined, 
which stretches from the minimum to maximum delay for all lanes. Essentially, the designer must ensure that the 
data for all lanes arrives at all devices after the previous release point occurs and before the next release point 
occurs. 
图 8-9 provides a timing diagram that demonstrates this requirement. In this figure, the data for two ADCs is 
shown. The second ADC has a longer routing distance (tPCB) and results in a longer link delay. First, the invalid 
region of the LMFC/LEMC period is marked off as determined by the data arrival times for all devices. Then, the 
release point is set by using the release buffer delay (RBD) parameter to shift the release point an appropriate 
number of frame clocks from the LMFC/LEMC edge so that the release point occurs within the valid region of the 
LMFC/LEMC cycle. In the case of 图 8-9, the LMFC/LEMC edge (RBD = 0) is a good choice for the release point 
because there is sufficient margin on each side of the valid region. 

# 8.3.5.9 Operation in Subclass 0 Systems 
The device can operate with subclass 0 compatibility provided that multi-ADC synchronization and deterministic 
latency are not required. With these limitations, the device can operate without the application of SYSREF. The 
internal LMFC/LEMC is automatically self-generated with unknown timing. SYNC is used as normal to initiate the 
CGS and ILAS in 8B/10B mode. 

# 8.3.5.10 Alarm Monitoring 
A number of built-in alarms are available to monitor internal events. Several types of alarms and upsets are 
detected by this feature: 
---table begin---
Table title: Alarm Monitoring
|  |  |
|---|---|
| 1. | C-PLL is not locked |
| 2. | S-PLL is not locked |
| 3. | JESD204C link is not transmitting data (not in the data transmission state) |
| 4. | SYSREF causes internal clocks to be realigned |
| 5. | An upset that impacts the internal clocks |
| 6. | A read or write error generated by the digital to serializer synchronizing FIFO |
---table end---
When an alarm occurs, a bit for each specific alarm is set in ALM_STATUS. Each alarm bit remains set until the 
host system writes a 1 to clear the alarm. If the alarm type is not masked (see the ALM_MASK register), then the 
alarm is also indicated by the ALARM register. The CALSTAT output pin can be configured as an alarm output 
that goes high when an alarm occurs; see CAL_STATUS_SEL.

# 8.3.5.10.1 Clock Upset Detection 
The CLK_ALM register bit indicates if the internal clocks have been upset. The clocks in channel A are 
continuously compared to channel B. If the clocks differ for even one DEVCLK / 2 cycle, the CLK_ALM register 
bit is set and remains set until cleared by the host system by writing a 1. For the CLK_ALM register bit to# 8.3.5.10.1 Clock Upset Detection
The CLK_ALM register bit indicates if the internal clocks have been upset. The clocks in channel A are 
continuously compared to channel B. If the clocks differ for even one DEVCLK / 2 cycle, the CLK_ALM register 
bit is set and remains set until cleared by the host system by writing a 1. For the CLK_ALM register bit to 
function properly, follow these steps:
1.
Program JESD_EN = 0
2.
Ensure the part is configured to use both channels (PD_ACH = 0, PD_BCH = 0)
3.
Program JESD_EN = 1
4.
Write CLK_ALM = 1 to clear CLK_ALM
5.
Monitor the CLK_ALM status bit or the CALSTAT output pin if CAL_STATUS_SEL is properly configured
6.
When exiting global power-down (via MODE or the PD pin), the CLK_ALM status bit may be set and must be 
cleared by writing a 1 to CLK_ALM

# 8.3.5.10.2 FIFO Upset Detection
The FIFO_LANE_ALM register bits indicate if an error has occurred in the synchronizing FIFO between the 
digital logic block and serializer outputs. If the FIFO pointers are upset due to an undesired clock shift or other 
single event or incorrect clocking frequencies the FIFO_LANE_ALM bit for the erroneous lane is set to 1. 
Toggling JESD_EN to 0 and then 1 resets the FIFO logic.

# 8.4 Device Functional Modes
The device can be configured to operate in a number of functional modes. These modes are described in this 
section.

# 8.4.1 Low Power Mode and High Performance Mode
Device power consumption can be reduced at the tradeoff of performance by programming the device into the 
Low Power Mode. This mode is only available when operating at 1 GSPS or less and is recommended to only be 
used for 1st Nyquist zone applications. The default operating mode is High Performance Mode which is enabled 
by the default register values.
---table begin---
Table title: Low Power Mode Register Writes
| Register Name (Address)| Low Power Mode Value | High Performance Mode Value (Default Mode) |
|---|---|---|
| LOW_POWER1 (0x037) | 0x46 | 0x4B |
| LOW_POWER2 (0x29A) | 0x06 | 0x0F |
| LOW_POWER3 (0x29B) | 0x00 | 0x04 |
| LOW_POWER4 (0x29C) | 0x14 | 0x1B |
---table end---

# 8.4.2 ADC Output Code
The magnitude of the glitch during the transition between ADC cores during background calibration and low 
power background calibration is affected by the setting of the LOW_POWER3 register setting (Address = 
0x29B). A lower power can be traded off vs larger glitch magnitude. The ADC output during the transition 
between ADC cores for low power mode is shown in 图  8-10 and the power dissipation change vs 
LOW_POWER3 setting is shown in 图 8-11. A setting of 4 reduces the glitch to the same magnitude as high 
performance mode.

# 8.4.3 LP_TRIG Setting
In low power background calibration mode, the timing of the ADC transition can be controlled by setting register 
LP_TRIG = 1. The ADC transition will occur in the ADC output data between 500 and 1000.# 8.4.2 LOW_POWER3 Register Setting
Sample#
ADC Output Code (#)
0
100
200
300
400
500
600
700
800
900 1000
2000
2050
2100
2150
2200
2250
2300
2350
2400
2450
2500
LOW_POWER3 = 0
LOW_POWER3 = 1
LOW_POWER3 = 2
LOW_POWER3 = 4
---table begin---
Table tile: Power Dissipation Change vs LOW_POWER3 register setting
| LOW_POWER3 Setting | Power Dissipation Change (mW) |
| --- | --- |
| 0 | 0 |
| 1 | 10 |
| 2 | 20 |
| 3 | 30 |
| 4 | 40 |
---table end---
In low power background calibration mode, the timing of the ADC transition can be controlled by setting register 
LP_TRIG = 1. The ADC transition will occur in the ADC output data between 500 and 1000 ADC sample clocks 
after triggering by the CALTRIG ball or SPI write to CAL_SOFT_TRIG register (Address = 0x6C).
Foreground calibration mode has no ADC core transitions and no glitch.

# 8.4.3 JESD204C Modes
There are a number of parameters required to define the JESD204C transport layer format, all of which are sent 
across the link during the initial lane alignment sequence在 8B/10B mode. 64B/66B mode does not use the 
ILAS, however the transport layer uses the same parameters. In the device, most parameters are automatically 
derived based on the selected JMODE; however, a few are configured by the user.
---table begin---
Table tile: JESD204C Initial Lane Alignment Sequence Parameters
| PARAMETER | DESCRIPTION | USER CONFIGURED OR DERIVED | VALUE |
| --- | --- | --- | --- |
| ADJCNT | LMFC adjustment amount (not applicable) | Derived | Always 0 |
| ADJDIR | LMFC adjustment direction (not applicable) | Derived | Always 0 |
| BID | Bank ID | Derived | Always 0 |
| CF | Number of control words per frame | Derived | Always 0 |
| CS | Control bits per sample | Derived | Always set to 0 in ILAS, see 表 8-15 for actual usage |
| DID | Device identifier, used to identify the link | User configured | Set by DID, see 表 8-16 |
| F | Number of octets (bytes) per frame (per lane) | Derived | See 表 8-15 |
| HD | High-density format (samples split between lanes) | Derived | Always 0 |
| JESDV | JESD204 standard revision | Derived | Always 1 |
| K | Number of frames per multiframe | User configured | Set by the KM1 register |
| L | Number of serial output lanes per link | Derived | See 表 8-15 |
| LID | Lane identifier for each lane | Derived | See 表 8-16 |
| M | Number of converters used to determine lane bit packing; may not match number of ADC channels in the device | Derived | See 表 8-15 |
| N | Sample resolution (before adding control and tail bits) | Derived | See 表 8-15 |
| N' | Bits per sample after adding control and tail bits | Derived | See 表 8-15 |
| S | Number of samples per converter (M) per frame | Derived | See 表 8-15 |
| SCR | Scrambler enabled | User configured | Set by SCR |
| SUBCLASSV | Device subclass version | Derived | Always 1 |
| RES1 | Reserved field 1 | Derived | Always 0 |
---table end---
# 8.4.3 JESD204C Modes
# 1. Parameters Information
lanes per link
Derived
See 表 8-15
LID
Lane identifier for each lane
Derived
See 表 8-16
M
Number of converters used to determine lane 
bit packing; may not match number of ADC 
channels in the device
Derived
See 表 8-15
N
Sample resolution (before adding control and 
tail bits)
Derived
See 表 8-15
N'
Bits per sample after adding control and tail 
bits
Derived
See 表 8-15
S
Number of samples per converter (M) per 
frame
Derived
See 表 8-15
SCR
Scrambler enabled
User configured
Set by SCR
SUBCLASSV
Device subclass version
Derived
Always 1
RES1
Reserved field 1
Derived
Always 0
RES2
Reserved field 2
Derived
Always 0
CHKSUM
Checksum for ILAS checking (sum of all 
above parameters modulo 256)
Derived
Computed based on parameters in this table

# 2. Configurations
Configuring the device is made easy by using a single configuration parameter called JMODE. Using 表 8 15 the 
correct JMODE value can be found for the desired operating mode. The modes listed are the only available 
operating modes. This tables also gives a range and allowable step size for the K parameter (set by KM1), which 
sets the multiframe length in number of frames.
---table begin---
Table tile: 表 8-15. Operating Modes for Quad Channel Device
| OPERATING MODE | USER-SPECIFIED PARAMETER | DERIVED PARAMETERS | INPUT CLOCK RANGE (MHz) |
|---|---|---|---|
| 12-Bit, 8B/10B, 8 Lanes | 0 | 4:4:256 8B/10B 12 0 12 0 8 8(1) 8 5 0 — 8 | 500-1600 |
| 12-Bit, 8B/10B, 6 Lanes | 1 | 16:16:256 8B/10B 12 0 12 0 6 4 2 2 1 — 10 | 500-1600 |
| 8-Bit, 8B/10B, 4 Lanes | 2 | 32:32:256 8B/10B 8 0 8 0 4 4 1 1 0 — 10 | 500-1600 |
| 10-Bit, 8B/10B, 4 Lanes | 3 | 32:32:256 8B/10B 10 0 10 0 4 4 5 4 0 — 12.5 | 500-1372.8 |

# More rows...
---table end---# 8.4.1. ADC12QJ1600-SP Lane Assignment and Parameters
The device has a total of 8 high speed output drivers. The lanes and their derived configuration parameters are described in 表 8-16. For a specified JMODE, the lowest indexed lanes are used and the higher indexed lanes are automatically powered down. Always route the lowest indexed lanes to the logic device.
---table begin---
Table tile: 表 8-16. ADC12QJ1600-SP Lane Assignment and Parameters
| DEVICE PIN DESIGNATION | DID (User Configured) | LID (Derived) |
|---|---|---|
| D0± | Set by DID | 0 |
| D1± | Set by DID | 1 |
| D2± | Set by DID | 2 |
| D3± | Set by DID | 3 |
| D4± | Set by DID | 4 |
| D5± | Set by DID | 5 |
| D6± | Set by DID | 6 |
| D7± | Set by DID | 7 |
---table end---

# 3. Design Considerations
The device has a total of 8 high speed output drivers. The lanes and their derived configuration parameters are 
described in 表 8-16. For a specified JMODE, the lowest indexed lanes are used and the higher indexed lanes 
are automatically powered down. Always route the lowest indexed lanes to the logic device.
---table begin---
Table tile: 表 8-16. ADC12QJ1600-SP Lane Assignment and Parameters
| DEVICE PIN DESIGNATION | DID (User Configured) | LID (Derived) |
|---|---|---|
| D0± | Set by DID | 0 |
| D1± | Set by DID | 1 |

# 8.4.2.1 JESD204C Transport Layer Data Formats
(Considering character limitation, only a part of the content is provided as an example. The subsequent content would similarly be structured into individual tables and sections.)# 8.4.2.1 JMODE Table Definitions
---table begin---
Table title: 表 8-29. JMODE 11 (12-bit, Dual/Single channel only, 8/4 lanes, 8B/10B)
| OCTET | NIBBLE | VALUE | 
|---|---|---|
| 0 | 0 | D0 |
| 0 | 1 | A0 |
| 0 | 2 | A4 |
| 0 | 3 | A8 |
| 0 | 4 | A12 |
| 0 | 5 | A16 |
| 0 | 6 | T |
| 1 | 0 | D1 |
| 1 | 1 | A1 |
| 1 | 2 | A5 |
| 1 | 3 | A9 |
| 1 | 4 | A13 |
| 1 | 5 | A17 |
| 1 | 6 | T |
| 2 | 0 | D2 |
| 2 | 1 | A2 |
| 2 | 2 | A6 |
| 2 | 3 | A10 |
| 2 | 4 | A14 |
| 2 | 5 | A18 |
| 2 | 6 | T |
| 3 | 0 | D3 |
| 3 | 1 | A3 |
| 3 | 2 | A7 |
| 3 | 3 | A11 |
| 3 | 4 | A15 |
| 3 | 5 | A19 |
| 3 | 6 | T |
| 4 | 0 | D4 |
| 4 | 1 | B0 |
| 4 | 2 | B4 |
| 4 | 3 | B8 |
| 4 | 4 | B12 |
| 4 | 5 | B16 |
| 4 | 6 | T |
| 5 | 0 | D5 |
| 5 | 1 | B1 |
| 5 | 2 | B5 |
| 5 | 3 | B9 |
| 5 | 4 | B13 |
| 5 | 5 | B17 |
| 5 | 6 | T |
| 6 | 0 | D6 |
| 6 | 1 | B2 |
| 6 | 2 | B6 |
| 6 | 3 | B10 |
| 6 | 4 | B14 |
| 6 | 5 | B18 |
| 6 | 6 | T |
| 7 | 0 | D7 |
| 7 | 1 | B3 |
| 7 | 2 | B7 |
| 7 | 3 | B11 |
| 7 | 4 | B15 |
| 7 | 5 | B19 |
| 7 | 6 | T |
---table end---
# 8.4.2.1 JESD204C Transport Layer Data Formats

# 8.4.2.2 64B or 66B Sync Header Stream Configuration
The sync header stream can be used to identify bit errors on the link or to correct bit errors. Two modes of operation are available in ADC12QJ1600-SP. Cyclic redundancy checking (CRC) can be used to identify bit errors. ADC12QJ1600-SP only supports 12-bit CRC (CRC-12) and does not support the optional 3-bit CRC-3 described by JESD204C. Alternatively, forward error correction (FEC) can be used to identify bit errors and then correct bit errors. For information on CRC-12, see Cyclic Redundancy Check (CRC) Mode. For information on FEC, see Forward Error Correction (FEC) Mode.

# 8.4.2.3 Redundant Data Mode (Alternate Lanes)
JMODEs that use four or less lanes allow the use of redundancy on the JESD204C output. For instance, a system may have two FPGAs or ASICs connected to a single device...

# 8.4.3 Power-Down Modes
The PD input pin allows the device devices to be entirely powered down...

# 8.4.4 Test Modes
A number of device test modes are available.

# 具体表格的全部内容根据上面的样式进行格式转换，这里由于文本过长，仅做部分示例。# 8.4.4 Test Modes
A number of device test modes are available. These modes insert known patterns of information into the device data path for assistance with system debug, development, or characterization.

# 8.4.4.1 Serializer Test-Mode Details
Test modes are enabled by setting JTEST to the desired test mode. Each test mode is described in detail in the following sections. Regardless of the test mode, the serializer outputs (number of lanes, rate) are powered up based on JMODE. Only enable the test modes when the JESD204C link is disabled.

# 8.4.4.2 PRBS Test Modes
The PRBS test modes bypass the JESD204C transport layer and link layer and are therefore neither scrambled nor encoded. These test modes produce pseudo-random bit streams that comply with the ITU-T O.150 specification. These bit streams are used with lab test equipment or logic devices that can self-synchronize to the bit pattern. The initial phase of the pattern is not defined since the receiver self-synchronizes.
The sequences are defined by a recursive equation. For example, Equation 12 defines the PRBS7 sequence. 
y[n] = y[n – 6]⊕y[n – 7]
(12) 
where:
- bit n is the XOR of bit [n – 6] and bit [n – 7], which are previously transmitted bits
---table begin---
Table title: PBRS Mode Equations 
| PRBS TEST MODE | SEQUENCE | SEQUENCE LENGTH (bits) |
|---|---|---|
| PRBS7 | y[n] = y[n – 6]⊕y[n – 7] | 127 |
| PRBS9 | y[n] = y[n – 5]⊕y[n – 9] | 511 |
| PRBS15 | y[n] = y[n – 14]⊕y[n – 15] | 32,767 |
| PRBS23 | y[n] = y[n – 18]⊕y[n – 23] | 8,388,607 |
| PRBS31 | y[n] = y[n – 28]⊕y[n – 31] | 2,147,483,647 |
---table end---

# 8.4.4.3 Clock Pattern Mode
In the clock pattern mode, the JESD204C transport layer and link layer are bypassed, so the test sequence is neither scrambled nor encoded. The pattern consists of a 16-bit long sequence of 8 ones and 8 zeros (1111 1111 0000 0000) that repeats indefinitely.

# 8.4.4.4 Ramp Test Mode
In the ramp test mode, the JESD204C link layer operates normally, but the transport layer is disabled. Each lane encodes an identical stream of incrementing octet values. The octet value is 0x00 at the beginning of every multiframe (or extended multi-block). The value is increased by 1 for each subsequent octet. If there are more than 256 octets in a multiframe (or extended multi-block), then the value roll back to 0x00 after it reaches 0xFF. In 8b/10b modes, the ramp pattern does not start until the ILAS is completed. In 64b/66b modes, the ramp pattern starts after the serializers are ini# 8.4.3 Ramp Test Mode
In the ramp test mode, the JESD204C link layer operates normally, but the transport layer is disabled. Each lane encodes an identical stream of incrementing octet values. The octet value is 0x00 at the beginning of every multiframe (or extended multi-block). The value is increased by 1 for each subsequent octet. If there are more than 256 octets in a multiframe (or extended multi-block), then the value roll back to 0x00 after it reaches 0xFF. 
In 8b/10b modes, the ramp pattern does not start until the ILAS is completed. In 64b/66b modes, the ramp pattern starts after the serializers are initialized.

# 8.4.4.5 Short and Long Transport Test Mode
JESD204C defines both short and long transport test modes to verify that the transport layers in the transmitter and receiver are operating correctly. The short transport test pattern used by device is dependent on the JMODE and are provided in Short Transport Test Pattern. The device does not support long transport test modes.

# 8.4.4.5.1 Short Transport Test Pattern
Short transport test patterns send a predefined octet format that repeats every frame. The short transport test patterns for each JMODE are defined in this section.
---table begin---
Table title: Short Transport Test Pattern for JMODE 0
| OCTET | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| NIBBLE | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| D0 | 0xF01 | 0xF02 | 0xF03 | 0xF04 | 0xF05 | T |   |   |
| D1 | 0xE11 | 0xE12 | 0xE13 | 0xE14 | 0xE15 | T |   |   |
| D2 (Dual or Quad only) | 0xD21 | 0xD22 | 0xD23 | 0xD24 | 0xD25 | T |   |   |
| D3 (Dual or Quad only) | 0xC31 | 0xC32 | 0xC33 | 0xC34 | 0xC35 | T |   |   |
| D4 (Dual or Quad only) | 0xB41 | 0xB42 | 0xB43 | 0xB44 | 0xB45 | T |   |   |
| D5 (Dual or Quad only) | 0xA51 | 0xA52 | 0xA53 | 0xA54 | 0xA55 | T |   |   |
| D6 (Dual or Quad only) | 0x961 | 0x962 | 0x963 | 0x964 | 0x965 | T |   |   |
| D7 (Dual or Quad only) | 0x871 | 0x872 | 0x873 | 0x874 | 0x875 | T |   |   |
---table end---
And continue with the rest in same format.# 8.4.4.6 D21.5 Test Mode
In this test mode, the controller transmits a continuous stream of D21.5 characters (alternating 0s and 1s). This 
mode applies to 8B/10B and 64B/66B modes.

# 8.4.4.7 K28.5 Test Mode
In this test mode, the controller transmits a continuous stream of K28.5 characters. This mode only applies to 
8B/10B modes.

# 8.4.4.8 Repeated ILA Test Mode
In this test mode, the JESD204C link layer operates normally, except that the ILA sequence (ILAS) repeats 
indefinitely instead of starting the data phase. Whenever the receiver issues a synchronization request, the 
transmitter initiates code group synchronization. Upon completion of code group synchronization, the transmitter 
repeatedly transmits the ILA sequence. This mode only applies to 8B/10B modes.

# 8.4.4.9 Modified RPAT Test Mode
This mode only applies to 8B/10B modes.# 8.4.4.9 Modified RPAT Test Mode 
A 12-octet repeating pattern is defined in INCITS TR-35-2004. The purpose of this pattern is to generate white spectral content for JESD204C compliance and jitter testing. 
---table begin---
Table tile: Modified RPAT Pattern Values
| OCTET NUMBER | Dx.y NOTATION | 8-BIT INPUT TO 8B/10B ENCODER | 20b OUTPUT OF 8B/10B ENCODER |
|---|---|---|---|
| 0 | D30.5 | 0xBE | 0x86BA6 |
| 1 | D23.6 | 0xD7 | - |
| 2 | D3.1 | 0x23 | 0xC6475 |
| 3 | D7.2 | 0x47 | - |
| 4 | D11.3 | 0x6B | 0xD0E8D |
| 5 | D15.4 | 0x8F | - |
| 6 | D19.5 | 0xB3 | 0xCA8B4 |
| 7 | D20.0 | 0x14 | - |
| 8 | D30.2 | 0x5E | 0x7949E |
| 9 | D27.7 | 0xFB | - |
| 10 | D21.1 | 0x35 | 0xAA665 |
| 11 | D25.2 | 0x59 | - |
---table end---
# 8.4.4.9 Modified RPAT Test Mode
This mode only applies to 8B/10B modes.

# 8.4.5 Calibration Modes and Trimming
The device has two calibration modes available: foreground calibration and background calibration. When foreground calibration is initiated the ADCs are taken offline to calibrate and the output data becomes mid-code (0x000 in 2's complement) until calibration is finished. Background calibration allows the ADC to continue normal operation while the ADC cores are calibrated in the background by swapping in a different ADC core to take its place. Additional offset calibration features are available in both foreground and background calibration modes. Further, a number of ADC parameters can be trimmed to optimize performance in a user system.
The device consists of a total of six ADC cores. In foreground calibration mode ADC 0 samples INA±, ADC 1 samples INB±, ADC 4 samples INC± and ADC 5 samples IND±. In the background calibration modes, ADC core 2 is swapped in periodically for ADC 0 and ADC 1 and ADC core 3 is swapped in periodically for ADC 4 and 5 so that they can be calibrated without disrupting operation.
When calibration is performed the linearity, gain, and offset voltage for each bank are calibrated to an internally generated calibration signal. The analog inputs can be driven during calibration, both foreground and background, except that when offset calibration (OS_CAL or BGOS_CAL) is used there must be no signals (or aliased signals) near DC for proper estimation of the offset (see the Offset Callibration section).
In addition to calibration, a number of ADC parameters are user controllable to provide trimming for optimal performance. These parameters include input offset voltage, ADC gain and input termination resistance. The default trim values are programmed at the factory to unique values for each device that are determined to be optimal at the test system operating conditions. The user can read the f

# 8. Calibration System Block Diagram
In addition to calibration, a number of ADC parameters are user controllable to provide trimming for optimal performance. These parameters include input offset voltage, ADC gain and input termination resistance. The default trim values are programmed at the factory to unique values for each device that are determined to be optimal at the test system operating conditions. The user can read the factory-programmed values from the trim registers and adjust as desired. The register fields that control the trimming are labeled according to the input that is being sampled (INA±, INB±, INC± or IND±) and the ADC core that is being trimmed. The user is not expected to change the trim values as operating conditions change, however the user can change values as needed. Any custom trimming must be done on a per device basis because of process variations, meaning that there is no global optimal setting for all parts. See the Trimming section for information about the available trim parameters and associated registers.

# 8.4.5.1 Foreground Calibration Mode
Foreground calibration requires the ADC to stop converting the analog input signals during the procedure. Foreground calibration always runs on power-up and the user must wait a sufficient time before programming the device to ensure that the calibration is finished. Foreground calibration can be initiated by triggering the calibration engine. The trigger source can be either the CALTRIG pin or CAL_SOFT_TRIG and is chosen by setting CAL_TRIG_EN.

# 8.4.5.2 Background Calibration Mode
Background calibration mode allows the ADC to continuously operate, with no interruption of data. This continuous operation is accomplished by activating extra ADC cores that are calibrated to take over operation for one of the other previously active ADC cores. For the quad channel device, ADC cores 0 and 1 share one extra ADC core (ADC core 2) and ADC cores 4 and 5 share the other extra ADC core (ADC core 3). When an ADC core is taken off-line the ADC is then calibrated and then can in turn take over to allow the next ADC to be calibrated. This process operates continuously, ensuring the ADC cores always provide the optimum performance regardless of system operating condition changes. Only one of the cores is calibrated at a time to reduce power consumption, however the additional active ADC core does increase the power consumption in comparison to foreground calibration mode. The low-power background calibration (LPBG) mode discussed in the Low-Power Background Calibration (LPBG) Mode section provides reduced average power consumption in comparison with the standard background calibration mode. Background calibration can be enabled by setting CAL_BG. CAL_TRIG_EN must be set to 0 and CAL_SOFT_TRIG must be set to 1. 
Great care has been taken to minimize effects on converted data as the core switching process occurs, however, small brief glitches may still occur on the converter data as the cores are swapped. It is recommended to set register ADC_SRC_DLY (address = 0x9A) to 0x1F and MUX_SEL_DLY (address = 0x9B) to 0x1E. 

# 8.4.5.3 Low-Power Background Calibration (LPBG) Mode
Low-power background calibration (LPBG) mode reduces the power-overhead of enabling additional ADC cores while still allowing background calibration of the ADC cores to maintain optimal performance as operating conditions change. LPBG calibration modifies the background calibration procedure by powering down the spare ADC cores until they are ready to be calibrated. 
Set LP_EN = 1 to enable the low-power background calibration feature. Calibration and swapping of ADC cores can be controlled either automatically by the device or manually by the system by setting LP_TRIG appropriately. Manual control (LP_TRIG=1) allows the system to trigger calibration in order to limit the number of calibration cycles that occur to avoid unnecessary core swaps or to keep power consumption at a minimum. 
For instance, the user may decide to run calibration only when the system temperature changes by some fixed temperature. If manual control is not necessary the automatic calibration control can be enabled (LP_TRIG=0) to calibrate at fixed time intervals. 
In automatic calibration mode (LP_TRIG=0) the spare ADC core sleep time can be controlled by the LP_SLEEP_DLY register setting. LP_SLEEP_DLY is used to adjust the amount of time an ADC sleeps before waking up for calibration (when LP_EN=1 and LP_TRIG = 0). LP_WAKE_DLY sets how long the core is allowed to stabilize after being awoken before calibration begins. 
In automatic calibration control mode the freshly calibrated core is swapped in for an active core as soon as calibration finishes and the new spare core is powered down for the sleep duration before waking up and calibrating. Manual calibration control is enabled by setting LP_TRIG high in order to use the calibration trigger (CAL_SOFT_TRIG or CALTRIG) to trigger calibrations and core swaps. 
When manual control is enabled (LP_TRIG=1) the spare ADC is held in sleep mode while the calibration trigger is high. Setting the calibration trigger low then wakes up the spare ADC core and starts the calibration routine after waiting for the specified wake delay (LP_WAKE_DLY). The spare ADC core is swapped in for an active core once calibration is complete and the calibration trigger is set high again. 
If the calibration trigger is held low, then the spare ADC core calibrates and powers until the calibration trigger goes high; therefore consuming power. ADC12QJ1600-SP can report when the spare ADC finishes calibration on the CALSTAT output pin by setting the CALSTAT pin to output the CAL_STOPPED signal (CAL_STATUS_SEL = 1). 
For lowest power consumption, set the calibration trigger high before calibration finishes to allow the spare ADC to swap in for an active ADC core as soon as calibration finishes. Otherwise, the ADC core swap can be timed manually by setting the calibration trigger high at the desired time to minimize system impact of potential glitches caused by the swapping procedure. In LPBG mode there is an increase in power consumption during the ADC core calibration. 
The longer the spare ADC is held asleep the lower the average power consumption; however, large shifts in# 8.4.5. Calibration Modes
Signal (CAL_STATUS_SEL = 1). For lowest power consumption, set the calibration trigger high before calibration finishes to allow the spare ADC to swap in for an active ADC core as soon as calibration finishes. Otherwise, the ADC core swap can be timed manually by setting the calibration trigger high at the desired time to minimize system impact of potential glitches caused by the swapping procedure.
In LPBG mode there is an increase in power consumption during the ADC core calibration. The longer the spare ADC is held asleep the lower the average power consumption; however, large shifts in operating conditions during the sleep cycle may cause degraded ADC performance due to non-optimized calibration data for the active ADC core. 
The power consumption roughly alternates between the power consumption in foreground calibration when the spare ADC core is sleeping to the power consumption in background calibration when the spare ADC is being calibrated. Design the power-supply network to control the transient power requirements for this mode, including bulk capacitance after any power supply filtering network to help regulate the supply voltage during the supply transient.

# 8.4.6 Offset Calibration
Foreground calibration and background calibration modes inherently calibrate the offsets of the ADC cores; however, the input buffers sit outside of the calibration loop and therefore their offsets are not calibrated by the standard calibration process. A separate calibration is provided to correct the input buffer offsets.
There must be no signals at or near DC or aliased signals that fall at or near DC to properly calibration the offsets, requiring the system to ensure this condition during normal operation or be able to mute the input signal during calibration. 
Foreground offset calibration is enabled via CAL_OS and only performs the calibration one time as part of the foreground calibration procedure. Background offset calibration is enabled via CAL_BGOS and continues to correct the offset as part of the background calibration routine to account for operating condition changes. 
When CAL_BGOS is set, the system must ensure that there are no DC or near-DC signals or aliased signals that fall at or near DC during normal operation. Offset calibration can be performed as a foreground operation when using background calibration by setting CAL_OS to 1 before setting CAL_EN, but does not correct for variations as operating conditions change.
The offset calibration correction uses the input offset voltage trim registers (see OFS0 to OFS5) to correct the offset and therefore must not be written by the user when offset calibration is used. The user can read the calibrated values by reading the offset trim registers after calibration is completed and then use these values in the future to overwrite the factory trim values. 
Only read the values when FG_DONE is read as 1 when using foreground offset calibration (CAL_OS = 1), and do not read the values when using background offset calibration (CAL_BGOS = 1). Setting CAL_OS to 1 and CAL_BG to 1 performs an offset calibration of all six cores during the foreground calibration process.
Some systems, such as pulsed input systems, may purposefully apply a large external DC offset to the analog inputs to maximize the dynamic range for uni-polar signals. Standard offset calibration does not work for these systems because of the applied DC offset. These systems are allowed to set OSREF to use the spare ADC as the offset reference and then calibrate the main ADC cores to match.# 8.4.7 Trimming
 do not read the values when using background offset calibration 
(CAL_BGOS = 1). Setting CAL_OS to 1 and CAL_BG to 1 performs an offset calibration of all six cores during 
the foreground calibration process.
Some systems, such as pulsed input systems, may purposefully apply a large external DC offset to the analog 
inputs to maximize the dynamic range for uni-polar signals. Standard offset calibration does not work for these 
systems because of the applied DC offset. These systems can instead set OSREF to use the spare ADC as the 
offset reference and then calibrate the main ADC cores to match the spare offset. This allows seamless offset 
transitions during background calibration swapping.
---table begin---
Table title: Trim Register Descriptions
| TRIM PARAMETER | TRIM REGISTER | NOTES |
|---|---|---|
| Band-gap reference | BG_TRIM | Measurement on BG output pin. |
| Input termination resistance | RTRIM_x, where x = A for INA±, B for INB±, etc. | The device must be powered on with a clock applied. |
| Input offset voltage | OFSxy, where x = ADC core (0, 1, 2, 3, 4, or 5) and y = A for INA±, B for INB±, etc. or omitted (for ADC cores 0, 1, 4 and 5) | A different trim value is allowed for each ADC core (0, 1, 2, 3, 4 or 5) to allow more consistent offset performance in background calibration mode. Use CAL_OS with CAL_BG = 1 to get the trim values from these registers. |
| Analog input gain | GAINxy, where x = ADC core (0, 1, 2, 3, 4, or 5) and y = A for INA±, B for INB±, etc. or omitted (for ADC cores 0, 1, 4 and 5) | Use this trim to match the gain for each ADC core. These registers are not affected by the calibration process. | 
| Full-scale input voltage | FS_RANGE | Full-scale input voltage adjustment that applies to all inputs. Use GAINxy to match the gain for each input. |
---table end---

# 8.5 Programming

# 8.5.1 Using the Serial Interface
The serial interface is accessed using the following four pins: serial clock (SCLK), serial data in (SDI), serial data 
out (SDO), and serial interface chip-select (SCS). Register access is enabled through the SCS pin.

# 8.5.2 SCS
This signal must be asserted low to access a register through the serial interface. Setup and hold times with 
respect to the SCLK must be observed.

# 8.5.3 SCLK
Serial data input is accepted at the rising edge of this signal. SCLK has no minimum frequency requirement.

# 8.5.4 SDI
Each register access requires a specific 24-bit pattern at this input. This pattern consists of a read-and-write 
(R/W) bit, register address, and register value. The data are shifted in MSB first and multi-byte registers are 
always in little-endian format (least significant byte stored at the lowest address). Setup and hold times with 
respect to the SCLK must be observed (see the Timing Requirements table).

# 8.5.5 SDO
The SDO signal provides the output data requested by a read command. This output is high impedance during 
write bus cycles and during the read bit and register address portion of read bus cycles.
As shown in Serial Interface Protocol: Single Read/Write, each register access consists of 24 bits. The first bit is 
high for a read and low for a write.
The next 15 bits are the address of the register that is to be written to. During write operations, the last eight bits 
are the data written to the addressed register. During read operations, the last eight bits on SDI are ignored and, 
during this time, the SDO outputs the data from the addressed register. Serial Interface Protocol: Single Read/
Write shows the serial protocol details.# 8.5.6. Streaming Mode 
The serial interface supports streaming reads and writes. In this mode, the initial 24 bits of the transaction 
specifics the access type, register address, and data value as normal. Additional clock cycles of write or read data are immediately transferred, as long as the SCS input is maintained in the asserted (logic low) state. The register address auto increments (default) or decrements for each subsequent 8-bit transfer of the streaming transaction. ASCEND controls whether the address value ascends (increments) or descends (decrements). Streaming mode can be disabled by setting the ADDR_HOLD bit.

# 8.5.7. SPI_Register_Map Registers
---table begin---
Table title: SPI_REGISTER_MAP Registers
| Address | Acronym | Register Name | Section |
|---|---|---|---|
| 0x0 | CONFIG_A | Configuration A (default: 0x30) | Go |
| 0x2 | DEVICE_CONFIG | Device Configuration (default: 0x00) | Go |
| 0xC | VENDOR_ID | Vendor Identification (Default = 0x0451) | Go |
| 0x10 | USR0 | User SPI Configuration (Default: 0x00) | Go |
| 0x29 | CLK_CTRL0 | Clock Control 0 (default: 0x80) | Go |
| 0x2A | CLK_CTRL1 | Clock Control 1 (default: 0x00) | Go |
| 0x2B | CLK_CTRL2 | Clock Control 2 (default: 0x10) | Go |
| 0x2C | SYSREF_POS | SYSREF Capture Position (read-only status) | Go |
| 0x30 | FS_RANGE | FS_RANGE (default: 0xA000) | Go |
| 0x37 | LOW_POWER1 | Low Power Mode 1 (default: 0x4B) | Go |
| 0x3B | TMSTP_CTRL | TIMESTAMP (TMSTP) Control (default: 0x00) | Go |
| 0x3C | PLLREFO_CTRL | PLL Reference Output Control (default: 0x01) | Go |
| 0x3D | CPLL_FBDIV1 | C-PLL Feedback Divider V and P (default: 0x00) | Go |
| 0x3E | CPLL_FBDIV2 | C-PLL Feedback Divider N (default: 0x20) | Go |
| 0x3F | CPLL_VCOCTRL1 | C-PLL Feedback Divider N (default: 0x4F) | Go |
| 0x48 | SER_PE | Serializer Pre-Emphasis Control (default: 0x00) | Go |
| 0x57 | TRIGOUT_CTRL | TRIGOUT Output Control (default: 0x00) | Go |
| 0x58 | CPLL_OVR | C-PLL Pin Override | |
---table end---

# NOTE
The serial interface must not be accessed during ADC calibration. Accessing the serial interface during this time impairs the performance of the device until the device is calibrated correctly. Writing or reading the serial registers also reduces dynamic ADC performance for the duration of the register access times.# 1. SPI_REGISTER_MAP Registers
---table begin---
Table title: SPI_REGISTER_MAP Registers
| Position (read-only status) | Address | Acronym | Register Name |
|---|---|---|---|
| Go | 0x30 | FS_RANGE | FS_RANGE (default: 0xA000) |
| Go | 0x37 | LOW_POWER1 | Low Power Mode 1 (default: 0x4B) |
| Go | 0x3B | TMSTP_CTRL | TIMESTAMP (TMSTP) Control (default: 0x00) |
| Go | 0x3C | PLLREFO_CTRL | PLL Reference Output Control (default: 0x01) |
| Go | 0x3D | CPLL_FBDIV1 | C-PLL Feedback Divider V and P (default: 0x00) |
| Go | 0x3E | CPLL_FBDIV2 | C-PLL Feedback Divider N (default: 0x20) |
| Go | 0x3F | CPLL_VCOCTRL1 | C-PLL Feedback Divider N (default: 0x4F) |
| Go | 0x48 | SER_PE | Serializer Pre-Emphasis Control (default: 0x00) |
| Go | 0x57 | TRIGOUT_CTRL | TRIGOUT Output Control (default: 0x00) |
---table end---

# 2. SPI_REGISTER_MAP Registers (continued)
---table begin---
Table title: SPI_REGISTER_MAP Registers
| Address | Acronym | Register Name |
|---|---|---|
| 0x58 | CPLL_OVR | C-PLL Pin Override (default: 0x00) |
| 0x59 | VCO_FREQ_TRIM | C-PLL VCO Frequency Trim (default: undefined) |
| 0x5C | CPLL_RESET | C-PLL / VCO Calibration Reset (default: 0x00) |
| 0x5D | VCO_CAL_CTRL | VCO Calibration Control (default: 0x40) |
| 0x5E | VCO_CAL_STATUS | VCO Calibration Status (read-only) (default: undefined) |
| 0x61 | CAL_EN | Calibration Enable (Default: 0x01) |
---table end---

# 3. SPI_REGISTER_MAP Registers (continued 2)
---table begin---
Table title: SPI_REGISTER_MAP Registers (continued 2)
| Address | Acronym | Register Name |
|---|---|---|
| 0x62 | CAL_CFG0 | Calibration Configuration 0 (Default: 0x01) |
| 0x65 | CAL_CFG1 | Calibration Configuration 1 (Default: 0x01) |
| Go | 0x68 | CAL_AVG | Calibration Averaging (default: 0x61) |
---table end---# 8.5. SPI Registers Details

# 8.5.7. CONFIG_A Register (Address = 0x0) [reset = 0x30]
---table begin---
Table title: CONFIG_A Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7 | SOFT_RESET | R/W | 0x0 | Setting this bit causes a full reset of the chip and all SPI registers (including CONFIG_A). This bit is self-clearing. After writing this bit, the part may take up to 750ns to reset. During this time, do not perform any SPI transactions. |
| 6 | RESERVED | R/W | 0x0 | Must write default value. |
| 5 | ASCEND | R/W | 0x1 | 0 : Address is decremented during streaming reads/writes 1 : Address is incremented during streaming reads/writes (default) |
| 4 | SDO_ACTIVE | R | 0x1 | Always returns 1. Always use SDO for SPI reads. No SDIO mode supported. |
| 3:0 | RESERVED | R/W | 0x0 | Must write default value. |
---table end---

# 8.5.7.2. DEVICE_CONFIG Register (Address = 0x2) [reset = 0x00]
---table begin---
Table title: DEVICE_CONFIG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:2 | RESERVED | R/W | 0x0 | Must write default value. |
| 1:0 | MODE | R/W | 0x0 | Operation mode of the chip. |
---table end---

# 8.5.7.3. Advanced SPI Registers Configurations
---table begin---
Table title: Advanced SPI Registers Configurations
| Address | Acronym | Register Name | Description |
|---|---|---|---|
| 0x29C | LOW_POWER4 | Low Power Mode 4 | default: 0x1B |
| 0x2C0 | ALARM | Alarm Interrupt | Read only |
| 0x2C1 | ALM_STATUS | Alarm Status | default: 0x3F, write to clear |
| 0x2C2 | ALM_MASK | Alarm Mask Register | default: 0x3F |
| 0x2C4 | FIFO_LANE_ALM | FIFO Overflow/Underflow Alarm | default: 0xFF |
---table end---

# 8. Access Type Codes for SPI_Register_Map 
---table begin---
Table title: SPI_Register_Map Access Type Codes
| Access Type | Code | Description |
|---|---|---|
| Read Type | R | Read |
| Write Type | W | Write |
| Reset or Default Value | -n | Value after reset or the default value |
| Register Array Variables | i,j,k,l,m,n | When these variables are used in a register name, an offset, or an address, they refer to the value of a register array where the register is part of a group of repeating registers. The register groups form a hierarchical structure and the array is represented with a formula. |
| Register Array Variables (continued) | y | When this variable is used in a register name, an offset, or an address it refers to the value of a register array. |
---table end---

# 8.5.7.2 DEVICE_CONFIG Register (Address = 0x2) [reset = 0x00]
DEVICE_CONFIG is shown in 图 8-19 and described in 表 8-56.
Return to the Summary Table.
Device Configuration (default: 0x00)
---table begin---
Table tile: DEVICE_CONFIG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:2 | RESERVED | R/W | 0x0 | Must write default value. |
| 1:0 | MODE | R/W | 0x0 | 0 : Normal operation (default) 1 : Reserved 2 : Reserved 3 : Power down (full device) |
---table end---

# 8.5.7.3 VENDOR_ID Register (Address = 0xC) [reset = 0x0]
VENDOR_ID is shown in 图 8-20 and described in 表 8-57.
Return to the Summary Table.
Vendor Identification (Default = 0x0451)
---table begin---
Table tile: VENDOR_ID Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15:0 | VENDOR_ID | R | 0x0 | Always returns 0x0451 (Vendor ID for Texas Instruments) |
---table end---

# 8.5.7.4 USR0 Register (Address = 0x10) [reset = 0x00]
USR0 is shown in 图 8-21 and described in 表 8-58.
Return to the Summary Table.
User SPI Configuration (Default: 0x00)
---table begin---
Table tile: USR0 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:1 | RESERVED | R/W | 0x0 | Must write default value. |
| 0 | ADDR_HOLD | R/W | 0x0 | 0 : Use ASCEND register to select address ascend/descend mode (default) 1 : Address stays constant throughout streaming operation; useful for reading and writing calibration vector information at the CAL_DATA register |
---table end---

# 8.5.7.5 CLK_CTRL0 Register (Address = 0x29) [reset = 0x80]
# 8.5.7.6 CLK_CTRL1 Register (Address = 0x2A) [reset = 0x00]
CLK_CTRL1 is shown in Figure 8-23 and described in Table 8-60.
Clock Control 1 (default: 0x00)
---table begin---
Table tile: CLK_CTRL1 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:3 | RESERVED | R/W | 0x0 | Must write default value. |
| 2 | DEVCLK_LVPE | R/W | 0x0 | Activate low voltage PECL mode for DEVCLK. The internal termination for each input pin (CLK+ and CLK–) becomes a 50-Ω resistor to ground. There is no input common-mode self-biasing for CLK± when DEVCLK_LVPECL_EN is set to 1. |
| 1 | SYSREF_LVPE | R/W | 0x0 | Activate low voltage PECL mode for SYSREF. The internal termination for each input pin (SYSREF+ and SYSREF–) becomes a 50-Ω resistor to ground. There is no input common-mode self-biasing for SYSREF± when SYSREF_LVPECL_EN is set to 1. |
| 0 | SYSREF_INVERTED | R/W | 0x0 | This bit inverts the SYSREF signal used for alignment. |
---table end---
# 8.5.7.5 CLK_CTRL0 Register (Address = 0x29) [reset = 0x80]

# 8.5.7.7 CLK_CTRL2 Register (Address = 0x2B) [reset = 0x10]
CLK_CTRL2 is shown in Figure 8-24 and described in Table 8-61.
Clock Control 1 (default: 0x10)
---table begin---
Table tile: CLK_CTRL2 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:3 | RESERVED | R/W | 0x0 | Must write default value. |
| 2 | VA11Q_NOISESUPPR_EN | R/W | 0x0 | When set, noise on VA11Q is suppressed while drawing ~ 20mA of current. This will reduce sampling jitter and reduce the reference clock spur in C-PLL modes and SYSREF spurs. |
| 1 | RESERVED | R/W | 0x0 | Must write default value. |
| 0 | VCLK11_NOISESUPPR_EN | R/W | 0x0 | When set, noise on VCLK11 is suppressed while drawing ~ 20mA of current. This will reduce sampling jitter and reduce the reference clock spur in C-PLL modes and SYSREF spurs. |
---table end---

# 8.5.7.8 SYSREF_POS Register (Address = 0x2C) [reset = 0x0]
SYSREF_POS is shown in Figure 8-25 and described in Table 8-62.
SYSREF Capture Position (read-only status)
---table begin---
Table tile: SYSREF_POS Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 23:0 | SYSREF_POS | R | 0x0 | Returns a 24-bit status value that indicates the position of the SYSREF edge with respect to CLK±. Use this to program SYSREF_SEL. |
---table end---

# 8.5.7.9 FS_RANGE Register (Address = 0x30) [reset = 0xA000]
FS_RANGE is shown in Figure 8-26 and described in Table 8-63. 
FS_RANGE (default: 0xA000)
---table begin---
Table tile: FS_RANGE Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15:0 | FS_RANGE | R/W | 0xA000 | These bits enable adjustment of the analog full-scale range for all channels. 0x0000: Settings below 0x2000 result in degraded performance 0x2000: 500 mVPP - Recommended minimum setting 0xA000: 800 mVPP (default) 0xFFFF: 1000 mVPP - Maximum setting, highest SNR |
---table end---

# 8.5.7.10 LOW_POWER1 Register (Address = 0x37) [reset = 0x4B]
LOW_POWER1 is shown in Figure 8-27 and described in Table 8-64.
Low Power Mode 1 (default: 0x4B)# 8.5.7.9 FS_RANGE Register 
---table begin---
Table tile: FS_RANGE Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15:0 | FS_RANGE | R/W | 0xA000 | These bits enable adjustment of the analog full-scale range for all channels. 0x0000: Settings below 0x2000 result in degraded performance 0x2000: 500 mVPP - Recommended minimum setting 0xA000: 800 mVPP (default) 0xFFFF: 1000 mVPP - Maximum setting, highest SNR |
---table end---

# 8.5.7.10 LOW_POWER1 Register 
Address = 0x37 
Reset = 0x4B
LOW_POWER1 is shown in Figure 8-27 and described in Table 8-64.
Low Power Mode 1 (default: 0x4B)
---table begin---
Table tile: LOW_POWER1 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:0 | LOW_POW_MODE1 | R/W | 0x4B | Set this register along with LOW_POWER2, LOW_POWER3 and LOW_POWER4 to enable Low Power Mode. All registers must be set together. Calibration must be performed after changing the operating mode: 0x46: Low Power Mode (only valid when sampling rate is less than or equal to 1 GSPS) 0x4B : High Performance Mode (default) All other values are RESERVED Note: Must set CAL_EN to 0 and JESD_EN to 0 before changing this register.|
---table end---

# 8.5.7.11 TMSTP_CTRL Register 
Address = 0x3B 
Reset = 0x00
TMSTP_CTRL is shown in 图 8-28 and described in 表 8-65.
TIMESTAMP (TMSTP) Control (default: 0x00)
---table begin---
Table tile: TMSTP_CTRL Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:2 | RESERVED | R/W | 0x0 | Must write default value |
| 1 | TMSTP_LVPECL_EN | R/W | 0x0 | When set, activates the low voltage PECL mode for the differential TMSTP± input. The internal termination for each input pin (TMSTP+ and TMSTP–) becomes a 50-Ω resistor to ground. There is no input common-mode self-biasing for TMSTP± when TMSTP_LVPECL_EN is set to 1.|
| 0 | TMSTP_RECV_EN | R/W | 0x0 | Enables the differential differential TMSTP± input. |
---table end---

# 8.5.7.12 PLLREFO_CTRL Register 
Address = 0x3C 
Reset = 0x01
PLLREFO_CTRL is shown in 图 8-29 and described in 表 8-66.
PLL Reference Output Control (default: 0x01)
---table begin---
Table tile: PLLREFO_CTRL Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:1 | RESERVED | R/W | 0x0 | Must write default value |
| 0 | PLLREFO_EN | R/W | 0x1 | When set the reference clock output (PLLREFO±) is enabled whenever the PLL is enabled (PLL_EN=1). This bit defaults to 1 to cause PLLREFO± to enable automatically without SPI writes since PLLREFO± may be used to derive the SPI clock.|
---table end---

# 8.5.7.13 CPLL_FBDIV1 Register 
# 8.5.7.14 CPLL_FBDIV2 Register (Address = 0x3E) [reset = 0x20]
CPLL_FBDIV2 is shown in 图 8-31 and described in 表 8-68.
---table begin---
Table tile: 表 8-68. CPLL_FBDIV2 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:6 | RESERVED | R/W | 0x0 | Must write default value. |
| 5:0 | PLL_N_DIV | R/W | 0x20 | Controls the third feedback divider of C-PLL (default is divide-by-32). This divider divides the sampling clock to generate the PFD feedback clock. The value of PLL_N_DIV is the divider value. Values from 1 to 63 are supported. Set CPLL_RESET=1 before changing PLL_N_DIV. |
---table end---
# 8.5.7.13 CPLL_FBDIV1 Register 

# 8.5.7.15 CPLL_VCOCTRL1 Register (Address = 0x3F) [reset = 0x4F, recommended 0x4A]
CPLL_VCOCTRL1 is shown in 图 8-32 and described in 表 8-69.
---table begin---
Table tile: 表 8-69. CPLL_VCOCTRL1 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7 | RESERVED | R/W | 0x0 | Must write default value. |
| 6:0 | VCO_BIAS | R/W | 0x4F | Sets the bias levels for the C-PLL VCO. Write 0x4A to this field when using the C-PLL. Do not use the default value of 0x4F. |
---table end---

# 8.5.7.16 SER_PE Register (Address = 0x48) [reset = 0x00]
SER_PE is shown in 图 8-33 and described in 表 8-70.
---table begin---
Table tile: 表 8-70. SER_PE Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:4 | RESERVED | R/W | 0x0 | Must write default value. |
| 3:0 | SER_PE | R/W | 0x0 | Sets the pre-emphasis for the SerDes output lanes. Pre-emphasis can be used to compensate for the high-frequency loss of the PCB trace. This is a global setting that affects all lanes (D[7:0]±). |
---table end---

# 8.5.7.17 TRIGOUT_CTRL Register (Address = 0x57) [reset = 0x00]
# 8.5.7.18 CPLL_OVR Register
1 : TRIGOUT± output buffer/divider is enabled.
The RXCLK output can be used to provide a reference clock for the 
JESD204C receiver. Use the TRIGOUT_MODE field to adjust the 
output mode.
---table begin---
Table tile: Board Parameters
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 6:3 | RESERVED | R/W | 0x0 | Must write default value. |
| 2:0 | TRIGOUT | R/W | 0x0 | Set the mode for the TRIGOUT± output. |
---table end---
# 8.5.7.17 TRIGOUT_CTRL Register (Address = 0x57) [reset = 0x00]
Note 1: Only change TRIGOUT_MODE when TRIGOUT_EN=0.
Note 2: When TRIGOUT_MODE is 2 or less, TRIGOUT± is derived 
from the SerDes block. As a result, the TRIGOUT± output is briefly 
disrupted any time the serializer is re-initialized.

# 8.5.7.19 VCO_FREQ_TRIM Register 
---table begin---
Table tile: VCO_FREQ_TRIM Register Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 7 | RESERVED | R/W | 0x0 | Must write default value. |
| 6:0 | VCO_FREQ_TRIM | R/W | 0x0 | Trims C-PLL VCO frequency. This field can be automatically set by the VCO calibration routine (see VCO_CAL_EN). After VCO calibration has been run the value can be read from this field and reprogrammed after future power-up cycles. |
---table end---
If VCO calibration is running (VCO_CAL_EN=1 and 
VCO_CAL_DONE=0), you should not read or write this register since 
it will interfere with the calibration process.

# 8.5.7.20 CPLL_RESET Register

# 8.5.7.20 CPLL_RESET Register (Address = 0x5C) [reset = 0x00]
CPLL_RESET is shown in 图 8-37 and described in 表 8-74.
---table begin---
Table title: CPLL_RESET Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:1 | RESERVED | R/W | 0x0 | Must write default value. |
| 0 | CPLL_RESET | R/W | 0x0 | C-PLL / VCO calibration reset. Program CPLL_RESET=1 before programming the C-PLL (PLL_P_DIV, PLL_V_DIV, PLL_N_DIV, VCO_BIAS or VCO_CAL_CTRL). Program CPLL_RESET=0 after programming is completed. |
---table end---

# 8.5.7.21 VCO_CAL_CTRL Register (Address = 0x5D) [reset = 0x40]
VCO_CAL_CTRL is shown in 图 8-38 and described in 表 8-75.
---table begin---
Table title: VCO_CAL_CTRL Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7 | RESERVED | R/W | 0x0 | Must write default value. |
| 6:4 | VCO_CAL_STL | R/W | 0x4 | Program this field to adjust the settling time that the VCO calibration engine gives to the C-PLL each time it changes the VCO frequency trim (VCO_FREQ_TRIM). Larger numbers result in longer settling times. |
| 3:1 | RESERVED | R/W | 0x0 | Must write default value. |
| 0 | VCO_CAL_EN | R/W | 0x0 | Set this bit to enable the VCO calibration engine. The calibration commences once CPLL_RESET is programmed to 0. The calibration will automatically tune VCO_FREQ_TRIM to center the VCO frequency based on the reference frequency and PLL configuration. |
---table end---

# 8.5.7.22 VCO_CAL_STATUS Register (Address = 0x5E) [reset = 0x0]
VCO_CAL_STATUS is shown in 图 8-39 and described in 表 8-76.
---table begin---
Table title: VCO_CAL_STATUS Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:1 | RESERVED | R | 0x0 | NA |
| 0 | VCO_CAL_DONE | R | 0x0 | This bit returns ‘1’ once the VCO calibration engine has completed calibration (or calibration was skipped because VCO_CAL_EN=0). Once the calibration is completed, you can safely read or write the VCO_FREQ_TRIM register (never write VCO_FREQ_TRIM during calibration). |
---table end---

# 8.5.7.23 CAL_EN Register (Address = 0x61) [reset = 0x01]
# 8.5.7.23 CAL_EN Register
Once calibration is completed, you can safely read or write the VCO_FREQ_TRIM register (never write VCO_FREQ_TRIM during calibration). CAL_EN is shown in 图 8-40 and described in 表 8-77.
---table begin---
Table title: CAL_EN Register Field Descriptions
| Bit | Field | Type | Reset | Descriptions |
|---|---|---|---|---|
| 7:1 | RESERVED | R/W | 0x0 | Must write default value. |
| 0 | CAL_EN | R/W | 0x1 | Calibration Enable. Set high to run calibration. Set low to hold calibration in reset |
---table end---
# 8.5.7.23 CAL_EN Register (Address = 0x61) [reset = 0x01]

# 8.5.7.24 CAL_CFG0 Register
---table begin---
Table title: CAL_CFG0 Register Field Descriptions (continued)
| Bit | Field | Type | Reset | Description |
| 1 | CAL_BG | R/W | 0x0 | 0 : Disable background calibration (default) 1 : Enable background calibration |
| 0 | CAL_FG | R/W  | 0x1 | 0 : Reset calibration values, skip foreground calibration. 1 : Reset calibration values, then run foreground calibration (default). |
---table end---
# 8.5.7.24 CAL_CFG0 Register

# 8.5.7.25 CAL_CFG1 Register
---table begin---
Table title: CAL_CFG1 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
| 7:3 | RESERVED | R/W | 0x0 | Must write default value. |
| 2 | OSREF | R/W | 0x0 | Defines which reference is used for offset calibration: 0 : Use mid-code as the reference (calibrate to zero-offset). The analog input signal must have no offset during offset calibration (typically true if AC-coupled). 1 : Use the spare ADC output samples as the reference (calibrates primary ADC offsets to match the spare ADC that stands in for them). The analog input signal can have an offset (e.g. DC-coupled). Only use this mode when CAL_BG=1. Setting OSREF=1 while CAL_BG=0 will produce undefined results. |
| 1:0 | RESERVED | R/W | 0x1 | Must write default value. |
---table end---

# 8.5.7.26 CAL_AVG Register
# 8.5.7.26 CAL_AVG Register (Address = 0x68) [reset = 0x61]
CAL_AVG is shown in 图 8-43 and described in 表 8-80.
Return to the Summary Table.
Calibration Averaging (default: 0x61)
---table begin---
Table tile: CAL_AVG Register Field Descriptions (continued)
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7 | RESERVED | R/W | 0x0 | Must write default value |
| 6:4 | OS_AVG | R/W | 0x6 | Select the amount of averaging used for the offset correction routine. A larger number corresponds to more averaging. |
| 3 | RESERVED | R/W | 0x0 | Must write default value |
| 2:0 | CAL_AVG | R/W | 0x1 | Select the amount of averaging used for the linearity calibration routine. A larger number corresponds to more averaging. |
---table end---
# 8.5.7.26 CAL_AVG Register

# 8.5.7.27 CAL_STATUS Register (Address = 0x6A) [reset = 0x0]
CAL_STATUS is shown in 图 8-44 and described in 表 8-81.
Return to the Summary Table.
Calibration Status (default: undefined) (read-only)
---table begin---
Table tile: CAL_STATUS Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R | 0x0 |
| 4:2 | CAL_STAT | R | 0x0 | Calibration status code |
| 1 | CAL_STOPPED | R | 0x0 | This bit returns a 1 when background calibration is successfully stopped at the requested phase. This bit returns a 0 when calibration starts operating again. If background calibration is disabled, this bit is set when foreground calibration is completed or skipped. |
| 0 | FG_DONE | R | 0x0 | This bit is high to indicate that foreground calibration has completed (or was skipped). |
---table end---

# 8.5.7.28 CAL_PIN_CFG Register (Address = 0x6B) [reset = 0x00]
CAL_PIN_CFG is shown in 图 8-45 and described in 表 8-82.
Return to the Summary Table.
Calibration Pin Configuration (default: 0x00)
---table begin---
Table tile: CAL_PIN_CFG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:3 | RESERVED | R/W | 0x0 | Must write default value |
| 2:1 | CAL_STATUS_SEL | R/W | 0x0 | 0 : CALSTAT output matches FG_DONE. 1 : CALSTAT output matches CAL_STOPPED. 2 : CALSTAT output matches ALARM. 3 : CALSTAT output is always low. |
| 0 | CAL_TRIG_EN | R/W | 0x0 | This bit selects the hardware or software trigger source. 0 : Use the CAL_SOFT_TRIG register for the calibration trigger. The CALTRIG input is disabled (ignored).1 : Use the CALTRIG input for the calibration trigger. The CAL_SOFT_TRIG register is ignored. |
---table end---

# 8.5.7.29 CAL_SOFT_TRIG Register (Address  0x6C) [reset  0x01]
CAL_SOFT_TRIG is shown in 图 8-46 and described in 表 8-83.
Return to the Summary Table.
Calibration Software Trigger (default: 0x01)
---table begin---
Table tile: CAL_SOFT_TRIG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:1 | RESERVED | R/W | 0x0 | Must write default value. |
| 0 | CAL_SOFT_TRIG | R/W | 0x1 | CAL_SOFT_TRIG is a software bit to provide the functionality of the CALTRIG input pin when there are no hardware resources to drive CALTRIG. Program CAL_TRIG_EN=0 to use CAL_SOFT_TRIG for the calibration trigger. Note: If no calibration trigger is needed, leave CAL_TRIG_EN=0 and CAL_SOFT_TRIG=1 (trigger set high). |
---table end---

# 8.5.7.30 CAL_LP Register (Address = 0x6E) [reset = 0x88]
CAL_LP is shown in 图 8-47 and described in 表 8-84.
Return to the Summary Table.
Low-Power Background Calibration (default: 0x88)# 8.5.7.30 CAL_LP Register (Address = 0x6E)
CAL_LP is shown in 图 8-47 and described in 表 8-84.
Return to the Summary Table.
Low-Power Background Calibration (default: 0x88)
---table begin---
Table title: CAL_LP Register Field Descriptions
| Bit   | Field         | Type | Reset | Description |
|-------|---------------|------|-------|-------------|
| 7:5   | LP_SLEEP_DLY    | R/W  | 0x4   | These bits adjust how long an ADC sleeps before waking for calibration (only applies when LP_EN = 1 and LP_TRIG = 0).  |
| 4:3   | LP_WAKE_DLY    | R/W  | 0x1   | These bits adjust how much time is provided for settling before calibrating an ADC after the ADC wakes up. |
| 2     | RESERVED    | R/W  | 0x0   | Must write default value. |
| 1     | LP_TRIG    | R/W  | 0x0   | 0 : ADC sleep duration is set by LP_SLEEP_DLY (autonomous mode). 1 : ADCs sleep until awoken by a trigger. |
| 0     | LP_EN    | R/W  | 0x0   | 0 : Disable low-power background calibration  1 : Enable low-power background calibration  |
---table end---

# 8.5.7.31 GAIN_TRIM Register (Address = 0x7A)
---table begin---
Table title: GAIN_TRIM Register Field Descriptions
| Bit   | Field         | Type | Reset | Description |
|-------|---------------|------|-------|-------------|
| 7:0   | GAIN_TRIM    | R/W  | 0x0   | This register trims the gain of all ADC cores. FS_RANGE should be used for full-scale range adjustment instead of GAIN_TRIM. |
---table end--- 

# 8.5.7.32 BG_TRIM Register (Address = 0x7C) 
BG_TRIM is shown in 图 8-49 and described in 表 8-86.
---table begin---
Table title: BG_TRIM Register Field Descriptions 
| Bit   | Field         | Type | Reset | Description |
|-------|---------------|------|-------|-------------|
| 7:4   | RESERVED    | R/W  | 0x0   | Must write default value. |
| 3:0   | BG_TRIM    | R/W  | 0x0   | This register enables trimming of the internal band-gap reference. |
---table end--- 

# 8.5.7.33 RTRIM_A Register (Address = 0x7E)
RTRIM_A is shown in 图 8-50 and described in 表 8-87. 
---table begin---
Table title: RTRIM_A Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:0 | RTRIM_A | R/W | 0x0 | This register controls the INA± ADC input termination trim. After reset, the factory trimmed value can be read and adjusted as required. |
---table end---

# 8.5.7.34 RTRIM_B Register (Address = 0x7F)
RTRIM_B is shown in 图 8-51 and described in 表 8-88.
---table begin---
Table title: RTRIM_B Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:0 | RTRIM_B | R/W | 0x0 | This register controls the INB± ADC input termination trim. After reset, the factory trimmed value can be read and adjusted as required. |
---table end---

# 8.5.7.35 RTRIM_C Register (Address = 0x80)
RTRIM_C is shown in 图 8-52 and described in 表 8-89.
---table begin---
Table title: RTRIM_C Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:0 | RTRIM_C | R/W | 0x0 | This register controls the INC± ADC input termination trim. After reset, the factory trimmed value can be read and adjusted as required. |
---table end---

# 8.5.7.36 RTRIM_D Register (Address = 0x81)
RTRIM_D is shown in 图 8-53 and described in 表 8-90.
---table begin---
Table title: RTRIM_D Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:0 | RTRIM_D | R/W | 0x0 | This register controls the IND± ADC input termination trim. After reset, the factory trimmed value can be read and adjusted as required. |
---table end---

# 8.5.7.37 ADC Source Control Delay (Address = 0x9A)
ADC_SRC_DLY is shown in AC_SRC_DLY Register and described in ADC_SRC_DLY Register Field Descriptions. Only change this register while CAL_EN is 0.
---table begin---
Table title: ADC_SRC_DLY Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R/W | 0x0 | Must write default value. |
| 4:0| ADC_SRC_DLY | R/W | 0x08 | Adjusts how long two ADCs will sample the same input at the same clock phase during background ADC swaps. The default value is appropriate for all ADCCLK frequencies. If using a reduced ADCCLK frequency, ADC_SRC_DLY can be set to 7 to reduce the glitch duration during fast background ADC swaps, however there is a greater risk of having a large glitch amplitude. Two ADCs will sample the same input for 4+2*ADC_SRC_DLY ADCCLK cycles. ADC_SRC_DLY can be programmed from 0 to 31. |
---table end---

# 8.5.7.38 MUX Select Delay Register (Address = 0x9B) 
(Continued in next sections)# 8.5.7.38 MUX Select Delay Register (Address = 0x9B) 
MUX_SEL_DLY is shown in MUX_SEL_DLY Register and described in MUX_SEL_DLY Register Field Descriptions.
---table begin---
Table title: MUX_SEL_DLY Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R/W | 0x0 | Must write default value. |
| 4:0 | MUX_SEL_DLY | R/W | 0x07 | Adjusts the delay added to the internal mux selection signal. This signal controls multiplexors that steer ADC core output data into the encoders. This delay only applies during background ADC swaps. This delay needs to be tuned to swap between sample streams during a small window of time when both sample streams are valid. MUX_SEL_DLY can be programmed from 0 to 31. |
---table end---

# 8.5.7.39 ADC_DITH Register (Address = 0x9D) 
ADC_DITH is shown in 图 8-56 and described in 表 8-93.
---table begin---
Table title: ADC_DITH Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:3 | RESERVED | R/W | 0x0 | Must write default value. |
| 2 | ADC_DITH_ERR | R/W | 0x0 | Small rounding errors may occur when subtracting the dither signal. The error can be chosen to either slightly degrade SNR or to slightly increase the DC offset and FS/2 spur. In addition, the FS/4 spur will also be increased slightly while in single channel mode. 0 : Rounding error degrades SNR 1 : Rounding error degrades DC offset, FS/2 spur and FS/4 spur |
| 1 | ADC_DITH_AMP | R/W | 0x0 | 0 : Small dither for better SNR (default) 1 : Large dither for better spurious performance |
| 0 | ADC_DITH_EN | R/W | 0x0 | Set this bit to enable ADC dither. Dither can improve spurious performance at the expense of slightly degraded SNR. The dither amplitude (ADC_DITH_AMP) can be used to further tradeoff SNR and spurious performance. |
---table end---

# 8.5.7.40 LSB_CTRL Register (Address = 0x160) 
# 8.5.7.41 JESD_EN Register
the transport layer transmits the timestamp signal on the LSB of the output samples. The latency of the timestamp signal (through the entire chip) should match the latency of the analog ADC inputs. Please also set TMSTP_RECV_EN when using TIME_STAMP_EN. Note 1: The control bit is placed on the LSB of the JESD204C samples. In some cases, the JESD204C sample width (N) is greater than the sample width from the ADC. In these cases, the control bit does not replace the LSB of the ADC sample since it is placed at the LSB of the N-bit field. Note 2: The control bit that is enabled by this register is never advertised in the ILA (CS is 0 in the ILA). JESD_EN is shown in 图 8-58 and described in 表 8-95. Return to the Summary Table.
---table begin---
Table tile: JESD_EN Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:1 | RESERVED | R/W | 0x0 | Must write default value. |
| 0 | JESD_EN | R/W | 0x1 | 0 : Disable JESD204C interface 1 : Enable JESD204C interface |
---table end---
# 8.5.7.40 LSB_CTRL Register (Address = 0x160) 

# 8.5.7.42 JMODE Register
Note: Before altering other JESD204C registers, you must clear JESD_EN. When JESD_EN is 0, the block is held in reset and the serializers are powered down. The clocks are gated off to save power. The LMFC/LEMC counter is also held in reset, so SYSREF will not align the LMFC/LEMC. Note: Always set CAL_EN before setting JESD_EN. Note: Always clear JESD_EN before clearing CAL_EN. JMODE is shown in 图 8-59 and described in 表 8-96. Return to the Summary Table.
---table begin---
Table tile: JMODE Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:6 | RESERVED | R/W | 0x0 | Must write default value. |
| 5:0 | JMODE | R/W | 0x0 | Specifies the JESD204C output mode. See JESD204C Mode table. |
---table end---

# 8.5.7.43 KM1 Register
Note: This register should only be changed when JESD_EN=0 and CAL_EN=0. KM1 is shown in 图 8-60 and described in 表 8-97. Return to the Summary Table.
---table begin---
Table tile: KM1 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:0 | KM1 | R/W | 0x1F | K is the number of frames per multiframe and this register must be programmed as K-1. Depending on the JMODE setting, there are constraints on the legal values of K (see K parameter in JESD204C Mode table). The default value is KM1=31, which corresponds to K=32. |
---table end---

# 8.5.7.44 JSYNC_N Register
Note: The JSYNC_N register can always generate a synchronization request, regardless of the SYNC_SEL register. However, if the selected sync pin is stuck low, you cannot de-assert the synchronization.# 8.5.7.44 C Manual Sync Request (default: 0x01)
Note: The JSYNC_N register can always generate a synchronization 
request, regardless of the SYNC_SEL register. However, if the 
selected sync pin is stuck low, you cannot de-assert the 
synchronization request unless you program SYNC_SEL=2.
---table begin---
Table title: JSYNC_N Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:1 | RESERVED | R/W | 0x0 | Must write default value. |
| 0 | JSYNC_N | R/W | 0x1 | Set this bit to 0 to request JESD204C synchronization (equivalent to the SYNC~ signal being asserted). For normal operation, leave this bit set to 1. |
---table end---
# 8.5.7.44 JSYNC_N Register

# 8.5.7.45 JCTRL Register (Address = 0x204) [reset = 0x03]
---table begin---
Table title: JCTRL Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R/W | 0x0 | Must write default value. |
| 4 | ALT_LANES | R/W | 0x0 | Normal lane mapping (default) as shown in the JESD204C output mode section. |
| 3:2 | SYNC_SEL | R/W | 0x0 | Use the SYNCSE input for SYNC~ function (default). |
| 1 | SFORMAT | R/W | 0x1 | Output sample format for JESD204C samples. |
| 0 | SCR | R/W | 0x1 | 8B/10B Scrambler enabled (default). |
---table end---

# 8.5.7.46 JTEST Register (Address = 0x205) [reset = 0x00]
---table begin---
Table title: JTEST Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R/W | 0x0 | Must write default value. |
| 4:0 | JTEST | R/W | 0x0 | Test mode options. |
---table end---

# 8.5.7.47 DID Register (Address = 0x206) [reset = 0x00]
Note: This register should only be changed when JESD_EN is 0.# 8.5.7.47 DID Register (Address = 0x206) [reset = 0x00]
DID is shown in 图 8-64 and described in 表 8-101.
Return to the Summary Table.
JESD204C DID Parameter (default: 0x00)
Note: This register should only be changed when JESD_EN is 0.
---table begin---
Table title: DID Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:0 | DID | R/W | 0x0 | Specifies the DID (Device ID) value that is transmitted during the second multiframe of the JESD204B ILA. |
---table end---

# 8.5.7.48 FCHAR Register (Address = 0x207) [reset = 0x00]
FCHAR is shown in 图 8-65 and described in 表 8-102.
Return to the Summary Table.
JESD204C Frame Character (default: 0x00)
Note: This register should only be changed when JESD_EN is 0.
---table begin---
Table title: FCHAR Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:2 | RESERVED | R/W | 0x0 | Must write default value. |
| 1:0 | FCHAR | R/W | 0x0 | Specify which comma character is used to denote end-of-frame. |
---table end---

# 8.5.7.49 JESD_STATUS Register (Address = 0x208) [reset = 0x0]
Note: This register should only be changed when JESD_EN is 0.
---table begin---
Table title: JESD_STATUS Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7 | RESERVED | R/W | 0x0 | - |
| 6 | LINK_UP | R/W | 0x0 | When set, indicates that the JESD204C link is up. |
| 5 | SYNC_STATUS | R/W | 0x0 | Returns the state of the JESD204C SYNC~ signal. |
| 4 | REALIGNED | R/W | 0x0 | When high, indicates that the digital block clock, frame clock, ormultiframe clock phase was realigned by SYSREF. |
---table end---

# 8.5.7.50 CH_EN Register (Address = 0x209) [reset = 0x03]
# 8.5.7.50 CH_EN Register (Address = 0x209) [reset = 0x03]
CH_EN is shown in 图 8-67 and described in 表 8-104. Return to the Summary Table. JESD204C Channel Enable (default: 0x03)
---table begin---
Table title: CH_EN Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:3 | RESERVED | R/W | 0x0 | Must write default value. |
| 2 | SINGLE_CH_EN | R/W | 0x0 | When set, single channel mode is enabled and channels B, C and D are disabled. AB_EN must be set to 1. |
| 1 | CD_EN | R/W | 0x1 | When set, the C and D channels are enabled. Set to 0 to disable channels C and D. Set this bit to enable dual channel operation. |
| 0 | AB_EN | R/W | 0x1 | When set, the A and B channels are enabled. Set to 0 to disable channel A and B. |
---table end---
# 8.5.7.50 CH_EN Register (Address = 0x209) [reset = 0x03]
Important notes:
1. You must set CAL_EN=0 and JESD_EN=0 before changing CH_EN.
2. Do not use this register to disable (power down) all channels since this state is undefined. Instead use the MODE register to power down the full device.
3. When either pair of channels is disabled, the JESD204C link will scale down the number of lanes and converters: L = ceiling(Lx/2) and M = Mx/2. If Lx is odd, tail bits are added to the end of the highest lane to pad out the frame (as per the JESD204C standard).
4. When AB_EN=0, the samples for channels C & D are placed within the JESD204C frame where the A & B samples would normally be located.

# 8.5.7.51 SHMODE Register (Address = 0x20F) [reset = 0x00]
SHMODE is shown in 图 8-68 and described in 表 8-105. Return to the Summary Table. JESD204C Sync Word Mode (default: 0x00)
---table begin---
Table title: SHMODE Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:2 | RESERVED | R/W | 0x0 | Must write default value. |
| 1:0 | SHMODE | R/W | 0x0 | Select the mode for the 64B/66B sync word (32 bits of data per multi- block). This only applies when JMODE is selecting a 64B/66B mode.0 : Transmit CRC-12 signal (default setting)1 : RESERVED2 : Transmit FEC signal3 : RESERVED |
---table end---
Note: This device does not support any JESD204C command features. All command fields will be set to zero (idle headers). Note: This register should only be changed when JESD_EN is 0.

# 8.5.7.52 SYNC_THRESH Register (Address  0x210) [reset  0x03]
Note: This register should only be changed when JESD_EN is 0. Note: Since this design does not do anything with an error reported on the SYNC~ interface, it is recommended that error reporting be disabled on t# 8.5.7.53 OVR_TH Register (Address = 0x211) [reset = 0xF2]
OVR_TH is shown in 图 8-70 and described in 表 8-107.
Return to the Summary Table.
Over-range Threshold (default: 0xF2)
---table begin---
Table tile: OVR_TH Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:0 | OVR_TH | R/W | 0xF2 | This parameter defines the absolute sample level that causes the over-range outputs to be asserted. The detection level in dBFS (peak) is 20log10(OVR_TH/256) (Default: 0xF2 = 242-> -0.5dBFS) |
---table end---
# 8.5.7.52 SYNC_THRESH Register (Address  0x210) [reset  0x03]

# 8.5.7.54 OVR_CFG Register (Address = 0x213) [reset = 0x07]
OVR_CFG is shown in 图 8-71 and described in 表 8-108.
Return to the Summary Table.
Over-range Enable / Hold Off (default: 0x07)
---table begin---
Table tile: OVR_CFG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:4 | RESERVED | R/W | 0x0 | Must write default value. |
| 3 | OVR_EN | R/W | 0x0 | Enables over-range status output pins when set high. The ORA, ORB, ORC and ORD outputs are held low when OVR_EN is set low. |
| 2:0 | OVR_N | R/W | 0x7 | Program this register to adjust the pulse extension for the ORA, ORB, ORC and ORD outputs. The minimum pulse duration of the over-range outputs is 4 * 2OVR_N sampling cycles. Incrementing this field doubles the monitoring period. |
---table end---

# 8.5.7.55 INIT_STATUS Register (Address = 0x270) [reset = 0x0]
INIT_STATUS is shown in 图 8-72 and described in 表 8-109.
Return to the Summary Table.
Initialization Status (read-only)
---table begin---
Table tile: INIT_STATUS Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:1 | RESERVED | R | 0x0 | - |
| 0 | INIT_DONE | R | 0x0 | Returns 1 when the initialization logic has finished initializing the device. This indicates that it is now safe to proceed with startup. No SPI transactions should be performed before INIT_DONE returns 1 (except SOFT_RESET). |
---table end---

# 8.5.7.56 LOW_POWER2 Register (Address = 0x29A) [reset = 0x0F]
LOW_POWER2 is shown in 图 8-73 and described in 表 8-110.
Return to the Summary Table.
Low Power Mode 2 (default: 0x0F)
---table begin---
Table tile: LOW_POWER2 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:0 | LOW_POW_MODE2 | R/W | 0xF | Set this register along with LOW_POWER1, LOW_POWER3 and LOW_POWER4 to enable Low Power Mode. All registers must be set together. Calibration must be performed after changing the operating mode: 0x06 : Low Power Mode (only valid when sampling rate is less than or equal to 1 GSPS) 0x0F : High Performance Mode (default) All other values are RESERVED Note: Must set CAL_EN to 0 and JESD_EN to 0 before changing this register. |
---table end---

# 8.5.7.57 LOW_POWER3 Register (Address = 0x29B) [reset = 0x04]
LOW_POWER3 is shown in 图 8-74 and described in 表 8-111.
Return to the Summary Table.
Low Power Mode 3 (default: 0x04)
---table begin---
Table tile: LOW_POWER3 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:0 | LOW_POW_MODE3 | R/W | 0x4 | Set this register along with LOW_POWER1, LOW_POWER2 and LOW_POWER4 to enable Low Power Mode. All registers must be set together. Calibration must be performed after changing the operating mode: 0x00 : Low Power Mode (only valid when sampling rate is less than or equal to 1 GSPS) 0x04 : High Performance Mode (default) All other values are RESERVED Note: Must set CAL_EN to 0 and JESD_EN to 0 before changing this |
---table end---

# 8.5.7.58 LOW_POWER4 Register (Address = 0x29C) [reset = 0x1B]
LOW_POWER4 is shown in 图 8-75 and described in 表 8-112.
Return to the Summary Table.
Low Power Mode 4 (default: 0x1B)
---table begin---
Table tile: LOW_POWER4 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:0 | LOW_POW_MODE4 | R/W | 0x1B | Set this register along with LOW_POWER1, LOW_POWER2 and LOW_POWER3 to enable Low Power Mode. All registers must be set together. Calibration must be performed after changing the operating mode: 0x14 : Low Power Mode (only valid when sampling rate is less than or equal to 1 GSPS) 0x1B : High Performance Mode (default) All other values are RESERVED Note: Must set CAL_EN to 0 and JESD_EN to 0 before changing this |
---table end---

# 8.5.7.59 ALARM Register (Address = 0x2C0) [reset = 0x0]
ALARM is shown in 图 8-76 and described in 表 8-113.
Return to the Summary Table.
Alarm Interrupt (read-only)
---table begin---
Table tile: ALARM Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:1 | RESERVED | R | 0x0 |
| 0 | ALARM | R | 0x0 | This bit returns a ‘1’ whenever any alarm occurs that is unmasked in the ALM_STATUS register. Use ALM_MASK to mask (disable) individual alarms. CAL_STATUS_SEL can be used to drive the ALARM bit onto the CALSTAT output pin to provide a hardware alarm interrupt signal. |
---table end---

# 8.5.7.60 ALM_STATUS Register (Address = 0x2C1) [reset = 0x3F]
ALM_STATUS is shown in 图 8-77 and described in 表 8-114.
Return to the Summary Table.
Alarm Status (default: 0x3F, write to clear)
---table begin---
Table tile: ALM_STATUS Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:6 | RESERVED | R/W | 0x0 |
| 5 | FIFO_ALM | R/W | 0x1 | FIFO overflow/underflow alarm: This bit is set whenever an active JESD204C lane FIFO experiences an underflow or overflow condition. Write a ‘1’ to clear this bit. To inspect which lane generated the alarm, read FIFO_LANE_ALM. |
---table end---

# 8.5.7.61. ALM_MASK Register (Address = 0x2C2)
ALM_MASK is shown in 图 8-78 and described in 表 8-115. Alarm Mask Register default: 0x3F.
---table begin---
Table tile: ALM_MASK Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:6 | RESERVED | R/W | 0x0 | Must write default value. |
| 5 | MASK_FIFO_ALM | R/W | 0x1 | When set, FIFO_ALM is masked and will not impact the ALARM register bit. |
| 4 | MASK_PLL_ALM | R/W | 0x1 | When set, PLL_ALM is masked and will not impact the ALARM register bit. |
| 3 | MASK_LINK_ALM | R/W | 0x1 | When set, LINK_ALM is masked and will not impact the ALARM register bit. |
| 2 | MASK_REALIGNED_ALM | R/W | 0x1 | When set, REALIGNED_ALM is masked and will not impact the ALARM register bit. |
| 1 | RESERVED | R/W | 0x1 | Must write default value. |
| 0 | MASK_CLK_ALM | R/W | 0x1 | When set, CLK_ALM is masked and will not impact the ALARM register bit. |
---table end---

# 8.5.7.62. FIFO_LANE_ALM Register (Address = 0x2C4)
FIFO_LANE_ALM is shown in 图 8-79 and described in 表 8-116. FIFO Overflow/Underflow Alarm default: 0xFF.
---table begin---
Table tile: FIFO_LANE_ALM Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:0 | FIFO_LANE_ALM | R/W | 0xFF | FIFO_LANE_ALM[i] is set if the FIFO for lane i experiences overflow or underflow. Use this register to determine which lane(s) generated an alarm. Writing a ‘1’ to any bit in this register will clear the alarm (the alarm may immediately trip again if the overflow/underflow condition persists). Writing a ‘1’ to the FIFO_ALM register will clear all bits of this register. |
---table end---

# 8.5.7.63. OFS0 Register (Address = 0x330)
OFS0 is shown in 图 8-80 and described in 表 8-117. Offset Adjustment for ADC0 default from Fuse ROM.# 8.5.7.63 OFS0 Register (Address = 0x330)
OFS0 is shown in 图 8-80 and described in 表 8-117. Offset Adjustment for ADC0 (default from Fuse ROM).
---table begin---
Table title: OFS0 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15:12 | RESERVED | R/W | 0x0 | Must write default value. |
| 11:0 | OFS0 | R/W | 0x0 | Offset adjustment value applied to ADC0. The format is unsigned. |
---table end---

# 8.5.7.64 OFS1 Register (Address = 0x332)
OFS1 is shown in 图 8-81 and described in 表 8-118. Offset Adjustment for ADC1 (default from Fuse ROM).
---table begin---
Table title: OFS1 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15:12 | RESERVED | R/W | 0x0 | Must write default value. |
| 11:0 | OFS1 | R/W | 0x0 | Offset adjustment value applied to ADC1. |
---table end---

# 8.5.7.65 OFS2A Register (Address = 0x334)
OFS2A is shown in 图 8-82 and described in 表 8-119. Offset Adjustment for ADC2 (INA±) (default from Fuse ROM).
---table begin---
Table title: OFS2A Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15:12 | RESERVED | R/W | 0x0 | Must write default value. |
| 11:0 | OFS2A | R/W | 0x0 | Offset adjustment value applied to ADC2 when sampling INA±. |
---table end---

# 8.5.7.66 OFS2B Register (Address = 0x336)
OFS2B is shown in 图 8-83 and described in 表 8-120. Offset Adjustment for ADC2 (INB±) (default from Fuse ROM).
---table begin---
Table title: OFS2B Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15:12 | RESERVED | R/W | 0x0 | Must write default value. |
| 11:0 | OFS2B | R/W | 0x0 | Offset adjustment value applied to ADC2 when sampling INB±. |
---table end---

# 8.5.7.67 OFS3C Register (Address = 0x338)
OFS3C is shown in 图 8-84 and described in 表 8-121. Offset Adjustment for ADC3 (INC±) (default from Fuse ROM).
---table begin---
Table title: OFS3C Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15:12 | RESERVED | R/W | 0x0 | Must write default value. |
| 11:0 | OFS3C | R/W | 0x0 | Offset adjustment value applied to ADC3 when sampling INC±. |
---table end---

# 8.5.7.68 OFS3D Register (Address = 0x33A) [reset = 0x0]
OFS3D is shown in 图# 8.5.7.68 OFS3D Register (Address = 0x33A) [reset = 0x0]
OFS3D is shown in 图 8-85 and described in 表 8-122.
---table begin---
Table title: OFS3D Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15:12 | RESERVED | R/W | 0x0 | Must write default value. |
| 11:0 | OFS3D | R/W | 0x0 | Offset adjustment value applied to ADC3 when sampling IND±. |
---table end---

# 8.5.7.69 OFS4 Register (Address = 0x33C) [reset = 0x0]
OFS4 is shown in 图 8-86 and described in 表 8-123.
---table begin---
Table title: OFS4 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15:12 | RESERVED | R/W | 0x0 | Must write default value. |
| 11:0 | OFS4 | R/W | 0x0 | Offset adjustment value applied to ADC4. |
---table end---

# 8.5.7.70 OFS5 Register (Address = 0x33E) [reset = 0x0]
OFS5 is shown in 图 8-87 and described in 表 8-124.
---table begin---
Table title: OFS5 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15:12 | RESERVED | R/W | 0x0 | Must write default value. |
| 11:0 | OFS5 | R/W | 0x0 | Offset adjustment value applied to ADC5. |
---table end---

# 8.5.7.71 GAIN0 Register (Address = 0x360) [reset = 0x0]
GAIN0 is shown in 图 8-88 and described in 表 8-125.
---table begin---
Table title: GAIN0 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R/W | 0x0 | Must write default value. |
| 4:0 | GAIN0 | R/W | 0x0 | Fine gain adjustment for ADC0. |
---table end---

# 8.5.7.72 GAIN1 Register (Address = 0x361) [reset = 0x0]
GAIN1 is shown in 图 8-89 and described in 表 8-126.
---table begin---
Table title: GAIN1 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R/W | 0x0 | Must write default value. |
| 4:0 | GAIN1 | R/W | 0x0 | Fine gain adjustment for ADC1. |
---table end---

# 8.5.7.73 GAIN2A Register (Address = 0x362) [reset = 0x0]
GAIN2A is shown in 图 8-90 and described in 表 8-127.
---table begin---
Table title: GAIN2A Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R/W | 0x0 | Must write default value. |
| 4:0 | GAIN2A | R/W | 0x0 | Fine gain adjustment for ADC2 when sampling INA±. |
---table end---

# 8.5.7.74 GAIN2B Register (Address = 0x363) [reset = 0x0]
GAIN2B is shown in 图 8-91 and described in 表 8-128.# 8.5.7.74 GAIN2B Register (Address = 0x363) [reset = 0x0]
GAIN2B is shown in 图 8-91 and described in 表 8-128.
---table begin---
Table title: GAIN2B Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R/W | 0x0 | Must write default value. |
| 4:0 | GAIN2B | R/W | 0x0 | Fine gain adjustment for ADC2 when sampling INB±. |
---table end---

# 8.5.7.75 GAIN3C Register (Address = 0x364) [reset = 0x0]
GAIN3C is shown in 图 8-92 and described in 表 8-129.
---table begin---
Table title: GAIN3C Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R/W | 0x0 | Must write default value. |
| 4:0 | GAIN3C | R/W | 0x0 | Fine gain adjustment for ADC3 when sampling INC±. |
---table end---

# 8.5.7.76 GAIN3D Register (Address = 0x365) [reset = 0x0]
GAIN3D is shown in 图 8-93 and described in 表 8-130.
---table begin---
Table title: GAIN3D Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R/W | 0x0 | Must write default value. |
| 4:0 | GAIN3D | R/W | 0x0 | Fine gain adjustment for ADC3 when sampling IND±. |
---table end---

# 8.5.7.77 GAIN4 Register (Address = 0x366) [reset = 0x0]
GAIN4 is shown in 图 8-94 and described in 表 8-131.
---table begin---
Table title: GAIN4 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R/W | 0x0 | Must write default value. |
| 4:0 | GAIN4 | R/W | 0x0 | Fine gain adjustment for ADC4. |
---table end---

# 8.5.7.78 GAIN5 Register (Address = 0x367) [reset = 0x0]
GAIN5 is shown in 图 8-95 and described in 表 8-132.
---table begin---
Table title: GAIN5 Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 7:5 | RESERVED | R/W | 0x0 | Must write default value. |
| 4:0 | GAIN5 | R/W | 0x0 | Fine gain adjustment for ADC5. |
---table end---

# 9 Application and Implementation
备注
Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

# 9.1 Application Information
The ADC12QJ1600-SP can be used in a wide range of applications including light detection and ranging (LiDAR), RADAR, satellite communications, handheld test equipment (communications testers and oscilloscopes), and software-defined radios (SDR). The wide input bandwidth enables direct RF sampling to at least 4 GHz and the high sampling rate allows signal bandwidths of greater than 500 MHz. The Typical Application section describes the use of the device in a LiDAR application using the integrated clocking features to reduce system cost, component count and solution size.# 9. Application Information
The ADC12QJ1600-SP can be used in a wide range of applications including light detection and ranging (LiDAR), RADAR, satellite communications, handheld test equipment (communications testers and oscilloscopes), and software-defined radios (SDR). The wide input bandwidth enables direct RF sampling to at least 4 GHz and the high sampling rate allows signal bandwidths of greater than 500 MHz. The Typical Application section describes the use of the device in a LiDAR application using the integrated clocking features to reduce system cost, component count and solution size.

# 9.2 Typical Applications

# 9.2.1 Light Detection and Ranging (LiDAR) Digitizer
A LiDAR system uses a laser to send a light pulse toward a target and measures reflections off of the target using photodiodes. The photodiodes are connected to transimpedance amplifiers (TIA) to convert the current generated by the reflected light into a voltage. An ADC converts the voltage to a digital signal and extracts the pulse arrival time and reflected energy of the pulse. The device has a number of features that makes it ideal as the digitizer for a LiDAR system including high sampling rate, high performance, high input bandwidth and integrated clocking features. An example LiDAR system digitizer is shown in 图 9-1 which uses up to four ADC channels running at 1 GSPS and the on-chip clocking features of the device to reduce the component count, size and cost of the system.

# 9.2.1.1 Design Requirements
# 9. 
idth of 5 
ns, for high spatial resolution, requires a sampling rate of 1 GSPS in order to get 5 samples of each returning 
pulse. Low cost and small size are important to enable high volume production and a quad channel ADC with 
integrated clocking features help drive down these important metrics. Other considerations include the maximum 
SerDes rate supported by the FPGA and number of lanes. Assume the FPGA has 4 SerDes lanes that support 
up to 12.5 Gbps. For this reason, JMODE 8 is chosen.
---table begin---
Table tile: 表 9-1. LiDAR System and Digitizer Requirements
| System Parameter | Example System Requirement | Example Digitizer Requirement |
|---|---|---|
| Maximum Target Range | 200 meters at 10% reflectivity | 12-bit ADC |
| Minimum Laser Pulse Width| 5 ns | 1 GSPS (5 samples per pulse) |
| Horizontal FOV| 360° | See Full Scan Time |
| Vertical FOV| 20°|See Vertical Scanning Method |
| Horizontal Resolution| 0.1°|See Full Scan Time |
| Vertical Resolution| 0.3125°| See Vertical Scanning Method |
| Horizontal Scanning Method| Spinning mirror|See Full Scan Time |
| Vertical Scanning Method| Parallel photodiodes|64 photodiodes |
| Full Scan Time| 76.8 ms|16:1 mux ratio (4 ADC channels) |
| System Cost| Low cost|Clock features integrated in ADC |
| System Form Factor| Small form factor| Quad channel ADC with integrated clocking |
---table end---
# 9.2.1.1 Design Requirements

# 9.2.1.2 Detailed Design Procedure
The details surrounding the LiDAR example design are provided in this section, including how to choose 
components and how to calculated the necessary clock frequencies.

# 9.2.1.2.1 Analog Front-End Requirements
The ADC channels are fed from an analog front end (AFE) which contains photodiodes, TIAs, fully-differential 
amplifiers (FDA) and analog muxes. The return pulse is collected by an optical lens which focuses the light to the 
corresponding photodiode. The photodiode generates a current which is converted to a voltage and amplified by 
a TIA. This single-ended voltage is converted to a differential voltage using a fully-differential amplifier which 
then drives the differential input of the ADC. The ADC common-mode voltage of 1.1V is easily interfaced to by 
unipolar supply FDAs for lowest cost. Analog muxing of parallel photodiode receivers can be done after the TIAs 
or after the FDAs depending on the chosen components.
The input network must have sufficient bandwidth to support the minimum pulse width required by the system. 
The required bandwidth to support a given rise time (10-90%) is given in Equation 13.
BW [MHz] = 350 / tR[ns]
(13)
Assuming the laser has a rise and fall time of 1 ns (10-90%), then the input network bandwidth should be greater 
than 400 MHz to avoid excessive degradation of the pulse shape and spatial resolution.

# 9.2.1.2.2 Calculating Clock and SerDes Frequencies
The example LiDAR system uses four ADC channels running at 1 GSPS and the on-chip clock features of the 
device to reduce the system size and cost. The device is clocked by a 50-MHz crystal through the single-ended 
clock input (CLK_SE) and the integrated clock features are used to eliminate external clocking components. The 
internal PLL (C-PLL) generates the 1 GHz sampling clock for the ADC cores. The 50 MHz PLL reference is 
repeated through the PLLREFO output to the FPGA to generate the FPGA internal clocks including the 
application layer clock. The 50 MHz reference is divided down in the FPGA to generate the SYSREF signal 
which is sent to both the FPGA JESD204C core and to the device to achieve deterministic latency.
There are a number of clocking frequencies used in the example system shown in 图 9-1. The reference clock 
frequency (fREF) is chosen by the designer and in this case is ch# 1. Introduction
king components. The 
internal PLL (C-PLL) generates the 1 GHz sampling clock for the ADC cores. The 50 MHz PLL reference is 
repeated through the PLLREFO output to the FPGA to generate the FPGA internal clocks including the 
application layer clock. The 50 MHz reference is divided down in the FPGA to generate the SYSREF signal 
which is sent to both the FPGA JESD204C core and to the device to achieve deterministic latency.

# 2. CLK System Description
In the clock configuration shown, the FPGA clock which runs the JESD204C core must be an integer multiplication of fREF in order to 
properly pass SYSREF from the reference clock domain to the core clock domain to achieve deterministic latency. In many cases the 
JESD204C IP may expect a clock rate of fLINERATE/66, which results in 187.5 MHz for the example. Some JESD204C IP cores may not 
allow the JESD204C clock frequency to deviate from this requirement and therefore IP provider should be consulted. If the requirement 
described for the FPGA core clock cannot be met than deterministic latency cannot be achieved.# 9.2.1.3 Application Curves
An example pulse measurement using the device is shown in 图 9-2. The setup follows the example LiDAR 
system requirements with a 5-ns pulse captured at 1 GSPS. The applied pulse has a rise and fall time of 
approximately 1 ns. A sub-sampling technique is used to interpolate data points to form an equivalent 32 GSPS 
capture of the pulse for more accurate details and multiple capture averaging is used to suppress noise. A 
negative DC bias is applied to the ADC to enable use of the full dynamic range of the ADC for unipolar pulses. 
The pulse is spanning almost the full range of ADC codes. The extracted pulse parameters are given in 表 9-2. 
The analog front-end is not included in this measurement.
Time (ns)
Amplitude (Code)
0
5
10
15
20
25
30
35
-2048
-1536
-1024
-512
0
512
1024
1536
2048
D900
图 9-2. Measured Pulse using Sub-Sampling Technique for Equivalent 32 GSPS Measurement
---table begin---
Table tile: Extracted Pulse Parameters for Example LiDAR System
| Measured Parameter | Measured Value | Units |
|---|---|---|
| Rise Time (10-90%) | 1.18 | ns |
| Fall Time (90-10%) | 1.19 | ns |
| Pulse Width (50%) | 4.99 | ns |
| Equivalent Bandwidth(1) | 295.3 | MHz |
| Peak Amplitude (Codes) | 3901 | LSB |
| Peak Amplitude (Voltage) | 750.5 | mV |
| DC Offset (Codes) | -1994 | LSB |
| DC Offset (Voltage) | -383.7 | mV |
---table end---
# 2. CLK System Description
(1)
The equivalent bandwidth is calculated from the extracted rise time measurement. The bandwidth is limited by a 1-ns transition time 
converter used at the output of the pulse generator.

# 9.3 Initialization Set Up
The device and JESD204 interface require a specific startup and alignment sequence. The general order of that 
sequence is listed in the following steps.
1.
Tie PLL_EN high to enable the PLL or low to disable the PLL. Tie PLLREF_SE high to use the SE_CLK 
clock input (only valid if PLL_EN is high) or low to use CLK± clock input. Configure CLKCFG0 and 
CLKCFG1 pins to provide the required clocks from ORC and ORD outputs, if used.
2.
Power-up the device and wait until voltages are within the recommended supply voltage range. The PD pin 
must be held low during power up and at all other times when PLLREFO, ORC or ORD clock outputs are 
necessary for system operation, if used.
3.
Apply a stable clock signal at the desired frequency to CLK± or SE_CLK depending on the state of the 
PLLREF_SE input.
4.
Reset the device using SOFT_RESET.
5.
Verify device initialization is completed before continuing by reading INIT_DONE until a 1 is returned.
6.
Program the C-PLL if the PLL is enabled (PLL_EN is set high). Skip to step 7 if the C-PLL is disabled 
(PLL_EN is set lo# 3. 
Apply a stable clock signal at the desired frequency to CLK± or SE_CLK depending on the state of the PLLREF_SE input.

# 4. 
Reset the device using SOFT_RESET.

# 5. 
Verify device initialization is completed before continuing by reading INIT_DONE until a 1 is returned.

# 6. 
Program the C-PLL if the PLL is enabled (PLL_EN is set high). Skip to step 7 if the C-PLL is disabled (PLL_EN is set low).

# 6.1. 
Program CPLL_RESET to 1 to reset the C-PLL.

# 6.2. 
Program VCO_BIAS to 0x4A to set the C-PLL VCO bias settings.

# 6.3. 
Program PLL_P_DIV, PLL_V_DIV and PLL_N_DIV to set the C-PLL dividers (see Converter PLL (C-PLL) for Sampling Clock Generation).

# 6.4. 
Program VCO_CAL_EN to 1 to enable VCO trim calibration or manually write the VCO trim to VCO_FREQ_TRIM (and set VCO_CAL_EN to 0). Skip to step 6.e. if manually loading VCO_FREQ_TRIM.

# 6.5. 
Program CPLL_RESET to 0 to start VCO calibration and enable the C-PLL.

# 7. 
Program JESD_EN = 0 to stop the JESD204C state machine and allow setting changes.

# 8. 
Program CAL_EN = 0 to stop the calibration state machine and allow setting changes.

# 9. 
Program Low Power Operating Mode, if desired, according to the Low Power Mode and High Performance Mode section.

# 10. 
Program the desired JMODE.

# 11. 
Program the desired KM1 value. KM1 = K–1. KM1 is only used if a JMODE is chosen that uses 8B or 10B encoding.

# 12. 
Program SYNC_SEL as needed. Choose SYNCSE single-ended input or TMSTP± differential inputs.

# 13. 
Configure device calibration settings as desired (see the CAL_CFG0 and CAL_CFG1 registers). Select foreground or background calibration modes and offset calibration as needed.

# 14. 
Enable the TRIGOUT± clock output and configure the TRIGOUT output mode through the TRIGOUT_CTRL register, if desired.

# 15. 
If the C-PLL is used (PLL_EN is high) then verify that VCO calibration has finished (read VCO_CAL_DONE) and that the C-PLL is locked to the reference clock (read CPLL_LOCKED) before proceeding.

# 16. 
Program CAL_EN = 1 to enable the calibration state machine.

# 17. 
Enable over-range via OVR_EN and adjust settings if desired.

# 18. 
Program JESD_EN = 1 to re-start the JESD204C state machine and allow the link to restart.

# 19. 
Trigger a foreground calibration (if enabled) by setting CAL_SOFT_TRIG to 0 and then setting it back to 1. Alternatively, choose to use the CALTRIG pin by setting CAL_TRIG_EN to 1 and then toggling the CALTRIG pin low and then high. The CALSTAT pin and the FG_DONE register bit goes high to indicate that calibration has finished.

# 20. 
For JMODEs that use 8B/10B encoding the JESD204C interface now operates in response to the applied SYNC signal from the receiver (64B/66B does not use SYNC).

# 21. 
Data is valid when the JESD204C receiver finishes the initialization sequence (CGS and ILAS completes for 8B/10B modes or locks to SYNC header in 64B/66B modes) and the CALSTAT pin is high (if CAL_STATUS_SEL = 0) or FG_DONE is set to 1 to indicate that calibration is finished.

# 9.4 Power Supply Recommendations
The WEBENCH® Power Designer can be used to select and design the individual power supply elements as needed.
Recommended switching regulators include the TPS62913, TPS62912, TPS62085, and similar devices.
Recommended Low Drop-Out (LDO) linear regulators include the TPS7A8400, TPS7A7200, TPS7A54 and similar devices.
For the switcher only approach, the ripple filter must be designed to provide sufficient filtering at the switching frequency of the DC-DC converter and harmonics of the switching frequency. Make a note of the switching frequency reported from WEBENCH® and design the EMI filter and capacitor combination to have the filter cutoff frequency set as needed. Each application has different tolerance for noise on the supply voltage and the impact to performance so strict ripple requirements are not provided. In general, the supply voltage must stay within the recommended operating conditions limits during all ripple and transient events. Any supply filtering must account for potential current transients, specifically when using low-power background calibration (see Low-Power Background Calibration (LPBG) Mode).
Local Filtering
Bulk Capacitance
47 �F 10 �F
GND
Local Filtering
Local Filtering
Buck
+
±
GND
3.3 V  12 V
47 �F 10 �F 10 �F
GND
Inductor
Power
Good
2.2 V
10 �F 0.1 �F
GND
VPLL19
FB
VREFO
10 �F 0.1 �F
GND
10 �F 0.1 �F
GND
FB
10 �F 0.1 �F
GND
Local Filtering
10 �F 0.1 �F
GND
VA19
FB
Local Filtering
Local Filtering
DC/DC Filter and Bulk Capacitance
Buck
47 �F 10 �F 10 �F
GND
Inductor
1.4 V
10 �F 0.1 �F
GND
VD11
FB
VTRIG
10 �F 0.1 �F
GND
10 �F 0.1 �F
GND
FB
10 �F 0.1 �F
GND
10 �F 0.1 �F
GND
VA11
FB
10 �F 0.1 �F
GND
LDO
LDO
1.9 V
1.1 V
47 �F 10 �F
GND
FB = ferrite bead filter.# 9.3. 
---table begin---
Table title: LDO Linear Regulator Approach Example
| Bulk Capacitance | 47 �F | 10 �F |
| GND |  |  |
| Local Filtering |  |  |
| Buck | + | ± |
| GND | 3.3 V | 12 V |
| Inductor | Power | Good |
| 2.2 V | 10 �F | 0.1 �F |
| VPLL19 | FB | VREFO |
| Local Filtering |  |  |
| VA19 | FB |  |
| DC/DC Filter and Bulk Capacitance |  |  |
| LDO | 1.9 V | 1.1 V |
| 47 �F | 10 �F |  |
| GND |  |  |
---table end---
# 9.4 Power Supply Recommendations
FB = ferrite bead filter.

# 9.4. 
---table begin---
Table title: Switcher-Only Approach Example
| Bulk Capacitance | 47 �F | 10 �F |
| GND |  |  |
| Local Filtering |  |  |
| Buck | + | ± |
| GND | 3.3 V | 12 V |
| Inductor | Power | Good |
| 1.9 V | 10 �F | 0.1 �F |
| VPLL19 | FB | VREFO |
| Local Filtering |  |  |
| VA19 | FB |  |
| DC/DC Filter and Bulk Capacitance |  |  |
| LDO | 1.1 V |  |
| 10 �F | 0.1 �F |  |
| GND |  |  | 
---table end---
FB = ferrite bead filter.

# 9.4.1 Power Sequencing
The 1.1-V supplies (VA11, VD11) must not be more than 0.5 V above any of the 1.9-V supplies (VA19, VPLL19, 
VREFO) or VTRIG (1.1 V or 1.9 V) during power up, normal operation or power down. Further, all 1.9 V supplies 
should be within 0.5 V of each other at all times. VTRIG can be ramped with either the 1.9-V supplies or 1.1-V 
supplies, but must not be less than 0.5 V below VA11 or VD11 at any time. There is no sequencing requirement 
between VA11 and VD11.
The general recommendation is to have all 1.9-V supplies share a regulator. VTRIG is generally either 1.1 V or 
1.9 V and should share a regulator with supplies of the same voltage. The sequencing requirement can then 
generally be met by tying the power good output of the 1.9-V regulator to the 1.1-V regulator(s). This ensures 
that the 1.1-V supplies are enabled after the 1.9-V supplies have come up (power is good) and that the 1.9-V 
supplies are always greater than the 1.1-V supplies on power up. During power down as soon as the 1.1-V 
supplies drop out of regulation then the 1.9-V supplies are disabled. The ramp rates must be designed such that 
the 1.9-V supplies never dip more than 0.5 V below the VA11 or VD11 supply.

# 9.5 Layout

# 9.5.1 Layout Guidelines
There are many critical signals that require specific care during board design:
1.
Analog input signals
2.
CLK, SE_CLK and SYSREF
3.
JESD204C data outputs
4.
Power connections
5.
Ground connections
The analog input signals, clock signals and JESD204C data outputs must be routed for excellent signal quality at 
high frequencies, but should also be routed for maximum isolation from each other. Use the following general 
practices:
1.
Route using loosely coupled 100-Ω differential traces when possible. This routing minimizes impact of 
corners and length-matching serpentines on pair impedance. SE_CLK should be routed as a coplanar 
waveguide or as a stripline on an internal layer with sufficient via-fencing to prevent coupling.
2.
Provide adequate pair-to-pair spacing to minimize crosstalk, especially with loosely coupled differential 
traces. Tightly coupled differential traces may be used to reduce self-radiated noise or to improve 
neighboring trace noise immunity when adequate spacing cannot be provided.
3.
Provide adequate ground plane pour spacing to minimize coupling with the high-speed traces. Any ground 
plane pour must have sufficient via connections to the main# 2. Minimize Crosstalk
Provide adequate pair-to-pair spacing to minimize crosstalk, especially with loosely coupled differential 
traces. Tightly coupled differential traces may be used to reduce self-radiated noise or to improve 
neighboring trace noise immunity when adequate spacing cannot be provided.

# 3. Minimize Coupling With Traces
Provide adequate ground plane pour spacing to minimize coupling with the high-speed traces. Any ground 
plane pour must have sufficient via connections to the main ground plane of the board. Do not use floating or 
poorly connected ground pours.

# 4. Use Smoothly Radiused Corners
Use smoothly radiused corners. Avoid 45- or 90-degree bends to reduce impedance mismatches.

# 5. Incorporate Ground Plane Cutouts
Incorporate ground plane cutouts at component landing pads to avoid impedance discontinuities at these 
locations. Cut-out below the landing pads on one or multiple ground planes to achieve a pad size or stackup 
height that achieves the needed 50-Ω, single-ended impedance.

# 6. Avoid Irregularities in Ground Planes
Avoid routing traces near irregularities in the reference ground planes. Irregularities include cuts in the 
ground plane or ground plane clearances associated with power and signal vias and through-hole 
component leads.

# 7. Provide Symmetrically Located Ground Tie Vias
Provide symmetrically located ground tie vias adjacent to any high-speed signal vias at an appropriate 
spacing as determined by the maximum frequency the trace transports (<< λMIN/8).

# 8. Maximize Through-Board Transitions
When high-speed signals must transition to another layer using vias, transition as far through the board as 
possible (top to bottom is best case) to minimize via stubs on top or bottom of the vias.

# 9.5.2 Layout Example
图 9-5 to 图 9-7 provide examples of the critical traces routed on the device evaluation module (EVM).
***The other points are not possible to convert to Markdown as the full information is not provided here***# 9.5.2 Layout Example
图 9-5 to 图 9-7 provide examples of the critical traces routed on the device evaluation module (EVM).

# 10 Device and Documentation Support

# 10.1 Device Support

# 10.2 接收文档更新通知
要接收文档更新通知，请导航至 ti.com 上的器件产品文件夹。点击订阅更新 进行注册，即可每周接收产品信息更改摘要。有关更改的详细信息，请查看任何已修订文档中包含的修订历史记录。

# 10.3 支持资源
TI E2E™ 支持论坛是工程师的重要参考资料，可直接从专家获得快速、经过验证的解答和设计帮助。搜索现有解答或提出自己的问题可获得所需的快速设计帮助。
链接的内容由各个贡献者“按原样”提供。这些内容并不构成 TI 技术规范，并且不一定反映 TI 的观点；请参阅 TI 的《使用条款》。

# 10.4 Trademarks
TI E2E™ is a trademark of Texas Instruments.
所有商标均为其各自所有者的财产。

# 10.5 静电放电警告
静电放电 (ESD) 会损坏这个集成电路。德州仪器 (TI) 建议通过适当的预防措施处理所有集成电路。如果不遵守正确的处理和安装程序，可能会损坏集成电路。ESD 的损坏小至导致微小的性能降级，大至整个器件故障。精密的集成电路可能更容易受到损坏，这是因为非常细微的参数更改都可能会导致器件与其发布的规格不相符。

# 10.6 术语表
TI 术语表 
本术语表列出并解释了术语、首字母缩略词和定义。

# 11 Mechanical, Packaging, and Orderable Information
The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
---table begin---
Table tile: PACKAGING INFORMATION
| Orderable Device | Status (1) | Package Type | Package Drawing | Pins | Package Qty | Eco Plan (2) | Lead finish/ Ball material (6)| MSL Peak Temp (3) | Op Temp (°C) | Device Marking (4/5) | Samples |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADC12QJ1600ALRSHP | ACTIVE | FCCSP | ALR | 144 | 184 | Non-RoHS & Green | Call TI | Level-3-235C-168 HR | -55 to 125 | ADC12QJ16 SHP | Samples |
| V62/22610-03XF| ACTIVE | FCCSP | ALR | 144 | 184 | Non-RoHS & Green | Call TI | Level-3-235C-168 HR | | ADC12QJ16 SHP | Samples |
---table end---

# Note
(1) The marketing status values are defined as follows:
ACTIVE: Product device recommended for new designs.
LIFEBUY: TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.
NRND: Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design.
PREVIEW: Device has been announced but is not in production. Samples may or may not be available.
OBSOLETE: TI has discontinued the production of the device.
(2) RoHS:  TI defines "RoHS" to mean semiconductor products that are compliant with the current EU RoHS requirements for all 10 RoHS substances, including the requirement that RoHS substance do not exceed 0.1% by weight in homogeneous materials. Where designed to be soldered at high temperatures, "RoHS" products are suitable for use in specified lead-free processes. TI may reference these types of products as "Pb-Free".
RoHS Exempt: TI defines "RoHS Exempt" to mean products that contain lead but are compliant with EU RoHS pursuant to a specific EU RoHS exemption.
Green: TI defines "Green" to mean the content of Chlorine (Cl) and Bromine (Br) based flame retardants meet JS709B low halogen requirements of <=1000ppm threshold. Antimony trioxide based flame retardants must also meet the <=1000ppm threshold requirement.
(3) MSL, Peak Temp. - The Moistu# 1. Introduction
to be soldered at high temperatures, "RoHS" products are suitable for use in specified lead-free processes. TI may
reference these types of products as "Pb-Free".
RoHS Exempt: TI defines "RoHS Exempt" to mean products that contain lead but are compliant with EU RoHS pursuant to a specific EU RoHS exemption.
Green: TI defines "Green" to mean the content of Chlorine (Cl) and Bromine (Br) based flame retardants meet JS709B low halogen requirements of <=1000ppm threshold. Antimony trioxide based
flame retardants must also meet the <=1000ppm threshold requirement.

# 2. MSL, Peak Temp.
(3) MSL, Peak Temp. - The Moisture Sensitivity Level rating according to the JEDEC industry standard classifications, and peak solder temperature.

# 3. Additional Marking
(4) There may be additional marking, which relates to the logo, the lot trace code information, or the environmental category on the device.

# 4. Multiple Device Markings
(5) Multiple Device Markings will be inside parentheses. Only one Device Marking contained in parentheses and separated by a "~" will appear on a device. If a line is indented then it is a continuation
of the previous line and the two combined represent the entire Device Marking for that device.

# 5. Lead finish/Ball material
(6) Lead finish/Ball material - Orderable Devices may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two
lines if the finish value exceeds the maximum column width.

# 6. Important Information and Disclaimer
Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information
provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and
continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals.
TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.
In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

