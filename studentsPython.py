if __name__ == '__main__':
#Lista vacía donde guardaremos nombre y calificación
    students = []
#Leer cuántos estudiantes se ingresarán  
    for _ in range(int(input())):
        students.append([input(), float(input())])
        #input() lee el nombre
        #float(input()) lee la calificación y la convierte a número decimal
        #e guarda como [nombre, calificación] dentro de la lista students

    scores = sorted(set([s[1] for s in students]))
    #s[1] toma solo las calificaciones de cada estudiante
    #set() elimina calificaciones repetidas
    #sorted() ordena las calificaciones de menor a mayor
    second = scores[1]
   #toma la segunda calificación más baja de la lista ordenada
    for name in sorted([s[0] for s in students if s[1] == second]):
    #s[0] toma el nombre del estudiante
    #if s[1] == second filtra los estudiantes con la segunda calificación más baja
    #sorted(...) ordena los nombres alfabéticamente
        print(name)
#imprime cada nombre en una línea