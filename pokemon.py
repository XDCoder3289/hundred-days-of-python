from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Chalmander", "Bubblasaurus"]) 
table.add_column("Pokemon Type", ["Electric", "Fire", "Water"])

print(table)
