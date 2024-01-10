 # CA-IS398x 8 通道隔离式数字输入接收器测试板说明


# 1.描述
此份文件描述了 CA-IS398x 系列 8 通道数字隔离式数字输入接收器评估板的使用方法。用户可以评
估芯片性能且对隔离系统进行系统性分析，从而提高开发速度。


# 2.芯片简介
CA-IS398x 系列器件提供 8 通道隔离式数字输入，适合工业应用中常用的 24V 数字逻辑。这些通道
可以吸收电流或者提供电流，并具有集成的安全额定隔离度。结合一些外部器件，CA-IS398x 可以满足
IEC 61311-2 开关类型 1、2 或 3 的要求。输入接口可实现双极性功能（拉电流或者灌电流），而且现场
侧无需电源。器件输出接口工作电压范围为 2.25V 至 5.5V，支持 2.5V、3.3V 和 5V 控制器。
CA-IS398x 系列产品包括并行和串行输出选项。并行输出选件提供内置的低通滤波器，以提高抗
噪性能、降低设计复杂度和成本。串行输出选件可以通过单个 MCU 接口级联总共 128 个通道（16 个
CA-IS3980S），同时可独立配置每个通道的去抖动滤波器时间常数。
下面以 CA-IS3980P 为例，介绍 CA-IS398x 系列的测试说明。


# 3.物料清单
---table begin---
Table tile:UG019_CA-IS398x物料清单表
| Item | Ref Des                   | Qty | Description                                     | Package  | MFR           PN         |
|------|---------------------------|-----|-------------------------------------------------|----------|--------------------------|
| 1    | CON1,CON2                 | 2   | CONN, 5.08mm, Rising Cage Clamp -              | -        | Wurth Elektronik 691236510002 |
| 2    | C1,C2                     | 2   | MLCC, 1μF /10V, X7R 0805 - Standard           | 0805     | -                        |
| 3    | C3                        | 1   | MLCC, 1μF /10V, X7R 0603 - Standard           | 0603     | -                        |
| 4    | CA1~CA8                   | 8   | MLCC, 2.2nF /10V, X7R 0603 - Standard         | 0603     | -                        |
| 5    | CB1~CB8                   | 8   | MLCC , 15pF/10V, X7R 0603 - Standard          | 0603     | -                        |
| 6    | S1,S2                     | 2   | SMA Connect, 2.54mm - - Standard              | -        | -                        |
| 7    | R1,R3                     | 2   | Resistor, 6.2kΩ, 1%, 1W 2512 Standard        | 2512     | -                        |
| 8    | R5,R7                     | 2   | Resistor, 1.5kΩ, 1%, 1W 2512 Standard        | 2512     | -                        |
| 9    | R9,R11,R13,R15            | 4   | Resistor, 2.7kΩ, 1%, 1W 2512 Standard        | 2512     | -                        |
| 10   | R2,R4                     | 2   | Resistor, 2.4kΩ, 1%, 1/8W 0805 Standard     | 0805     | -                        |
| 11   | R6,R8                     | 2   | Resistor, 390Ω, 1%, 1/8W 0805 Standard      | 0805     | -                        |
| 12   | R10,R12,R14,R16           | 4   | Resistor, 750Ω, 1%, 1/8W 0805 Standard     | 0805     | -                        |
| 13   | U1                        | 1   | CA-IS3980P SSOP20 Chipanalog -                | SSOP20   | -                        |
| 14   | TP1,TP3,TP5,TP7,TP9,TP11, | 16  | Test Point, Yellow, Through Hole, 1mm -      | -        | Keystone 5009           |
|      | TP13,TP15,TP17,TP19,TP21, |     |                                                 |          |                          |
|      | TP23, TP25, TP27, TP29,   |     |                                                 |          |                          |
|      | TP31                      |     |                                                 |          |                          |
| 15   | TP6,TP6,TP12,TP14,TP20,   | 8   | Test Point, Black, Through Hole, 1mm -        | -        | Keystone 5001           |
|      | TP22,TP28,TP30            |     |                                                 |          |                          |
| 16   | J1~J16                    | 16  | Header, 2 pin, 2.54mm - - Standard             | -        |                          |
| 17   | P1,P2                     | 2   | Header, 2*4 pin, 2.54mm - - Standard          | -        |                          |
| 18   | PCB                       | 1   | Two Layers PCB, FR-4, 1.6mm Thickness         | -        | PCB-A019-01              |
---table end---


#  4.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、6.5 位多功能万用表安捷伦 34465A、高频信号
发生器等。


# 5.硬件连接
1. 将直流电压源连接到 CON2；
2. 函数发生器输出一定频率和幅值的信号连接到 CON1，用跳线帽短接 J1，使输入信号通过分压电
阻 R1 和 R2 加到各个通道的输入端 A 和 COM 端；
3. 用示波器测量 B1 通道输出端的信号；
4.用同样方法测试其他通道。


# 6.测试示例
图 6 为在评估板上所测的数字隔离器 CA-IS3980P 的典型输入和输出波形。输入信号频率为
125kHz， 占空比为 50%的方波。示波器蓝色波形为芯片第一通道输入端 A1 和 COM 之间的电压信号，
绿色波形为芯片第一通道输出端 B1 和 GND 之间的电压。


# 7. 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。
 http://www.chipanalog.com
