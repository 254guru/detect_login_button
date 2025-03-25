import cv2
import matplotlib
# matplotlib.use("Agg")  # Use non-interactive backend
import matplotlib.pyplot as plt

def visualize_detection(image_path, detected_coordinates, output_path="detected_login_button.png"):
    """Marks the detected login button on the image and saves it."""
    if detected_coordinates is None:
        print("No login button detected. Skipping visualization.")
        return

    detected_x, detected_y = detected_coordinates
    image = cv2.imread(image_path)

    # Draw a red circle at the detected position
    cv2.circle(image, (detected_x, detected_y), 10, (0, 0, 255), -1)  # Red dot

    # Convert to RGB for Matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the marked image
    plt.figure(figsize=(12, 6))
    plt.imshow(image_rgb)
    plt.title("Detected Login Button Position")
    plt.axis("off")
    plt.show()
    
    # Save instead of showing (prevents GUI issues)
    # plt.savefig(output_path)
    # print(f"Visualization saved as {output_path}")

if __name__ == "__main__":
    from detect_login_button import capture_screenshot, find_login_button
    
    screenshot_path = capture_screenshot()
    coordinates = find_login_button(screenshot_path)
    visualize_detection(screenshot_path, coordinates)
