Blood Vein Detection System
📌 Project Overview

The Blood Vein Detection System helps medical staff locate veins for injections and IV infusions using Near-Infrared (NIR) imaging and OpenCV (CLAHE algorithm). This low-cost and real-time solution reduces patient discomfort and improves accuracy in clinical procedures.

🧬 Biological Principle

Hemoglobin absorbs NIR light (740–940 nm) more strongly than surrounding skin and tissues.

Under IR illumination, veins appear darker.

The IR-sensitive camera captures this contrast, and image processing enhances vein visibility.

⚙️ Technical Workflow

IR LEDs illuminate the skin.

IR Camera captures the live feed.

Raspberry Pi + Python + OpenCV process each frame.

CLAHE algorithm enhances local contrast.

Output displayed in real time.

🛠️ Components Used

Raspberry Pi 4

Pi NoIR / IR Camera

IR LEDs (850 nm) + resistors

NPN transistor (2N2222) for LED control

Power supply (5V, ≥2.5A)

HDMI display

💻 Software Stack

Language: Python

Libraries: OpenCV, NumPy, RPi.GPIO

Algorithm: CLAHE (Contrast Limited Adaptive Histogram Equalization)

![img1](https://github.com/user-attachments/assets/478b79b4-e702-431e-a8ec-86b414c12001)
![img2](https://github.com/user-attachments/assets/fa2b3692-fa3c-4b51-b10e-83840ac72f16)
