class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance
    
if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(f"DatabaseConnection 1 ID: {id(db1)}")
    print(f"DatabaseConnection 2 ID: {id(db2)}")
    print("Both instances are the same:", db1 is db2)