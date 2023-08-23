#Promedio de duración.
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5
#Diferecnias de duración.
diferencias_min = 100 - (dalto_curso / otros_cursos_min * 100)
diferencias_max = round(100 - (dalto_curso / otros_cursos_max * 100),1)
diferencias_promedio = 100 - (dalto_curso / otros_cursos_promedio * 100)

print(f"El curso de dalto dura un {diferencias_min}% menos que el mas corto")
print(f"El curso de dalto dura un {diferencias_max}% menos que el mas largo")
print(f"El curso dura un {diferencias_promedio}% menos que el promedio de los cursos")
#Duración de crudos
crudo_promedio = 5
crudo_dalto = 3.5

resultado_crudos= float(crudo_promedio) - crudo_dalto
resultado_crudos_porcentaje= 100 - (crudo_dalto / crudo_promedio * 100)

print(f"La diferencia en horas de el crudo es {resultado_crudos}h")
print(f"La diferencia en porcentaje del contenido crudo es del {resultado_crudos_porcentaje}%")
