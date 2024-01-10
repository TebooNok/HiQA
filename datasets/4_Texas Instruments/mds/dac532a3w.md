# dac532a3w

# DAC53xAxW 10-Bit Three-Channel and Two-Channel Voltage-Output and Current-Output Smart DAC With I2C or SPI

# 1. Features
Current-source DAC:
- 1-LSB DNL
- Two ranges: 300 mA and 220 mA
- 770-mV headroom
Dual (DAC532A3W only) voltage-output DACs:
- 1-LSB DNL
- Gains of 1 ×, 1.5 ×, 2 ×, 3 ×, and 4 ×
Programmable comparator mode on channel 1
High-impedance output when VDD is off
High-impedance and resistive pull-down power-down modes
50-MHz SPI-compatible interface
Automatically detects I2C or SPI
- 1.62-V VIH with VDD = 5.5 V
General-purpose input/output (GPIO) configurable 
as multiple functions
Predefined waveform generation: sine, cosine, triangular, sawtooth
User-programmable nonvolatile memory (NVM)
Internal or power-supply as reference
Wide operating range:
- Power supply: 3 V to 5.5 V
- Temperature: –40˚C to +125˚C

# 2. Applications
Tablet (multimedia)
Chromebook and WOA
Dashboard camera
Endoscope
Analog security camera
Wireless security camera

# 3. Description
The three-channel DAC532A3W and the dual-channel DAC530A2W (DAC53xAxW) are 10-bit, buffered voltage-output and current-output smart digital-to-analog-converters (DAC). The DAC53xAxW devices support a current source that can be used for linear control of laser diodes and miniature motors. These devices support Hi-Z power-down mode and Hi-Z output during power-off conditions for voltage output. Channel 1 can be configured as a voltage-output DAC or a comparator. The voltage-output DACs provide a force-sense option for use as a programmable comparator and current sink. The multifunction GPIO, function generation, and programmable nonvolatile memory (NVM) enable these smart DACs for processor-less applications and design reuse. These devices automatically detect SPI or I2C interfaces and contain an internal reference.
The DAC53xAxW feature set combined with the tiny package and low power make these smart DACs an excellent choice for applications such as laser diode power control and voice-coil motor (VCM) control in camera lens auto focus and zoom applications.
---table begin---
Table title: Device Information
| Part Number | Package(1) | Package Size (Nom)(2) |
|---|---|---|
| DAC532A3W | YBH (DSBGA, 16) | 1.72 mm × 1.72 mm |
| DAC530A2W | YBH (DSBGA, 16) | 1.72 mm × 1.72 mm |
---table end---
- For more information see Section 11.
- The package size (length × width) is a nominal value and includes pins, where applicable.
DAC530A2W
VDD
IDAC
NVM
Internal 
Reference
LDO
Output Configuration
Logic
CAP
AGND
SDA/SCLK
SCL/SYNC
A0/SDI
GPIO/SDO
1.5 �F
100 nF
VOUT
LOW
HIGH
VDD
Digital Interface
BUFFER
BUFFER
PVDD
PGND
FB
VOICE 
COIL 
MOTOR
VVCM
Voice Coil Motor Control Using DAC530A2W

# 4. Pin Configuration and Functions
# 4.1. DAC532A3W: YBH (16-pin DSBGA) Package, Top View
---table begin---
Table title: DAC532A3W: Pin Functions
| Pin No. | Name | Type | Description |
|---|---|---|---|
| A1 | PVDD | Power | Power supply for the current source. Connect this pin to VDD with low trace impedance |
| A2 | VOUT1 | Output | Voltage output on DAC channel 1. |
| A3 | VOUT0 | Output | Voltage output on DAC channel 0. |
| A4 | GPIO/SDO | Input/Output | General-purpose input/output configurable as LDAC, PD, PROTECT, RESET, SDO, and STATUS. For STATUS and SDO, c |
---table end---
# 4. Pin Configuration and Functions

# 4.2. DAC530A2W: YBH (16-pin DSBGA) Package, Top View
---table begin---
Table title: DAC530A2W: Pin Functions
| Pin No. | Name | Type | Description |
|---|---|---|---|
| A1 | PVDD | Power | Power supply for the current source. Connect this pin to VDD with low trace impedance |
| A2 | VOUT1 | Output | Voltage output on DAC channel 1. |
| A3 | NC | -- | Solder this ball to the pad. |
| A4 | GPIO/SDO | Input/Output | General-purpose input/output configurable as LDAC, PD, PROTECT, RESET, SDO, and STATUS. |
---table end---# 5. Specifications

# 5.1 Absolute Maximum Ratings
Over operating free-air temperature range (unless otherwise noted)(1)
---table begin---
Table title: Absolute Maximum Ratings
| Parameter | Min | Max | Units |
|---|---|---|---|
| VDD Supply voltage, VDD to AGND | -0.3 | 6 | V |
| PVDD Supply voltage, PVDD to VDD | -0.3 | 0.3 | V |
| Digital inputs to AGND | -0.3 | VDD + 0.3 | V |
| VFB1 to AGND | -0.3 | VDD + 0.3 | V |
| VOUTX to AGND | -0.3 | VDD + 0.3 | V |
| IOUT to AGND | -0.3 | VDD + 0.3 | V |
| Current into any pin except the IOUT, VOUTx, VDD, PVDD, PGND, and AGND pins | -10 | 10 | mA |
| TJ Junction temperature | -40 | 150 | °C |
| Tstg Storage temperature | -65 | 150 | °C |
---table end---
Note: Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions. 

