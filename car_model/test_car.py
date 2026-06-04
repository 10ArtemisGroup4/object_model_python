from car_class_definition import Car

#adding class colors for aesthetics and presentation
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

def print_header(title):
    print()
    print(Color.CYAN + Color.BOLD + "  ╔══════════════════════════════════════════════╗" + Color.RESET)
    print(Color.CYAN + Color.BOLD + f"  ║  {title:<44}║" + Color.RESET)
    print(Color.CYAN + Color.BOLD +
          "  ╚══════════════════════════════════════════════╝" + Color.RESET)
    print()