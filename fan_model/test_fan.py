from fan_class_definition import Fan

def display_fan(label, fan):
    print(f" {label}")
    print(f" Speed : {Fan._SPEED_LABELS[fan.speed]}")
    print(f" Radius: {fan.radius}")
    print(f" Color : {fan.color}")
    print(f" On    : {fan.on}")
    print(f" Status:", end=" ")
    fan.status()
    print()

def main():
    print()
    print("==========================================")
    print("         Fan Class - Test Program         ")
    print("==========================================")
    print()

    #fan objects
    fan1 = Fan(speed=Fan.FAST, radius=10, color="yellow", on=True)
    fan2 = Fan(speed=Fan.MEDIUM, radius=5, color="blue", on=False)

    #display properties
    display_fan("Fan Object 1:", fan1)
    display_fan("Fan Object 2:", fan2)

    print("===========================================")
    print()

    if __name__ == "__main__":
        main()