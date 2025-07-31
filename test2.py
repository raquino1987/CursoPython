from tabulate import tabulate
from colorama import init, Fore
init(autoreset=True)

from dataclasses import dataclass
@dataclass

class numero:
    numero: int
       
    def evaluar(self):
        if self.numero & 1:
            resultado = "El número es impar"
            if self.numero == 7:
                extra = "El número ingresado es un comodín"
        else:
            resultado = "El número es par"
            if self.numero == 10:
                extra = "El número ingresado es 10"
        return resultado, extra if 'extra' in locals() else None

    def sumar(self, numerosum):
        return self.numero + numerosum

def encabezado():
    print(Fore.GREEN + "=" * 78)
    print(Fore.GREEN + " " * 24 + "Evaluador y Sumador de Números" + " " * 24)
    print(Fore.GREEN + "=" * 78)

def main():
    encabezado()
    historial = []
    
    while True:
        try:
            numeroeva = numero(int(input("\n Ingrese un número: ")))
            resultado, extra = numeroeva.evaluar()
            print(Fore.YELLOW + f"\n {resultado}")
            if extra:
                print(Fore.YELLOW + f"\n {extra}")
            
            sumados = numeroeva.sumar(int(input("\n Ingrese un número para sumar: ")))
            print(Fore.YELLOW + f"\n La suma es: {sumados}")
            
            historial.append((numeroeva.numero, resultado, extra if extra else "N/A", sumados))
                                    
            continuar = input("\n ¿Desea continuar? (s/n): ").strip().lower()
            if continuar != 's':
                break
        
        except ValueError:
            print(Fore.RED + "\n Error: Por favor, ingrese un número válido.")

    print("\n Resumen de operaciones:")
    titulo = ["Número", "Clasificación", "Extra", "Suma"]
    print(tabulate(historial, headers=titulo, tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()