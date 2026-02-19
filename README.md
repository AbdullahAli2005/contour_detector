# Hand Gesture Recognition using OpenCV

A real-time hand gesture recognition system built with Python and OpenCV. This project captures live video from your webcam, detects a hand inside a defined Region of Interest (ROI), analyzes convexity defects, and estimates the number of fingers extended.

---

## 🚀 Features

* Real-time webcam capture
* Region of Interest (ROI) based detection
* Contour detection and convex hull visualization
* Convexity defect analysis
* Finger counting using geometric angle calculation
* Live on-screen finger count display

---

## 🧠 How It Works

1. The webcam feed is captured using OpenCV.
2. A fixed Region of Interest (ROI) is defined where the hand should be placed.
3. The ROI is converted to grayscale and blurred to reduce noise.
4. Otsu thresholding is applied to segment the hand from the background.
5. The largest contour is assumed to be the hand.
6. A convex hull is generated around the hand contour.
7. Convexity defects (gaps between fingers) are detected.
8. Using triangle geometry and cosine rule, angles are calculated.
9. Angles less than or equal to 90° are counted as extended fingers.

This approach uses classical computer vision techniques — no machine learning or deep learning is involved.

---

## 📦 Installation

Make sure Python 3.8+ is installed.

Install required dependencies:

```bash
pip install opencv-python numpy
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Controls:

* Place your hand inside the green rectangle.
* Press **Q** to exit the application.

---



## 📄 License

This project is open-source and available under the MIT License.


