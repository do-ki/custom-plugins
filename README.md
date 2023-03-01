*Custom plug-ins used for my flipper inspired UI pwnagotchi. Most of it are modified or combined plugins to easily integrate with [V0r-t3x LCD Colorized Darkmode Mod](https://github.com/V0r-T3x/pwnagotchi_LCD_colorized_darkmode) and [Fancygotchi](https://github.com/V0r-T3x/fancygotchi). The coordinates in dashboard.toml file are designed for Pimoroni Display Hat Mini and will **not work** properly on other screens without changing the values.*

![image](https://user-images.githubusercontent.com/123346661/222113846-b158d751-6bed-41ab-b79f-03fad511d718.png) ![image](https://raw.githubusercontent.com/do-ki/custom-plugins/main/img/dashboard_d.png)


###### DASHBOARD Plugin  
- Display the following: RAM, CPU, Temperature, Battery (pivoyager), Deauth Counter, Total Handshakes, Total Crack Handshakes, Clock and Internet status(in progress).

Requirements:

Pivoyager  
"I2C" needs to be enabled (e.g. via raspi-config).  

sudo raspi-config

In the menu, select Interfacing Options
- Next select P5 I2C
- Choose yes when asked if you want to enable I2C
- Choose yes when asked if you want to reboot.  

Pivoyager binary is also needed.  

curl -O https://www.omzlo.com/downloads/pivoyager.tar.gz  
tar xvf pivoyager.tar.gz  
sudo mv pivoyager /usr/local/bin/  

Note: use dashboard2.py if you dont use Pivoyager UPS
