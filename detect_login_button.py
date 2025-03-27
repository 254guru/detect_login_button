import cv2
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

def capture_screenshot(driver, output_file="screenshot.png"):
    """Captures a screenshot of the current page."""
    driver.save_screenshot(output_file)
    print(f"📸 Screenshot saved as {output_file}")
    return output_file

def find_login_button_selenium(driver):
    """Finds login button using Selenium."""
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")

    login_keywords = ["login", "log in", "sign in"]
    login_buttons = []

    for button in buttons + links:
        text = button.text.strip().lower()
        if any(keyword in text for keyword in login_keywords):
            login_buttons.append(button)

    return login_buttons

def find_login_button_opencv(image_path):
    """Detects login buttons visually using OpenCV."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected_buttons = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if 80 < w < 250 and 20 < h < 70:  # Filter based on button-like sizes
            detected_buttons.append((x, y, w, h))

    return detected_buttons

def highlight_button(driver, button):
    """Highlights the detected login button."""
    driver.execute_script("arguments[0].style.border='3px solid red'", button)

def click_button(driver, button):
    """Clicks the detected login button."""
    try:
        ActionChains(driver).move_to_element(button).click().perform()
        print("✅ Login button clicked successfully!")
    except Exception as e:
        print(f"⚠️ Failed to click the button: {e}")

def detect_and_click_login(url, auto_click=True):
    """Detects login button using both Selenium and OpenCV."""
    options = Options()
    options.add_argument("--start-maximized")  # Open live browser

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(3)  # Wait for elements to load

    # Try Selenium first
    login_buttons = find_login_button_selenium(driver)

    if login_buttons:
        print(f"🔍 Found {len(login_buttons)} login button(s) using Selenium.")
        for btn in login_buttons:
            highlight_button(driver, btn)
            print(f"➡ Detected: {btn.text} at {btn.location}")

            if auto_click:
                click_button(driver, btn)
    else:
        print("❌ No login button detected via Selenium. Using OpenCV...")

        # Take a screenshot and use OpenCV
        screenshot_path = capture_screenshot(driver)
        detected_buttons = find_login_button_opencv(screenshot_path)

        if detected_buttons:
            print(f"🔍 Found {len(detected_buttons)} login button(s) using OpenCV.")
            for (x, y, w, h) in detected_buttons:
                print(f"📍 Detected button at: x={x}, y={y}, width={w}, height={h}")
        else:
            print("❌ No login button detected.")

    driver.quit()

if __name__ == "__main__":
    url = "https://tublian.com"  # Change to any website
    detect_and_click_login(url, auto_click=True)
