import requests
from bs4 import BeautifulSoup
urls = {
    "tesco1" : "https://www.tesco.com/groceries/en-GB/shop/fresh-food/chilled-soup-sandwiches-and-salad-pots/lunch-meal-deals/all?shelf=%C2%A33.90%20Meal%20Deal%20Mains&viewAll=shelf",
    "tesco2" : "https://www.tesco.com/groceries/en-GB/shop/fresh-food/chilled-soup-sandwiches-and-salad-pots/lunch-meal-deals/all?shelf=Meal%20Deal%20Snacks&viewAll=shelf",
    "tesco3" : "https://www.tesco.com/groceries/en-GB/shop/fresh-food/chilled-soup-sandwiches-and-salad-pots/lunch-meal-deals/all?shelf=Meal%20Deal%20Drinks&viewAll=shelf"
}

headers = {
    'authority': 'www.tesco.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'consumer=default; DCO=wdc; _csrf=JdB2EVbKeEj5Im8hQLg278wy; ighs-sess=eyJhbmFseXRpY3NTZXNzaW9uSWQiOiJkYWIxNTM3YmU0Mjc0NmI4ZDBiNTBhOTI0ZWQ1YzQyNyIsInN0b3JlSWQiOiIzMDYwIn0=; ighs-sess.sig=XjgYRV8U-5JLkVFVRRVKaxmIbs8; AKA_A2=A; atrc=5ae7a4e1-72ae-4eb3-af2a-1015c5af6f5b; ak_bmsc=0673F5F840A7C04FB135D44CE7DFE190~000000000000000000000000000000~YAAQQ6ATAtr8BTWOAQAApmQyORfFIl+SMtkL87o99oQs8Q7WDc7dcJ5+8IpTm1Skz8ltu+xI7pFtt10VD9z06105FozDchxNhAJSIM2Q0NUUoSXsIYucgd13Loyb9mpIa9ZuWxGrV2IpabCrSAazJYPR61gQ3w2iwqBWfZdU2eNUQHqAn1qNEOVNEBJvIf60SlbFleJ6lT58QBENdMbeWinRr45f7SQUD0QkRCD+TH4xkSbRFa8W8P6n5ypuGGQ+nnLng20AKeWz8i+GTRa4/8tJ7qpxMtKHJ4keXrAQWSfDgjo0+WBWq3YOeJNc3rBDKbb8/9+7OU+qWis8SFH6TDnRsxceHoqVjghzav9XznasyvB/y5qNvt+2TmFPwX2yxgMTWU9io1ympBDHUKK6zIAZOe4Dc2ocPkPrfCe+85c84tRwrBu6GfPsqSq/gjGGkf9TLuWXucDbn8Wm2GDbFJ130iMcsFFG7MFFnQwb9VO1Ca25bJEdNdhWEPp2cTCgfrPzpyACayDW1w==; bm_mi=CA064F6D23AEB3DD6C93B1B1D444479E~YAAQQ6ATAtv8BTWOAQAApmQyORdUcD0r+SwyzwZcX/xiWGjsLJXc0s5qy6wnEhDERKLvniqqW1cqhaLwC+PGAETKupwvOgxRknY/2tiZ3xr0SuxFf3ZbyhQxaphMyF/jX4bdt8YPewxmgHUTsgDZDw8SHjTzNcuD/CYQF+l7JZ18MWeDPqfrQzqxqtaYarwVNINz1XH5rZdcQ91m+s6BU6w3HSMtDEACeZgkIYdfPiLdZ38T7f//IlF04Ed2pTuEkHzlX0kIBzLbkBoAueJtfgSna246zPdY0K+5gZa8m1jfyf3weCvldFdQI22oN0rhmlJf+1A0DHo0B0Q1LOGOgRSKEBRe0FPvqJSd9e0HVPl9aSjYl7JPaYh76indq6eytVJWY7GCqGYGsta1moJQixA5FjrNzV6wZrgRGrxhuGh0Z9qf149I/g==~1; bm_sz=656F0D2097DFD266060E9EE8CC7A6F48~YAAQQ6ATAt38BTWOAQAApmQyORf/Jy7VhXYhiakwL9W3bJKC3+qxEPuaHmTZkE2Zg4aWLjUNLaXE9VcP8C7vnRqm1vJs+X8uM/7uJKi41B8MX7yhI0T07ESLK7PNA4Gbfwx1cgC/2/cR7968K1UM7nzwOWdTfoLfSrQcObcsCuQEGMfwgmmzp9UgubzISwD3P2Ndd+UkkX7Dw6HSEFJCNh6YA28F6DJ5xpKfakhLyBEOjVBAb46VFHtz6LbzlgYKX8I3D86pW4j8zeZJsF+YXaKC2SEWaUJxV2Xub8rJ8k+Dky3ilkztEWb+ppCS6C+2lUcaAWQH1k4O6ZtDyumPDGk1FejeoeUkV2zIo53NSobnCyj9nkrA~3486017~3425588; akavpau_tesco_groceries=1710356890~id=0a6aba9069c1a13d8d3ceea12107f4bc; _abck=983094A90C2661F7A949A3048D186CDC~-1~YAAQNqATAt0NrTaOAQAAK6E0OQshF7psWfplPB60JMiaAnvxD6ut1KfuRi8JhwnzGN4cCQBILczcLpedzJVq5PKx5IQMdI88rCVh0PlO/jp/2Bwa20qNiqNp+5KB5ooLJqGAXk7efMD/l7BwB0Rh9Vk10cae96amsakQDMcTLA4o3ohwbgrRlYG/F4eUxFlgJZgqv0yVgURKtBV3V/sVgGCRwDvEYe4/AiJsoKiMlyPs3c0gaZrycrs7omhONGVt3oO1I7EYLFkf1YzGU0RTFtz15LiMOet7OWnbvAb00HMJEUqWluT3qJtKL2e1VDUf6X8gpI2L6Q8PXV/spdzSFwSxG8uEmo3vOF9kZOQgcCA5jvb2BICfeBclJgs20qXzt1F8bhAa79EJ~-1~-1~1710360188; bm_sv=7BA4C23BC1A25074192B93713E358FDF~YAAQHKATAsojwjWOAQAAZSA5ORc22Mhw+tWFs79iXYjdp82WOsaW8Cq9n7hfD2rovzHd5k1rsK6d+0tiqhAiOFdkcS9CkFOnf5F9qsftEZfkQHPW5VqW77B306y4S9wqNvF7FVzQdI/KirSRpP/uiwD2bm5uQ6fdWg1wcz00/SNl0clPSIVO563p3oV+7FOh+tNUd+omf0Gw5qlvDcZyCkgY9sS0iDNadTkNYDnVobaeS1l/GuuxNv8u8TbeDPE=~1',
    'referer': 'https://www.tesco.com/groceries/en-GB/shop/fresh-food/chilled-soup-sandwiches-and-salad-pots/lunch-meal-deals/all?shelf=%C2%A33.90%20Meal%20Deal%20Mains&viewAll=shelf',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

print("\nTesco Deals")
mealPage = requests.get(urls.get("tesco1"), headers=headers, allow_redirects=True)
snackPage = requests.get(urls.get("tesco2"), headers=headers)
drinkPage = requests.get(urls.get("tesco3"), headers=headers)

mealPageText = mealPage.text

print(mealPageText)
snackPageText = snackPage.text
drinkPageText = drinkPage.text

# mealPageSoup = BeautifulSoup(mealPageText, 'html.parser')
# snackPageSoup = BeautifulSoup(snackPageText, 'html.parser')
# drinkPageSoup = BeautifulSoup(drinkPageText, 'html.parser')

# pageTexts = [mealPageSoup, snackPageSoup, drinkPageSoup]

# items = mealPageSoup.find_all(class_="product-list--list-item")
# print(items)
# # for page in pageTexts:
# #     #Count items
# #     items = page.find(class_="product-list--list-item")
# #     print(items)