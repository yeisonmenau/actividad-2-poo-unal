from persona import Persona

if __name__ == "__main__":
    
    persona_uno = Persona("Pedro", "Perez", "12345678", 1990)
    persona_dos = Persona("Luis", "León", "87654321", 1985)
    
    print(persona_uno.mostrar_atributos())
    print(persona_dos.mostrar_atributos())