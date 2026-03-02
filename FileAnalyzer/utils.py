import hashlib, logging
from colorama import Fore, init

init(autoreset=True)

logging.basicConfig(filename="fileanalyzer.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def hash_filename(url):
    return hashlib.sha256(url.encode()).hexdigest()

def print_colored(text, risk):
    color = Fore.RED if risk == "HIGH" else Fore.YELLOW if risk == "MEDIUM" else Fore.GREEN
    print(color + text)
