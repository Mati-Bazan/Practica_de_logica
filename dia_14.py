#  Fechas
# Como trabajar con fechas

from datetime import datetime # Objetos de tipo fecha 

now = datetime.now() # Fecha actual
# print(now)

birth_date = datetime(1997,2,9,12,0,0) # Fecha de nacimiento | 12 = horas, 0 = minutos, 0 segundos
# print(birth_date)

# Cuántos años han transcurrido entre ambas fechas}
difference  = now - birth_date # En python se puedo hacer calculos simples con fechas -> dias  

print(difference.days // 365) # difference.days almacena los dias entre ambas fechas | // 365 división entera

"""
Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
"""
# Día, mes y año
print(birth_date.strftime("%d/%m/%y")) # Formateo "dia/mes/año" | 09/02/97
print(birth_date.strftime("%d/%m/%Y")) # 09/02/1997

# Hora, minuto y segundo
print(birth_date.strftime("%H:%M:%S")) # 12:00:00 | horas, min, seg

# Día de año.
print(birth_date.strftime("%j")) # 040 | dia 40 del año

# Día de la semana.
print(birth_date.strftime("%A")) # Sunday

# Nombre del mes.
print(birth_date.strftime("%h")) # Feb
print(birth_date.strftime("%B")) # February

# Por defecto en base a donde se definio la fecha
print(birth_date.strftime("%c")) # Sun Feb  9 12:00:00 1997
print(birth_date.strftime("%x")) # 02/09/97
print(birth_date.strftime("%X")) # 12:00:00

# AM / PM
print(birth_date.strftime("%p")) # PM
