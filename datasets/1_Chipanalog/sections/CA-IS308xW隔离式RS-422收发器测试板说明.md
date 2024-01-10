 # CA-IS308xW隔离式RS-422收发器测试板说明


# 1.描述
此份文件描述了 CA-IS3080W 隔离式 RS-422 收发器评估板的使用方法。使用户可以评估芯片性能且
对隔离系统进行系统性分析，从而提高开发速度。


# 2.芯片简介
CA-IS3080W、CA-IS3086W、CA-IS3080WX、CA-IS3086WX 是隔离式 RS-422 收发器,具有高电磁抗扰
度和低辐射特性。CA-IS3080W、CA-IS3086W、CA-IS3080WX、CA-IS3086WX 工作于全双工模式。
CA-IS3080W、CA-IS3086W、CA-IS3080WX、CA-IS3086WX 器件具有高绝缘能力,有助于防止数据总线
或其他电路上的噪声和浪涌进入本地接地端,从而干扰或损坏敏感电路。高 CMTI 能力可以保证数字信号
的正确传输。CA-IS3080W、CA-IS3086W、CA-IS3080WX、CA-IS3086WX 器件采用 16 引脚宽体 SOIC 封
装。这些器件支持绝缘耐压高达 5 kVRMS。
该 EVM 可以用于 CA-IS3080W、CA-IS3086W、CA-IS3080WX、CA-IS3086WX 的验证。
主要区别如下表所示：
---table begin---
Table tile:UG020_CA-IS308xW 物料清单表
| 型号        | VCC1（V）范围 | VCC2（V）范围 | 传输速度(Mbps) | 额定耐压(V) | 封装        |
|-------------|----------------|----------------|-----------------|-------------|-------------|
| CA-IS3080W  | 2.5~5.5        | 4.5~5.5        | 0.5             | 5000        | SOIC16-WB   |
| CA-IS3086W  | 2.5~5.5        | 4.5~5.5        | 10              | 5000        | SOIC16-WB   |
| CA-IS3080WX | 2.5~5.5        | 4.5~5.5        | 0.5             | 5000        | SOIC16-WB   |
| CA-IS3086WX | 2.5~5.5        | 4.5~5.5        | 10              | 5000        | SOIC16-WB   |
---table end---

# 2.1.芯片简介
---table begin---
Table tile:UG020_CA-IS308xW 芯片简介表
| Item | Ref Des | Qty | Description | Package | MFR PN |
|------|---------|-----|-------------|---------|--------|
| 1    | U1      | 1   | Isolated RS-422 transceiver | SOIC16-WB | Chipanalog CA-IS3080W |
| 2    | C1, C8  | 2   | Tantalum cap, 22uF | 7343 | AVX TAJD226K025RNJ |
| 3    | C2, C5, C9, C14 | 4 | MLCC, 10uF/10V, X7R | 0805 | Standard |
| 4    | C3, C10 | 2   | MLCC, 1μF/10V, X7R | 0603 | Standard |
| 5    | C4, C11 | 2   | MLCC, 100nF/10V, X7R | 0603 | Standard |
| 6    | C6, C13 | 2   | MLCC, 10nF/10V, X7R | 0603 | Standard |
| 7    | C7, C12 | 2   | MLCC, 1nF/10V, X7R | 0603 | Standard |
| 8    | C15, C16 | 2  | MLCC, 50pF/10V, X7R | - | Standard |
| 9    | CON1, CON2 | 2 | CONN, 5.08mm, Rising Cage Clamp | - | Wurth Elektronik 691236510002 |
| 10   | J1, J2, J3, J4 | 4 | Header, 3 pin, 2.54mm | - | Standard |
| 11   | J5, J6, J7, J8 | 4 | Header, 2 pin, 2.54mm | - | Standard |
| 12   | R1, R2, R3, R4 | 4 | SMD res, 1206, 1%, 30R | - | Standard |
| 13   | S1, S2, S3, S4, S5, S6, S7, S8 | 8 | SMA Connector | - | Keystone 5001 |
| 14   | TP1, TP3, TP5, TP7, TP9, TP11, TP13, TP15, TP17, TP19 | 10 | Test Point, Red, Through Hole, 1mm | - | Keystone 5005 |
| 15   | TP2, TP4, TP6, TP8, TP10, TP12, TP14, TP16, TP18, TP20 | 10 | Test Point, Black, Through Hole, 1mm | - | Keystone 5006 |
| 16   | PCB-A24-01 | 1 | Two layers PCB, FR-4, PCB-A024-01, 1.6mm thickness | - | - |
---table end---


#  3.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、高频信号发生器等。


# 4.硬件连接
1. 将直流电压源连接到 CON1 和 CON2；注意隔离 RS-422 两侧供电电压不能超过 5.5V。
2. 函数发生器输出一定频率和幅值的信号，连接输入端 DI；注意该频率不能超过 250kHz。
3. 通过示波器测量 DI，Y，Z，RO 的信号。


# 5.测试示例
图 为在评估板上所测的 CA-IS3080W 典型输入和输出波形。输入电源电源电压 VCC1=VCC2=5.0 V。
输入信号 DI 频率为 250kHz，幅度为 5.0V，占空比为 50%的方波。DI，Y，Z，RO 信号如下图所示（A 和
Y 短接，B 和 Z 短接）。


#  6.重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。