# 5.2 ESD Ratings
---table begin---
Table title: ESD Ratings
| Parameter | Value | Units |
|---|---|---|
| V(ESD) Electrostatic discharge Human body model (HBM), per ANSI/ESDA/JEDEC JS-001, all pins(1) | ±2000 | V |
| Charged device model (CDM), per ANSI/ESDA/JEDEC JS-002, all pins(2) | ±500 | V |
---table end---
Note: 
(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

# 5.3 Recommended Operating Conditions
Over operating free-air temperature range (unless otherwise noted)
---table begin---
Table title: Recommended Operating Conditions
| Parameter | Min | Nom | Max | Units |
|---|---|---|---|---|
| VDD Positive supply voltage to ground (AGND), resistive or diode load | 3 | - | 5.5 | V |
| Positive supply voltage to ground (AGND), inductive load | 3 | - | 4.5 | V |
| PVDD Positive supply voltage to ground (PGND) | VDD | - | - | V |
| VIH Digital input high voltage, 3 V < VDD ≤ 5.5 V | 1.62 | - | - | V |
| VIL Digital input low voltage | 0.4 | - | - | V |
| CCAP External capacitor on CAP pin | 0.5 | - | 15 | μF |
| TA Ambient temperature | -40 | - | 125 | °C |
---table end---

# 5.4 Thermal Information
# 1. Dynamic Performance
---table begin---
Table tile: Dynamic Performance
| Parameter | Test Conditions | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| tsett | Output voltage settling time 1/4 to 3/4 scale and 3/4 to 1/4 scale settling to 10%FSR, VDD = 5.5 V | - | - | 20 | µs |
| tsett | Output voltage settling time 1/4 to 3/4 scale and 3/4 to 1/4 scale settling to 10%FSR, VDD = 5.5 V, internal VREF, gain = 4 × | - | - | 25 | µs |
| Slew rate | VDD = 5.5 V | - | - | 0.3 | V/µs |
| Power-on glitch magnitude | At start-up | - | - | 75 | mV |
---table end---
# 5.4 Thermal Information

# 2. Output-Enable Glitch Magnitude
---table begin---
Table tile: Output-Enable Glitch Magnitude
| Parameter | Test Conditions | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| Output-enable glitch magnitude | DAC output disabled to enabled, DAC registers at zero scale, RL = 100 kΩ | - | - | 250 | mV |
---table end---

# 3. Output Noise Voltage
---table begin---
Table tile: Output Noise Voltage
| Parameter | Test Conditions | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| Vn | Output noise voltage (peak-to-peak) f = 0.1 Hz to 10 Hz, DAC at midscale, VDD = 5.5 V | - | - | 50 | µVPP |
---table end---

# 4. Power-Supply Rejection Ratio (ac)(4)
---table begin---
Table tile: Power-Supply Rejection Ratio (ac)(4)
| Parameter | Test Conditions | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| Power-supply rejection ratio (ac)(4) | Internal VREF, gain = 4 ×, 200-mV 50-Hz or 60-Hz sine wave superimposed on power supply voltage, DAC at midscale | - | - | -68 | dB |
---table end---

# 5. Code-Change Glitch Impulse
---table begin---
Table tile: Code-Change Glitch Impulse
| Parameter | Test Conditions | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| Code-change glitch impulse | ±1-LSB change around midscale, including feedthrough | - | - | 10 | nV-s |
---table end---

# 6. Code-Change Glitch Impulse Magnitude
---table begin---
Table tile: Code-Change Glitch Impulse Magnitude
| Parameter | Test Conditions | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| Code-change glitch impulse magnitude | ±1-LSB change around midscale, including feedthrough | - | - | 15 | mV |
---table end---

# 7. Power
---table begin---
Table tile: Power
| Parameter | Test Conditions | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| IDD | Current flowing into VDD(2) (5) DAC532A3W: Normal operation, DACs at full scale, digital pins static | - | - | 150 | µA/ch |
---table end---

# 8. Static Performance
---table begin---
Table tile: Static Performance
| Parameter | Test Conditions | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| Resolution | | | 10 | | Bits |
| INL | Integral nonlinearity At minimum output-voltage headroom | -1.25 | | 1.25 | LSB |
---table end---

# 9. Output
---table begin---
Table tile: Output
| Parameter | Test Conditions | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| Output range(1) | IOUT-GAIN = 000b | - | - | 300 | mA |
| Output voltage headroom(2) | Sourcing current at 300 mA | 770 | | 1500 | mV |
---table end---

# 10. Dynamic Performance
# 1. Electrical Characteristics
Test conditions: At 5 °C, VDD = 3.5, and digital inputs at VDD or AGND (unless otherwise noted)
---table begin---
Table tile: Dynamic Performance
| Parameter | Test Conditions | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| tsett | Output current settling time 1/4 to 3/4 scale and 3/4 to 1/4 scale settling to 1 LSB, VDD = 3 V, diode load | - | - | 60 | µs |
| tsett | 1/8 to 3/8 scale and 3/8 to 1/8 scale settling to 1 LSB, VDD = 4 V, inductive load, CL = 470 nF | - | - | 260 | µs |
| Overshoot | DAC code changed from 1/4 scale to 3/4 scale, diode load | - | 0.7 | - | % |
| Overshoot | DAC powered down, full-scale current programmed as MARGIN-HIGH with slew rate setting 32-LSB and 4-µs step, the DAC is powered up, and then the margin start is commanded immediately, diode load | - | 1 | - | % |
| Overshoot | DAC powered down, midscale current programmed as MARGIN-HIGH with slew rate setting 32-LSB and 4-µs step, the DAC is powered up, and then the margin start is commanded immediately, inductive load | - | 1 | - | % |
| Overshoot | DAC at zero scale, full-scale current programmed as MARGIN-HIGH with slew rate setting 32-LSB and 4-µs step, and then the margin start is commanded, diode load | - | 1 | - | % |
| Overshoot | DAC at zero scale, midscale current programmed as MARGIN-HIGH with slew rate setting 32-LSB and 4-µs step, and then the margin start is commanded, inductive load, CL = 470 nF | - | 1 | - | % |
| Overshoot | DAC at full scale, zero-scale current programmed as MARGIN-LOW with slew rate setting 32-LSB and 4-µs step, and then the margin start is commanded, diode load | - | -1 | - | % |
| Overshoot | DAC at midscale, zero-scale current programmed as MARGIN-LOW with slew rate setting 32-LSB and 4-µs step, and then the margin start is commanded, inductive load, CL = 470 nF | - | -1 | - | % |
| Vn | Output noise current (peak to peak) 0.1 Hz to 10 Hz, DAC at 1/4 scale, inductive load, CL = 470 nF | - | 50 | - | µAPP |
| Output noise density | f = 1 kHz, DAC at 1/4 scale, inductive load, CL = 470 nF | - | 159 | - | nA/√Hz |
| Power-supply rejection ratio (ac) | 200-mV 50-Hz or 60-Hz sine wave superimposed on power-supply voltage, DAC at 1/4 scale, inductive load, CL = 470 nF | - | 1.7 | - | LSB/V |
| IDD | Current flowing into VDD(3), Normal operation, DAC at midscale | - | 172 | - | µA |
---table end---
# 10. Dynamic Performance
Use the device in the minimum current range to meet the electrical specifications. These devices do not have automatic thermal shutdown. The external circuitry must maintain the junction temperature within the specified limits. The current flowing into VDD does not account for the load current sourced or sinked on the IOUT pins.

# 2. Electrical Characteristics: Comparator Mode
# 4. OUTPUT
---table begin---
Table tile: OUTPUT
| PARAMETER | TEST CONDITIONS | MIN | MAX | UNIT |
|---|---|---|---|---|
| Input voltage | VFB1 resistor network connected to ground | 0 | VDD | V |
| Input voltage | VFB1 resistor network disconnected from ground | 0 | VDD × (1/3 – 1/100) | V |
| VOL | Logic low output voltage | ILOAD = 100 μA, output in open-drain mode | 0.1 | | V |
---table end---
# 2. Electrical Characteristics: Comparator Mode

# 5. DYNAMIC PERFORMANCE
---table begin---
Table tile: DYNAMIC PERFORMANCE
| PARAMETER | TEST CONDITIONS | MIN |  TYP |  MAX |  UNIT |
|---|---|---|---|---|---|
| tresp | Output response time, DAC at midscale with 10-bit resolution, FB1 input at Hi-Z, and transition step at FB1 node is (VDAC – 2 LSB) to (VDAC + 2 LSB), transition time measured between 10% and 90% of output, output current of 100 µA, comparator output configured in push-pull mode, load capacitor at DAC output is 25 pF | - | - | 10 | µs |
---table end---
**Note:**
1. Specified by design and characterization, not production tested.
2. This specification does not include the total unadjusted error (TUE) of the DAC.

# 5.8. Electrical Characteristics: General
---table begin---
Table tile: Electrical Characteristics: General
| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
|---|---|---|---|---|---|
| INTERNAL REFERENCE Initial accuracy | - | 1.1979 | 1.212 | 1.224 | V |
| Reference-output temperature coefficient(1) (2) | - | - | 73 | - | ppm/°C |
| EEPROM Endurance(1) | –40°C ≤ TA ≤ +85°C | - | 20000 | - | Cycles |
| Data retention(1) | - | - | 50 | - | Years |
| EEPROM programming write cycle time(1) | - | - | - | 200 | ms |
| Device boot-up time(1) | Time taken from power valid (VDD ≥ 3 V) to output valid state (output state as programmed in EEPROM), 0.5-µF capacitor on the CAP pin | - | - | 5 | ms |
| DIGITAL INPUTS Digital feedthrough | Voltage output mode, DAC output static at midscale, fast mode plus, SCL toggling | - | 20 | - | nV-s |
| Pin capacitance | Per pin | - | - | 10 | pF |
| POWER-DOWN MODE IDD Current flowing into VDD | DAC in deep-sleep mode, internal reference powered down, SDO mode disabled | - | 1.5 | 3 | µA |
| DAC in sleep mode, internal reference powered down | - | - | 28 | - | |
| IDD Current flowing into VDD(1) | DAC in sleep mode, internal reference enabled, additional current through internal reference | - | - | 10 | µA |
| DAC channels enabled, internal reference enabled, additional current through internal reference per DAC channel in voltage-output mode | - | - | 12.5 | - | |
| HIGH-IMPEDANCE OUTPUT ILEAK Current flowing into VOUT and VFB | DAC in Hi-Z output mode, 3 V ≤ VDD ≤ 5.5 V | - | - | 10 | nA |
---table end---
**Note:**
1. Specified by design and characterization, not production tested.
2. Measured at –40°C and +125°C and calculated the slope.

# 5.9. Timing Requirements: I2C Standard Mode
---table begin---
Table tile: Timing Requirements: I2C Standard Mode
| PARAMETER | MIN | NOM | MAX | UNIT |
|---|---|---|---|---|
| fSCL SCL frequency | - | 100 | - | kHz |
| tBUF Bus free time between stop and start conditions | 4.7 | - | - | µs |
---table end---

# 5.10. Timing Requirements: I2C Fast Mode
# 5.10. Timing Requirements: I2C Fast Mode
All input signals are timed from VIL to 70% of Vpull-up, 3 V ≤ VDD ≤ 5.5 V, –40°C ≤ TA ≤ +125°C, and 1.7 V ≤ Vpull-up ≤ VDD.
---table begin---
Table tile: Timing Requirements: I2C Fast Mode
| PARAMETER | MIN | NOM | MAX | UNIT |
|---|---|---|---|---|
| fSCL SCL frequency | - | 400 | - | kHz |
| tBUF Bus free time between stop and start conditions | 1.3 | - | - | µs |
| tHDSTA Hold time after repeated start | 0.6 | - | - | µs |
| tSUSTA Repeated start setup time | 0.6 | - | - | µs |
| tSUSTO Stop condition setup time | 0.6 | - | - | µs |
| tHDDAT Data hold time | 0 | - | - | ns |
| tSUDAT Data setup time | 100 | - | - | ns |
| tLOW SCL clock low period | 1300 | - | - | ns |
| tHIGH SCL clock high period | 600 | - | - | ns |
| tF Clock and data fall time | 300 | - | - | ns |
| tR Clock and data rise time | 300 | - | - | ns |
| tVDDAT Data valid time, R = 360 Ω, Ctrace = 23 pF, Cprobe = 10 pF | - | 0.9 | - | µs |
| tVDACK Data valid acknowledge time, R = 360 Ω, Ctrace = 23 pF, Cprobe = 10 pF | - | 0.9 | - | µs |
---table end---
# 5.10. Timing Requirements: I2C Fast Mode

# 5.11 Timing Requirements: I2C Fast-Mode Plus
# 5.14 Timing Requirements: SPI Read and Daisy Chain Operation (FSDO = 1)
All input signals are specified with tr = tf = 1 V/ns (10% to 90% of VIO) and timed from a voltage level of (VIL + VIH) / 2,
1.7 V ≤ VIO ≤ 5.5 V, 3 V ≤ VDD ≤ 5.5 V,  –40°C ≤ TA ≤ +125°C, and FSDO = 1
---table begin---
| - | MIN | NOM | MAX | UNIT |
|---|---|---|---|---|
| fSCLK Serial clock frequency | - | - | 2.5 | MHz |
| tSCLKHIGH SCLK high time | - | - | 175 | ns | 
| tSCLKLOW SCLK low time | - | - | 175 | ns |
| tSDIS SDI setup time | - | - | 8 | ns |
| tSDIH SDI hold time | - | - | 8 | ns |
| tCSS SYNC to SCLK falling edge setup time | - | - | 300 | ns |
| tCSH SCLK falling edge to SYNC rising edge | - | - | 300 | ns |
| tCSHIGH SYNC high time | - | - | 1 | µs |
| tSDODLY SCLK rising edge to SDO falling edge, IOL ≤ 5 mA, CL = 20 pF. | - | - | 300 | ns |
---table end---
# 5.11 Timing Requirements: I2C Fast-Mode Plus

# 5.15 Timing Requirements: GPIO
All input signals are specified with tr = tf = 1 V/ns (10% to 90% of VIO) and timed from a voltage level of (VIL + VIH) / 2,
1.7 V ≤ VIO ≤ 5.5 V, 3 V ≤ VDD ≤ 5.5 V, and  –40°C ≤ TA ≤ +125°C
---table begin---
| - | MIN | NOM | MAX | UNIT |
|---|---|---|---|---|
| tGPIHIGH GPI high time | - | - | 2 | µs |
| tGPILOW GPI low time | - | - | 2 | µs |
| tGPAWGD LDAC falling edge to DAC update delay(1) | - | - | 2 | µs |
| tCS2LDAC SYNC rising edge to LDAC falling edge | - | - | 1 | µs |
| tSTP2LDAC I2C stop bit rising edge to LDAC falling edge | - | - | 1 | µs |
| tLDACW LDAC low time | - | - | 2 | µs |
(1) The GPIOs can be configured as a channel-specific or global LDAC function.
---table end---

# 5.16 Timing Diagrams
VIH  
VIL  
SDA  
SCL  
Note: Start bit, Sr: Repeated start bit, P: Stop bit

# 5.17 Typical Characteristics: Voltage Output
# 5.18 Voltage Output INL vs Temperature
---table begin---
| Temperature (°C) | Voltage Output INL (LSB) |
|---|---|
| -40 | -1.25 |
| -25 | -1 |
| -10 | -0.75 |
| 5 | -0.5 |
| 20 | -0.25 |
| 35 | 0 |
| 50 | 0.25 |
| 65 | 0.5 |
| 80 | 0.75 |
| 95 | 1 |
| 110 | 1.25 |
---table end---
# 5.17 Typical Characteristics: Voltage Output
CH0 MIN  
CH1 MIN  
CH0 MAX  
CH1 MAX  

# 5.19 Voltage Output INL vs Supply Voltage
---table begin---
| Supply Voltage (V) | Voltage Output INL (LSB) |
|---|---|
| 3 | -1.25 |
| 3.625 | -1 |
| 4.25 | -0.75 |
| 4.875 | -0.5 |
| 5.5 | -0.25 |
---table end---
CH0 MAX  
CH1 MAX  
CH0 MIN  
CH1 MIN  

# 5.20 Voltage Output DNL vs Digital Input Code
---table begin---
| Code | Voltage Output DNL (LSB) |
|---|---|
| 0 | -1 |
| 128 | -0.8 |
| 256 | -0.6 |
| 384 | -0.4 |
| 512 | -0.2 |
| 640 | 0 |
| 768 | 0.2 |
| 896 | 0.4 |
| 1016 | 0.6 |
---table end---
Channel 0  
Channel 1  
Internal reference, gain = 4 ×

# 5.21 Voltage Output DNL vs Digital Input Code - Continued
---table begin---
| Code | Voltage Output DNL (LSB) |
|---|---|
| 0 | -1 |
| 128 | -0.8 |
| 256 | -0.6 |
| 384 | -0.4 |
| 512 | -0.2 |
| 640 | 0 |
| 768 | 0.2 |
| 896 | 0.4 |
| 1016 | 0.6 |
---table end---
Channel 0  
Channel 1

# 5.22 Voltage Output DNL vs Temperature
---table begin---
| Temperature (°C) | Voltage Output DNL (LSB) |
|---|---|
| -40 | -1 |
| -25 | -0.8 |
| -10 | -0.6 |
| 5 | -0.4 |
| 20 | -0.2 |
| 35 | 0 |
| 50 | 0.2 |
| 65 | 0.4 |
| 80 | 0.6 |
| 95 | 0.8 |
| 110 | 1 |
| 125 | 1.25 |
---table end---
Channel 0  
Channel 1  
DAC channels at midscale

# 5.23 Voltage Output DNL vs Supply Voltage
---table begin---
| Supply Voltage (V) | Voltage Output DNL (LSB) |
|---|---|
| 3 | -1 |
| 3.25 | -0.8 |
| 3.5 | -0.6 |
| 3.75 | -0.4 |
| 4 | -0.2 |
| 4.25 | 0 |
| 4.5 | 0.2 |
| 4.75 | 0.4 |
| 5 | 0.6 |
| 5.25 | 0.8 |
| 5.5 | 1 |
---table end---
Channel 0  
Channel 1  
DAC channels at midscale  

# 5.24 Voltage Output TUE vs Digital Input Code
---table begin---
| Code | Voltage Output TUE (%FSR) |
|---|---|
| 0 | -1.5 |
| 128 | -1.2 |
| 256 | -0.9 |
| 384 | -0.6 |
| 512 | -0.3 |
| 640 | 0 |
| 768 | 0.3 |
| 896 | 0.6 |
| 1023 | 0.9 |
---table end---
Channel 0  
Channel 1  
Internal reference, gain = 4 ×

# 5.25 Voltage Output TUE vs Digital Input Code - Continued
---table begin---
| Code | Voltage Output TUE (%FSR) |
|---|---|
| 0 | -1.5 |
| 128 | -1.2 |
| 256 | -0.9 |
| 384 | -0.6 |
| 512 | -0.3 |
| 640 | 0 |
| 768 | 0.3 |
| 896 | 0.6 |
| 1023 | 0.9 |
---table end---
Channel 0  
Channel 1

# 5.26 Voltage Output TUE vs Temperature
---table begin---
| Temperature (°C) | Voltage Output TUE (%FSR) |
|---|---|
| -40 | -1.5 |
| -25 | -1.2 |
| -10 | -0.9 |
| 5 | -0.6 |
| 20 | -0.3 |
| 35 | 0 |
| 50 | 0.3 |
| 65 | 0.6 |
| 80 | 0.9 |
| 95 | 1.2 |
| 110 | 1.5 |
| 125 | 1.5 |
---table end---
Channel 0  
Channel 1  
DAC channels at midscale

# 5.27 Voltage Output TUE vs Supply Voltage
---table begin---
| Supply Voltage (V) | Voltage Output TUE (%FSR) |
|---|---|
| 3 | -1.5 |
| 3.5 | -1.2 |
| 4 | -0.9 |
| 4.5 | -0.6 |
| 5 | -0.3 |
| 5.5 | 0 |
---table end---
Channel 0  
Channel 1  
DAC channels at midscale

# 5.28 Voltage Output Offset Error vs Temperature
---table begin---
| Temperature (°C) | Voltage Output Offset Error (%FSR) |
|---|---|
| -40 | -0.5 |
| -25 | -0.4 |
| -10 | -0.3 |
| 5 | -0.2 |
| 20 | -0.1 |
| 35 | 0 |
| 50 | 0.1 |
| 65 | 0.2 |
| 80 | 0.3 |
| 95 | 0.4 |
| 110 | 0.5 |
| 125 | 0.5 |
---table end---
Channel 0  
Channel 1

# 5.29 Voltage Output Gain Error vs Temperature
---table begin---
| Temperature (°C) | Voltage Output Gain Error (%FSR) |
|---|---|
| -40 | -0.5 |
| -25 | -0.4 |
| -10 | -0.3 |
| 5 | -0.2 |
| 20 | -0.1 |
| 35 | 0 |
| 50 | 0.1 |
| 65 | 0.2 |
| 80 | 0.3 |
| 95 | 0.4 |
| 110 | 0.5 |
| 125 | 0.5 |
---table end---
Channel 0  
Channel 1

# 5.30 Voltage Output AC PSRR vs Frequency
---table begin---
| Frequency (Hz) | Voltage Output AC PSRR (dB) |
|---|---|
| 10 | -90 |
| 20 | -80 |
| 30 | -70 |
| 50 | -60 |
| 100 | -50 |
| 200 | -40 |
| 500 | -30 |
| 1000 | -20 |
| 10000 | -10 |
| 100000 | 0 |
---table end---
Channel 0  
Channel 1

# 5.31 Voltage Output Code-to-Code Glitch - Rising Edge
Time (s)
0
10
20
30
40
50
LDAC (1V/div)
VOUT (1 LSB/div)

# 5.32 Voltage Output Code-to-Code Glitch - Falling Edge
Time (s)
0
10
20
30
40
50
LDAC (1 V/div)
VOUT (1 LSB/div)

# 5.33 Voltage Output Switching Characteristics
Time (s)
0
10
20
30
40
50
VOUT (0.5 V/div)
Trigger (1 V/div)
Settling Band (+10%FSR)
Settling band (-10%FSR)
Zero scale to full scale switch# 5.19 Voltage Output Code-to-Code Glitch - Rising Edge
Time (s)
0
10
20
30
40
50
LDAC (1V/div)
VOUT (1 LSB/div)

# 5.20 Voltage Output Code-to-Code Glitch - Falling Edge
Time (s)
0
10
20
30
40
50
LDAC (1 V/div)
VOUT (1 LSB/div)

# 5.21 Voltage Output Setting Time - Rising Edge
Time (s)
0
10
20
30
40
50
VOUT (0.5 V/div)
Trigger (1 V/div)
Settling Band (+10%FSR)
Settling band (-10%FSR)
Zero scale to full scale swing 

# 5.22 Voltage Output Setting Time - Falling Edge
Time (s)
0
10
20
30
40
50
VOUT (0.5 V/div)
Trigger (1 V/div)
Settling Band (-10%FSR)
Settling Band (+10%FSR)
Full scale to zero scale swing

# 5.23 Voltage Output Power-On Glitch
Time (s)
0
200
400
600
800
1000
1200
1400
1600
VDD (1 V/div)
VOUT (15 mV/div)
DAC in Hi-Z power-down mode
---table begin---
Table title: Voltage-Output Noise Density
| Frequency (Hz) | Voltage-Output Noise Density (V/Hz) |
|---|---|
| 10 | 20 |
| 30 | 50 |
| 100 | 200 |
| 500 | 1000 |
| 10000 | 100000 |
| 0 | 0.3 |
| 0.6 | 0.9 |
| 1.2 | 1.5 |
| 1.8 | 2.1 |
| 2.4 | 2.7 |
| 3 | -
---table end---

# 5.24 Voltage Output Noise Density
Time (s)
Voltage-Output Flicker Noise (V)
0
2
4
6
8
10
-50
-40
-30
-20
-10
0
10
20
30
40
50
Channel 0
Channel 1
Internal reference, gain = 4 ×, f = 0.1 Hz to 10 Hz

# 5.25 Voltage Output Flicker Noise
Time (s)
Voltage-Output Flicker Noise (V)
0
2
4
6
8
10
-25
-20
-15
-10
-5
0
5
10
15
20
25
Channel 0
Channel 1
f = 0.1 Hz to 10 Hz 

# 5.26 Current Output INL vs Digital Input Code
---
Following are some more contents....# 5.33 Current Output DNL vs Temperature
---table begin---
Table Tile: Current Output DNL vs Temperature
| Supply Voltage (V) | Current Output DNL (LSB) |
|---|---|
| 3 | -1 |
| 3.5 | -0.75 |
| 4 | -0.5 |
| 4.5 | -0.25 |
| 5 | 0 |
| 5.5 | 0.25 |
---table end---
# 5.26 Current Output INL vs Digital Input Code

# 5.34 Current Output DNL vs Supply Voltage
---table begin---
Table Title: Current Output DNL vs Supply Voltage
| Supply Voltage (V) | Current Output DNL (LSB) |
|---|---|
| 3 | -1 |
| 3.5 | -0.75 |
| 4 | -0.5 |
| 4.5 | -0.25 |
| 5 | 0 |
| 5.5 | 0.25 |
---table end---

# 5.35 Current Output Offset Error vs Temperature
---table begin---
Table Title: Current Output Offset Error vs Temperature
| Temperature (°C) | Current-Output Offset Error (mA) |
|---|---|
| -40 | -6 |
| -25 | -4 |
| -10 | -2 |
| 5 | 0 |
| 20 | 2 |
| 35 | 4 |
| 50 | 6 |
---table end---

# 5.36 Current Output Gain Error vs Temperature
---table begin---
Table Title: Current Output Gain Error vs Temperature
| Temperature (°C) | Current-Output Gain Error (%FSR) |
|---|---|
| -40 | 0 |
| -25 | 3.32 |
| -10 | 6.64 |
| 5 | 9.96 |
| 20 | 13.28 |
| 35 | 16.6 |
| 50 | 19.92 |
| 65 | 23.24 |
| 80 | 26.56 |
| 95 | 29.88 |
| 110 | 33.2 |
---table end---

# 5.38 Current Output vs Load Voltage
---table begin---
Table Title: Current Output vs Load Voltage
| Load Voltage (V) | Current Output (mA) |
|---|---|
| 0 | 0 |
| 0.5 | 20 |
| 1 | 40 |
| 1.5 | 60 |
| 2 | 80 |
| 2.5 | 100 |
| 3 | 120 |
| 3.5 | 140 |
---table end---

# 5.50 Comparator Response Time: Low‑to‑High Transition
---table begin---
Table Title: Comparator Response Time: Low‑to‑High Transition
| Time (µs) | VAIN (1 LSB/div) | VOUT (1 V/div) |
|---|---|---|
| 0 | 0 | 0 |
| 2 | 0 | 1 |
| 4 | 1 | 1 |
| 6 | 1 | 1 |
| 8 | 2 | 2 |
| 10 | 2 | 2 |
| 12 | 3 | 2 |
| 14 | 3 | 3 |
| 16 | 4 | 3 |
| 18 | 4 | 4 |
| 20 | 5 | 4 |
---table end---

# 5.51 Comparator Response Time: High‑to‑Low Transition
---table begin---
Table Title: Comparator Response Time: High‑to‑Low Transition
| Time (µs) | VAIN (1 LSB/div) | VOUT (1 V/div) |
|---|---|---|
| 0 | 0 | 0 |
| 2 | 0 | 1 |
| 4 | 1 | 1 |
| 6 | 1 | 1 |
| 8 | 2 | 2 |
| 10 | 2 | 2 |
| 12 | 3 | 2 |
| 14 | 3 | 3 |
| 16 | 4 | 3 |
| 18 | 4 | 2 |
| 20 | 5 | 4 |
---table end--- 

# 5.52 Comparator Offset Error vs Temperature
---table begin---
Table title: Comparator Offset Error vs Temperature
| Temperature (°C) | Comparator Offset Error (mV) |
|---|---|
| -40 | -6 |
| -25 | -4.8 |
| -10 | -3.6 |
| 5 | -2.4 |
| 20 | -1.2 |
| 35 | 0 |
| 50 | 1.2 |
| 65 | 2.4 |
| 80 | 3.6 |
| 95 | 4.8 |
| 110 | 6 |
| 125 | -6 |
---table end--- 

# 5.53 Internal Reference vs Temperature 
---table begin---
Table title: Internal Reference vs Temperature
| Temperature(°C) | Internal Reference (V) |
|---|---|
| -40 | 1.208 |
| -25 | 1.209 |
| -10 | 1.21 |
| 5 | 1.211 |
| 20 | 1.212 |
| 35 | 1.213 |
| 50 | 1.214 |
| 65 | 1.215 |
| 80 | 1.216 |
| 95 | 1.217 |
| 110 | 1.218 |
---table end---

# 5.54 Internal Reference vs Supply Voltage
---table begin---
Table title: Internal Reference vs Supply Voltage
| Supply Voltage (V) | Internal Reference (V) |
|---|---|
| 3 | 1.21279 |
| 3.5 | 1.212805 |
| 4 | 1.21282 |
| 4.5 | 1.212835 |
| 5 | 1.21285 |
| 5.5 | 1.212865 |
| 1.21288 | 1.212895 |
| 1.21291 | 1.212925 |
| 1.21294 | Internal reference |
---table end---

# 5.55 Power-Down Current vs Temperature
---table begin---
Table title: Power-Down Current vs Temperature
| Temperature (°C) | Internal Reference (V) |
|---|---|
| -40 | 0 |
| -25 | 0.5 |
| -10 | 1 |
| 5 | 1.5 |
| 20 | 2 |
| 35 | 2.5 |
| 50 | 3 |
| 65 | VDD 5.5 V |
| 80 | VDD 3.0 V |
| 95 | Deep-sleep mode |
| 110 | Figure 5-56. Power-Down Current vs Temperature |
| 125 | |
---table end---

# 5.57 Boot-Up Time vs Capacitance on CAP pin
---table begin---
Table title: Boot-Up Time vs Capacitance on CAP pin
| External Capacitance on CAP Pin (µF) | Boot-up Time (ms) |
|---|---|
| 0.5 | 0 |
| 3.5 | 1 |
| 6.5 | 2 |
| 9.5 | 3 |
| 12.5 | 4 |
| 15 | 5 |
---table end---

# 6 Detailed Description
6.1 Overview
The three-channel DAC532A3W and the dual-channel DAC530A2W (DAC53xAxW) are a 10-bit, buffered 
voltage-output and current-output smart DACs. The DAC channel 2 acts as a current source. The DAC channel 
1 is configurable as voltage output or comparator input. The DAC outputs are changed to Hi-Z when VDD is 
off; a feature useful in voltage-margining applications. This smart DAC contains NVM, an internal reference, 
automatically detectable I2C or SPI, force-sense output, and a general-purpose input. This device supports 
Hi-Z power-down modes by default, which can be configured to 10 kΩ-GND or 100 kΩ-GND for voltage-output 
channels using the NVM. The DAC53xAxW has a power-on-reset (POR) circuit that makes sure all the registers 
start with default or user-programmed settings using NVM. The DAC53xAxW operates with either an internal 
reference or with a power supply as the reference.
The DAC53xAxW supports I2C standard mode (100kbps), fast mode (400kbps), and fast-mode plus (1Mbps). 
The I2C interface can be configured with four target addresses using the A0 pin. SPI mode supports a 3-wire 
interface by default with up to 50-MHz SCLK input. The GPIO/SDO input can be configured as SDO in the 
NVM for SPI read capability. The GPIO/SDO input can alternatively be configurable as LDAC, PD, STATUS, 
FAULT-DUMP, RESET, and PROTECT functions.
The DAC53xAxW also include digital slew rate control, and supports standard waveform generation such as 
sine, cosine, triangular, and sawtooth waveforms. These devices can generate pulse-width modulation (PWM) 
output with the combination of the triangular or sawtooth waveform and the FB1 pin. The force-sense outputs of 
channel 1 can be used as a programmable comparator.# 6.1 Smart DAC
th up to 50-MHz SCLK input. The GPIO/SDO input can be configured as SDO in the 
NVM for SPI read capability. The GPIO/SDO input can alternatively be configurable as LDAC, PD, STATUS, 
FAULT-DUMP, RESET, and PROTECT functions.
The DAC53xAxW also include digital slew rate control, and supports standard waveform generation such as 
sine, cosine, triangular, and sawtooth waveforms. These devices can generate pulse-width modulation (PWM) 
output with the combination of the triangular or sawtooth waveform and the FB1 pin. The force-sense outputs of 
channel 1 can be used as a programmable comparator. The comparator mode allows programmable hysteresis, 
latching comparator, window comparator, and fault-dump to the NVM. These features enable the DAC53xAxW 
to go beyond the limitations of a conventional DAC that depends on a processor to function. As a result of 
processor-less operation and the smart feature set, the DAC53xAxW is called a smart DAC.

# 6.2 Functional Block Diagram
DAC 
Register
DAC 
Buffer
BUF
Power-Down 
Logic
I2C / SPI / GPIO
Power-On 
Reset
AGND
VDD
DAC
Internal
Reference
Nonvolatile 
Memory
CAP
LDO
+
-
R2
VOUT0 
(DAC532A3W Only)
GPIO/SDO
A0/SDI
SCL/SYNC
SDA/SCLK
R1
Channel 0
Output 
Configuration
MUX
AGND
BUF
Power-Down 
Logic
DAC
+
-
R2
R1
Channel 1
Output 
Configuration
VOUT1
FB1
DAC 
Register
DAC 
Buffer
DAC 
Register
DAC 
Buffer
AMP1
Power-Down 
Logic
DAC
+
-
IOUT
Channel 2
Output 
Configuration
AGND
PVDD
PVDD
RSET
RA
RB
PGND
+
-
AMP2
D1
Internal 
Reference

# 6.3 Feature Description

# 6.3.1 Smart Digital-to-Analog Converter (DAC) Architecture
The voltage-output DAC channels of the DAC53xAxW devices consist of a string architecture with a voltage-
output amplifier, as well as an external feedback pin on channel 1. Section 6.2 shows the DAC architecture 
within the block diagram that operates from a 3-V to 5.5-V power supply. The DAC has an internal voltage 
reference of 1.21 V. Optionally, use the power supply as a reference. The voltage-output mode supports multiple 
programmable output ranges.
The DAC53xAxW devices support Hi-Z output when VDD is off, maintaining very low leakage current at the 
output pins with up to 1.25 V of forced voltage. The DAC output pin also starts up in high-impedance mode by 
default, making these devices an excellent choice for voltage margining and scaling applications. To change the 
power-up mode to 10 kΩ-GND or 100 kΩ-GND, program the corresponding DAC-PDN-x field in the COMMON-
CONFIG register and load these bits in the device NVM.
The DAC53xAxW devices support comparator mode on channel 1. The FB1 pin acts as an input for the 
comparator. The DAC architecture supports inversion of the comparator output using register settings. The 
comparator outputs can be push-pull or open-drain. The comparator mode supports programmable hysteresis 
using the margin-high and margin-low register fields, latching comparator, and window comparator. The 
comparator outputs are accessible internally by the device.
Channel 2 functions as a current source with a minimum 770-mV headroom at 300-mA output. Make sure the 
junction temperature of the device is kept within the recommended limit while using the current output.
The DAC53xAxW devices include a smart feature set to enable processor-less operation and high integration. 
The NVM enables a predictable start-up. In the absence of a processor or when the processor or software fails, 
the GPIO triggers the DAC output without the SPI or I2C interface. The integrated functions and the FB1 pin 
enable PWM output for control applications.

# 6.3.2 Digital Input/Outpu# 6.3.2 Digital Input/Output
The DAC53xAxW have four digital I/O pins that include I2C, SPI, and GPIO interfaces. These devices automatically detect I2C and SPI protocols at the first successful communication after power-on, and then connect to the detected interface. After an interface protocol is connected, any change in the protocol is ignored. 
The I2C interface uses the A0 pin to select from among four address options. The SPI interface is a three-wire interface by default. No readback capability is available in this mode. The GPIO/SDO pin can be configured in the register map and then programmed in to the NVM as the SDO function. The SPI readback mode is slower than the write mode. The programming interface pins are:
* I2C: SCL, SDA, A0
* SPI: SCLK, SDI, SYNC, SDO/GPIO
The GPIO/SDO can be configured as multiple functions other than SDO. These are LDAC, PD, STATUS, PROTECT, FAULT-DUMP, and RESET. All the digital pins are open-drain when used as outputs. Therefore, all the output pins must be pulled up to the desired I/O voltage using external resistors.

# 6.3.3 Nonvolatile Memory (NVM)
The DAC53xAxW contain NVM bits. These memory bits are user programmable and erasable, and retain the set values in the absence of a power supply. All the register bits, shown in the highlighted gray cells in Section 7, can be stored in the NVM by setting NVM-PROG = 1 in the COMMON-TRIGGER register. The NVM-PROG is an autoresetting bit. The default values for all the registers in the DAC53xAxW are loaded from NVM as soon as a POR event is issued.
The DAC53xAxW also implement NVM-RELOAD bit in the COMMON-TRIGGER register. Set this bit to 1 and the device starts an NVM-reload operation. After completion, the device autoresets the NVM-RELOAD bit to 0. During the NVM write or reload operation, all read/write operations to the device are blocked. The Electrical Characteristics: General section provides the timing specification for the NVM write cycle. The processor must wait for the specified duration before resuming any read or write operation on the SPI or I2C interface.

# 6.4 Device Functional Modes

# 6.4.1 Voltage-Output Mode
The voltage-output mode for each DAC channel 0 and DAC channel 1 can be entered by selecting the power-up option in the DAC-PDN-0 and DAC-PDN-1 fields, respectively in the COMMON-CONFIG register. Short the VOUT1/AIN1 and FB1 pins of channel 1 externally for closed-loop amplifier output. An open FB1 pin saturates the amplifier output on channel 1. To achieve the desired voltage output, select the correct reference option, select the amplifier gain for the required output range, and program the DAC code in the DAC-0-DATA and DAC-1-DATA registers, respectively for channel 0 and channel 1.

# 6.4.1.1 Voltage Reference and DAC Transfer Function
Figure 6-1 shows that there are two voltage reference options possible with the DAC53xAxW: internal reference and the power supply as reference. The DAC transfer function in the voltage-output and comparator modes changes based on the voltage reference selection. Internal Reference VDD MUX REF-GAIN-0 REF-GAIN-1 EN-INT-REF DAC Ladder + – VOUT0 VOUT1 FB1 R1 R2 DAC-PDN-0 (Hi-Z) DAC-PDN-1 (Hi-Z) DAC-PDN-0 DAC-PDN-1 10 k� or 100 k � AGND DAC-PDN-0 DAC-PDN-1 DAC Ladder PVDD PGND IOUT IOUT-GAIN DAC-PDN-2 DAC-PDN-2 1.2 k � SW1 SW2

# 6.4.1.1.1 Internal Reference
The DAC53xAxW contains an internal reference that is disabled by default. To enable the internal reference, write 1 to bit EN-INT-REF in the COMMON-CONFIG register. The internal reference generates a fixed 1.21-V voltage (typical). On channel 0, use the REF-GAIN-0 bit in the DAC-0-GAIN-CONFIG register to achieve gains of 1.5 ×, 2 ×, 3 ×, or 4 × for the DAC output voltage (VOUT). Similarly on channel 1, use the REF-GAIN-1 bit in the DAC-1-GAIN-CMP-CONFIG register. Equation 1 shows the DAC transfer function using the internal reference, in Volts. 
VOUT = DAC_DATA/2^(N) × VREF × GAIN
where:
• N is the resolution in bits, 10.
• DAC_DATA is the decimal equivalent of the binary code that is loaded to the DAC-x-DATA bit in the DAC-x-DATA register. DAC_DATA ranges from 0 to 2^(N) - 1.
• VREF is the internal reference voltage = 1.21 V (typical).
• GAIN = 1.5 ×, 2 ×, 3 ×, or 4 ×, based on REF-GAIN-x bits.

# 6.4.1.1.2 Power-Supply as Reference
The DAC53xAxW can operate with the power-supply pin (VDD) as a reference. Equation 2 shows DAC transfer function in Volts, when the power-supply pin is used as reference. The gain at the output stage is always 1 ×.
VOUT = DAC_DATA/2^(N) × VDD
where:
• N is the resolution in bits, 10.
• DAC_DATA is the decimal equivalent of the binary code that is loaded to the DAC-x-DATA bit in the DAC-x-DATA register.
• DAC_DATA ranges from 0 to 2^(N) – 1.
• VDD is used as the DAC reference voltage.

# 6.4.2 Current-Output Mode
To enable current output on DAC channel 2 (IOUT), write 00b to DAC-PDN-2 bits in the COMMON-CONFIG register. Select the desired current-output range by writing to the IOUT-GAIN bits in the DAC-2-GAIN-CONFIG register. The transfer function of the output current is shown in Equation 3, in Amperes.
IOUT = DAC_DATA/2^(N) × GAIN × K
where:
• N is the resolution in bits, 10.
• DAC_DATA is the decimal equivalent of the binary code that is loaded to the DAC-2-DATA bit as specified in the DAC-2-DATA register.
• GAIN is the value of the IOUT-GAIN setting as specified in the DAC-2-GAIN-CONFIG register.
• K is the transfer function constant, 0.5241 (typical).

# 6.4.3 Comparator Mode
DAC channel 1 can be configured as programmable comparator in the voltage-output mode. To enter the comparator mode for channel 1, write 1 to the CMP-1-EN bit in DAC-1-GAIN-CMP-CONFIG register. The comparator output can be configured as push-pull or open-drain using the CMP-1-OD-EN bit. To enable the comparator output on the output pin, write 1 to the CMP-1-OUT-EN bit. To invert the comparator output, write 1 to the CMP-1-INV-EN bit. The FB1 p# 6.4.3 Comparator Mode
DAC channel 1 can be configured as programmable comparator in the voltage-output mode. To enter the comparator mode for channel 1, write 1 to the CMP-1-EN bit in DAC-1-GAIN-CMP-CONFIG register. The comparator output can be configured as push-pull or open-drain using the CMP-1-OD-EN bit. To enable the comparator output on the output pin, write 1 to the CMP-1-OUT-EN bit. To invert the comparator output, write 1 to the CMP-1-INV-EN bit. The FB1 pin has a finite impedance. By default, the FB1 pin is in the high-impedance mode. To disable high-impedance on the FB1 pin, write 1 to the CMP-1-HIZ-IN-DIS bit. 
In the Hi-Z input mode, the comparator input range is limited to:
For GAIN = 1 ×, 1.5 ×, or 2 ×: VFB1 ≤ (VREF × GAIN) / 3
For GAIN = 3 ×, or 4 ×: VFB1 ≤ (VREF × GAIN) / 6
Any higher input voltage is clipped.
---table begin---
Table title: Comparator Output Configuration
| CMP-1-EN | CMP-1-OUT-EN | CMP-1-OD-EN | CMP-1-INV-EN | CMPX-OUT PIN |
|---|---|---|---|---|
| 0 | X | X | X | Comparator not enabled |
| 1 | 0 | X | X | No output |
| 1 | 1 | 0 | 0 | Push-pull output |
| 1 | 1 | 0 | 1 | Push-pull and inverted output |
| 1 | 1 | 1 | 0 | Open-drain output |
| 1 | 1 | 1 | 1 | Open-drain and inverted output |
---table end---

# 6.4.3.1 Programmable Hysteresis Comparator
Table 6-2 shows that comparator mode provides hysteresis when the CMP-1-MODE bit is set to 01b. Figure 6-4 shows that the hysteresis is provided by the DAC-1-MARGIN-HIGH and DAC-1-MARGIN-LOW registers.
When the DAC-1-MARGIN-HIGH is set to full-code or the DAC-1-MARGIN-LOW is set to zero-code, the comparator works as a latching comparator that is, the output is latched after the threshold is crossed. The latched output can be reset by writing to the corresponding RESET-CMP-FLAG-1 bit in the COMMON-DAC-TRIG register. Figure 6-5 shows the behavior of a latching comparator with active low output, and Figure 6-6 shows the behavior of a latching comparator with active high output.
Note: The value of the DAC-1-MARGIN-HIGH register must be greater than the value of the DAC-1-MARGIN-LOW register. The comparator output in the hysteresis mode can only be noninverting; that is, the CMP-1-INV-EN bit in the DAC-1-GAIN-CMP-CONFIG register must be set to 0. For the reset to take effect in latching mode, the input voltage must be within DAC-1-MARGIN-HIGH an
---table begin---
Table title: Comparator Mode Selection
| CMP-1-MODE BIT FIELD | COMPARATOR CONFIGURATION |
|---|---|
| 00 | Normal comparator mode. No hysteresis or window operation. |
| 01 | Hysteresis comparator mode. DAC-1-MARGIN-HIGH and DAC-1-MARGIN-LOW registers set the hysteresis. |
| 10 | Window comparator mode. DAC-1-MARGIN-HIGH and DAC-1-MARGIN-LOW registers set the window bounds. |
| 11 | Invalid setting |
---table end---# 6.4.3.2 Programmable Window Comparator
Window comparator mode on channel 1 is enabled by setting the CMP-1-MODE bit to 10b (see also Table 6-2). Figure 6-7 shows that the window bounds are set by the DAC-1-MARGIN-HIGH and the DAC-1-MARGIN-
LOW registers. The output of the window comparator is indicated by the WIN-CMP-1 bit in the CMP-STATUS 
register. The comparator output (WIN-CMP-1) can be latched by writing 1 to the WIN-LATCH-EN bit in the COMMON-CONFIG register. After being latched, the comparator output can be reset using the corresponding RESET-CMP-FLAG-1 bit in the COMMON-DAC-TRIG register. For the reset to take effect, the input must be within the window bounds.
A single comparator is used per channel to check both the margin-high and margin-low limits of the window. Therefore, the window comparator function has a finite response time (see also Electrical Characteristics: Comparator Mode section). The static behavior of the WIN-CMP-1 bit is not reflected at the output pins. Set the 
CMP-1-OUT-EN bit to 0. The WIN-CMP-1 bit must be read digitally using the communication interface. This bit can also be mapped to the GPIO/SDO pin (see also Table 6-9).
Note:
1. The value of the DAC-1-MARGIN-HIGH register must be greater than that of the DAC-1-MARGIN-LOW register.
2. Set the SLEW-RATE-1 bit to 0000b (no-slew) and LOG-SLEW-EN-1 bit to 0b in the DAC-1-FUNC-CONFIG register to get the best response time from the window comparator.
3. The CMP-1-OUT-EN bit in the DAC-1-GAIN-CMP-CONFIG register can be set to 0b to eliminate undesired toggling of the VOUT1/AIN1 pin.

# 6.4.4 Fault-Dump Mode
The DAC53xAxW provides a feature to save a few registers into the NVM when the FAULT-DUMP bit is triggered or when the GPIO mapped to fault-dump is triggered (see also Table 6-8). This feature is useful in system-level fault management to capture the state of the device or system just before a fault is triggered, and to allow diagnosis after the fault has occurred. The registers saved when fault-dump is triggered, are:
1. CMP-STATUS[7:0]
2. DAC-0-DATA[15:8]
3. DAC-1-DATA[15:8]
4. DAC-2-DATA[15:8]
Note: When the fault-dump cycle is in progress, any change in the data can corrupt the final outcome. Make sure the comparator and the DAC codes are stable during the NVM write cycle.
---table begin---
Table title: Fault-Dump NVM Storage Format
| column0 | column1 | column2 |
|---|---|---|
| **Data** | **Must be stable** | **During NVM write cycle** |
| CMP-STATUS[7:0] | ✓ | ✓ |
| DAC-0-DATA[15:8] | ✓ | ✓ |
| DAC-1-DATA[15:8] | ✓ | ✓ |
| DAC-2-DATA[15:8] | ✓ | ✓ |
---table end---# 6.4.4 Fault Management
This feature is useful in system-level fault management to capture the state of the device or system just before a fault is triggered, and to allow diagnosis after the fault has occurred. The registers saved when fault-dump is triggered, are:
* CMP-STATUS[7:0]
* DAC-0-DATA[15:8]
* DAC-1-DATA[15:8]
* DAC-2-DATA[15:8]
Note: When the fault-dump cycle is in progress, any change in the data can corrupt the final outcome. Make sure the comparator and the DAC codes are stable during the NVM write cycle.

# Table 6-3 Fault-Dump NVM Storage Format
---table begin---
Table tile: Fault-Dump NVM Storage Format
| NVM ROWS | B31-B24 | B23-B16 | B15-B8 | B7-B0 |
|---|---|---|---|---|
| Row1 | CMP-STATUS[7:0] | Don't care | Don't care | |
| Row2 | DAC-2-DATA[15:8] | Don't care | DAC-0-DATA[15:8] | DAC-1-DATA[15:8] |
---table end---
The data captured in the NVM after the fault dump can be read in a specific sequence. Steps are provided in the subsequent sections.

# 6.4.5 Application-Specific Modes
This section provides the details of application-specific functional modes available in the DAC53xAxW.

# 6.4.5.1 Voltage Margining and Scaling
Voltage margining or scaling is a primary application for the DAC53xAxW. This section provides specific features available for this application such as Hi-Z output, slew-rate control, and PROTECT input.

# 6.4.5.1.1 High-Impedance Output and PROTECT Input
All the DAC output channels remain in a Hi-Z when VDD is off. Specific details are availaible in subsequent sections of the document.
Table 6-8 shows how the GPIO/SDO pin of the DAC53xAxW can be configured as a PROTECT function. PROTECT takes the DAC outputs to a predictable state with a slewed or direct transition. This function is useful in systems where a fault condition (such as a brownout), a subsystem failure, or a software crash requires that the DAC outputs reach a predefined state without the involvement of a processor. The detected event can be fed to the GPIO/SDO pin that is configured as the PROTECT.# 6.4.5 DAC Power Up and Power Down
Up and power down of the DAC without impacting the feedback loop of the DC/DC converter or the linear regulator.
---table begin---
Table tile: Table 6-8. GPIO/SDO pin configuration for DAC53xAxW
| PROTECT-CONFIG FIELD | FUNCTION |
|---|---|
| 00 | Switch to Hi-Z power-down (no slew) |
| 01 | Switch to DAC code stored in NVM (no slew) and then switch to Hi-Z power-down |
| 10 | Slew to margin-low code and then switch to Hi-Z power-down |
| 11 | Slew to margin-high code and then switch to Hi-Z power-down |
---table end---
The PROTECT function takes the DAC outputs to a predictable state with a slewed or direct transition. This function is useful in systems where a fault condition (such as a brownout), a subsystem failure, or a software crash requires that the DAC outputs reach a predefined state without the involvement of a processor. The detected event can be fed to the GPIO/SDO pin that is configured as the PROTECT input. The PROTECT function can also be triggered using the PROTECT bit in the COMMON-TRIGGER register.  

# 6.4.5.1 PROTECT Function
After the PROTECT function is triggered, the write functionality is disabled on the communication interface until the function is completed.
The PROTECT-FLAG bit in the CMP-STATUS register is set to 1 when the PROTECT function is triggered. This bit can be polled by reading the CMP-STATUS register. After the PROTECT function is complete, a read command on the CMP-STATUS register resets the PROTECT-FLAG bit.

# 6.4.5.1.1 Configuring PROTECT function
---table begin---
Table tile: Table 6-4. PROTECT Function Configuration
| FUNCTION | PROTECT-CONFIG FIELD |
|---|---|
| Switch to Hi-Z power-down (no slew) | 00 |
| Switch to DAC code stored in NVM (no slew) and then switch to Hi-Z power-down | 01 |
| Slew to margin-low code and then switch to Hi-Z power-down | 10 |
| Slew to margin-high code and then switch to Hi-Z power-down | 11 |
---table end---

# 6.4.5.1.2 Programmable Slew-Rate Control
When the DAC data registers are written, the voltage (VOUTX) or current (IOUT) on DAC output immediately transitions to the new code following the slew rate and settling time specified in the Electrical Characteristics.
The slew rate control feature allows the user to control the rate at which the output voltage (VOUT) changes. When this feature is enabled (using the SLEW-RATE-x[3:0] bits), the DAC output changes from the current code to the code in the DAC-x-MARGIN-HIGH or DAC-x-MARGIN-LOW registers (when margin high or low commands are issued to the DAC) using the step size and time-period per step set in CODE-STEP-x and SLEW-RATE-x bits in the DAC-x-FUNC-CONFIG register:
- SLEW-RATE-x defines the time-period per step at which the digital slew updates.
- CODE-STEP-x defines the number of LSBs by which the output value changes at each update, for the corresponding channels.

# 6.4.5.1.3 Settings for Slew-Rate Control
---table begin---
Table tile: Table 6-6. SLEW-RATE-x Settings
| SLEW-RATE-x | Time-Period per Step |
|---|---|
| 00 | Fast |
| 01 | Medium |
| 10 | Slow |
| 11 | Very Slow |
---table end---
# 6.4.5.1.3 Settings for Slew-Rate Control
Table 6-5 and Table 6-6 show different settings available for CODE-STEP-x and SLEW-RATE-x. With the default slew rate control setting of no-slew, the output changes immediately at a rate limited by the output drive circuitry and the attached load.
When the slew rate control feature is used, the output changes happen at the programmed slew rate. Figure 6-9 shows that this configuration results in a staircase formation at the output. Do not write to CODE-STEP-x, SLEW-RATE-x, or DAC-x-DATA during the output slew operation. Equation 4 provides the equation for the calculating the slew time (tSLEW).

# 6.4.5.1.4 Programmable Slew-Rate Control Calculation
---table begin---
Table title: Slew Rate
| REGISTER | SLEW-RATE-x[3] | SLEW-RATE-x[2] | SLEW-RATE-x[1] | SLEW-RATE-x[0] | TIME PERIOD (PER STEP) |
|---|---|---|---|---|---|
| DAC-x-FUNC-CONFIG | 0 | 0 | 0 | 0 | No slew (default) |
| DAC-x-FUNC-CONFIG | 0 | 0 | 0 | 1 | 4 µs |
| DAC-x-FUNC-CONFIG | 0 | 0 | 1 | 0 | 8 µs |
| DAC-x-FUNC-CONFIG | 0 | 0 | 1 | 1 | 12 µs |
| DAC-x-FUNC-CONFIG | 0 | 1 | 0 | 0 | 18 µs |
| DAC-x-FUNC-CONFIG | 0 | 1 | 0 | 1 | 27 µs |
| DAC-x-FUNC-CONFIG | 0 | 1 | 1 | 0 | 40.5 µs |
| DAC-x-FUNC-CONFIG | 0 | 1 | 1 | 1 | 60.75 µs |
| DAC-x-FUNC-CONFIG | 1 | 0 | 0 | 0 | 91.13 µs |
| DAC-x-FUNC-CONFIG | 1 | 0 | 0 | 1 | 136.69 µs |
| DAC-x-FUNC-CONFIG | 1 | 0 | 1 | 0 | 239.2 µs |
| DAC-x-FUNC-CONFIG | 1 | 0 | 1 | 1 | 418.61 µs |
| DAC-x-FUNC-CONFIG | 1 | 1 | 0 | 0 | 732.56 µs |
| DAC-x-FUNC-CONFIG | 1 | 1 | 0 | 1 | 1281.98 µs |
| DAC-x-FUNC-CONFIG | 1 | 1 | 1 | 0 | 2563.96 µs |
| DAC-x-FUNC-CONFIG | 1 | 1 | 1 | 1 | 5127.92 µs |
---table end---
# 6.4.5.1.4 Programmable Slew-Rate Control Calculation

# 6.4.5.2 Function Generation
The DAC53xAxW implement a continuous function or waveform generation feature. These devices can generate a triangular wave, sawtooth wave, and sine wave independently for every channel.

# 6.4.5.2.1 Triangular Waveform Generation
Figure 6-10 shows that the triangular waveform uses the DAC-x-MARGIN-LOW (FUNCTION-MIN) and DAC-x-MARGIN-HIGH (FUNCTION-MAX) registers for minimum and maximum levels, respectively. The frequency of the waveform depends on the min and max levels, CODE-STEP and SLEW-RATE settings as shown in Equation 5. An external RC load with a time-constant larger than the slew-rate settings can be dominant over the internal frequency calculation. The CODE-STEP-x and SLEW-RATE-x settings are available in the DAC-x-FUNC-CONFIG register. Writing 0b000 to the FUNC-CONFIG-x bit field in the DAC-x-FUNC-CONFIG register selects triangular waveform.
fTRIANGLE = 1 / (2 × TIME_STEP × CEILING (FUNCTION_MAX − FUNCTION_MIN) / CODE_STEP)
where
- TIME_STEP is the SLEW-RATE-x setting specified in Table 6-6.
- CODE_STEP is the CODE-STEP-x setting specified in Table 6-5.
- FUNCTION_MAX is the decimal value of DAC-x-MARGIN-HIGH bits in the DAC-x-MARGIN-HIGH register.
- FUNCTION_MIN is the decimal value of the DAC-x-MARGIN-LOW bits in the DAC-x-MARGIN-LOW register.

# 6.4.5.2.2 Sawtooth Waveform Generation
Figure 6-11 shows the sawtooth and the inverse sawtooth waveforms use the DAC-x-MARGIN-LOW (FUNCTION-MIN) and DAC-x-MARGIN-HIGH (FUNCTION-MAX) registers for minimum and maximum levels, respectively. The frequency of the waveform depends on the min and max levels, CODE-STEP and SLEW-RATE settings as shown in Equation 6. An external RC load with a time constant larger than the slew-rate settings can be dominant over the internal frequency calculation. The CODE-STEP-x and SLEW-RATE-x settings are available in the DAC-x-FUNC-CONFIG register. Write 0b001 to the FUNC-CONFIG-x bit field in the DAC-x-FUNC-CONFIG register to select sawtooth waveform, and write 0b010 to select inverse sawtooth waveform.
fSAWTOOTH = 1 / (TIME_STEP × CEILING (FUNCTION_MAX − FUNCTION_MIN) / CODE_STEP + 1)
where
- TIME_STEP is the SLEW-RATE-x setting specified in Table 6-6.
- CODE_STEP is the CODE-STEP-x setting specified in Table 6-5.
- FUNCTION_MAX# 6.4.5.2.2 Sawtooth and Inverse Sawtooth Waveform 
RC load with a time constant larger than the slew-rate settings can be dominant over the internal frequency calculation. The CODE-STEP-x and SLEW-RATE-x settings are available in the DAC-x-FUNC-CONFIG register. Write 0b001 to the FUNC-CONFIG-x bit field in the DAC-x-FUNC-CONFIG register to select sawtooth waveform, and write 0b010 to select inverse sawtooth waveform.
fSAWTOOTH = 1 / (TIME_STEP × CEILING (FUNCTION_MAX − FUNCTION_MIN) / CODE_STEP + 1)
where
- TIME_STEP is the SLEW-RATE-x setting specified in Table 6-6.
- CODE_STEP is the CODE-STEP-x setting specified in Table 6-5.
- FUNCTION_MAX
---table begin---
Table tile: Sawtooth Waveform Table
| Parameter | Description |
|---|---|
| TIME_STEP | The SLEW-RATE-x setting specified in Table 6-6. |
| CODE_STEP | The CODE-STEP-x setting specified in Table 6-5. |
| FUNCTION_MAX | is the decimal value of the DAC-x-MARGIN-HIGH bits in the DAC-x-MARGIN-HIGH register. |
| FUNCTION_MIN | is the decimal value of the DAC-x-MARGIN-LOW bits in the DAC-x-MARGIN-LOW register.|
---table end---

# 6.4.5.2.3 Sine Waveform Generation
The sine wave function uses 24 preprogrammed points per cycle. The frequency of the sine wave depends on the SLEW-RATE settings as shown in Equation 7:
fSINE_WAVE = 1 / (24 × SLEW_RATE) (7) 
where SLEW_RATE is the SLEW-RATE-x setting as specified in Table 6-6.
An external RC load with a time constant larger than the slew-rate settings can be dominant over the internal frequency calculation. The SLEW-RATE-x setting is available in the DAC-x-FUNC-CONFIG register. Writing 0b100 to the FUNC-CONFIG-x bit field in the DAC-x-FUNC-CONFIG register selects sine wave. The codes for the sine wave are fixed. Use the gain settings at the output amplifier for changing the full-scale output using the internal reference option. The gain settings are accessible through the DAC-GAIN-0, DAC-GAIN-1, and IOUT-GAIN bits in the DAC-0-GAIN-CONFIG, DAC-1-GAIN-CMP-CONFIG, and DAC-2-GAIN-CONFIG registers, respectively. 
---table begin---
Table tile: Sine Wave Data Points
| SEQUENCE | 12-BIT VALUE |
|---|---|
| 0 (0° phase start) | 0x800 |
| 1 | 0x9A8 |
| 2 | 0xB33 |
| 3 | 0xC87 |
| 4 | 0xD8B |
| 5 | 0xE2F |
| 6 (90° phase start) | 0xE66 |
| 7 | 0xE2F |
| 8 (120° phase start) | 0xD8B |
| 9 | 0xC87 |
| 10 | 0xB33 |
| 11 | 0x9A8 |
| 12 | 0x800 |
| 13 | 0x658 |
| 14 | 0x4CD |
| 15 | 0x379 |
| 16 (240° phase start) | 0x275 |
| 17 | 0x1D1 |
| 18 | 0x19A |
| 19 | 0x1D1 |
| 20 | 0x275 |
| 21 | 0x379 |
| 22 | 0x4CD |
| 23 | 0x658 |
---table end---

# 6.4.6 Device Reset and Fault Management
This section provides the details of power-on-reset (POR), software reset, and other diagnostics and fault-management features of DAC53xAxW.

# 6.4.6.1 Power-On Reset (POR)
The DAC53xAxW family of devices includes a power-on reset (POR) function that controls the output voltage at power up. After the VDD supply has been established, a POR event is issued. The POR causes all registers to initialize to default values, and communication with the device is valid only after a POR (boot-up) delay. The default value for all the registers in the DAC53xAxW is loaded from NVM as soon as the POR event is issued. When the device powers up, a POR circuit sets the device to the default mode. To ensure that a POR occurs, VDD must be less than 0.7 V for at least 1 ms. When VDD drops to less than 1.65 V, but remains greater than 0.7 V, a POR does not occur.# 6. Power On Reset (POR)
The "Power On Reset" (POR) is a critical event that controls the output voltage at power up. After the VDD supply has been established, a POR event is issued. The POR causes all registers to initialize to default values, and communication with the device is valid only after a POR (boot-up) delay. The default value for all the registers in the DAC53xAxW is loaded from NVM as soon as the POR event is issued. When the device powers up, a POR circuit sets the device to the default mode.

# 7. Using the POR Circuit
Figure 6-13 indicates that the POR circuit requires specific VDD levels to make sure that the internal capacitors discharge and reset the device at power up. To make sure that a POR occurs, VDD must be less than 0.7 V for at least 1 ms. When VDD drops to less than 1.65 V, but remains greater than 0.7 V (shown as the undefined region), the device may or may not reset under all specified temperature and power-supply conditions. In this case, initiate a POR. When VDD remains greater than 1.65 V, a POR does not occur.

# Table
---table begin---
Table title: NVM CRC Alarm Bits
| Alarm Bit | Description |
|---|---|
| NVM-CRC-FAIL-USER | Indicates the status of user-programmable NVM bits |
| NVM-CRC-FAIL-INT | Indicates the status of internal NVM bits |
---table end---

# 8. External Reset
An external reset to the device can be triggered through the GPIO/SDO pin or through the register map. To initiate a device software reset event, write the reserved code 1010b to the RESET field in the COMMON-TRIGGER register. A software reset initiates a POR event. 

# 9. Register-Map Lock
The DAC53xAxW implement a register-map lock feature that prevents an accidental or unintended write to the DAC registers. The device locks all the registers when the DEV-LOCK bit in the COMMON-CONFIG register is set to 1. However, the software reset function through the COMMON-TRIGGER register is not blocked when using the I2C interface. To bypass the DEV-LOCK setting, write 0101b to the DEV-UNLOCK bits in the COMMON-TRIGGER register.

# 10. NVM Cyclic Redundancy Check (CRC)
The DAC53xAxW implement a cyclic redundancy check (CRC) feature for the NVM to make sure that the data stored in the NVM is uncorrupted. There are two types of CRC alarm bits implemented in DAC53xAxW:
- NVM-CRC-FAIL-USER
- NVM-CRC-FAIL-INT
The NVM-CRC-FAIL-USER bit indicates the status of user-programmable NVM bits, and the NVM-CRC-FAIL-INT bit indicates the status of internal NVM bits. The CRC feature is implemented by storing a 16-bit CRC (CRC-16-CCITT) along with the NVM data each time NVM program operation (write or reload) is performed and during the device start up.

# 11. NVM-CRC-FAIL-USER Bit
A logic 1 on NVM-CRC-FAIL-USER bit indicates that the user-programmable NVM data is corrupt. During this condition, all registers in the DAC are initialized with factory reset values, and any DAC registers can be written to or read from. To reset the alarm bits to 0, issue a software reset (see also Section 6.4.6.2) command, or cycle power to the DAC. A software reset or power-cycle also reloads the user-programmable NVM bits. In case the failure persists, reprogram the NVM.

# 12. NVM-CRC-FAIL-INT Bit
A logic 1 on NVM-CRC-FAIL-INT bit indicate...# 6.4.6.4.1. NVM-CRC-FAIL-USER Bit
A logic 1 on NVM-CRC-FAIL-USER bit indicates that the user-programmable NVM data are corrupt. During this condition, all registers in the DAC are initialized with factory reset values, and any DAC registers can be written to or read from. To reset the alarm bits to 0, issue a software reset (see also Section 6.4.6.2) command, or cycle power to the DAC. A software reset or power-cycle also reloads the user-programmable NVM bits. In case the failure persists, reprogram the NVM.

# 6.4.6.4.2. NVM-CRC-FAIL-INT Bit
A logic 1 on NVM-CRC-FAIL-INT bit indicates that the internal NVM data are corrupt. During this condition, all registers in the DAC are initialized with factory reset values, and any DAC registers can be written to or read from. In case of a temporary failure, to reset the alarm bits to 0, issue a software reset (see also Section 6.4.6.2) command or cycle power to the DAC. A permanent failure in the NVM makes the device unusable.

# 6.4.7. General-Purpose Input/Output (GPIO) Modes
Together with I2C and SPI, the DAC53xAxW also support a GPIO that can be configured in the NVM for multiple functions. This pin allows for updating the DAC output channels and reading status bits without using the programming interface, thus enabling processor-less operation. In the GPIO-CONFIG register, write 1 to the GPI-EN bit to set the GPIO/SDO pin as an input, or write 1 to the GPO-EN bit to set the pin as output. There are global and channel-specific functions mapped to the GPIO/SDO pin. For channel-specific functions, select the channels using the GPI-CH-SEL field in the GPIO-CONFIG register.
Note:
Pull the GPIO/SDO pin high or low when not used. When the GPIO/SDO pin is used as RESET, the configuration must be programmed into the NVM. Otherwise, the setting is cleared after the device resets.
---table begin---
Table tile: General Purpose Input Function Map
| REGISTER | BIT FIELD | VALUE | CHANNELS | GPIO EDGE / LEVEL | FUNCTION |
|---|---|---|---|---|---|
| GPIO-CONFIG | GPI-CONFIG | 0000 | All | Falling edge | Trigger DEEP-SLEEP mode. |
|  |  |  |  | Rising edge | Bring the device out of deep-sleep. |
|  |  | 0010 | All | Falling edge | Trigger FAULT-DUMP |
|  |  |  |  | Rising edge | No effect |
|  |  | 0100 | As per GPI-CH-SEL | Falling edge | Channel power-down. Pulldown resistor as per the DAC-PDN-x setting |
|  |  |  |  | Rising edge | Channel power-up |
|  |  | 0101 | All | Falling edge | Trigger PROTECT function |
|  |  |  |  | Rising edge | No effect |
|  |  | 0111 | All | Falling edge | Trigger CLR function |
|  |  |  |  | Rising edge | No effect |
|  |  | 1000 | As per GPI-CH-SEL, both the SYNC-CONFIG-X and the GPI-CH-SEL must be configured for every channel. | Falling edge | Trigger LDAC function |
|  |  |  |  | Rising edge | No effect |
|  |  | 1001 | As per GPI-CH-SEL | Falling edge | Stop function generation |
|  |  |  |  | Rising edge | Start function generation |
|  |  | 1010 | As per GPI-CH-SEL | Falling edge | Trigger margin-low |
|  |  |  |  | Rising edge | Trigger margin-high |
|  |  | 1011 | All | Low pulse | Trigger device RESET |
---table end---# 6.5 Programming
The DAC53xAxW are programmed through either a 3-wire SPI or 2-wire I2C interface. A 4-wire SPI mode is 
enabled by mapping the GPIO/SDO pin as SDO. The SPI readback operates at a lower SCLK than the standard 
SPI write operation. The type of interface is determined based on the first protocol to communicate after device 
power up. After the interface type is determined, the device ignores any change in the type while the device is 
on. The interface type can be changed after a power cycle.

# 6.5.1 SPI Programming Mode
An SPI access cycle for DAC53xAxW is initiated by asserting the SYNC pin low. The serial clock, SCLK, can 
be a continuous or gated clock. SDI data are clocked on SCLK falling edges. The SPI frame for DAC53xAxW 
is 24 bits long. Therefore, the SYNC pin must stay low for at least 24 SCLK falling edges. The access cycle 
ends when the SYNC pin is deasserted high. If the access cycle contains less than the minimum clock edges, 
the communication is ignored. By default, the SDO function is not enabled (three-wire SPI). In the three-wire 
SPI mode, if the access cycle contains more than the minimum clock edges, only the first 24 bits are used by 
the device. When SYNC is high, the SCLK and SDI signals are blocked, and SDO becomes Hi-Z to allow data 
readback from other devices connected on the bus.
---table begin---
Table title: SPI Read/Write Access Cycle
| BIT   | FIELD    | DESCRIPTION                                                                                       |
|-------|----------|---------------------------------------------------------------------------------------------------|
| 23    | R/W      | Identifies the communication as a read or write command to the address register: R/W = 0 sets a write operation. R/W = 1 sets a read operation |
| 22-16 | A[6:0]   | Register address: specifies the register to be accessed during the read or write operation      |
| 15-0  | DI[15:0] | Data cycle bits: If a write command, the data cycle bits are the values to be written to the register with address A[6:0]. If a read command, the data cycle bits are don't care values.|
---table end---
Figure 6-14. SPI Write Cycle
Read operations require that the SDO function is first enabled by setting the SD

# 1. SPI Write Cycle
Write operations require that the SDO function is first enabled by setting the SDO-EN bit in the INTERFACE-CONFIG register. This configuration is called four-wire SPI. A write operation is initiated by issuing a write command access cycle. After the read command, a second access cycle must be issued to get the requested data.
---table begin---
Table 6-10: Write Operation command
| BIT | FIELD | DESCRIPTION |
|---|---|---|
| 23 | R/W | Identifies the communication as a read or write command to the address register: R/W = 0 sets a write operation. R/W = 1 sets a read operation |
| 22-16 | A[6:0]   | Register address: specifies the register to be accessed during the read or write operation      |
| 15-0  | DI[15:0] | Data cycle bits: If a write command, the data cycle bits are the values to be written to the register with address A[6:0]. If a read command, the data cycle bits are don't care values.|
---table end---

# 2. SDO Output Access Cycle
Read operations require that the SDO function is first enabled by setting the SDO-EN bit in the INTERFACE-CONFIG register.
---table begin---
Table 6-11: Echo Echo R/W from previous access cycle
| BIT | FIELD | DESCRIPTION |
|---|---|---|
| 23 | R/W | Echo R/W from previous access cycle |
| 22-16 | A[6:0] | Echo register address from previous access cycle |
| 15 | DI[15:0] | Readback data requested on previous access cycle |
---table end---

# 3. SPI Daisy-Chain Connection
The daisy-chain operation is also enabled with the SDO pin. Figure 6-16 shows that in daisy-chain mode, multiple devices are connected in a chain with the SDO pin of one device is connected to SDI pin of the following device. The SPI host drives the SDI pin of the first device in the chain.

# 4. I2C Programming Mode
The DAC53xAxW devices have a 2-wire serial interface (SCL and SDA), and one address pin (A0); see also the pin diagram in the Pin Configuration and Functions section. The I2C bus consists of a data line (SDA) and a clock line (SCL) with pullup structures. When the bus is idle, both SDA and SCL lines are pulled high. All the I2C-compatible devices connect to the I2C bus through the open drain I/O pins, SDA and SCL.
The I2C specification states that the device that controls communication is called a controller, and the devices that are controlled by the controller are called targets. The controller generates the SCL signal. The controller also generates special timing conditions (start condition, repeated start condition, and stop condition) on the bus to indicate the start or stop of a data transfer. Device addressing is completed by the controller. The controller on an I2C bus is typically a microcontroller or digital signal processor (DSP). The DAC53xAxW family operates as a target on the I2C bus. A target ac# 1. 
The device that controls communication is called a controller, and the devices that are controlled by the controller are called targets. The controller generates the SCL signal. The controller also generates special timing conditions (start condition, repeated start condition, and stop condition) on the bus to indicate the start or stop of a data transfer. Device addressing is completed by the controller. The controller on an I2C bus is typically a microcontroller or digital signal processor (DSP). The DAC53xAxW family operates as a target on the I2C bus. A target acknowledges controller commands, and upon controller control, receives or transmits data.

# 2. 
Typically, the DAC53xAxW family operates as a target receiver. A controller writes to the DAC53xAxW, a target receiver. However, if a controller requires the DAC53xAxW internal register data, the DAC53xAxW operate as a target transmitter. In this case, the controller reads from the DAC53xAxW. According to I2C terminology, read and write refer to the controller.

# 3.
The DAC53xAxW family supports the following data transfer modes:
• Standard mode (100kbps)
• Fast mode (400kbps)
• Fast mode plus (1.0Mbps)

# 4.
The data transfer protocol for standard and fast modes is exactly the same; therefore, both modes are referred to as F/S-mode in this document. The fast mode plus protocol is supported in terms of data transfer speed, but not output current. The low-level output current is 3 mA; similar to the case of standard and fast modes. 

# 5. 
The DAC53xAxW family supports 7-bit addressing. The 10-bit addressing mode is not supported. The device supports the general call reset function. Sending the following sequence initiates a software reset within the device: start or repeated start, 0x00, 0x06, stop. The reset is asserted within the device on the rising edge of the ACK bit, following the second byte.

# 6. 
Other than specific timing signals, the I2C interface works with serial bytes. At the end of each byte, a ninth clock cycle generates and detects an acknowledge signal. An acknowledge is when the SDA line is pulled low during the high period of the ninth clock cycle.

# 7. Fundamentals of Data Transfer
1. The controller initiates data transfer by generating a start condition. All I2C-compatible devices recognize a start condition.
2. The controller then generates the SCL pulses, and transmits the 7-bit address and the read/write direction bit (R/W) on the SDA line. During all transmissions, the controller makes sure that data are valid. All devices recognize the address sent by the controller and compare the address to the respective internal fixed address. Only the target device with a matching address generates an acknowledge by pulling the SDA line low during the entire high period of the 9th SCL cycle. When the controller detects this acknowledge, the communication link with a target has been established.

# 3. 
The controller generates further SCL cycles to transmit (R/W bit 0) or receive (R/W bit 1) data to the target. In either case, the receiver must acknowledge the data sent by the transmitter. The acknowledge signal can be generated by the controller or by the target, depending on which is the receiver. The 9-bit valid data sequences consists of eight data bits and one acknowledge-bit, and can continue as long as necessary.

# 4. 
Figure 6-19 shows that to signal the end of the data transfer, the controller generates a stop condition by pulling the SDA line from low-to-high while the SCL line is high. This action releases the bus and stops the communication link with the addressed target. All I2C-compatible devices recognize the stop condition. Upon receipt of a stop condition, the bus is released, and all target devices then wait for a start condition followed by a matching address.

# 6.5.2.2 I2C Update Sequence
Table 6-12 shows that for a single update, the DAC53xAxW require a start condition, a valid I2C address byte, a command byte, and two data bytes.
---table begin---
Table tile: Update Sequence
| | |
|---|---|
| MSB | ... |
| LSB | ACK |
| MSB | ... |
| LSB | ACK |
| MSB | ... |
| LSB | ACK |
| MSB | ... |
| LSB | ACK |
---table end---

# 6.5.2.2.1 Address Byte
Table 6-13 depicts the address byte, the first byte received from the controller device following the start condition. The first four bits (MSBs) of the# 6.5.2.2.1 Address Byte
The first byte received from the controller device following the start condition is the address byte. The first four bits (MSBs) of the address are factory preset to 1001b. The next three bits of the address are controlled by the A0 pin. The A0 pin input can be connected to VDD, AGND, SCL, or SDA. The A0 pin is sampled during the first byte of each data frame to determine the address. The device latches the value of the address pin, and consequently responds to that particular address.
---table begin---
Table tile: Address Byte (Table 6-13)
| COMMENT | MSB | LSB |
|---|---|---|
| General address | 1 0 0 1 | See Table 6-14 (target address column) 0 or 1 |
| Broadcast address | 1 0 0 0 | 1 1 1 0 |
---table end---

# 6.5.2.3 I2C Read Sequence
To read any register the following command sequence must be used:
1. Send a start or repeated start command with a target address and the R/W bit set to 0 for writing. The device acknowledges this event.
2. Send a command byte for the register to be read. The device acknowledges this event again.
3. Send a repeated start with the target address and the R/W bit set to 1 for reading. The device acknowledges this event.
4. The device writes the MSDB byte of the addressed register. The controller must acknowledge this byte.
5. Finally, the device writes out the LSDB of the register.
The broadcast address cannot be used for reading.
---table begin---
Table tile: Read Sequence (Table 6-15)
| S | MSB | … | R/W (0) | ACK | MSB | … | LSB | ACK | Sr | MSB | … | R/W (1) | ACK | MSB | … | LSB | ACK | MSB | … | LSB | ACK |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | Address byte | Section 6.5.2.2.1 | Command byte | Section 6.5.2.2.2 | Sr | Address byte | Section 6.5.2.2.1 | MSDB | LSDB | From controller | Target | From controller | Target | From controller | Target | From target | Controller | From target | Controller |
---table end---

# 7 Register Map
# 1. Table 7.2. Register Map: Common Registers
---table begin---
Table tile: Register Map
| REGISTER(1) (2) | MOST SIGNIFICANT DATA BYTE (MSDB) | LEAST SIGNIFICANT DATA BYTE (LSDB) |
|---|---|---|
| COMMON-CONFIG | WIN-LATCH-EN | DEV-LOCK |
| EE-READ-ADDR | EN-INT-REF | DAC-PDN-1 |
| RESERVED | DAC-PDN-0 | RESERVED |
| DAC-PDN-2 | RESERVED | COMMON-TRIGGER |
| DEV-UNLOCK | RESET | LDAC |
| CLR | X | FAULT-DUMP |
| PROTECT | READ-ONE-TRIG | NVM-PROG |
| NVM-RELOAD | COMMON-DAC-TRIG | X |
| TRIG-MAR-LO-2 | TRIG-MAR-HI-2 | START-FUNC-2 |
| X | TRIG-MAR-LO-0 | TRIG-MAR-HI-0 |
| START-FUNC-0 | RESET-CMP-FLAG-1 | TRIG-MAR-LO-1 |
| TRIG-MAR-HI-1 | START-FUNC-1 | GENERAL-STATUS |
| NVM-CRC-FAIL-INT | NVM-CRC-FAIL-USER | X |
| DAC-BUSY-1 | DAC-BUSY-0 | X |
| DAC-BUSY-2 | NVM-BUSY | DEVICE-ID |
| VERSION-ID | CMP-STATUS | X |
| PROTECT-FLAG | WIN-CMP-1 | X |
| CMP-FLAG-1 | X | GPIO-CONFIG |
| GF-EN | X | GPO-EN |
| GPO-CONFIG | GPI-CH-SEL | GPI-CONFIG |
| GPI-EN | DEVICE-MODE-CONFIG | RESERVED |
| PROTECT-CONFIG | RESERVED | X |
| INTERFACE-CONFIG | X | TIMEOUT-EN |
| X | RESERVED | X |
| FSDO-EN | X | SDO-EN |
| SRAM-CONFIG | X | SRAM-ADDR |
| SRAM-DATA | SRAM-DATA | BRDCAST-DATA |
| BRDCAST-DATA | X |
---table end---
# 7 Register Map
(1) The highlighted gray cells indicate the register bits or fields that are stored in the NVM.
(2) X = Don't care.

# 2. Table 7.3. Register Names
---table begin---
Table tile: Register Names
| I2C/SPI ADDRESS | REGISTER NAME | SECTION |
|---|---|---|
| 00h | NOP | Section 7.1 |
| 01h | DAC-2-MARGIN-HIGH | Section 7.4 |
| 02h | DAC-2-MARGIN-LOW | Section 7.7 |
| 03h | DAC-2-GAIN-CONFIG | Section 7.10 |
| 06h | DAC-2-FUNC-CONFIG | Section 7.14 |
| 0Dh | DAC-0-MARGIN-HIGH | Section 7.2 |
| 0Eh | DAC-0-MARGIN-LOW | Section 7.6 |
| 0Fh | DAC-0-GAIN-CONFIG | Section 7.8 |
| 12h | DAC-0-FUNC-CONFIG | Section 7.12 |
| 13h | DAC-1-MARGIN-HIGH | Section 7.3 |
| 14h | DAC-1-MARGIN-LOW | Section 7.6 |
| 15h | DAC-1-GAIN-CMP-CONFIG | Section 7.9 |
| 17h | DAC-1-CMP-MODE-CONFIG | Section 7.11 |
| 18h | DAC-1-FUNC-CONFIG | Section 7.13 |
| 19h | DAC-2-DATA | Section 7.17 |
| 1Bh | DAC-0-DATA | Section 7.15 |
| 1Ch | DAC-1-DATA | Section 7.16 |
| 1Fh | COMMON-CONFIG | Section 7.18 |
| 20h | COMMON-TRIGGER | Section 7.19 |
| 21h | COMMON-DAC-TRIG | Section 7.20 |
| 22h | GENERAL-STATUS | Section 7.21 |
| 23h | CMP-STATUS | Section 7.22 |
| 24h | GPIO-CONFIG | Section 7.23 |
| 25h | DEVICE-MODE-CONFIG | Section 7.24 |
| 26h | INTERFACE-CONFIG | Section 7.25 |
| 2Bh | SRAM-CONFIG | Section 7.26 |
| 2Ch | SRAM-DATA | Section 7.27 |
| 50h | BRDCAST-DATA | Section 7.28 |
---table end---

# 3. Table 7.4. Access Type Codes
# 7.2. DAC-0-MARGIN-HIGH Register
---table begin---
Table tile: DAC-0-MARGIN-HIGH Register Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15-4 | DAC-0-MARGIN-HIGH[9:0] | R/W | 000h | Margin-high code for DAC channel 0 output. Data are in straight-binary format. MSB left aligned. Use the following bit alignment: DAC532A3W: {DAC-0-MARGIN-HIGH[9:0], X, X} X = Don't care bits. |
| 3-0 | X | X | 0h | Don't care |
---table end---
# 3. Table 7.4. Access Type Codes

# 7.3. DAC-1-MARGIN-HIGH Register
---table begin---
Table title: DAC-1-MARGIN-HIGH Register Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15-4 | DAC-1-MARGIN-HIGH[9:0] | R/W | 000h | Margin-high code for DAC channel 1 output. Data are in straight-binary format. MSB left aligned. Use the following bit alignment: DAC532A3W: {DAC-1-MARGIN-HIGH[9:0], X, X} X = Don't care bits. |
| 3-0 | X | X | 0h | Don't care |
---table end---

# 7.4. DAC-2-MARGIN-HIGH Register
And so on... For the other chapters.# 7.8 DAC-0-GAIN-CONFIG Register (address = 0Fh) [reset = 0000h]
---table begin---
Table 7-12. DAC-0-GAIN-CONFIG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15-13 | X | X | 0h | Don't care |
| 12-10 | REF-GAIN-0 | R/W | 0h | 001: Gain = 1 ×, VDD as reference. 010: Gain = 1.5 ×, internal reference. 011: Gain = 2 ×, internal reference. 100: Gain = 3 ×, internal reference. 101: Gain = 4 ×, internal reference. Others: Invalid. |
| 9-0 | X | X | 000h | Don't care |
---table end---
# 7.4. DAC-2-MARGIN-HIGH Register

# 7.9 DAC-1-GAIN-CMP-CONFIG Register (address = 15h) [reset = 0000h]
---table begin---
Table 7-13. DAC-1-GAIN-CMP-CONFIG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15-13 | X | X | 0h | Don't care |
| 12-10 | REF-GAIN-1 | R/W | 0h | 001: Gain = 1 ×, VDD as reference. 010: Gain = 1.5 ×, internal reference. 011: Gain = 2 ×, internal reference. 100: Gain = 3 ×, internal reference. 101: Gain = 4 ×, internal reference. Others: Invalid. |
...Append the rest of the tables as per this format...# 7.12 DAC-0-FUNC-CONFIG Register (address = 12h) [reset = 0000h]
---table begin---
| X | X | 000h | Don't care |
| --- | --- | --- | --- |
---table end---
# 7.9 DAC-1-GAIN-CMP-CONFIG Register (address = 15h) [reset = 0000h]

# 7.13 DAC-0-FUNC-CONFIG Register Field Descriptions
---table begin---
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15 | CLR-SEL-0 | R/W | 0h | 0: Clear DAC channel 0 to zero scale. 1: Clear DAC channel 0 to midscale. |
| 14 | SYNC-CONFIG-0 | R/W | 0h | 0: DAC channel 0 output updates immediately after a write command. 1: DAC channel 0 output updates with LDAC pin falling-edge or when the LDAC bit in the COMMON-TRIGGER register is set to 1. |
| 13 | BRD-CONFIG-0 | R/W | 0h | 0: Don't update DAC channel 0 with broadcast command. 1: Update DAC channel 0 with broadcast command. |
---table end---
NOTE: Many tables are abbreviated, continue to format other tables in a similar manner...

# 7.13 DAC-1-FUNC-CONFIG Register (address = 18h) [reset = 0000h]
---table begin---
| X | X | 000h | Don't care |
| --- | --- | --- | --- |
---table end---

# 7.14 DAC-1-FUNC-CONFIG Register Field Descriptions
# 7.14 DAC-2-FUNC-CONFIG Register (address = 06h) [reset = 0000h]
---table begin---
|   |   | 0h | Don't care |
|---|---|---|---|
---table end---
# 7.14 DAC-1-FUNC-CONFIG Register Field Descriptions

# 7.15 DAC-2-FUNC-CONFIG Register Field Descriptions
---table begin---
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15 | CLR-SEL-2 | R/W | 0h | 0: Clear DAC channel 2 to zero scale. 1: Clear DAC channel 2 to midscale. |
| 14 | SYNC-CONFIG-2 | R/W | 0h | 0: DAC channel 2 output updates immediately after a write |
---table end---

# 7.16 DAC-2-FUNC-CONFIG Register Field Detailed Descriptions
---table begin---
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15 | CLR-SEL-2 | R/W | 0h | 0: Clear DAC channel 2 to zero scale. 1: Clear DAC channel 2 to midscale. |
| 14 | SYNC-CONFIG-2 | R/W | 0h | 0: DAC channel 2 output updates immediately after a write |
---table end---

# 7.17 DAC-2-FUNC-CONFIG Register Full Descriptions
# 7.14 DAC-2-FUNC-CONFIG Register (address = 06h) [reset = 0000h]
---table begin---
Table title: DAC-2-FUNC-CONFIG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15 | CLR-SEL-2 | R/W | 0h | 0: Clear DAC channel 2 to zero scale. 1: Clear DAC channel 2 to midscale. |
| 14 | SYNC-CONFIG-2 | R/W | 0h | 0: DAC channel 2 output updates immediately after a write command. 1: DAC channel 2 output updates with LDAC pin falling-edge or when the LDAC bit in the COMMON-TRIGGER register is set to 1. |
| 13 | BRD-CONFIG-2 | R/W | 0h | 0: Don't update DAC channel 2 with broadcast command. 1: Update DAC channel 2 with broadcast command. |
---table end---
# 7.17 DAC-2-FUNC-CONFIG Register Full Descriptions

# 7.15 Linear-Slew Mode
---table begin---
Table title: FUNC-GEN-CONFIG-BLOCK-2 Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | ---- | --- |
| 12-11 | PHASE-SEL-2 | R/W | 0h | 00: 0° 01: 120° 10: 240° 11: 90° |
| 10-8 | FUNC-CONFIG-2 | R/W | 0h | 000: Triangular wave 001: Sawtooth wave 010: Inverse sawtooth wave 100: Sine wave 111: Disable function generation Others: Invalid |
| 7 | LOG-SLEW-EN-2 | R/W | 0h | 0: Enable linear slew |
| 6-4 | CODE-STEP-2 | R/W | 0h | CODE-STEP for linear slew mode: 000: 1-LSB 001: 2-LSB 010: 3-LSB 011: 4-LSB 100: 6-LSB 101: 8-LSB 110: 16-LSB 111: 32-LSB |
| 3-0 | SLEW-RATE-2 | R/W | 0h | SLEW-RATE for linear slew mode: 0000: No slew for margin-high and margin-low. Invalid for waveform generation. 0001: 4 µs/step 0010: 8 µs/step 0011: 12 µs/step 0100: 18 µs/step 0101: 27.04 µs/step 0110: 40.48 µs/step 0111: 60.72 µs/step 1000: 91.12 µs/step 1001: 136.72 µs/step 1010: 239.2 µs/step 1011: 418.64 µs/step 1100: 732.56 µs/step 1101: 1282 µs/step 1110: 2563.96 µs/step 1111: 5127.92 µs/step |
---table end---

# 7.16 Logarithmic Slew Mode
---table begin---
Table title: FUNC GEN CONFIG BLOCK 2 Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 12-11 | PHASE-SEL-2 | R/W | 0h | 00: 0° 01: 120° 10: 240° 11: 90° |
| 10-8 | FUNC-CONFIG-2 | R/W | 0h | 000: Triangular wave 001: Sawtooth wave 010: Inverse sawtooth wave 100: Sine wave 111: Disable function generation Others: Invalid |
| 7 | LOG-SLEW-EN-2 | R/W | 0h | 1: Enable logarithmic slew. In logarithmic slew mode, the DAC output moves from the DAC-2-MARGIN-LOW code to the DAC-2-MARGIN-HIGH code, or vice versa, in 3.125% steps. |
| 6-4 | RISE-SLEW-2 | R/W | 0h | SLEW-RATE for logarithmic slew mode (DAC-2-MARGIN-LOW to DAC-2-MARGIN-HIGH): 000: 4 µs/step 001: 12 µs/step 010: 27.04 µs/step 011: 60.72 µs/step 100: 136.72 µs/step 101: 418.64 µs/step 110: 1282 µs/step 111: 5127.92 µs/step |
| 3-1 | FALL-SLEW-2 | R/W | 0h | SLEW-RATE for logarithmic slew mode (DAC-2-MARGIN-HIGH to DAC-2-MARGIN-LOW): 000: 4 µs/step 001: 12 µs/step 010: 27.04 µs/step 011: 60.72 µs/step 100: 136.72 µs/step 101: 418.64 µs/step 110: 1282 µs/step 111: 5127.92 µs/step |
---table end---

# 7.17 DAC-0-DATA Register (address = 1Bh) [reset = 0000h]
---table begin---
Table title: DAC-0-DATA Register Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15-4 | DAC-0-DATA[9:0] | R/W | 000h | Data for DAC output. |

# 7.15 DAC-0-DATA Register (address = 1Bh) [reset = 0000h]
---table begin---
Table title: DAC-0-DATA Register Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15-4 | DAC-0-DATA[9:0] | R/W | 000h | Data for DAC output. |
| 3-0 | X | X | 0h | Don't care |
---table end---

# 7.16 DAC-1-DATA Register (address = 1Ch) [reset = 0000h]
---table begin---
Table title: DAC-1-DATA Register Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15-4 | DAC-1-DATA[9:0] | R/W | 000h | Data for DAC output. |
| 3-0 | X | X | 0h | Don't care |
---table end---

# 7.17 DAC-2-DATA Register (address = 19h) [reset = 0000h]
---table begin---
Table title: DAC-2-DATA Register Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15-4 | DAC-2-DATA[9:0] | R/W | 000h | Data for DAC output. |
| 3-0 | X | X | 0h | Don't care |
---table end---

# 7.18 COMMON-CONFIG Register (address = 1Fh) [reset = 0FFFh]
---table begin---
Table title: COMMON-CONFIG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
| --- | --- | --- | --- | --- |
| 15 | WIN-LATCH-EN | R/W | 0h | Non-latching window-comparator output. 1: Latching window-comparator output |
| 14 | DEV-LOCK | R/W | 0h | Device not locked 1: Device locked, the device locks all the registers. To set this bit back to 0 (unlock device), write to the unlock code to the DEV-UNLOCK field in the COMMON-TRIGGER register first, followed by a write to the DEV-LOCK bit as 0. |
| 13 | EE-READ-ADDR | R/W | 0h | Fault-dump read enable at address 0x00. 1: Fault-dump read enable at address 0x01. |
| 12 | EN-INT-REF | R/W | 0h | Disable internal reference. 1: Enable internal reference. This bit must be set before using internal reference gain settings. |
| 11-10 | DAC-PDN-1 | R/W | 3h | Power-up DAC channel 1. 01: Power-down DAC channel 1 with 10 kΩ to AGND. 10: Power-down DAC channel 1 with 100 kΩ to AGND. 11: Power-down DAC channel 1 with Hi-Z to AGND. |
| 9 | RESERVED | R/W | 1h | Always write 1h. |
| 8-7 | DAC-PDN-0 | R/W | 3h | Power-up DAC channel 0. 01: Power-down DAC channel 0 with 10 kΩ to AGND. 10: Power-down DAC channel 0 with 100 kΩ to AGND. 11: Power-down DAC channel 0 with Hi-Z to AGND. |
| 6-3 | RESERVED | R/W | Fh | Always write Fh. |
| 2-1 | DAC-PDN-2 | R/W | 3h | Power-up DAC channel 2. Others: Power-down DAC channel 2 with 1.2 kΩ to AGND. |
| 0 | RESERVED | R/W | 1h | Always write 1h. |
---table end---

# 7.19 COMMON-TRIGGER Register (address = 20h) [reset = 0000h]
# 7.20 COMMON-DAC-TRIG Register (address = 21h) [reset = 0000h]
---table begin---
Table Title: COMMON-DAC-TRIG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 14, 6, 2 | TRIG-MAR-LO-x | W | 0h | 0: Don't care 1: Trigger margin-low command. This bit self-resets |
| 13, 5, 1 | TRIG-MAR-HI-x | W | 0h | 0: Don't care 1: Trigger margin-high command. This bit self-resets |
| 12, 4, 0 | START-FUNC-x | R/W | 0h | 0: Stop function generation1: Start function generation as per FUNC-GEN-CONFIG-x in the DAC-x-FUNC-CONFIG register |
| 15, 11-7 | X | X | 00h | Don't care |
| 3 | RESET-CMP-FLAG-1 | W | 0h | Latching-comparator output unaffected 1: Reset latching-comparator and window-comparator output. This bit self-resets. |
---table end---
# 7.19 COMMON-TRIGGER Register (address = 20h) [reset = 0000h]

# 7.21 GENERAL-STATUS Register (address = 22h) [reset = 20h, DEVICE-ID, VERSION-ID]
# 1. GENERAL-STATUS Register Field Descriptions
---table begin---
Table tile: GENERAL-STATUS Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15 | NVM-CRC-FAIL-INT | R | 0h | 0: No CRC error in OTP.1: Indicates a failure in OTP loading. A software reset or power-cycle can bring the device out of this condition in case of temporary failure |
| 14 | NVM-CRC-FAIL-USER | R | 0h | 0: No CRC error in NVM loading1: Indicates a failure in NVM loading. The register settings are corrupted. The device allows all operations during this error condition. Reprogram the NVM to get original state. A software reset brings the device out of this temporary error condition |
| 13 | X | X | 1h | Don't care |
| 12 | DAC-1-BUSY | R | 0h | 0: DAC channel 1 can accept commands.1: DAC channel 1 does not accept commands. |
| 11 | DAC-0-BUSY | R | 0h | 0: DAC channel 0 can accept commands.1: DAC channel 0 does not accept commands. |
| 10 | X | X | 0h | Don't care |
| 9 | DAC-2-BUSY | R | 0h | 0: DAC channel 2 can accept commands.1: DAC channel 2 does not accept commands. |
| 8 | NVM-BUSY | R | 0h | 0: NVM is available for read and write.1: NVM is not available for read or write. |
| 7-2 | DEVICE-ID | R | DAC532A3W: 04h<br>DAC530A2W: 06h | Device identifier. |
| 1-0 | VERSION-ID | R | 00h | Version identifier. |
---table end---
# 7.21 GENERAL-STATUS Register (address = 22h) [reset = 20h, DEVICE-ID, VERSION-ID]

# 2. CMP-STATUS Register (address = 23h) [reset = 000Ch]
This section contains a description about the CMP-STATUS Register.
---table begin---
Table tile: CMP-STATUS Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15-9 | X | X | 0h | Don't care |
| 8 | PROTECT-FLAG | R | 0h | 0: PROTECT operation not triggered.1: PROTECT function is completed or in progress. This bit resets to 0 when read. |
| 7 | WIN-CMP-1 | R | 0h | Window comparator output from channel 1. The output is latched or unlatched based on the WINDOW-LATCH-EN setting in the COMMON-CONFIG register. |
| 6-4 | X | X | 0h | Don't care |
| 3 | CMP-FLAG-1 | R | 1h | Synchronized comparator output from channel 1. |
| 2-0 | X | X | 4h | Don't care |
---table end---

# 3. GPIO-CONFIG Register (address = 24h) [reset = 0000h]
# 7.24 DEVICE-MODE-CONFIG Register (address = 25h) [reset = 0000h]
Figure 7-24. DEVICE-MODE-CONFIG Register
---table begin---
Table tile: DEVICE-MODE-CONFIG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15-10 | RESERVED | R/W | 00h | Always write 00h. |
| 9-8 | PROTECT-CONFIG | R/W | 0h | 00: Switch to Hi-Z power-down (no slew) 01: Switch to DAC code stored in NVM (no slew) and then switch to Hi-Z power-down 10: Slew to margin-low code and then switch to Hi-Z power-down 11: Slew to margin-high code and then switch to Hi-Z power-down |
| 7-5 | RESERVED | R/W | 0h | Always write 0h. |
| 4-0 | X | X | 00h | Don't care |
---table end---
# 3. GPIO-CONFIG Register (address = 24h) [reset = 0000h]

# 7.25 INTERFACE-CONFIG Register (address = 26h) [reset = 0000h]
Figure 7-25. INTERFACE-CONFIG Register
---table begin---
Table title: INTERFACE-CONFIG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15-13 | X | X | 0h | Don't care |
| 12 | TIMEOUT-EN | R/W | 0h | 0: I2C timeout disabled 1: I2C timeout enabled |
| 11-9 | X | X | 0h | Don't care |
| 8 | RESERVED | R/W | 0h | Always write 0. |
| 7-3 | X | X | 00h | Don't care |
| 2 | FSDO-EN | R/W | 0h | 0: Fast SDO disabled 1: Fast SDO enabled |
| 1 | X | X | 0h | Don't care |
| 0 | SDO-EN | R/W | 0h | 0: SDO disabled 1: SDO enabled on GPIO/SDO pin |
---table end---

# 7.26 SRAM-CONFIG Register (address = 2Bh) [reset = 0000h]
# 7.26 SRAM-CONFIG Register (address = 2Bh) [reset = 0000h]
---table begin---
Table tile: SRAM-CONFIG Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15-8 | X | X | 00h | Don't care |
| 7-0 | SRAM-ADDR | R/W | 00h | 8-bit SRAM address. Writing to this register field configures the SRAM address to be accessed next. This address automatically increments after a write to the SRAM. |
---table end---
# 7.26 SRAM-CONFIG Register (address = 2Bh) [reset = 0000h]

# 7.27 SRAM-DATA Register (address = 2Ch) [reset = 0000h]
---table begin---
Table tile: SRAM-DATA Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15-0 | SRAM-DATA | R/W | 0000h | 16-bit SRAM data. This data is written to or read from the address configured in the SRAM-CONFIG register. |
---table end---

# 7.28 BRDCAST-DATA Register (address = 50h) [reset = 0000h]
---table begin---
Table tile: BRDCAST-DATA Register Field Descriptions
| Bit | Field | Type | Reset | Description |
|---|---|---|---|---|
| 15-4 | BRDCAST-DATA[9:0] | R/W | 000h | Broadcast code for all DAC channels. Data are in straight-binary format. MSB left-aligned. Use the following bit-alignment: DAC532A3W: {BROADCAST-DATA[9:0], X, X} X = Don't care bits. The BRD-CONFIG-X bit in the DAC-x-FUNC-CONFIG register must be enabled for the respective channels. |
| 3-0 | X | X | 0h | Don't care. |
---table end---

# 8 Application and Implementation
Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI’s customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

# 8.1 Application Information
The DAC53xAxW is a family of two- and three-channel, buffered, voltage-output and current-output smart DACs that include NVM and an internal reference, and is available in a 1.72-mm × 1.72-mm (nominal) package. The current output DAC (IDAC) can source up to 300-mA with low headroom. The voltage output DACs (VDACs) have configurable reference and gain options. The DAC53xAxW supports Hi-Z power-down mode and Hi-Z output during power-off conditions. The multi-function GPIO, function generation, NVM enable these smart DACs for use without the need for run-time software.

# 8.2 Typical Application
The DAC53xAxW can be used in camera auto-focus applications that feature voice coil motors (VCM). The lens of the camera is connected to the spring of the VCM which is controlled with a constant current. The DAC53xAxW is a low-power device which is an excellent feature for battery-powered applications that require low-power consumption. This example circuit uses the 300-mA IDAC output to source the VCM current and control the lens position. The DAC53xAxW features a flyback diode connected from the IDAC output to ground to protect the DAC53xAxW when connected to inductive loads. The second DAC channel is configured as a programmable comparator to monitor the VCM voltage (VVCM). The output of the programmable comparator is connected to the GPIO/SDO pin which sets the IDAC output to zero-scale if VVCM is greater than the programmed threshold. The DAC53xAxW has a # 1. Introduction
ery-powered applications that require low-power consumption. This example circuit uses the 300-mA IDAC output to source the VCM current and control the lens position. The DAC53xAxW features a flyback diode connected from the IDAC output to ground to protect the DAC53xAxW when connected to inductive loads. The second DAC channel is configured as a programmable comparator to monitor the VCM voltage (VVCM). The output of the programmable comparator is connected to the GPIO/SDO pin which sets the IDAC output to zero-scale if VVCM is greater than the programmed threshold. The DAC53xAxW has a programmable slew rate that can be used to gradually increase the current through the VCM to reduce ringing.

# 2. DAC530A2W Configurations
DAC530A2W
VDD
IDAC
NVM
Internal 
Reference
LDO
Output Configuration
Logic
CAP
AGND
SDA/SCLK
SCL/SYNC
A0/SDI
GPIO/SDO
1.5 �F
100 nF
VOUT
LOW
HIGH
VDD
Digital Interface
BUFFER
BUFFER
PVDD
PGND
FB
VOICE 
COIL 
MOTOR
VVCM

# 3. Design Requirements and Parameters
---table begin---
Table title: Design Parameters
| PARAMETER | VALUE |
|---|---|
| VDD | 3.3 V |
| PVDD | 3.3 V |
| IDAC nominal output | 120 mA |
| Programmable comparator threshold | 1 V |
---table end---

# 4. Detailed Design Procedure
8.2.2 Detailed Design Procedure
The full-scale IDAC output range is 350 mA. The nominal IDAC output for this application is 120 mA. The IDAC code required to set the IDAC output to 120 mA is calculated by Equation 8.
DAC_2_DATA = 120mA 2 3 * 0.5241 * 210 = 352d (8)
The IDAC uses the internal reference. Enable the internal reference in the COMMON-CONFIG register before enabling the IDAC output.
The power dissipation of the IDAC channel is a function of the PVDD supply voltage, the current output, and the voltage of the IDAC pin (VIDAC). The headroom voltage (VHEADROOM) is calculated as the difference between PVDD and VIDAC. Minimize VHEADROOM to reduce the power dissipation of the device while also meeting the minimum VHEADROOM requirement. The IDAC output cannot source the full-scale current output if VHEADROOM is lower than the specified voltage. Figure 8-2 shows the output current directions and the key voltages that impact power dissipation. The IDAC output contributes to power dissipation proportionally to the output current multiplied by the VHEADROOM voltage.
IDAC
PVDD
LOAD
IDAC
VIDAC
+
–
VHEADROOM
+
–
Figure 8-2. IDAC Power Dissipation
The VOUT1 channel of the DAC53xAxW can be configured as a programmable comparator. In the DAC-1- GAIN-CMP-CONFIG register.

# 8.2.3 Application Curves
Time (s)
Voltage (V)
0
2.5
5
7.5
10
12.5
15
17.5
20
22.5
25
0
0.5
1
1.5
2
2.5
3
3.5
GPIO (V)
VIOUT (V)
Figure 8-3. Comparator Toggle

# 8.3 Power Supply Recommendations
The DAC53xAxW do not require specific power-supply sequencing. These devices require a single power supply, VDD and PVDD. Short VDD and PVDD with a low-impedance PCB trace. To minimize noise from the power supply, connect a 1-μF to 10-μF capacitor and 100-nF bypass capacitor. Use a bypass capacitor with a value approximately 1.5 µF for the CAP pin.
*Note*
The DAC53xAxW do not provide automatic thermal shutdown. Therefore, the external circuit design must maintain the junction temperature within the specified limits.

# 8.4 Layout

# 8.4.1 Layout Guidelines
The DAC53xAxW pin configuration separates the analog, digital, and power pins for an optimized layout. For signal integrity, separate the digital and analog traces, and place decoupling capacitors close to the device pins.

# 8.4.2 Layout Example
GPIO/SDO
SCL/SYNC
A0/SDI
SDA/SCLK
A1
A2
A3
A4
B1
B2
B3
B4
C1
C2
C3
C4
D1
D2
D3
D4
PVDD 
Decoupling 
Capacitor
VDD 
Decoupling 
Capacitor
GND
VDD
GND
LDO Bypass 
Capacitor
VIO
VOUT1
/AIN1
IOUT
VIO
VIO
VIO
DAC532A3W, DAC530A2W
GND
PVDD
VDD
GND
FB1
PVDD
GND
Figure 8-4. Layout Example
*Note*: The ground and power planes have been omitted for clarity.

# 9 Device and Documentation Support
TI offers an extensive line of development tools. Tools and software to evaluate the performance of the device, generate code, and develop solutions are listed below.

# 9.1 Documentation Support

# 9.1.1 Related Document# 9. Device and Documentation Support
TI offers an extensive line of development tools. Tools and software to evaluate the performance of the device, generate code, and develop solutions are listed below.

# 9.1. Documentation Support

# 9.1.1. Related Documentation
The following EVM user's guide is available: AFE532A3W Evaluation Module user's guide

# 9.2. Receiving Notification of Documentation Updates
To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on Notifications to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

# 9.3. Support Resources
TI E2E™ support forums are an engineer's go-to source for fast, verified answers and design help — straight from the experts. Search existing answers or ask your own question to get the quick design help you need.
Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

# 9.4. Trademarks
TI E2E™ is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.

# 9.5. Electrostatic Discharge Caution
This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.
ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

# 9.6. Glossary
TI Glossary 
This glossary lists and explains terms, acronyms, and definitions.

# 10. Revision History
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
---table begin---
Table tile: Revision History
| DATE | REVISION | NOTES |
|---|---|---|
| November 2023 | * | Initial Release |
---table end---

# 11. Mechanical, Packaging, and Orderable Information
(1) The marketing status values are defined as follows:
ACTIVE: Product device recommended for new designs.
LIFEBUY: TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.
NRND: Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design.
PREVIEW: Device has been announced but is not in production. Samples may or may not be available.
OBSOLE# 1. DAC Characteristics
---table begin---
Table title: DAC Characteristics
|   |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| 125 | DAC | 530A2 | Samples | DAC532A3YBHR | ACTIVE | DSBGA | YBH | 16 | 3000 | RoHS & Green |
|   |   | 532A3 | Samples |   |   |   |   |   |   |   |
---table end---
# 11. Mechanical, Packaging, and Orderable Information

# 2. Marketing Status Definition
(1) The marketing status values are defined as follows:
- ACTIVE: Product device recommended for new designs.
- LIFEBUY: TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.
- NRND: Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design.
- PREVIEW: Device has been announced but is not in production. Samples may or may not be available.
- OBSOLETE: TI has discontinued the production of the device.

# 3. Regulation Definitions
(2) RoHS:  TI defines "RoHS" to mean semiconductor products that are compliant with the current EU RoHS requirements for all 10 RoHS substances, including the requirement that RoHS substances do not exceed 0.1% by weight in homogeneous materials. Where designed to be soldered at high temperatures, "RoHS" products are suitable for use in specified lead-free processes. TI may reference these types of products as "Pb-Free".
RoHS Exempt: TI defines "RoHS Exempt" to mean products that contain lead but are compliant with EU RoHS pursuant to a specific EU RoHS exemption.
Green: TI defines "Green" to mean the content of Chlorine (Cl) and Bromine (Br) based flame retardants meet JS709B low halogen requirements of <=1000ppm threshold. Antimony trioxide based flame retardants must also meet the <=1000ppm threshold requirement.

# 4. MSL and Peak Temperature
(3) MSL, Peak Temp. - The Moisture Sensitivity Level rating according to the JEDEC industry standard classifications, and peak solder temperature.

# 5. Marking Informations
(4) There may be additional marking, which relates to the logo, the lot trace code information, or the environmental category on the device.

# 6. Multi-device Markings
(5) Multiple Device Markings will be inside parentheses. Only one Device Marking contained in parentheses and separated by a "~" will appear on a device. If a line is indented then it is a continuation of the previous line and the two combined represent the entire Device Marking for that device.

# 7. Lead finish/ball Material
(6) Lead finish/Ball material - Orderable Devices may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

# 8. Important Information and Disclaimer
> Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals.
TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.
In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

# 9. Tape and Reel Information
TAPE AND REEL INFORMATION
Reel Width (W1)
REEL DIMENSIONS
A0
B0
K0
W
Dimension designed to accommodate the component length
Dimension designed to accommodate the component thickness
Overall width of the carrier tape
Pitch between successive cavity centers
Dimension designed to accommodate the component width
TAPE DIMENSIONS
K0
P1
B0 W
A# 1. LIABILITY DISCLAIMER
numbers and other limited information may not be available for release. 
In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

# 2. TAPE AND REEL INFORMATION
---table begin---
Table tile: Pocket Quadrants
| Sprocket Holes | Q1 | Q2 | Q3 | Q4 | User Direction of Feed | P1 | Reel Diameter |
|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - |
---table end---
# 2. TAPE AND REEL INFORMATION
**All dimensions are nominal**

# 3. DEVICE AND PACKAGE INFORMATION
---table begin---
Table title: Device and Package Information
| Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DAC530A2YBHR | DSBGA | YBH | 16 | 3000 | 180.0 | 8.4 | 1.94 | 1.94 | 0.69 | 4.0 | 8.0 | Q1 |
| DAC532A3YBHR | DSBGA | YBH | 16 | 3000 | 180.0 | 8.4 | 1.94 | 1.94 | 0.69 | 4.0 | 8.0 | Q1 |
---table end---
Pack Materials-Page 1

# 4. TAPE AND REEL BOX DIMENSIONS
---table begin---
Table title: TAPE AND REEL BOX DIMENSIONS
| Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm) |
|---|---|---|---|---|---|---|---|
| DAC530A2YBHR | DSBGA | YBH | 16 | 3000 | 182.0 | 182.0 | 20.0 |
| DAC532A3YBHR | DSBGA | YBH | 16 | 3000 | 182.0 | 182.0 | 20.0 |
---table end---
Pack Materials-Page 2

