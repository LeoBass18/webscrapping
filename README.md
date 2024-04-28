## Script de Busca e comparação de Preços do PlayStation 5

Este script automatiza a busca por preços do PlayStation 5 em 3 diferentes sites de comércio eletônico escolhidos por mim:
Magazine Luiza, Amazon e Americanas. 
Ele utiliza as bibliotecas Selenium e BeautifulSoup para navegar pelos sites, extrair informações dos produtos e analisar o HTML das páginas.
O scrapping é feito apenas na primeira página de cada site de busca.

### Funcionalidades
- Busca Automática: O script acessa automaticamente os URLs fornecidos dos sites alvo, já com o termo de pesquisa "playstation 5", e busca por produtos relacionados ao PlayStation 5.
- Extração de Informações: Utilizando BeautifulSoup, ele extrai o título e o preço de cada produto encontrado.
- Filtragem por Preço e Título para garantirmos que estamos comparando apenas o produto escolhido: Verifica se o título do produto contém a string "playstation 5" e se o preço é maior ou igual a R$ 3000, descartando produtos irrelevantes.
- Identificação do Produto mais Barato e mais Caro: Registra o produto com o menor e o maior preço encontrado durante a busca.
- Identifica o site onde está o maior e o menor preço.

  As URLs utilizadas foram:

  - Magazine Luiza": "https://www.magazineluiza.com.br/busca/aparelho+console+playstation+5/"
  - Amazon": "https://www.amazon.com.br/s?k=aparelho+playstation+5&s=price-desc-rank&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1MKOLIDHFOX94&qid=1714250653&sprefix=aparelho+playstation+5%2Caps%2C145&ref=sr_st_price-desc-rank&ds=v1%3A77%2FXNoI6NDcEsos2cFwMHEr3eW4p%2BfESslXd2Qm51hk"
  - Americanas": "https://www.americanas.com.br/busca/console-playstation-5"
 
  ### Em 28/04/2024 o resultado da pesquisa foi:


Produto com o menor preço:
Produto: Console PlayStation 5 Standard Edition Branco + Controle Sem Fio Dualsense Branco
Preço: 3437.9
Site: Magazine Luiza

Produto com o maior preço:
Produto: Console PlayStation 5 Standard Edition SSD 825GB + Spider Man 2 com Controle
Preço: 6249.9
Site: Magazine Luiza


# Aluno: Leonardo da Rocha Mello
