   from flask import Flaskimport os
   app = Flask(__name__)
   
   @app.route("/")def hello():
       # Fixed: Now loading safely from system environment variables
       AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "development_fallback")
       return "Hello, Azure DevOps World!"
   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)
