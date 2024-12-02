from Components import menu, intro, play_game
import sys

def main():
    while True:
        choice = menu()
        if choice == "start":
            intro_result = intro()
            if intro_result == "exit":
                break
            else:
                play_game()
        elif choice == "exit":
            sys.exit()

if __name__ == "__main__":
    main()

