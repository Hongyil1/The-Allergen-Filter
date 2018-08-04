import requests
import time
import random
from bs4 import BeautifulSoup
from requests import adapters

# Get a pool of proxy
def get_proxy_list(old_proxy_list):
    """
    This function scrapes free proxy from https://free-proxy-list.net/
    :return: A list of proxy, length is 30. e.g. ['36.67.227.195:8080', '74.116.59.8:53281']
    """
    url = "https://free-proxy-list.net/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    s = requests.Session()

    try:
        r = s.get(url, headers=headers)
    except:
        # Use loop to solve the connection problem
        r = ''
        while r == '':
            try:
                proxy = random.choice(old_proxy_list)
                r = s.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
                break
            except:
                print("Connection refused by the server, change proxy.")
                continue

    soup = BeautifulSoup(r.text, "lxml")
    s.close()

    proxy_list = []
    tag_tbody = soup.find("tbody")
    tag_trs = tag_tbody.find_all("tr")
    for tr in tag_trs:
        tag_tds = tr.find_all("td")
        proxy = tag_tds[0].text + ":" + tag_tds[1].text
        proxy_list.append(proxy)

    # leave the first 30 proxy
    proxy_list = proxy_list[:30]
    return proxy_list

# Get data from Coles:
def get_from_cloes(brand, item_name, proxy_list):
    coles_search_url = 'https://shop.coles.com.au/a/a-national/everything/search/'
    # pre-process the brand variable and item_name variable
    brand = brand.strip().lstrip()
    item_name = item_name.strip().lstrip()
    brand = brand.replace(" ", "%20")
    item_name = item_name.replace(" ", "%20")
    request_url = coles_search_url + brand + "%20" + item_name

    # Send request to Coles website
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    s = requests.Session()
    s.keep_alive = False

    try:
        r = s.get(requests_url, headers=headers)
    except:
        # Use loop to solve the connection fail
        r = ''
        while r == '':
            print("Connection refused by the server, change proxy.")
            proxy = random.choice(proxy_list)
            r = s.get(requests_url, headers=headers, proxies={"http": proxy, "https": proxy})

    soup = BeautifulSoup(r.text, 'lxml')
    s.close()


    return  request_url


if __name__ == "__main__":
    # old_proxy_list = ['186.42.215.30:53281', '103.15.241.225:53281']
    # proxy_list = get_proxy_list(old_proxy_list)
    # print(proxy_list)
    # requests_url = get_from_cloes("french fries", "  original  ")
    # print(requests_url)
    # url = "https://shop.coles.com.au/a/a-national/everything/browse/bread-bakery/packaged-bread-bakery?pageNumber=1"
    url = "https://shop.coles.com.au/a/a-national/product/tip-top-bread-cafe-raisin-loaf-extra-thick"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    s = requests.Session()
    s.keep_alive = False

    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    print(soup)
    # link = soup.find_all("a", {"class": "shelfProductTile-descriptionLink"})
    # for a in link:
    #     print(a.text())
    # print(link)
    # product_brand = soup.find_all('span', {"class": "product-brand"})
    # print(product_brand)
    # for a in product_brand:
    #     print(a.text())
    # divs_product = soup.find_all("div", class_="product")
    # print(divs_product)
    # for div_product in divs_product:
    #     print(divs_product)
    #     product_brand = div_product.find('span', {"class": "product-brand"})
    #     product_name = div_product.find('span', {"class": "product-name"})
    #     print("brand: ", product_brand, "name: ", product_name)

