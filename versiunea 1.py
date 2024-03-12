from pynput.mouse import Listener
import cv2


# Function to capture an image from the camera
def capture_image(x,y):
    camera = cv2.VideoCapture(0)  # 0 means the default camera
    ret, frame = camera.read()
    if ret:
        cv2.imwrite(f"captured_image_{x,y}.jpg", frame)
        print("Image captured successfully!")
    camera.release()


def on_click(x, y, button, pressed):
    if button == button.left and pressed:
        print(f"Left mouse button clicked at coordinates: ({x}, {y})")
        capture_image(x,y)


# Create and start the listener
with Listener(on_click=on_click) as listener:
    listener.join()