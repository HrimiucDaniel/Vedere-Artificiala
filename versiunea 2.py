from pynput.mouse import Listener
import cv2
from screeninfo import get_monitors
import sys

cap = cv2.VideoCapture(0)


def get_screen_resolution():
    screen_width = get_monitors()[0].width
    screen_height = get_monitors()[0].height
    return screen_width, screen_height


def capture_image(x, y):
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    ret, frame = cap.read()
    print(ret)

    if ret:
        width, height = get_screen_resolution()
        photo_title = f"captured_image_{x}_{y}_res_{width}_{height}.jpg"
        cv2.imwrite(photo_title, frame)
        print("Image captured successfully!")
    else:
        print("Error: Failed to capture image.")


def on_click(x, y, button, pressed):
    try:
        if pressed:
            print(f"Mouse clicked at: ({x}, {y})")
            capture_image(x, y)
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)


def main():
    print("Listening for mouse clicks. Press Ctrl+C to exit.")
    with Listener(on_click=on_click) as listener:
        listener.join()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)