from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Discord login credentials
DISCORD_EMAIL = "discordalt5081@gmail.com"
DISCORD_PASSWORD = "SatyaJojo*1"

# Channel URL
CHANNEL_URL = "https://discord.com/channels/1231677046019850301/1263420640590037023"  # Replace with actual server and channel IDs

def login_to_discord(driver):
    driver.get("https://discord.com/login")
    time.sleep(5)  # Wait for the login page to load

    email_field = driver.find_element("name", "email")
    password_field = driver.find_element("name", "password")

    email_field.send_keys(DISCORD_EMAIL)
    password_field.send_keys(DISCORD_PASSWORD)
    email_field.send_keys(Keys.RETURN)

    time.sleep(10)  # Allow time for login to complete

def send_bump_command(driver):
    driver.get(CHANNEL_URL)
    time.sleep(5)  # Wait for the channel to load

    # Locate the message input box
    message_box = driver.switch_to.active_element
    message_box.send_keys("/")
    time.sleep(1)  # Wait for autocomplete suggestions to appear

    # Type "bump" and select it from the autocomplete menu
    message_box.send_keys("bump")
    time.sleep(1)  # Wait for the autocomplete to update
    message_box.send_keys(Keys.TAB)  # Select the `/bump` command from autocomplete
    message_box.send_keys(Keys.RETURN)  # Execute the command

    print("Bump command sent successfully.")
    time.sleep(2)  # Pause briefly to ensure the command executes

def main():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed and set up
    try:
        login_to_discord(driver)
        while True:
            send_bump_command(driver)
            time.sleep(7200)  # Wait 2 hours before bumping again
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
