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
def print_divider():
    print(Color.BLUE + "  ──────────────────────────────────────────────" + Color.RESET)

def display_speed(action, step, speed):
    bar_length = speed // 5
    bar = "#" * bar_length
    print(f" {Color.YELLOW}{action} #{step:<2}{Color.RESET}" f"Speed: {Color.GREEN}{speed:>3} mph{Color.RESET}" f"{Color.MAGENTA}{bar}{Color.RESET}")

def display_car_info(label, car):
    print(f"  {Color.BOLD}{label}{Color.RESET}")
    print(f"    {Color.CYAN}Year  :{Color.RESET} {car.get_year_model()}")
    print(f"    {Color.CYAN}Make  :{Color.RESET} {car.get_make()}")
    print(f"    {Color.CYAN}Speed :{Color.RESET} {car.get_speed()} mph")
    print()

def test_drive():
    print_header(" Build and Test Drive Your Own Car!")

    year = input(f" {Color.YELLOW} Enter year model:{Color.RESET} ").strip()
    make = input(f" {Color.YELLOW} Enter car make:{Color.RESET} ").strip()

    my_car = Car(year, make)
    print()
    disply_car_info(" Your Car:", my_car)

    while True:
        try:
            acc = int(input(f" {Color.GREEN} Enter acceleration:{Color.RESET} "))
            if acc >= 0:
                break
            print(f" {Color.RED} Input a positive number.{Color.RESET}")
        except ValueError:
            print(f" {Color.RED} Invalid Acceleration.{Color.RESET}")
    print()
    print(f"  {Color.BOLD}Accelerating...{Color.RESET}")
    for i in range(1, acc + 1):
        my_car.accelerate()
        display_speed("Accelerate", i, my_car.get_speed())

    print()