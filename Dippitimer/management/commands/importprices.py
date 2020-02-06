from django.core.management.base import BaseCommand, CommandError
from Dippitimer.models import *
from bs4 import BeautifulSoup
import requests
class Command(BaseCommand):
    help = 'Do the pricing'


    def handle(self, *args, **options):
        url='https://www.corabastos.com.co/sitio/historicoApp2/reportes/prueba.php'
        cat = ['Hortalizas/Verduras','Frutas','Tuberculos','Platanos','Granos y Procesados', 'Lacteos', 'Carnes y Pescados', 'Huevos']
        page = requests.get(url, verify=False)
        content = page.text
        soup = BeautifulSoup(content, 'html.parser')
        table = soup.find_all("table")
        for index,tables in enumerate(table):
            headers = [header.text.replace('\n','').replace('\t','') for header in tables.find_all('th')]
            results = [{headers[i]: cell.text for i, cell in enumerate(row.find_all('td'))}
            for row in tables.find_all('tr')]
            results.pop(0)
            for result in results:
                Nombre = (result.get('Nombre'))
                Unidad = (result.get ('  Unidad'))
                Precio = (int(result.get('  Valor x Unidad').replace('$','').replace(',','')))
                ing = Ingrediente(nombre = Nombre, unidad = Unidad, preciohoy = Precio, categoria = cat[index])
                ing.save()
        