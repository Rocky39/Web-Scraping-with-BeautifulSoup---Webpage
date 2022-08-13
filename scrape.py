# 1. Import Libraries
from bs4 import BeautifulSoup
import requests
from csv import writer

# 2. Connect to Webpage-URL that shall be scrapped
url = "https://www.pararius.com/apartments/amsterdam"
page = requests.get(url)
# print(page) (only needed for check after connecting to Webpage-URL)

# 3. Create an Object-Soup
soup = BeautifulSoup(page.content, 'html.parser') # get content of the webpage

# 4. Search for all sections with the class-name 'xxx' (section)
lists = soup.find_all('section', class_="listing-search-item")

# Final: Download to CSV
with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)

    # 5. Connect to HTML-elements
    for list in lists:
        title = list.find('a', class_="listing-search-item__link listing-search-item__link--title").text.replace('\n','')
        location = list.find('div', class_="listing-search-item__sub-title").text.replace('\n', '')
        price = list.find('div', class_="listing-search-item__price").text.replace('\n', '')
        area = list.find('li', class_="illustrated-features__item illustrated-features__item--surface-area").text.replace('\n', '')

    # 6. Check if scraping was successful (only needed for check after setting connections to HTML-Elements)
    # info = [title, location, price, area]
    # print(info)

        # Final: Download to CSV
        info = [title, location, price, area]
        thewriter.writerow(info)