#!/usr/bin/env python

print('Content-Type: text/html\r\n\r\n')

# Laden der Bestelldaten aus der Textdatei
orders = []
with open('warenkorb.txt', 'r') as file:
    for line in file:
        order = line.strip().split(',')
        orders.append(order)

# Anzeigen der Bestellübersicht
print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print('  <meta charset="UTF-8">')
print('  <title>Bestellübersicht</title>')
print('  <link rel="stylesheet" type="text/css" href="style.css">')
print('</head>')
print('<body>')
print('  <div class="container">')
print('    <h1>Bestellübersicht</h1>')
print('    <table>')
print('      <tr>')
print('        <th>Artikel</th>')
print('        <th>Menge</th>')
print('        <th>Name</th>')
print('        <th>Werk/Abteilung</th>')
print('        <th>Kostenstelle</th>')
print('      </tr>')

for order in orders:
    artikel, menge, name, werk, kostenstelle = order
    print('      <tr>')
    print(f'        <td>{artikel}</td>')
    print(f'        <td>{menge}</td>')
    print(f'        <td>{name}</td>')
    print(f'        <td>{werk}</td>')
    print(f'        <td>{kostenstelle}</td>')
    print('      </tr>')

print('    </table>')
print('  </div>')
print('</body>')
print('</html>')
