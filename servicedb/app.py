from queue_handler import QueueHandler
from db_connection import Database

def main():
    db = Database()
    queue = QueueHandler(db)
    queue.start_listening()

if __name__ == "__main__":
    main()