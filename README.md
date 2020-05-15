# Welcome

This script will use Chrome and selenium to auto download files for ENSC225 lectures for the purpose of saving 10-30 repeated clicks


## Instruction
 1. Install the selenium and PySimpleGUI packages using pip or conda whatever you prefer.

 2. This repo has the driver for Chrome version 81 on macOS. If you have other versions of Chrome or OS, please download the driver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and replace chromedriver. 
 
 3. You need to edit these in autoDL.py for your environment<br/>
	 - **DLdir**: This is the path to a designated download directory<br/>
	 - **path**(for Windows): Windows uses \ so you need to adopt that<br/>
	 - **topics**: This is a list of topics you want to download so change it according to your need
	 - **line33**: Because this is public I had to hide the password, if you are enrolled in ENSC225 you should have the password

 4. Give executable permissions to the driver and autoDL.py and you should be good to go. Run python3 gui.py.<br/>
 *The browser or website glitches sometimes just close the opend browser and run again.
