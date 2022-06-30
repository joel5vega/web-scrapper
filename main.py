from bs4 import BeautifulSoup
url = 'https://directoriodecarga.com/bolivia/?&sector=&pais=BO&clave=&pag='
with open  ('home.html','r') as html_file:
    content =html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # empresas = soup.find_all('h2')
    empresas = soup.find_all('a',class_="tooltip-1")
    for empresa in empresas:
        print(empresa.ref)
        print(empresa.text.strip())
    