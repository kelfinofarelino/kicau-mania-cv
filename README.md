# 🦅 Kicau Mania Computer Vision

<div align="center">
  <video src="https://github.com/kelfinofarelino/kicau-mania-cv/assets/DEMO.mp4" width="100%" controls>
    Your browser does not support the video tag.
  </video>
  <p><i>Demo interaksi deteksi gestur "Kicau Mania" secara real-time.</i></p>
</div>

An interactive Computer Vision project using Python, OpenCV, and MediaPipe to detect specific hand gestures and trigger a Picture-in-Picture (PiP) video response in real-time. 

## 🚀 Features
- **Real-time Hand Tracking**: Utilizes Google's MediaPipe for robust hand landmark detection.
- **Heuristic Gesture Recognition**: Specifically programmed to detect a dual-hand gesture:
  - **Hand 1**: Positioned near the face (mimicking covering the mouth).
  - **Hand 2**: Moving horizontally continuously (mimicking a fanning motion).
- **Dynamic Video Overlay**: Automatically triggers and plays a local video (`kicau-mania.mp4`) as an overlay when the gesture combination is successfully recognized.

## 🛠️ Tech Stack
- **Python 3.x**
- **OpenCV** (Video capturing, image processing, array manipulation)
- **MediaPipe** (Hand landmark estimation)

## 💻 Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/yourusername/kicau-mania-vision.git](https://github.com/yourusername/kicau-mania-vision.git)
cd kicau-mania-vision
```
   
2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
Add your video:
Place your reaction video in the assets/ directory and name it kicau-mania.mp4.


3. **Run the application:**
```bash
python main.py
```

## **🎮 How to Use**
1. Ensure your webcam is connected and the lighting is sufficient.
2. Step back so both of your hands are visible to the camera.
3. Bring one hand up to your mouth.
4. Use your other hand to make a fanning motion (moving left and right).
5. The "Kicau Mania" video will appear in the top right corner!
6. Press q to exit the application.

👤 Author
Farelino Kelfino