import cv2
import matplotlib.pyplot as plt
from detect_login_button import capture_screenshot, find_login_button_opencv

def visualize_detection(image_path, detected_buttons, output_path="detected_login_button.png"):
    """Marks detected login buttons and saves the visualization."""
    if not detected_buttons:
        print("❌ No login button detected. Skipping visualization.")
        return

    image = cv2.imread(image_path)

    for (x, y, w, h) in detected_buttons:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)  # Red box

    # Convert for display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Show image
    plt.figure(figsize=(10, 5))
    plt.imshow(image_rgb)
    plt.title("Detected Login Button(s)")
    plt.axis("off")
    plt.show()

    # Save the result
    cv2.imwrite(output_path, image)
    print(f"✅ Visualization saved as {output_path}")

if __name__ == "__main__":
    screenshot_path = "screenshot.png"
    detected_buttons = find_login_button_opencv(screenshot_path)

    if detected_buttons:
        visualize_detection(screenshot_path, detected_buttons)
