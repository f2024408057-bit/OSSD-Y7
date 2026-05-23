import requests
from bs4 import BeautifulSoup
import csv

# Function to get car data
def get_car_data(car):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = f'https://www.pakwheels.com/new-cars/pricelist/{car}'

    response = requests.get(url, headers=headers)

    cars = []

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        tables = soup.find_all('table')

        for table in tables:

            rows = table.find_all('tr')

            for row in rows:

                cols = row.find_all('td')

                if len(cols) >= 2:

                    name = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)

                    cars.append({
                        'Name': name,
                        'Price': price
                    })

    else:
        print("Page not available!")

    return cars


# Save data to CSV
def save_to_csv(data, filename):

    with open(filename, mode='w', newline='', encoding='utf-8') as file:

        writer = csv.DictWriter(
            file,
            fieldnames=['Name', 'Price']
        )

        writer.writeheader()

        writer.writerows(data)

    print(f"\nData saved in {filename}")


# Interface
print("=" * 40)
print("      PAKWHEELS CAR SCRAPER")
print("=" * 40)

car = input("Enter manufacturer name: ")

data = get_car_data(car)

if data:

    print("\nCars Found:\n")

    for i in data:
        print(i['Name'], "-", i['Price'])

    save_to_csv(data, f"{car}.csv")

else:
    print("No data found")