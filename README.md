# ✊ Rock Paper Scissors

A Rock-Paper-Scissors game played with your **hand** in front of a webcam. Show a fist, an open palm or two fingers, and the computer answers with its own move. Built with Python, OpenCV and MediaPipe — no keyboard, no mouse, no controller.

I built it as a computer-vision project: the interesting part was not the game logic, but turning a live video feed into a reliable "which gesture is this?" decision.

## 🍿 Technologies

- Python 3.11
- OpenCV
- MediaPipe (hand tracking)
- cvzone (`HandDetector`, PNG overlay)
- NumPy
- Pillow

## ✨ Features

- **Live hand detection** through the webcam, with the 21 hand landmarks drawn on screen.
- **Gesture recognition** from the fingers-up pattern:
  | Fingers up | Move |
  | --- | --- |
  | `[0,0,0,0,0]` — fist | ✊ Rock |
  | `[1,1,1,1,1]` — open palm | ✋ Paper |
  | `[0,1,1,0,0]` — two fingers | ✌️ Scissors |
- **Countdown before each round**, so you have time to make your move.
- **Random AI move**, displayed as an image overlaid on the game board.
- **Live score** for the AI and the player.
- **Composited game board**: your webcam feed, the AI's move, the timer and both scores on one canvas.

## 🎮 How to play

1. Run `python main.py` — a window opens with your webcam feed.
2. Press **`S`** to start a round.
3. Make your gesture within the 3-second countdown.
4. The AI plays, the winner is scored, and the board updates.
5. Press **`S`** again for another round.
6. Close the window to quit.

## 🧑‍🍳 The Process

I started with the camera, not the game: reading frames, resizing and cropping them so the player's hand sits in the right part of the board. Getting the geometry right first meant the rest of the work had a stable canvas.

Next came hand detection. `cvzone`'s `HandDetector` wraps MediaPipe and returns the hand landmarks plus a list of which fingers are up — `[1,1,1,1,1]` for an open palm, `[0,0,0,0,0]` for a fist. That list is the entire bridge between computer vision and game logic: one comparison per gesture.

Then the game loop: a countdown timer, a random move for the AI, and a rules table deciding who scores. I drew the AI's move with `overlayPNG`, which keeps the transparent background of the PNGs.

The last step was composition — placing the webcam feed, the AI move, the timer and the scores at fixed coordinates on a background image so the whole thing reads like a game board rather than a debug window.

## 📚 What I Learned

- **Webcam handling in OpenCV**: capture, resize and crop frames, and why the crop coordinates depend on the resize factor.
- **Hand landmarks with MediaPipe**: 21 points per hand, and how `fingersUp()` turns them into a simple array.
- **Mapping vision to logic**: a gesture becomes an integer, and the game itself is just comparisons — a clean separation of concerns.
- **Image composition**: overlaying transparent PNGs with `cvzone.overlayPNG` and positioning elements by pixel coordinates.
- **Real-time loops**: keeping per-frame work cheap, since everything runs at camera frame rate.
- **Pinning dependencies**: MediaPipe is sensitive to NumPy versions, so `requirements.txt` fixes exact versions.

## 💡 How can it be improved?

- Support both hands and multi-round matches.
- Add sound effects and a visible winner message per round.
- Detect gestures continuously instead of sampling once when the timer ends.
- Add a quit key (`q` or `Esc`) instead of closing the window.
- Handle "no hand detected" with a clear on-screen message.
- Improve the scissors gesture — `[0,1,1,0,0]` also matches some other two-finger poses.
- Add a difficulty level where the AI reacts to the player's move.
- Package it as an executable with PyInstaller.

## 🏃 Running the Project

### Requirements

- Python 3.11
- A working webcam
- Windows, macOS or Linux

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/zeinebsmaoui/rock-paper-scissors.git
   cd rock-paper-scissors
   ```

2. Create a virtual environment and install the dependencies:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   # source .venv/bin/activate # macOS / Linux
   pip install -r requirements.txt
   ```

3. Run the game:

   ```bash
   python main.py
   ```

4. Press **`S`** to start a round.

If the camera window does not open, check that no other application is using the webcam and that `cv2.VideoCapture(0)` points at the right device.

## 🎥 Video

<!-- Add a short GIF or MP4 of a round here. -->
