# run.py
 
# Add your settings here... this is a temporary location, as the settings for a Flask app
# should be stored separate from your main program.
DEBUG = True
 
from app import app
 
if __name__ == "__main__":
   #app.run()
   app.run(debug=True, host='0.0.0.0', port=5000)
