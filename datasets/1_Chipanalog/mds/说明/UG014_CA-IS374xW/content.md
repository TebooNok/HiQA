 # CA-IS374x 高速四通道字隔离器测试板说明


# 1. 描述
此份文件描述了 CA-IS374x 测试板的相关使用说明，其中有产品介绍、原理图、PCB 布线图、物料
清单等。CA-IS374x 测试板可以用来简单评估 CA-IS374x 数字隔离的参数性能。


# 2.芯片简介
CA-IS374x 是一款高性能四通道数字隔离器，具有精确的时序特性和低电源损耗。 在隔离 CMOS
数字 I/O 时， CA-IS374x 器件可提供高电磁抗扰度和低辐射。所有器件版本均具有施密特触发器输入，
可实现高抗噪性能。 每条隔离通道的逻辑输入和输出缓冲器均由二氧化硅 (SiO2) 绝缘栅隔离。
CA-IS3740/CA-IS3741/CA-IS3742 是四通道数字隔离器。CA-IS3740 四个通道都在同一个方向上，输
出侧（B 侧）具有输出使能； CA-IS3741 具有三个前向和一个反向通道，两侧均具有输出使能； CA￾IS3742 具有两个前向和两个反向通道，两侧都有输出使能。 所有设备都具有故障安全模式选项。 如
果输入侧电压或信号丢失，对于后缀为 L 的设备，默认输出为低，对于带有后缀 H 的设备，默认输出
为高。
通过改变 BOM 表，CA-IS374x 测试板可以用于评估如下型号的高速四通道数字隔离器。
表 1 适用 CA_IS374x 测试板的高速四通道数字隔离器型号
---table begin---
Table tile:UG014_CA-IS374xW 测试板的高速四通道数字隔离器型号表
| 型号         | 输入通道数 A 侧 | 输入通道数 B 侧 | 故障安全输出状态 | 额定耐压 (kV) | 输出使能 | 封装        |
|--------------|------------------|------------------|-------------------|----------------|----------|-------------|
| CA-IS3740LW  | 4                | 0                | 低                | 5.0            | 有       | SOIC16-WB   |
| CA-IS3740HW  | 4                | 0                | 高                | 5.0            | 有       | SOIC16-WB   |
| CA-IS3741LW  | 3                | 1                | 低                | 5.0            | 有       | SOIC16-WB   |
| CA-IS3741HW  | 3                | 1                | 高                | 5.0            | 有       | SOIC16-WB   |
| CA-IS3742LW  | 2                | 2                | 低                | 5.0            | 有       | SOIC16-WB   |
| CA-IS3742HW  | 2                | 2                | 高                | 5.0            | 有       | SOIC16-WB   |

---table end---


下面以 CA-3741HW 为例，介绍 CA-IS374x 系列的测试说明。


 # 3.物料清单
---table begin---
Table tile:UG014_CA-IS374xW物料清单表
| Item | Ref Des                      | Qty | Description                        | Package         | MFR PN           |
|------|------------------------------|-----|------------------------------------|-----------------|------------------|
| 1    | C1, C4                       | 2   | MLCC, 4.7uF/16V,X7R 0805 - Standard | 0805 - Standard | -                |
| 2    | C2, C3, C5, C7               | 4   | MLCC, 1uF/16V,X7R 0805 - Standard | 0805 - Standard | -                |
| 3    | C6, C8                       | 2   | MLCC, 0.1uF/16V,X7R 0805 - Standard | 0805 - Standard | -                |
| 4    | C12, C14, C15, C16           | 4   | MLCC, 15pF/16V,X7R 0603 - Standard | 0603 - Standard | -                |
| 5    | CA-IS3741HW                  | 1   | 4-Channel high-speed Digital Isolator SOP16WB | SOP16WB | Chipanalog CA-IS3741HW |
| 6    | J1, J2, J3, J4, J5, J6, J7, J8, J9, J10 | 10  | Header 3 pin, 2.54mm - - -           | -               | -                |
| 7    | P1, P2                       | 2   | CONN, 5.08mm, Terminal Block - - -  | -               | -                |
| 8    | S1, S2, S3, S4, S5, S6, S7, S8 | 8   | SMA Connect, 2.54mm SMA - - -        | -               | -                |
| 9    | TP1, TP2                     | 2   | Test Point, Red, Through Hole, 1mm - | -               | Keystone 5000    |
| 10   | TP3, TP4, TP13, TP14, TP15,TP16, TP17, TP18, TP19, TP20 | 10 | Test Point, Black, Through Hole, 1mm - | -          | Keystone 5009    |
| 11   | TP5, TP6, TP7, TP8, TP9, TP10, TP11, TP12 | 8 | Test Point, Yellow, Through Hole, 1mm - | -     | Keystone 5001    |
| 12   | PCB                          | 1   | Two Layers PCB， FR-4, PCB-A023-00, 1mm thickness, - - - | - | -                |
               | -           | -           |
---table end---




# 4. 测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、高频信号发生器等。


# 5.硬件连接
1. 将直流电压源连接到 P1，P2；
2. 将 ENA，ENB 通过跳线帽连接到 High；
3. 函数发生器输出一定频率和幅值的信号，连接到各个通道的输入端；
4. 通过示波器测量各个通道输出端，用示波器观察各个通道信号。



# 6.测试示例
下面是以 CA-IS3641H 为例，测试一些典型波形，包括启动波形、输出短路波形、输出纹波、输出
动态响应、各个通道的信号传输眼图等。



# 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。
 http://www.chipanalog.com
