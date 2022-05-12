from bs4 import BeautifulSoup

with open  ('home.html','r') as html_file:
    content =html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    empresas = soup.find_all('h2')

    for empresa in empresas:
        print(empresa.text.strip())
    