import sys
import os
import sys
sys.path.append(os.getcwd())
from backend import make_app

app = make_app()

if __name__ == "__main__":
    app.run()
