import requests

from rich.console import Console
from rich.table import Table 

planet_url ="https://swapi.info/api/planets"

url_to_send = planet_url 

response = requests.get(url_to_send)

data = response.json() 

console = Console()
table = Table(title="Star Wars Planets")


table.add_column("NAME", style="cyan")
table.add_column("DIAMETER", style="magenta")
table.add_column("POLULATION", style="green")

for planet in data: 
    table.add_row(planet["name"], planet["diameter"], planet["population"])

console.print(table)