import requests
from bs4 import BeautifulSoup
all_quotes=[]
url="https://quotes.toscrape.com"
page="/page/1/"
while page:
    res=requests.get(f"{url}{page}")
    print(f"srapping {url}{page}")
    soup = BeautifulSoup(res.text, "html.parser")
    # print(soup.body)
    quotes=soup.find_all(class_="quote")
    for quote in quotes:
        # print()
        all_quotes.append({
            "quote":quote.find(class_="text").get_text(),
            "author":quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"]
        })
    next_btn=soup.find(class_="next")
    page=next_btn.find("a")["href"] if next_btn else None


print(all_quotes)    