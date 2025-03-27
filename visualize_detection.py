import cv2
import matplotlib.pyplot as plt
from detect_login_button import capture_screenshot, find_login_button, detect_and_click_login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def visualize_detection(image_path, detected_coordinates, output_path="detected_login_button.png"):
    """Marks detected login buttons on the image, saves it, and displays it."""
    if not detected_coordinates:
        print("❌ No login buttons detected. Skipping visualization.")
        return

    image = cv2.imread(image_path)

    # Mark each detected button
    for coords in detected_coordinates:
        x, y = coords["x"], coords["y"]
        cv2.circle(image, (x, y), 10, (0, 0, 255), -1)  # Red dot

    # Convert to RGB for Matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the marked image
    plt.figure(figsize=(12, 6))
    plt.imshow(image_rgb)
    plt.title("Detected Login Button(s)")
    plt.axis("off")
    plt.show()

    # Save the result
    cv2.imwrite(output_path, image)
    print(f"✅ Visualization saved as {output_path}")

if __name__ == "__main__":
    url = input("🌐 Enter website URL: ").strip()
    
    driver, coordinates_list, highlighted_screenshot = detect_and_click_login(url, auto_click=False)

    if coordinates_list:
        visualize_detection(highlighted_screenshot, coordinates_list)

    if driver:
        driver.quit()
