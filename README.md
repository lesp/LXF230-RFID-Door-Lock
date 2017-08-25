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




