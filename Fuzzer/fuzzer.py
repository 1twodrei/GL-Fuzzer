from selenium import webdriver
from urllib.parse import quote

with open('/payload-parameters.txt', 'r') as file:
    payload_parameters = [line.strip() for line in file.readlines() if line.strip()]


vulnerable_url = 'https://example.com/vulnerable_endpoint'

driver = webdriver.Safari()

for parameter in payload_parameters:
    url_with_payload = f"{vulnerable_url}?input={quote(parameter)}"

    driver.get(url_with_payload)

    # Check if an alert is present (indicating potential XSS)
    try:
        alert = driver.switch_to.alert
        print(f"XSS Possible with parameter: {parameter}")
        alert.dismiss()  # Dismiss the alert
    except:
        pass  # No alert

driver.quit()
