import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def capture_screenshot(url="https://tublian.com", output_file="tublian_screenshot.png"):
    """Captures a screenshot of the given URL and saves it as an image."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1024x768")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get(url)
    driver.save_screenshot(output_file)
    driver.quit()
    
    print(f"Screenshot saved as {output_file}")
    return output_file

def find_login_button(image_path):
    """Detects the login button based on color and shape filtering."""
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define yellow color range (specific to Tublian's login button)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([40, 255, 255])

    # Create a mask for yellow regions
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Find contours in the masked image
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    button_contour = None
    max_area = 0

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h
        aspect_ratio = w / float(h)

        # Ensure the detected area is button-sized and rectangular
        if 2 < aspect_ratio < 6 and 1000 < area < 5000:  
            if area > max_area:
                max_area = area
                button_contour = (x, y, w, h)

    if button_contour:
        x, y, w, h = button_contour
        return (x + w // 2, y + h // 2)  # Center of the button

    return None

if __name__ == "__main__":
    screenshot_path = capture_screenshot()
    coordinates = find_login_button(screenshot_path)
    print(f"Login button coordinates: {coordinates}" if coordinates else "Login button not detected.")
