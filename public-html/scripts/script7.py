# (IGNORAR) Para que no subraye errores pequeños e irrelevantes de sintaxis
# pylint: disable=C0103, C0114, C0303, C0304, C0305, C0301, C0116
"""
9.	Simular el comportamiento de un programa que realiza 3 consultas a una base de datos remota, cada una con un tiempo de respuesta variable entre 1 y 5 segundos. Se quiere comparar la concurrencia usando hilos, tareas asíncronas y procesos
"""
import threading
import time
import multiprocessing
import asyncio
print("====================== EJERCICIO 6 (8.) ======================")

def consulta_base(consulta, tiempo):
    print(f"-> CONSULTA: {consulta}")
    print("REALIZANDO CONSULTA...")
    time.sleep(tiempo)
    print("CONSULTA REALIZADA")

async def consulta_base_async(consulta, tiempo):
    print(f"-> CONSULTA: {consulta}")
    print("REALIZANDO CONSULTA...")
    await asyncio.sleep(tiempo)
    print("CONSULTA REALIZADA")

def consulta_base_proceso(consulta, tiempo):
    print(f"-> CONSULTA: {consulta}")
    print("REALIZANDO CONSULTA...")
    time.sleep(tiempo)
    print("CONSULTA REALIZADA")

consultas = [
    ("Consulta A", 5),
    ("Consulta B", 5),
    ("Consulta C", 5)
]

inicio = time.time()

hilos = []

for consul, t in consultas:
    h = threading.Thread(target=consulta_base, args=(consul, t))
    h.start()
    hilos.append(h)

for h in hilos:
    h.join()

print("Tiempo total:", time.time() - inicio)

print("----------------------\n")

async def main():
    inicio_async = time.time()

    await asyncio.gather(
        consulta_base_async("Consulta A", 3),
        consulta_base_async("Consulta B", 3)
    )

    print("Tiempo total:", time.time() - inicio_async)

asyncio.run(main())

print("----------------------\n")

if __name__ == "__main__":
    inicio_proceso = time.time()

    procesos = []
    for consul, t in consultas:
        p = multiprocessing.Process(target=consulta_base_proceso, args=(consul, t))
        p.start()
        procesos.append(t)
    
    for p in procesos:
        p.join()

    print("Tiempo total:", time.time() - inicio_proceso)


print("==============================================================")
