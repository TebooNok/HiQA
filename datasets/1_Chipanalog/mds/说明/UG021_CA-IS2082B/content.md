 # CA-IS2082B超小型隔离式RS-485收发器测试板说明


# 1.描述
此份文件描述了 CA-IS2082B 隔离式 RS-485 收发器评估板的使用方法。使用户可以评估芯片性能且
对隔离系统进行系统性分析，从而提高开发速度。


#  2.芯片简介
CA-IS2082B 是隔离式 RS-485 收发器,具有高电磁抗扰度和低辐射特性。CA-IS2082B 工作于半双工模
式。
CA-IS2082B 器件具有高绝缘能力,有助于防止数据总线或其他电路上的噪声和浪涌进入本地接地端,
从而干扰或损坏敏感电路。高 CMTI 能力可以保证数字信号的正确传输。CA-IS2082B 器件采用 16 引脚
SSOP16 封装。这些器件支持绝缘耐压高达 2.5 kVRMS。
该 EVM 可以用于 CA-IS2082B 的验证。
下面以 CA-2082B 为例,介绍 CA-IS2082B 的测试说明。


# 3.物料清单
---table begin---
Table tile:UG021_CA-IS2082B物料清单表
| Item | Ref Des | Qty | Description | Package | MFR PN |
|------|---------|-----|-------------|---------|--------|
| 1    | C1, C5  | 2   | Tantalum cap, 22uF | 7343 | AVX TAJD226K025RNJ |
| 2    | C4, C6  | 2   | MLCC, 100nF/10V, X7R | 0603 | Standard |
| 3    | C3, C7, C9 | 3 | MLCC, 1μF/10V, X7R | 0603 | Standard |
| 4    | C2, C8, C10 | 3 | NA | - | Standard |
| 5    | C11    | 1   | MLCC, 50pF/10V, X7R | - | Standard |
| 6    | CON1, CON2 | 2 | CONN, 5.08mm, Rising Cage Clamp | - | Wurth Elektronik 691236510002 |
| 7    | J1, J2, J3 | 3 | Header, 3 pin, 2.54mm | - | Standard |
| 8    | J4     | 1   | Header, 2 pin, 2.54mm | - | Standard |
| 9    | R1, R2 | 2   | SMD resister, 27Ω, 1% 1206 | - | Standard |
| 10   | S1, S2, S3, S4, S5, S6 | 6 | SMA Connect, 2.54mm | - | Standard |
| 11   | TP1, TP3, TP5, TP7, TP11, TP13, TP15 | 7 | Test Point, Yellow, Through Hole, 1mm | - | Keystone 5009 |
| 12   | TP2, TP4, TP6, TP8, TP10, TP12, TP14, TP16 | 8 | Test Point, Black, Through Hole, 1mm | - | Keystone 5001 |
| 13   | TP9    | 1   | Test Point, Red, Through Hole, 1mm | - | Keystone 5005 |
| 14   | U1     | 1   | Isolated RS-485 transceiver | SSOP16 | Chipanalog CA-IS2082B |
| 15   | PCB    | 1   | Two layers PCB, FR-4, PCB-A009-00, 1.6mm thickness | - | - |
---table end---


#  4.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、高频信号发生器等。


# 5.硬件连接
1. 将直流电压源连接到 CON1 和 CON2；注意隔离 RS-485 两侧供电电压不能超过 5.5V。
2. 函数发生器输出一定频率和幅值的信号，连接输入端 DI；注意该频率不能超过 2.5MHz。
3. 通过示波器测量 DI，A，B，RO 的信号。


# 6.测试示例
图 为在评估板上所测的 CA-IS2082B 典型输入和输出波形。输入电源电源电压 VCC1=VCC2=5.0 V。输
入信号 DI 频率为 2.5MHz，幅度为 5.0V，占空比为 50%的方波。DI，A，B，RO 信号如下图所示。


# 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。
 http://www.chipanalog.com
