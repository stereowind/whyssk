import session
import logging

# Default logger settings
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s (%(module)s) [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Main program flow
if __name__ == '__main__':
    while True:
        try:
            # Initialize welcome screen and session settings
            session.initialize()
            logging.debug("Session successfully initialized")
            # Start the main session flow
            session.main()
            logging.debug("Session successfully finished!")
        except Exception as e:
            logging.exception("Error occurred! Error message:")
        finally:
            choice = str(input("\n[y/n] Would you like to restart the session?\n"))
            if choice.lower() == 'y':
                logging.info("Session restarted")
                pass
            elif choice.lower() == 'n':
                logging.info("Session completed, shutting down...")
                break
    # Clear the screen before finishing the program
    session.clear()
