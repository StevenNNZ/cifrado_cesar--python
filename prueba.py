# Definir función para encriptar mensaje
def encriptarMensaje(mensaje, clave):
    mensajeEncriptado = '';
    abcEncriptado = getAbcEncriptado(clave);

    for msj in mensaje:
        i= 0;
        while i < len(abc):
            if msj == ' ':
                mensajeEncriptado += ' ';
                break;

            elif msj == abc[i]:
                mensajeEncriptado += abcEncriptado[i];
            
            i += 1;


    return mensajeEncriptado;

# Definir función para generar el abecedario según la claves
def getAbcEncriptado(clave):
    list1 = [];
    list2 = [];
    posicion = 0;

    for letra in abc:
        if( posicion != clave):
            posicion += 1;
            list2.append(letra);
        else:
            list1.append(letra)

    return list1 + list2;

def desEncriptarMensaje(mensaje, clave):
    mensajeDesencriptado = '';
    abcEncriptado = getAbcEncriptado(clave);

    for msj in mensaje:
        i= 0;
        while i < len(abcEncriptado):
            if msj == ' ':
                mensajeDesencriptado += ' ';
                break;

            elif msj == abcEncriptado[i]:
                mensajeDesencriptado += abc[i];
            
            i += 1;

    return mensajeDesencriptado;

def ejecutar(opc):
    # Capturar datos (el mensaje y la clave)
    mensaje = str(input("Ingrese el mensaje: "));
    clave = int(input("Por favor ingrese la clave: "));

    # Pasamos el mensaje a mayúsculas y lo organizamos en un vector
    mensaje = list(mensaje.upper())

    # Según si 
    if( opc == 1):
        # Llamamos la función de encriptar
        print ("Mensaje encriptado: " + encriptarMensaje(mensaje, clave) );
    else:
        print ("Mensaje desencriptado: " + desEncriptarMensaje(mensaje, clave));

# _________INICIO DEL PROGRAMA_________
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M' , 'N', 'Ñ', 'O', 'P' ,'Q' , 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ];


while True :
    print( f"\n|---------------------| CIFRADO CESAR |---------------------| \n->Por favor indique [1] si desea encriptar un mensaje \n->Por favor indique [2] si desea desencriptar un mensaje \n->Digite 3 para salir del programa ")
    opcion = int(input("-> "));

    if( opcion == 3):
        break;

    ejecutar(opcion)
        