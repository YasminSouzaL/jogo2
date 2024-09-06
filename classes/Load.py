import pickle
import os

class Load:
    def __init__(self, filename="savefile.pkl"):
        self.filepath = os.path.join(r'data\save\savefile.pkl', filename)

    def save_game(self, state):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
       
        with open(self.filepath, 'wb') as file:
            pickle.dump(state, file)

    def load_game(self, screen):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'rb') as file:
                state = pickle.load(file)
                screen.load_state(state)



