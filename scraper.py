import requests
from bs4 import BeautifulSoup

urls = {
    "coop" : "https://www.coop.co.uk/products/deals/lunchtime-meal-deal"
}


page = requests.get(urls.get("coop"))

pageText = page.text
cardCount = pageText.count("""<article class="coop-c-card coop-c-card--product coop-c-card--alcohol coop-l-flex__item">""")

soup = BeautifulSoup(pageText, 'html.parser')
def soupToSandwich(soup):
    """Turn messy web soup of food items into clean list of food items"""
    cleanList = []
    for item in soup:
        itemStr = str(item).split(">")[1].replace("</h3", "").replace("&amp;", "&")
        listSpaced = itemStr#.split(" ")[:-1]
        itemName = str(listSpaced.split(" ")[:-1]).replace("[", "").replace("]", "").replace(",", "",).replace("\'", "") #str(item).split(">")[1].replace("</h3", "").replace("&amp;", "&")
        cleanList.append(itemName)
    return cleanList

mainFoodSection = soup.select("#mains .coop-c-card__title")
mainFoods = soupToSandwich(mainFoodSection)
sideFoodSection = soup.select("#snacks .coop-c-card__title")
sideFoods = soupToSandwich(sideFoodSection)
drinkSelection = soup.select("#drinks .coop-c-card__title")
drinks = soupToSandwich(drinkSelection)


print(f"{len(mainFoods)} Mains:")
print(mainFoods)
print(f"{len(sideFoods)} Sides:")
print(sideFoods)
print(f"{len(drinks)} Drinks:")
print(drinks)
allFoods = mainFoods + sideFoods + drinks
print(f"Total items found: {len(allFoods)}")

allPrices = soup.find_all("span", class_="coop-u-member-deal-blue")
itemPrices = []
for price in allPrices:
    # print(price.get_text())
    itemPrices.append(float(price.get_text().replace("£", "")))
mains = soup.find(id="mains")

#Establish dict of all foods and their prices
foodPrices = {allFoods[i]: itemPrices[i] for i in range(len(allFoods))}


def price(item):
    """Gets the price of an item"""
    return foodPrices.get(item)

#Find best value Main
maxPrice = 0
bestMain = None
for m in mainFoods:
    foodPrice = price(m)
    if foodPrice > maxPrice:
        maxPrice = foodPrice
        bestMain = m

maxPrice = 0
bestSide = None
for s in sideFoods:
    foodPrice = price(s)
    if foodPrice > maxPrice:
        maxPrice = foodPrice
        bestSide = s

maxPrice = 0
bestDrink = None
for d in drinks:
    foodPrice = price(d)
    if foodPrice > maxPrice:
        maxPrice = foodPrice
        bestDrink = d

bestMainPrice = price(bestMain)
bestSidePrice = price(bestSide)
bestDrinkPrice = price(bestDrink)
mealDealPrice = 4.0
print("\n----------------------------")
print("Best meal deal calculated (price):")
print(f"Main: {bestMain} (£{bestMainPrice})")
print(f"Side: {bestSide} (£{bestSidePrice})")
print(f"Drink: {bestDrink} (£{bestDrinkPrice})")
totalValue = bestMainPrice+bestSidePrice+bestDrinkPrice
print(f"Total value: £{totalValue}")
print(f"Actually paid: £{mealDealPrice}")
print(f"Money saved: £{totalValue - mealDealPrice}")
