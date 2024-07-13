import datetime
import time

entrada = str(input("Digite a hora para ligar (HH:MM)"))
#entrada = "02:08"

hr = entrada.split(':')

t_desp = datetime.datetime.combine( datetime.datetime.now().date(),
                                    datetime.time( int(hr[0]), int(hr[1])) )

print("Despertar as: ", t_desp)

while True:

    printsHoras = datetime.datetime.now()

    print(printsHoras)

    if printsHoras >= t_desp:
       print("Acordar")
       break

    time.sleep(1)