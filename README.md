

# 📹 Motion Detector

A simple and efficient **real-time motion detection system** built using **Python + OpenCV**. The project captures live video from your webcam, detects motion in the frame, highlights moving objects, and optionally saves snapshots or logs activity. Perfect for beginners learning computer vision or building basic surveillance applications.

---

## 🚀 Features

* ✔ Real-time video processing
* ✔ Automatic motion detection using frame differencing / background subtraction
* ✔ Highlights detected motion with bounding boxes
* ✔ Adjustable sensitivity (threshold & area)
* ✔ Works with any webcam
* ✔ Clean and lightweight code

---

## 🛠 Technologies Used

* **Python 3**
* **OpenCV (cv2)**
* **NumPy**

---

## 📌 How It Works

1. Reads video frames from the webcam
2. Converts frames to grayscale and applies Gaussian blur
3. Compares the current frame with a reference frame
4. Detects differences indicating motion
5. Draws a rectangle around moving areas
6. Displays the processed video in real-time

---

## 🧩 Use Cases

* Home security
* Activity monitoring
* Computer vision learning
* Object movement tracking
* Surveillance prototypes

---

## ▶️ Getting Started

```bash
pip install opencv-python numpy
python motion_detector.py
```

---

## 📷 Demo (optional)

You can add gifs or screenshots here.

---

## 🤝 Contributions

Feel free to fork this project and submit pull requests!

---


