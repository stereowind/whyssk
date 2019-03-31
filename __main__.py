import session


def start():
    session.initialize()
    session.main()


if __name__ == '__main__':
    while True:
        try:
            start()
        except Exception as e:
            print("Error occurred! Error message:")
            print(str(e))
        finally:
            choice = str(input("\n[y/n] Would you like to restart the session?\n"))
            if choice.lower() == 'y':
                pass
            elif choice.lower() == 'n':
                break
    session.clear()
