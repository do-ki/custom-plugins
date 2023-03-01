**Custom plug-ins used for my flipper inspired UI pwnagotchi. Most of it are modified or combined to to easily integrate with V0r-t3x Colorized Mod and Fancygotchi. This coordinates supply in the toml fill will only work on Pimoroni Display Hat Mini and will not work properly on other screens without changing the coordinates in config.toml.**

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
