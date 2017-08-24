#! /bin/bash
echo "Installation of the SPI library is thanks to Simon Monk's Clever Card Kit"
echo "Take a look at https://github.com/simonmonk/clever_card_kit for more information"
cd /home/$USER
sudo apt-get install python3-dev
git clone https://github.com/simonmonk/SPI-Py.git
cd SPI-Py
sudo python3 setup.py install
cd /home/$USER
git clone https://github.com/lesp/LXF230-RFID-Door-Lock
sudo pip3 install logzero
