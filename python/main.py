
from selenium import webdriver
import time

URL = 'https://www.federalpay.org/paycheck-protection-program/nd/58503' 


driver = webdriver.Chrome( executable_path="../chromedriver.exe" )

driver.get(URL)
time.sleep(8)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# div = soup.select_one("ppp-loans")
# table = pd.read_html(soup)
# print(table[0])
# pd.read_table()
output = driver.find_element_by_xpath('//*[@id="ppp-loans"]').text
# time.sleep(4)

output_split = output.split('\n')
output_split = output_split[1:]

with open("../temp.txt", "w") as f:
    f.write('\n'.join(output_split))

driver.close()


