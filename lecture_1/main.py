from colorama import init, Fore, Back, Style

# Initialize colorama with autoreset to prevent color bleeding
init(autoreset=True)

def main():
    # Print colored Hello World examples
    print(f"{Fore.RED}{Back.YELLOW}Hello World!{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Hello World in Green!{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{Style.BRIGHT}Hello World in Bright Blue!{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{Back.CYAN}Hello World with Magenta text and Cyan background!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
