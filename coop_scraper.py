import requests
from bs4 import BeautifulSoup

urls = {
    "coop" : "https://www.coop.co.uk/products/deals/lunchtime-meal-deal",
}


print("\nCoop Deals")
print(f"Connecting to: {urls.get('coop')}")
page = requests.get(urls.get("coop"))

pageText = page.text

cardCount = pageText.count("""<article class="coop-c-card coop-c-card--product coop-c-card--alcohol coop-l-flex__item">""")

soup = BeautifulSoup(pageText, 'html.parser')
def soupToSandwich(soup):
    """Turn messy web soup of food items into clean list of food items"""
    cleanList = []
    for item in soup:
        itemStr = str(item).split(">")[1].replace("</h3", "").replace("&amp;", "and").replace("&", "and")
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
minPrice = 10.0
bestMain = None
worstMain = None
for m in mainFoods:
    foodPrice = price(m)
    if foodPrice >= maxPrice:
        maxPrice = foodPrice
        bestMain = m
    if foodPrice < minPrice:
        minPrice = foodPrice
        worstMain = m

maxPrice = 0
minPrice = 10.0
bestSide = None
worstSide = None
for s in sideFoods:
    foodPrice = price(s)
    if foodPrice >= maxPrice:
        maxPrice = foodPrice
        bestSide = s
    if foodPrice < minPrice:
        minPrice = foodPrice
        worstSide = s
maxPrice = 0
minPrice = 10.0
bestDrink = None
worstDrink = None
for d in drinks:
    foodPrice = price(d)
    if foodPrice >= maxPrice:
        maxPrice = foodPrice
        bestDrink = d
    if foodPrice < minPrice:
        minPrice = foodPrice
        worstDrink = d
mealDealPrice = 4.0
def toMoney(num):
    money = '{:.2f}'.format(num)
    return money

bestMainPrice = price(bestMain)
bestSidePrice = price(bestSide)
bestDrinkPrice = price(bestDrink)

print("----------------------------")
print("Best meal deal calculated (price):")
print(f"Main: {bestMain} (£{toMoney(bestMainPrice)})")
print(f"Side: {bestSide} (£{toMoney(bestSidePrice)})")
print(f"Drink: {bestDrink} (£{toMoney(bestDrinkPrice)})")
totalValue = bestMainPrice+bestSidePrice+bestDrinkPrice
print(f"Total value: £{toMoney(totalValue)}")
print(f"Actually paid: £{toMoney(mealDealPrice)}")
print(f"Money saved: £{toMoney(totalValue - mealDealPrice)}")

worstMainPrice = price(worstMain)
worstSidePrice = price(worstSide)
worstDrinkPrice = price(worstDrink)
print("\n----------------------------")
print("Worst meal deal calculated (price):")
print(f"Main: {worstMain} (£{toMoney(worstMainPrice)})")
print(f"Side: {worstSide} (£{toMoney(worstSidePrice)})")
print(f"Drink: {worstDrink} (£{toMoney(worstDrinkPrice)})")
totalValue = worstMainPrice+worstSidePrice+worstDrinkPrice
print(f"Total value: £{toMoney(totalValue)}")
print(f"Actually paid: £{toMoney(mealDealPrice)}")
print(f"Money saved: £{toMoney(totalValue - mealDealPrice)}")

