from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Update these with your Discord credentials
DISCORD_EMAIL = "discordalt5081@gmail.com"
DISCORD_PASSWORD = "SatyaJojo*1"
SERVER_URL = "https://discord.com/channels/1231677046019850301/1263420640590037023"  # Replace with your server's channel URL

def main():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Required for non-root users
    chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid memory issues
    chrome_options.add_argument("--disable-gpu")  # Reduce resource usage
    chrome_options.add_argument("--disable-extensions")  # Prevent interference by extensions

    # Set up the WebDriver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    try:
        # Step 1: Open Discord login page
        driver.get("https://discord.com/login")
        print("Discord login page loaded.")

        # Step 2: Log in to Discord
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys(DISCORD_EMAIL)
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(DISCORD_PASSWORD)
        password_input.send_keys(Keys.RETURN)
        print("Logged in to Discord.")

        # Wait for login to complete
        time.sleep(5)

        # Step 3: Navigate to the server's channel
        driver.get(SERVER_URL)
        print(f"Navigated to server channel: {SERVER_URL}")

        # Wait for the page to load
        time.sleep(5)

        # Step 4: Send the /bump command
        message_box = driver.find_element(By.CSS_SELECTOR, "div[role='textbox']")
        message_box.send_keys("/bump")
        time.sleep(1)  # Wait before pressing enter
        message_box.send_keys(Keys.RETURN)
        print("/bump command sent.")

        # Step 5: Confirm the message was sent (Optional)
        time.sleep(5)
        print("Automation completed successfully.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
