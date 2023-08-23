import re
import csv
import pandas as pd
from zavzem_podatkov import slovar_igralcev

podatki_tabele = [[ime, *statistike] for ime,statistike in slovar_igralcev.items()]
tabela = pd.DataFrame(podatki_tabele, columns = ["Ime", "Igre", "Minute", "Tocke", "FGM", "FGA", "FG%","3P", "3PA","3P%","FTM","FTA","FT%","OREB","DREB","REB","AST","STL","BLK","TOV","EFG%","TS%"])
tabela.index = tabela.index +1
tabela = tabela.applymap(lambda x: x.replace(",","")) #igrane igre, so imele , in se niso kodirale kakor int, vendar kot string

podatki_csv = "podatki_csv"
tabela.to_csv(podatki_csv, index = False)
#ustvarjena je tabela in csv file, ki je zelo podobna, kot ta na strani : https://www.nba.com/stats/alltime-leaders 





