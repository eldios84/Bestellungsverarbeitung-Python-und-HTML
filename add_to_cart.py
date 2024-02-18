#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()

artikel = form.getvalue('artikel')
menge = form.getvalue('menge')
name = form.getvalue('name')
werk = form.getvalue('werk')
kostenstelle = form.getvalue('kostenstelle')

# Speichern der Daten in einer Textdatei
with open('warenkorb.txt', 'a') as file:
    file.write(f'{artikel},{menge},{name},{werk},{kostenstelle}\n')

# Weiterleitung zur Bestellübersicht
print('Location: bestelluebersicht.py\r\n')
