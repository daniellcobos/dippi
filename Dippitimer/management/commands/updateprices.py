from django.core.management.base import BaseCommand, CommandError
from Dippitimer.models import *
from bs4 import BeautifulSoup
import requests
class Command(BaseCommand):
    help = 'Do the pricing'
    

    def handle(self, *args, **options):
        url='https://www.corabastos.com.co/sitio/historicoApp2/reportes/prueba.php'
        
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
                Precio = (int(result.get('  Valor x Unidad').replace('$','').replace(',','')))
                ings = Ingrediente.objects.filter(nombre = Nombre)
                for ing in ings:
                    ing.precioayer = ing.preciohoy
                    ing.preciohoy = Precio
                    ing.descuento =  False if ing.precioayer <= ing.preciohoy else True
                    ing.save()
        for plato in Plato.objects.all():
            preciohoy = 0
            for li in ListaIngredientes.objects.filter(plato = plato):
                try:
                    # ppi (precio por ingrediente)
                    ppi = li.cantidad * li.ingrediente.preciohoy
                    preciohoy= preciohoy + ppi
                except Exception:
                    self.stdout.write(Exception)
            plato.precioayer = plato.preciohoy
            plato.preciohoy = preciohoy
            plato.descuento =  False if plato.precioayer < plato.preciohoy else True
            plato.save()