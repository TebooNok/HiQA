 # CA-IS2092W 带电源的数字隔离器测试板说明


# 1.描述
此份文件描述了 CA-IS2092W 测试板的相关使用说明,其中有产品介绍、原理图、PCB 布线图、物料
清单以及部分测试数据等。CA-IS2092W 评估板可以用来简单评估 CA-IS2092W 内置的隔离电源以及 RS￾485/RS-422 收发器的参数性能等。


# 2.芯片简介
CA-IS2092W 是集成隔离电源的隔离式 RS-485/RS-422 收发器,具有高电磁抗扰度和低辐射特性。CA￾IS2092W 工作于半双工模式。
CA-IS2092W 器件具有高绝缘能力,有助于防止数据总线或其他电路上的噪声和浪涌进入本地接地端,
从而干扰或损坏敏感电路。高 CMTI 能力可以保证数字信号的正确传输。CA-IS2092W 器件采用 16 引脚
宽体 SOIC 封装这些器件支持绝缘耐压高达 5 kVRMS。


# 3.物料清单
---table begin---
Table tile:UG016_CA-IS2092W 物料清单表
| Item | Ref Des             | Qty | Description                                 | Package | MFR PN                       |
|------|---------------------|-----|---------------------------------------------|---------|------------------------------|
| 1    | CON1                | 1   | CONN, 5.08mm, Rising Cage Clamp             | -       | Wurth Elektronik 691236510002 |
| 2    | FBL1, FBL2          | 2   | Beed 600Ohm 0805 Linekey                   | -       | FBG2912-601Y                |
| 3    | C1                  | 1   | Tantalum cap, 22uF 7343                    | -       | AVX TAJD226K025RNJ           |
| 4    | C2, C5, C8          | 3   | MLCC, 10μF/10V, X7R 0805 - Standard        | -       | -                            |
| 5    | C3                  | 1   | MLCC, 1μF /10V, X7R 0603 - Standard        | -       | -                            |
| 6    | C4, C6, C9          | 3   | MLCC, 100nF/10V, X7R 0603 - Standard       | -       | -                            |
| 7    | C7, C10             | 2   | MLCC, 10nF/10V, X7R 0603 - Standard        | -       | -                            |
| 8    | C11                | 2   | MLCC, 50pF/10V, X7R 0603 - Standard        | -       | -                            |
| 9    | R1, R2              | 2   | Resistor , 27Ω, 1% 1206 - Standard         | -       | -                            |
| 10   | S1, S2, S3, S4, S5,  | 6   | SMA Connect, 2.54mm - - Standard           | -       | -                            |
|      | S6                  |     |                                             |         |                              |
| 11   | L1                  | 1   | 24uH, 0.7mm, 4.5mm*12mm - Wurth Elektronik | -       | 7447043                      |
| 12   | U1                  | 1   | CA-IS2092W SOIC16-WB Chipanalog CA-IS2092W | -       | -                            |
| 13   | TP9, TP17           | 2   | Test Point, Red, Through Hole, 1mm -       | -       | Keystone 5000                |
| 14   | TP1, TP3, TP5, TP7,  | 7   | Test Point, Yellow, Through Hole, 1mm -    | -       | Keystone 5009                |
|      | TP11, TP13, TP15    |     |                                             |         |                              |
| 15   | TP2, TP4, TP6, TP8, | 9   | Test Point, Black, Through Hole, 1mm -    | -       | Keystone 5001                |
|      | TP10, TP12, TP14,   |     |                                             |         |                              |
|      | TP16, TP18          |     |                                             |         |                              |
| 16   | J1, J2, J3, J6      | 4   | Header, 3 pin, 2.54mm - - Standard         | -       |                              |
| 17   | J4, J5              | 2   | Header, 2 pin, 2.54mm - - Standard         | -       |                              |
| 18   | PCB                 | 1   | Four layers PCB, FR-4, PCB-A003-01,        | -       | -                            |
|      |                     |     | 1.0mm thickness, 100mm*100mm,              |         |                              |
|      |                     |     | The distance between Inner Layer1 and Inner|         |                              |
|      |                     |     | Layer2 should be greater than 0.4mm.      |         |                              |
---table end---


#  4.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、6.5 位多功能万用表安捷伦 34465A、高频信号
发生器等。


# 5.硬件连接
1. 将直流电压源连接到 CON1；
2. 函数发生器输出一定频率和幅值的信号,连接到各个通道的输入端；
3. 通过示波器测量各个通道输出端,用示波器观察各个通道信号。


# 6.测试示例
下面是以 CA-IS2092W 为例,测试一些典型波形,包括启动波形、输出纹波、输出动态响应、RS485 隔
离信号传递等。


# 7.PCB 布线建议
1. CA-IS2092W内置开关电源,为副边侧和外部模块提供稳压电源。输入侧VCC和输出侧VISO的旁路电容和
供电电容的位置放尽可能摆放在靠近芯片的管脚,距离应控制在2mm以内,如下图18和图19所示。当
需要在供电电源线和地线中放置过孔,应放置在电容相对于芯片管脚的外侧,而非放置在电容和芯片之
间,以减少过孔寄生电感的影响,如下图20和图21所示。
2. CA-IS2092W/98W集成隔离开关电源,存在一定的传导噪声和辐射噪声。适当的PCB拼接电容,对改善传
导干扰和辐射干扰有一定的作用。如在PCB原边GNDA和副边GNDB之间的拼接电容以及VCC/VISO对
GNDA/GNDB的拼接电容,如下图22,图23。此外,在PCB边缘处放置一系列间隔距离不大于3mm至4mm
的地过孔,形成边缘防护,如下图24所示。


# 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。
 http://www.chipanalog.com
