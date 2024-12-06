from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Replace these with your Discord login credentials and channel URL
DISCORD_EMAIL = "discordalt5081@gmail.com"
DISCORD_PASSWORD = "SatyaJojo*1"
CHANNEL_URL = "https://discord.com/channels/1231677046019850301/1263420640590037023"

def main():
    # Setup Chrome WebDriver with options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("Opening Discord...")
        driver.get("https://discord.com/login")
        time.sleep(5)

        # Log in to Discord
        email_box = driver.find_element(By.NAME, "email")
        email_box.send_keys(DISCORD_EMAIL)

        password_box = driver.find_element(By.NAME, "password")
        password_box.send_keys(DISCORD_PASSWORD)
        password_box.send_keys(Keys.RETURN)
        print("Logging in...")
        time.sleep(10)

        # Navigate to the channel
        print(f"Navigating to channel: {CHANNEL_URL}")
        driver.get(CHANNEL_URL)
        time.sleep(10)

        # Locate the message box
        print("Looking for the message box...")
        message_box = driver.find_element(By.CSS_SELECTOR, "div[role='textbox']")

        # Type and send /bump
        print("Sending /bump...")
        message_box.click()
        message_box.send_keys("/bump")
        message_box.send_keys(Keys.RETURN)

        print("Bump command sent successfully!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