# 5. DIE SIZE BALL GRID ARRAY
NOTES: 
1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
---table begin---
Table title: Basic Grid Array Details
| - | - | - | - | - | 
|---|---|---|---|---|
| BALL A1 CORNER | SEATING PLANE | BALL TYP | 0.05 C | - |
| - | - | - | - | - |
---table end---
D: Max = 1.748 mm, Min = 1.687 mm
E: Max = 1.748 mm, Min = 1.687 mm
0.05 MIN
0.05 MAX

# 6. DIE SIZE BALL GRID ARRAY (continued)
NOTES: (continued)
3. Final dimensions may vary due to manufacturing tolerance considerations and also routing constraints. See Texas Instruments Literature No. SNVA009 (www.ti.com/lit/snva009).
4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release.

# 7. IMPORTANT NOTICE AND DISCLAIMER
TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES “AS IS” AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.
These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.
These resources 

# 1. Disclaimer
AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

# 2. Intended Use
These resources are intended for skilled developers designing with TI products. You are solely responsible for 
(1) selecting the appropriate TI products for your application, 
(2) designing, validating and testing your application, 
(3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

# 3. Terms and Conditions
These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

# 4. Product Terms
TI’s products are provided subject to TI’s Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI’s provision of these resources does not expand or otherwise alter TI’s applicable warranties or warranty disclaimers for TI products.

# 5. Rejection of Additional Terms
TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

# 6. Mailing Address
Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265

