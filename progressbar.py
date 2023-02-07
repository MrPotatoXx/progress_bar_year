import datetime
import calendar
from tqdm import tqdm

def calcular_progreso(dia, mes, ano, hora, minuto):
    fecha_inicio_ano = datetime.datetime(ano, 1, 1)
    fecha_actual = datetime.datetime(ano, mes, dia, hora, minuto)
    delta = fecha_actual - fecha_inicio_ano
    minutos_transcurridos = delta.total_seconds() / 60
    progreso = minutos_transcurridos / 525600 * 100
    return progreso

ahora = datetime.datetime.now()
dia = ahora.day
mes = ahora.month
ano = ahora.year
hora = ahora.hour
minuto = ahora.minute

progreso = calcular_progreso(dia, mes, ano, hora, minuto)

with tqdm(total=100, bar_format="{percentage:3.4f}%|{bar}|100%") as barra:
    barra.update(progreso)