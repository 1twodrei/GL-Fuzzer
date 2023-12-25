from selenium import webdriver
from urllib.parse import quote

# Load payload parameters from the file
with open('/payload-parameters.txt', 'r') as file:
    payload_parameters = [line.strip() for line in file.readlines() if line.strip()]

# Assuming you have a vulnerable URL to test
vulnerable_url = 'https://example.com/vulnerable_endpoint'

# Initialize the Chrome WebDriver (you can use other browsers too)
driver = webdriver.Chrome()

# Loop through each payload parameter
for parameter in payload_parameters:
    # Construct the URL with the parameter to test
    url_with_payload = f"{vulnerable_url}?input={quote(parameter)}"

    # Open the URL
    driver.get(url_with_payload)

    # Check if an alert is present (indicating potential XSS)
    try:
        alert = driver.switch_to.alert
        print(f"XSS Possible with parameter: {parameter}")
        alert.dismiss()  # Dismiss the alert
    except:
        pass  # No alert found

# Close the browser session
driver.quit()
