import datetime
import calendar
from tqdm import tqdm

def calcular_progreso(dia, hora, minuto):
    minutos_transcurridos = (dia - 1) * minutos_dia + hora * 60 + minuto
    progreso = minutos_transcurridos / minutos_ano * 100
    return progreso

ahora = datetime.datetime.now()
dia = ahora.day
hora = ahora.hour
minuto = ahora.minute

if calendar.isleap(ahora.year):
	minutos_ano = 366 * 24 * 60
else :
	minutos_ano = 365 * 24 * 60

minutos_dia = 24 * 60

progreso = calcular_progreso(dia, hora, minuto)

with tqdm(total=100, bar_format="{percentage:3.4f}%|{bar}|100%") as barra:
    barra.update(progreso)
