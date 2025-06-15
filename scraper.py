from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Open the nopCommerce demo website
driver.get("https://demo.nopcommerce.com/")
time.sleep(2)

# Find all product elements
products = driver.find_elements(By.CLASS_NAME, "product-item")

# Create and open a CSV file to save product data
with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price"])  # Write header row

    # Extract and write product name and price
    for product in products:
        try:
            name = product.find_element(By.CLASS_NAME, "product-title").text
            price = product.find_element(By.CLASS_NAME, "actual-price").text
            writer.writerow([name, price])
        except Exception as error:
            print("Skipped one product due to error:", error)

# Close the browser
driver.quit()
print("✅ Scraping completed.")
