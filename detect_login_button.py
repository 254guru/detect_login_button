import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def capture_screenshot(url, output_file="screenshot.png"):
    """Captures a screenshot of the given URL and returns the WebDriver instance."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1280x800")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    driver.save_screenshot(output_file)
    print(f"📸 Screenshot saved as {output_file}")

    return driver, output_file

def find_login_button(driver):
    """Detects login/sign-in buttons dynamically from a webpage."""
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")

    login_keywords = ["login", "log in", "sign in"]
    detected_buttons = []

    for element in buttons + links:
        text = element.text.strip().lower()
        if any(keyword in text for keyword in login_keywords):
            detected_buttons.append((element, element.location))

    return detected_buttons

def highlight_button(driver, button):
    """Adds a red border around the detected login button."""
    driver.execute_script("arguments[0].style.border='3px solid red'", button)

def click_button(driver, button):
    """Simulates a click on the detected login button in a new tab."""
    try:
        ActionChains(driver).move_to_element(button).key_down(Keys.CONTROL).click().key_up(Keys.CONTROL).perform()
        print("✅ Login button clicked successfully in a new tab!")
    except Exception as e:
        print(f"⚠️ Failed to click the button: {e}")

def detect_and_click_login(url, auto_click=True):
    """Full pipeline: Detects, highlights, and optionally clicks the login button."""
    driver, screenshot_before = capture_screenshot(url)
    login_buttons = find_login_button(driver)

    if login_buttons:
        print(f"🔍 {len(login_buttons)} login button(s) detected.")
        coordinates_list = []
        for btn, coords in login_buttons:
            highlight_button(driver, btn)
            coordinates_list.append(coords)
            print(f"🔵 Button: {btn.text} at {coords}")

            if auto_click:
                click_button(driver, btn)

        # Capture another screenshot after highlighting
        screenshot_after = "highlighted_screenshot.png"
        driver.save_screenshot(screenshot_after)
        print(f"📸 Updated screenshot saved as {screenshot_after}")

        return driver, coordinates_list, screenshot_after
    else:
        print("❌ No login button detected.")
        driver.quit()
        return None, None, None

if __name__ == "__main__":
    url = input("🌐 Enter website URL: ").strip()
    detect_and_click_login(url, auto_click=True)
