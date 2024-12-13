import os,time

usuarios = [
    {"usuario": "sebastian", "clave": "1234", "saldo": 50000, "biblioteca": ["Hollow Knight: Silksong", "Metroid Prime 4"]},
    {"usuario": "kat", "clave": "4321", "saldo": 63020, "biblioteca": ["Genshin Impact", "Shiro Neko New Project"]},
    {"usuario": "fernanda", "clave": "9999", "saldo": 43800, "biblioteca": ["FANTASY LIFE i: La pequeña ladrona del tiempo", "Tale of Ronin"]}
]

Juegos_stock= [
    {"codigo": 1,"nombre": "Splatoon 3", "precio": 10000, "stock": 5},
    {"codigo": 2,"nombre": "Kirby y la tierra olvidada", "precio": 24500, "stock": 2},
    {"codigo": 3,"nombre": "Mario + Rabbids Sparks of Hope", "precio": 15500, "stock": 11},
    {"codigo": 4,"nombre": "Just Dance® 2023", "precio": 40000, "stock": 1},
    {"codigo": 5,"nombre": "Pokémon Púrpura", "precio": 31000, "stock": 7},
    {"codigo": 6,"nombre": "Pokémon Escarlata", "precio": 30000, "stock": 5} # El Stock no sera actualizado ya que no agregamos funciones para comprar
]

carrito = []#lista vacia

print("*************************************")
print("*  Bienvenido a MyGame Store  *")
print("*************************************")
print("*************************************")
print("*          Control de acceso  *")
print("*************************************")
print("*************************************")

usuario_actual = None #usuario actual es una variable vacia o "0" que luego será definida cuando hagamos login

def eliminar():
    ver_carrito()
    try:
        codi_juego = int(input("Ingrese el código del juego que desea eliminar: "))
        juego_a_eliminar = None
        
        for juego in carrito:
            if juego['codigo'] == codi_juego:
                juego_a_eliminar = juego
                break
        
        if juego_a_eliminar: # si el carrito tiene algo que eliminar es True
            carrito.remove(juego_a_eliminar)
            print(f"{juego_a_eliminar['nombre']} ha sido eliminado del carrito.")
        else:
            print("Juego no encontrado en el carrito.")
            eliminar()
        
        return 
    except ValueError:
        print("Error: Ingrese un código válido.")
        eliminar()
    

def mostrarjuegos():
    print("Juegos en stock:")
    for juego in Juegos_stock:
        print(f"Codigo: {juego['codigo']}, Nombre: {juego['nombre']}, Precio: ${juego['precio']}, Stock: {juego['stock']}")

def billetera():
    for x in usuarios:
        if usuario_actual == x["usuario"]:
            saldo = x["saldo"]
            print(f"Tu saldo actual es de: ${saldo}")

def ingresodinero():
    billetera()
    try:
        ingreso=int(input("¿Cuanto dinero desea ingresar?\t"))
        for x in usuarios:
            if usuario_actual==x["usuario"]:
                saldo_actual=x["saldo"]+ingreso
                x["saldo"] = saldo_actual
                print("Su nuevo saldo es: $",saldo_actual)
    except ValueError as k:
        print(f"ingrese un monto valido, error :{k}")
        time.sleep(2)
        os.system("cls")
        ingresodinero()
        
def ver_carrito():
    print("Tu carrito de compras:")
    if not carrito: # una lista vacia se considera false, este codigo nos dice que el print se ejecuta si la lista se encuentra en False/Vacia la lista es carrito[]
        print("Tu carrito está vacío.")
    else:
        for juego in carrito:# juego es una variable, si carrito es True entonces nos muestra los juegos que contiene
            print(f"- {juego['nombre']} a ${juego['precio']}")

def agregar_al_carrito():
    mostrarjuegos()
    juego_agregado = int(input("Ingrese el codigo del juego que desea agregar al carrito:\t"))
    for juego in Juegos_stock:
        if juego["codigo"] == juego_agregado and juego["stock"]>0:
            carrito.append(juego)#agregar el juego al final de la lista carrito
            print(f"{juego['nombre']} ha sido agregado al carrito.")
            return # Termina la ejecucion de la funcion despues de agregar el juego evitando iteraciones innecesarias
        
    print("Juego no encontrado o sin stock disponible.")

def agregar_usuario():
    nuevo_usuario = input("Ingrese el nombre de usuario del nuevo usuario:\t")
    nueva_clave = input("Ingrese la contraseña del nuevo usuario:\t")
    for usuario in usuarios:
        if usuario["usuario"] == nuevo_usuario:
            print("El nombre de usuario ya existe.")
            return agregar_usuario()
    usuarios.append({"usuario": nuevo_usuario, "clave": nueva_clave, "saldo": 0, "biblioteca": []})
    print("Nuevo usuario agregado con éxito.")

def ver_usuarios():
    for usuario in usuarios:# usuario recorre la lista usuarios en busca de "usuario"
        print(usuario["usuario"])

def default():
    print("Ingrese opciones válidas")
    

switch = {1:mostrarjuegos,2:ingresodinero,3:agregar_al_carrito,4:eliminar,5:agregar_usuario,6:ver_carrito,7:ver_usuarios}

def menu():
    respuesta = "si"
    while respuesta == "si":
        try:
             #debe haber CRUD
            print("Opción 1: Mostrar juegos en stock")  #READ 
            print("Opción 2: Ingresar dinero a billetera")#UPDATE
            print("Opción 3: Agregar juego al carrito")#update
            print("Opción 4: eliminar juego del carrito")#UPDATE/DELETE
            print("Opción 5: Agregar nuevo usuario") #CREATE/UPDATE
            print("Opción 6: Ver carrito de compras")#READ
            print("Opción 7: Ver usuarios")
            opcion = int(input("Ingrese el número de opción:\t"))
            switch.get(opcion, default)()
            respuesta = input("¿Ingresar al menú nuevamente? SI/NO\t").lower()
            time.sleep(1)
            os.system("cls")
            if respuesta != "si" or respuesta != "no":
                print("ingrese una respuesta entre si/no\n")
                respuesta = input("¿Ingresar al menú nuevamente? SI/NO\t").lower()
            else:
                break
        except ValueError as k:
            print("Ingrese una Opcion Valida")
            time.sleep(1)
            os.system("cls")
    

            
            
def inicio():
    global usuario_actual
    respuesta = "si"
    while respuesta == "si":
        usuario = input("Ingrese su nombre de usuario: ") 
        clave = input("Ingrese su contraseña: ")
        for x in usuarios:
            if x["usuario"] == usuario and x["clave"] == clave:
                usuario_actual = usuario
                print("Inicio de sesión exitoso.")
                time.sleep(1)
                os.system("cls")
                menu()
                return
        print("Usuario o contraseña incorrectos. Inténtelo de nuevo.")
        respuesta = input("¿Intentar nuevamente? SI/NO: ").lower()

inicio()
