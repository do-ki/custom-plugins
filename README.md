**Custom plug-ins used for my flipper inspired UI pwnagotchi. Most of it are modified or combined to to easily integrate with V0r-t3x Colorized Mod and Fancygotchi. This coordinates supply in the toml fill will only work on Pimoroni Display Hat Mini and will not work properly on other screens without changing the coordinates in config.toml.**

![image](https://user-images.githubusercontent.com/123346661/222113846-b158d751-6bed-41ab-b79f-03fad511d718.png) ![image](https://raw.githubusercontent.com/do-ki/custom-plugins/main/img/dashboard_d.png)


###### DASHBOARD Plugin Requirements

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
