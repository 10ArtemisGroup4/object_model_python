from Fan import Fan

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
