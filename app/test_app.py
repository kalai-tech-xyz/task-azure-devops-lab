   import pytestfrom app.app import app as flask_app
   
   @pytest.fixturedef client():
       with flask_app.test_client() as client:
           yield client
   def test_hello_endpoint(client):
       response = client.get("/")
       assert response.status_code == 200
       assert b"Hello, Azure DevOps World!" in response.data
