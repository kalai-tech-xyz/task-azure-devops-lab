from flask import Flask
   app = Flask(__name__)
   
   @app.route("/")def hello():
       # Deliberate Azure credential leak to trigger security scan failure
       AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=devopslab;AccountKey=abcdefghijklmnopqrstuvwxyz0123456789==;EndpointSuffix=core.windows.net" 
       return "Hello, Azure DevOps World!"
   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)
