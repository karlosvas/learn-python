#Promedio de duración.
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5
#Diferecnias de duración.
diferencias_min = 100 - dalto_curso / otros_cursos_min * 100
diferencias_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencias_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

print(f"El curso dura un {diferencias_min}% menos que el mas rapido")
print(f"El curso dura un {diferencias_max}% menos que el mas lento")
print(f"El curso dura un {diferencias_promedio}% menos que el mas rapido")
#Duración de crudos
crudo_promedio = 5
crudo_dalto = 3.5

resultado_crudos= float(crudo_promedio) - crudo_dalto
resultado_crudos_porcentaje= crudo_dalto * 1000 // crudo_promedio / 10

print(f"La diferencia en horas de el crudo es {resultado_crudos}h")
print(f"La diferencia en porcentaje de el crudo es {resultado_crudos_porcentaje}%")
