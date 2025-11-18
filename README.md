Blood Vein Detection System

A real-time vein detection project using Raspberry Pi, IR imaging, and OpenCV (CLAHE) to assist medical professionals in identifying veins for procedures like intravenous injections and blood extraction.

1. Overview

Locating veins can be challenging in cases such as obesity, dehydrated patients, pediatric patients, darker skin tone, or low blood pressure. This leads to multiple needle insertion attempts, causing pain and increasing clinical time.

This project proposes a portable, low-cost real-time vein detection system using near-infrared imaging and image processing. The system uses Pi NoIR camera and IR LEDs to capture vein patterns, then processes the image using CLAHE for enhanced visibility and displays it live using a screen.

2. Objectives

To detect veins in real time using Raspberry Pi and IR imaging.

To enhance visibility using image processing techniques.

To design a compact, portable unit for use in clinical environments.

To reduce failed vein access attempts and improve procedural accuracy.

3. Working Principle

Hemoglobin absorbs near-infrared light (850–940 nm) more than surrounding tissue.

IR LEDs illuminate the skin surface.

Pi NoIR camera captures reflected IR light – veins appear darker.

Image is converted to grayscale and enhanced using CLAHE algorithm.

The processed image is displayed live, helping clinicians identify vein locations.

This process is non-invasive and medically safe.

4. Hardware Components

Raspberry Pi 4B

Pi NoIR Camera Module

IR LED module (850 nm)

12V battery (for LED power)

Relay module (GPIO controlled)

Display (5-inch LCD)

Connecting ribbon cable and wires

3D printed enclosure (for compact design)

5. Software and Technologies

Python, OpenCV

CLAHE (Contrast Limited Adaptive Histogram Equalization)

RPi.GPIO for hardware control

Raspberry Pi OS

IDE (Thonny / Jupyter / Terminal-based execution)

6. Methodology

IR illumination and image capture

Grayscale conversion

CLAHE-based enhancement

Frame display in real-time

Output visualization on screen

![img1](https://github.com/user-attachments/assets/478b79b4-e702-431e-a8ec-86b414c12001)
![img2](https://github.com/user-attachments/assets/fa2b3692-fa3c-4b51-b10e-83840ac72f16)

9. Safety Notes

  The system uses low-power IR LEDs, which are completely non-invasive and safe.

  No skin penetration or heating occurs.

  Technology is similar to pulse oximeters and night-vision imaging.

10. Results

  Successfully detected veins in real time.

  Demonstrated in Engineering Clinics internal review.

  Selected among top 10 out of 1600+ projects.

  Received positive feedback for practical medical application.

11. Future Enhancements

      Skin-surface projection system.

      AI-based vein segmentation.

      Complete handheld ergonomic design.

      Battery-powered standalone operation.
