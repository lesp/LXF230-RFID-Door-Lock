# LXF230 RFID Controlled Magnetic Door Lock

![alt](https://www.linuxformat.com/forums/images/lxf.gif)

A simple project for all models of Raspberry Pi.

## Installation

Clone the repository, or run the install script from the terminal

```
curl https://raw.githubusercontent.com/lesp/LXF230-RFID-Door-Lock/master/install.sh | bash
```

Enable the SPI interface. Then build this circuit.
![alt](https://raw.githubusercontent.com/lesp/LXF230-RFID-Door-Lock/master/Images/CircuitDiagram_bb.png)

## Extra information

![alt](https://raw.githubusercontent.com/lesp/LXF230-RFID-Door-Lock/master/Images/12V%20Connectors.JPG)
The best tool to connect the 12V GND connection is a Wago connector, it creates a common connection. So one GND connection becomes many, it also enables us to safely connect the GND from the 12V PSU to GND connection of the magnetic door lock.

![alt](https://raw.githubusercontent.com/lesp/LXF230-RFID-Door-Lock/master/Images/RelayBoard2.JPG)
Relays isolate the higher voltage 12V circuit from the low voltage circuit for the Raspberry Pi. This unit cost about £3 from eBay.

![alt](https://raw.githubusercontent.com/lesp/LXF230-RFID-Door-Lock/master/Images/RFID1.JPG)
The RFID reader is an RFID-RC522, you can find them really cheap on eBay but we used the [Monk Make Clever Card Kit](https://www.monkmakes.com/cck/) as it offers a complete kit, along with a great guide. We reviewed it in LXF229, so take a look.


