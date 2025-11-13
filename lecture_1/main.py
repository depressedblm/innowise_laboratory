from colorama import Fore, Back, Style, init

# Инициализация colorama для Windows
init(autoreset=True)

def main():
    print(Fore.RED + "Это красный текст")
    print(Fore.GREEN + "Это зеленый текст")
    print(Back.YELLOW + "Это текст с желтым фоном")
    print(Style.BRIGHT + "Это яркий текст")
    print(Fore.BLUE + Back.WHITE + "Синий текст на белом фоне")

if __name__ == "__main__":
    main()
