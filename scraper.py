import requests
from bs4 import BeautifulSoup

urls = {
    "coop" : "https://www.coop.co.uk/products/deals/lunchtime-meal-deal"
}

page = requests.get(urls.get("coop"))
pageText = page.text
cardCount = pageText.count("""<article class="coop-c-card coop-c-card--product coop-c-card--alcohol coop-l-flex__item">""")
print(f"Number of food items found: {cardCount}")

soup = BeautifulSoup(pageText, 'html.parser')



allItems = soup.find_all("h3", class_="coop-c-card__title")
allPrices = soup.find_all("span", class_="coop-u-member-deal-blue")
itemPrices = []
for price in allPrices:
    # print(price.get_text())
    itemPrices.append(price.get_text())
mains = soup.find(id="mains")

# food_sections = soup.find_all('div', class_='food-l-section')
# mainSoup = (food_sections[0])

# mainCount = 
print(f"Mains: ")
print(f"Sides: ")
print(f"Drinks: ")

print("Entire Menu:")
itemNames = []
itemWeights = []
for item in allItems:
    itemStr = str(item).split(">")[1].replace("</h3", "").replace("&amp;", "&")
    listSpaced = itemStr#.split(" ")[:-1]
    itemName = str(listSpaced.split(" ")[:-1]).replace("[", "").replace("]", "").replace(",", "",).replace("\'", "") #str(item).split(">")[1].replace("</h3", "").replace("&amp;", "&")
    itemWeight = listSpaced.split(" ")[-1]
    if itemWeight == "Sandwich":
        itemWeight = "Unknown"
    
    # print(f"{itemName} - {itemWeight}")
    itemNames.append(itemName)
    itemWeights.append(itemWeight)


for i in range(0, len(itemNames)):
    print(f"Item: {itemNames[i]}, Weight: {itemWeights[i]}, Price: {itemPrices[i]}")