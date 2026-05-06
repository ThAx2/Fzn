#!/usr/bin/env python3

import requests
import argparse
import os
import socket
from datetime import datetime

class Colors:
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    VERDE = '\033[92m'
    AMARILLO = '\033[93m'
    ROJO = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

INFO = f"{Colors.CYAN}[*]{Colors.RESET}"
SUCCESS = f"{Colors.VERDE}[+]{Colors.RESET}"
ERROR = f"{Colors.ROJO}[!]{Colors.RESET}"

def banner():
    art = f"""{Colors.MAGENTA}
  ███████╗███████╗███╗   ██╗
  ██╔════╝╚══███╔╝████╗  ██║
  █████╗    ███╔╝ ██╔██╗ ██║
  ██╔══╝   ███╔╝  ██║╚██╗██║
  ██║     ███████╗██║ ╚████║
  ╚═╝     ╚══════╝╚═╝  ╚═══╝ {Colors.RESET}v1.0
 {Colors.BOLD}Fast Fuzzing Tool by ThAx2{Colors.RESET}
    """
    print(art)

def target_analysis(url):
    print(f"{Colors.BOLD}{Colors.CYAN}--- TARGET ANALYSIS ---{Colors.RESET}")
    
    url_clean = url.rstrip('/')
    url_visual = f"{url_clean}{Colors.MAGENTA}/$fzn{Colors.RESET}"
    
    try:
        host = url_clean.replace('http://', '').replace('https://', '').split('/')[0]
        ip = socket.gethostbyname(host)
        
        r = requests.get(url_clean, timeout=5)
        server = r.headers.get('Server', 'Unknown')
        
        print(f"{INFO} Target: {Colors.CYAN}{url_visual}")
        print(f"{SUCCESS} IP: {Colors.AMARILLO}{ip}{Colors.RESET}")
        print(f"{INFO} Server: {Colors.MAGENTA}{server}{Colors.RESET}")
        print(f"{INFO} Status: {Colors.VERDE}{r.status_code} OK{Colors.RESET}")
        
    except Exception as e:
        print(f"{ERROR} No se pudo completar el análisis inicial: {e}")

def main():
    parser = argparse.ArgumentParser(
        description=f"{Colors.CYAN}Fzn - Advanced Fuzzing Tool{Colors.RESET}",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('-u', '--url', type=str, required=True, help='URL del objetivo')
    parser.add_argument('-w', '--wordlist', type=str, required=True, help='Ruta del diccionario')
    parser.add_argument('-t', '--thread', type=int, default=5, help='Hilos a usar (Default: 5)')
    parser.add_argument('-a', '--agent', type=float, default=5.2, help='Rotación de User-Agent (seg)')
    parser.add_argument('-p', '--proxy', type=str, help='Proxy (ej: 127.0.0.1:8080)')

    args = parser.parse_args()

    if not args.url.startswith(('http://', 'https://')):
        print(f"{ERROR} La URL debe comenzar con http:// o https://")
        exit(1)

    if not os.path.isfile(args.wordlist):
        print(f"{ERROR} Wordlist no encontrada: {args.wordlist}")
        exit(1)
    banner()
    target_analysis(args.url)
    
    print(f"\n{Colors.AMARILLO}[!] Motor de ataque y módulos de Ruby en auditoría interna.{Colors.RESET}")
    print(f"{Colors.AMARILLO}[!] Próxima actualización v1.1 - Esté atento al repositorio.{Colors.RESET}")

if __name__ == "__main__":
    main()
