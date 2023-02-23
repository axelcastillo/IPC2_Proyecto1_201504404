 #----Menu   
def Menu():
    print("PROYECTO 1 IPC2")
    print("--- Seleccione una opcion ---")
    print('1. Cargar Archivo XML')
    print('2. Gestionar Organismos')
    print('3. Salir')
    salida = int(input("Ingrese su opcion:"))
    return salida

print("Proyecto 1 IPC2")

def main():
    call = ""
    opcion = Menu()
    while opcion != 4:
     if opcion == 1:
         print("se ingreso el archivo XML")
         opcion=Menu()
         break
     elif opcion == 2:
        print("")
       
        opcion=Menu()
        break
     elif opcion == 3:
        print("")
        break
     elif opcion == 4:
        SystemExit
        opcion = Menu()
        break
     else:
        print("Entrada no valida")

if __name__ == "__main__":
      main()
      
      
      