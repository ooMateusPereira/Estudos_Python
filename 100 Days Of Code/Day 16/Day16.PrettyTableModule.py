from prettytable import PrettyTable
table = PrettyTable()

# table.field_names = ('Pokemon Name', 'Type')
# table.add_row(['Pikachu', 'Eletric'])
# table.add_row(['Squirtle', 'Water'])
# table.add_row(['Charmander', 'Fire'])

# Another way to do the same thing.

table.add_column('Pokemon Name', ['Pakachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Eletric', 'Water', 'Fire'])
table.align = 'l'
print(table)