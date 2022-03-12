# Prototype of a autonomous selfi drone utilizing pose estimation

[![Python Pytest](https://github.com/Baumwollboebele/autonnomous_selfie_drone/actions/workflows/python_pytest.yml/badge.svg)](https://github.com/Baumwollboebele/autonnomous_selfie_drone/actions/workflows/python_pytest.yml)&nbsp;&nbsp;&nbsp;[![Python Linting](https://github.com/Baumwollboebele/autonnomous_selfie_drone/actions/workflows/python_linting.yml/badge.svg)](https://github.com/Baumwollboebele/autonnomous_selfie_drone/actions/workflows/python_linting.yml)

# Table of Contents

1. [Summary](#summary)
2. [Getting Started](#getting-started)
3. [Technical Details](#tello-drone)
4. [Sources](#sources)

# Summary

<img style="float: right;" src="/images/tello_drone.jpg" height="200"/>


This repository contains the code and documentation of an autonomous selfie drone.
The drone used for this project was the [Tello](https://www.ryzerobotics.com/de/tello) drone from Ryze.

The purpose of the project was to create an autonomous drone which is capable of making images which can be triggered by poses.
In addition to that, the drone should be able to be controlled via poses.

By utilizing the [BlazePose](https://arxiv.org/abs/2006.10204) CNN, three poses can be detected.
- Right arm up: Which enables the drone to move to its left side (right side of the viewers perspective).
- Left arm up: Which enables the drone to move to its right side (left side of the viewers perspective).
- Arms crossed: Will trigger a countdown, then take a picture.

Additionally the drone will keep its position relative to the persons face centerpoint when no pose can be detected.

> A documentation of the codebase can be found here: [Documentation](https://baumwollboebele.github.io/autonnomous_selfie_drone/)


<hr/>

# Getting Started

The project was written with `Python 3.9.7`, it is highly recommended to use this version 
if you want to run the project.

1. Install the requirements:</br>
```pip install -r requirements.txt```

2. Turn on your Tello Education and connect to its WLAN.

3. Change to the directory `/source` and run the Main.py file:</br>
```python Main.py```


# Technical Details

| **Aircraft** ||
|-------|--------|
|Weight (including Propeller Guards)| 87g |
|Max Speed| 8m/s |
|Max Flight Time| 13 minutes|
|Operating Temperature Range| 0°C to 40°C|
|Operating Frequency Range| 2.4Ghz to 2.4835Ghz|
|Transmitter (EIRP)| 20 dBm (FCC), 19 dBm(CE), 19dBm (SRRC)

| **Camera** ||
|-------|--------|
|Max Image Size| 2592x1936|
|Video Recording Modes| HD: 1280x720 30p |
|Video Format| MP4|

| **Flight Battery** ||
|-------|--------|
|Capacity| 1100 mAh|
|Voltage|3.8 V|
|Battery Type| LiPo|
|Energy| 4.18 Wh|


# Sources

Mediapipe:
https://github.com/google/mediapipe<br>
Mediapipe Pose:
https://google.github.io/mediapipe/solutions/pose</br>
DJITelloPy:
https://github.com/damiafuentes/DJITelloPy/<br>
BlazePose:
https://arxiv.org/abs/2006.10204

