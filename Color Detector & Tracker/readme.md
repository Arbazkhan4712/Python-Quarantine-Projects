# CoDAT - Color detection and tracker

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-swag.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

CoDAT is a python based application to detect color from images and track colors & objects in realtime using HSV object detection method. CoDAT uses basic computer vision tools to achieve this.

![Alt text](assets/gif1.gif?raw=true "CoDAT")

## How to Download

Download this project from here [Download CoDAT](https://downgit.github.io/#/home?url=https://github.com/pyGuru123/OpenCV-Projects/tree/main/Color%20Detector%20%26%20Tracker)

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following packages :-
* numpy
* requests
* pandas
* opencv-contrib-python
* Pillow

```bash
pip install numpy
pip install requests
pip install pandas
pip install opencv-contrib-python
pip install Pillow
```

or, just run this command in terminal from inside this project folder

```bash
pip3 install -r requirements.txt
```

## Usage

Double click the application.py to open the GUI application, select any of the button to start detecting and tracking colors.

1. Detect Color : This feature detects color from the selected picture. Just import an image and click anywhere on it find out the color name
2. Track objects from image : This feature allows you to track colors from a imported image. Just choose a image and click detect, in the next screen adjust HSV values to track colors.
3. Track objects in realtime : You can track objects in realtime using this feature. Just select whether you want to track objects using your pc camera or using your android camera ( IP Webcam required). If choosen pc camera, pass 0 as your camera id and on choosing stream/android pass the local stream url from IP Webcam, and again on the next screen adjust hsv values to detect objects

![Alt text](assets/gif2.gif?raw=true "CoDAT")
![Alt text](assets/gif3.gif?raw=true "CoDAT")

### How to get streaming server IP from IP Webcam

1. Go to playstore, install IP Webcam application.
2. Turn on your phone hotspot and connect it with pc.
3. Open app, scroll to bottom, click Start Server for Video stream ( allow permissions when asked )
4. It will open your android camera and start video stream, at the bottom it shows IPv4 address, this is your server IP

![Alt text](assets/ipwebcam.png?raw=true "IP Webcam")

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.