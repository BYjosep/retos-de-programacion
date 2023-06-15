"""

Escribe un programa que reciba un texto y transforme lenguaje natural a
"lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 se caracteriza por sustituir caracteres alfanuméricos.
- Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
  con el alfabeto y los números en "leet".
  (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

"""
def reemplazar_letras(cadena, letras_a_reemplazar, caracteres_reemplazo):
    """
    Función que reemplaza las letras especificadas por otros caracteres en una cadena de texto.

    Args:
        cadena (str): La cadena de texto original.
        letras_a_reemplazar (str): Las letras que se deben reemplazar.
        caracteres_reemplazo (str): Los caracteres por los que se deben reemplazar las letras.
    
    Returns:
        str: La cadena de texto modificada.
    """
    for letra, caracter in zip(letras_a_reemplazar, caracteres_reemplazo):
        cadena = cadena.replace(letra, caracter)
    return cadena

mensaje = input("introduce el texto \n")
letras_a_reemplazar =  "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
caracteres_reemplazo = "Д","ß","(","[)","3","|=","<-","#","1","]","|<","|_","|\/|","И","Ø","|o","(_,)","Я","5","7","|_|","\/","\/\/","><","Ч","2","4","8","©","|)","€","ƒ","(_+","|-|","!","_|","|{","|","^^","ท","[]","|>","9","®","§","†","µ","|/","Ш","Ж","¥","%"

hacker_Text = reemplazar_letras(mensaje, letras_a_reemplazar, caracteres_reemplazo)
print(hacker_Text)

#letras
    #*Mayusculas
       
        #!"A" = "Д"
        #!"B" = "ß"
        #!"C" = "("
        #!"D" = "[)"
        #!"E" = "3"
        #!"F" = "|="
        #!"G" = "<-"
        #!"H" = "#"
        #!"I" = "1"
        #!"J" = "]"
        #!"K" = "|<"
        #!"L" = "|_"
        #!"M" = "|\/|"
        #!"N" = "И"
        #!"O" = "Ø"
        #!"P" = "|o"
        #!"Q" = "(_,)"
        #!"R" = "Я"
        #!"S" = "5"
        #!"T" = "7"
        #!"U" = "|_|"
        #!"V" = "\/"
        #!"W" = "\/\/"
        #!"X" = "><"
        #!"Y" = "Ч"
        #!"Z" = "2"
    
    #*Minusculas
        #!"a" = "4"
        #!"b" = "8"
        #!"c" = "©"
        #!"d" = "|)"
        #!"e" = "€"
        #!"f" = "ƒ"
        #!"g" = "(_+"
        #!"h" = "|-|"
        #!"i" = "!"
        #!"j" = "_|"
        #!"k" = "|{"
        #!"l" = "|"
        #!"m" = "^^"
        #!"n" = "ท"
        #!"o" = "[]"
        #!"p" = "|>"
        #!"q" = "9"
        #!"r" = "®"
        #!"s" = "§"
        #!"t" = "†"
        #!"u" = "µ"
        #!"v" = "|/"
        #!"w" = "Ш"
        #!"x" = "Ж"
        #!"y" = "¥"
        #!"z" = "%"