"""
Module Documentation Goes Here
"""
from project import create_app

# Flask App Setup
app = create_app() 

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 5000, debug = True)