import re
import pandas as pd

datoteka_txt = ""

with open("igralci.txt") as r:
    datoteka_txt += r.read()

slovar_igralcev = {}

def html_v_vzorec(txt):
    vzorec_ime = r"data-has-children=\"(true|false)\">(.*?)</a></td><td>(.*?)</td><td>(\d*)</td><td>(\d*?)</td><td>(\d*?)</td><td>(\d*?)</td><td>(.*?)</td><td>(-|.*?)</td><td>(-|.*?)</td><td>(-|.*?)</td><td>(-|.*?)</td><td>(-|.*?)</td><td>(-|.*?)</td><td>(-|.*?)</td><td>(-|.*?)</td><td>(-|.*?)</td><td>(-|.*?)</td><td>(-|.*?)</td><td>(-|.*?)</td><td>(-|.*?)</td><td>(.*?)</td><td>(.*?)</td></tr><tr>"
    
    return vzorec_ime

def html_v_slovar():
    matches = re.finditer(html_v_vzorec(datoteka_txt), datoteka_txt,flags=re.DOTALL)
    for match in matches:
        slovar_igralcev[match.group(2)] = (match.group(3),match.group(4),match.group(5),match.group(6),match.group(7),match.group(8),match.group(9),match.group(10),match.group(11), match.group(12), match.group(13), match.group(14), match.group(15), match.group(16),match.group(17), match.group(18), match.group(19), match.group(20),match.group(21),match.group(22),match.group(23))

html_v_slovar()
#slovar_igralcev je sedaj slovar, sestavljen na nasleden način: ime igralca je ključ, nato pa v tuplu naslednje statistike(igrane igre, minute odigrane, točke, število zadetkov iz igre, število poskusov iz igre, procent narejenih košov iz igre, število zadetih trojic, število poskusov trojic, procent zadetih trojic, število zadetkov iz prostih strelov, število poskusov iz prostih strelov, procent zadetih iz prostih strelov, skoki v napadu, skoki v obrambi, vsi skoki, asistence, odvzete žoge, blokade, zgubljene žoge,"učinkoviti procenti", "true" shooting percentage)

podatki_tabele = [[ime, *statistike] for ime,statistike in slovar_igralcev.items()]
tabela = pd.DataFrame(podatki_tabele, columns = ["Ime", "Igre", "Minute", "Tocke", "FGM", "FGA", "FG%","3P", "3PA","3P%","FTM","FTA","FT%","OREB","DREB","REB","AST","STL","BLK","TOV","EFG%","TS%"])
tabela.index = tabela.index +1
tabela = tabela.applymap(lambda x: x.replace(",","")) #igrane igre, so imele , in se niso kodirale kakor int, vendar kot string

podatki_csv = "podatki_csv"
tabela.to_csv(podatki_csv, index = False)
#ustvarjena je tabela in csv file, ki je zelo podobna, kot ta na strani : https://www.nba.com/stats/alltime-leaders 

