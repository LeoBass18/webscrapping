#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup

# Função para converter o preço para um formato numérico
def convert_price(price):
    try:
        return float(price.replace("R$", "").replace(".", "").replace(",", "."))
    except ValueError:
        return None

# Função para verificar se o título contém "playstation 5"
def contains_playstation_5(title):
    return "playstation 5" in title.lower()

# URLs dos sites alvo
urls = {
    "Magazine Luiza": "https://www.magazineluiza.com.br/busca/aparelho+console+playstation+5/",
    "Amazon": "https://www.amazon.com.br/s?k=aparelho+playstation+5&s=price-desc-rank&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1MKOLIDHFOX94&qid=1714250653&sprefix=aparelho+playstation+5%2Caps%2C145&ref=sr_st_price-desc-rank&ds=v1%3A77%2FXNoI6NDcEsos2cFwMHEr3eW4p%2BfESslXd2Qm51hk",
    "Americanas": "https://www.americanas.com.br/busca/console-playstation-5?"
}

# Inicializar o driver do Selenium
driver = webdriver.Chrome()

# Definir um tempo de espera implícito
driver.implicitly_wait(10)

# Dicionário para armazenar os preços mínimos e seus respectivos produtos e sites
min_price = float('inf')
min_price_product = None

# Dicionário para armazenar os preços máximos e seus respectivos produtos e sites
max_price = float('-inf')
max_price_product = None

# Iterar sobre os URLs dos sites alvo
for site, url in urls.items():
    # Acessar o site
    driver.get(url)

    # Criar um objeto BeautifulSoup com o conteúdo HTML da página
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Encontrar todos os elementos que contêm informações dos produtos
    if site == "Magazine Luiza":
        products = soup.find_all("li", {"class": "sc-kTbCBX ciMFyT"})
    elif site == "Amazon":
        products = soup.find_all("div", {"class": "s-result-item"})
    elif site == "Americanas":
        products = soup.find_all("div", {"class": "inStockCard__Wrapper-sc-1ngt5zo-0 iRvjrG"})

    # Iterar sobre os elementos dos produtos e extrair as informações desejadas
    for product in products:
        # Título do produto
        if site == "Magazine Luiza":
            title_element = product.find("h2", {"class": "sc-fvwjDU fbccdO"})
        elif site == "Amazon":
            title_element = product.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"})
        elif site == "Americanas":
            title_element = product.find("h3", {"class": "styles__Name-sc-1e4r445-0 fYqJrQ product-name"})

        if title_element:
            title = title_element.text.strip()
        else:
            title = "N/A"

        # Verificar se o título contém "playstation 5"
        if not contains_playstation_5(title):
            continue

        # Preço do produto
        if site == "Magazine Luiza":
            price_element = product.find("p", {"class": "sc-kpDqfm eCPtRw sc-bOhtcR dOwMgM"})
        elif site == "Amazon":
            price_element = product.find("span", {"class": "a-offscreen"})
        elif site == "Americanas":
            price_element = product.find("span", {"class": "src__Text-sc-154pg0p-0 styles__PromotionalPrice-sc-yl2rbe-0 dthYGD list-price"})

        if price_element:
            price = convert_price(price_element.text.strip())
        else:
            price = None

        # Atualizar o preço mínimo e o produto correspondente, se aplicável
        if price is not None and price >= 3000:
            if price < min_price:
                min_price = price
                min_price_product = (title, site)
            if price > max_price:
                max_price = price
                max_price_product = (title, site)

# Fechar o driver do Selenium após a conclusão
driver.quit()

# Exibir o produto com o menor preço
if min_price_product:
    print("Produto com o menor preço:")
    print("Produto:", min_price_product[0])
    print("Preço:", min_price)
    print("Site:", min_price_product[1])
else:
    print("Nenhum produto encontrado.")

# Exibir o produto com o maior preço
if max_price_product:
    print("Produto com o maior preço:")
    print("Produto:", max_price_product[0])
    print("Preço:", max_price)
    print("Site:", max_price_product[1])
else:
    print("Nenhum produto encontrado.")


# In[ ]:




