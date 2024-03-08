from bs4 import BeautifulSoup

# Assuming 'html_content' contains the HTML content of the webpage you're scraping
# You can obtain it using requests or any other method

html_content = """
<html>
  <body>
    <div class="food-l-section plp-manual food-u-colour-bg--">...</div>
    <div class="food-l-section plp-manual food-u-colour-bg--">...</div>
    <div class="other-section">...</div>
  </body>
</html>
"""

# Parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all div elements with the class "food-l-section"
food_sections = soup.find_all('div', class_='food-l-section')

# Print or process the found elements
for section in food_sections:
    print(section)