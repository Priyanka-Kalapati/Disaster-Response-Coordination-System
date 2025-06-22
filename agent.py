class Agent:
    def __init__(self, name):
        self.name = name

    def send(self, receiver, message):
        print(f"Sending message to {receiver}: {message}")