import os

try:
   if os.environ["PRODUCTION"]:
      dataUrl = "http://data.hasura/v1/query"
      dataHeaders = {"Content-Type": "application/json", "X-Hasura-Role":"anonymous", "X-Hasura-User-Id":"0"}

      # URL and headers for the nutrition info api call
      dataUrl_nutrition = "https://trackapi.nutritionix.com/v2/natural/nutrients"
      dataheaders_nutrition = {
    "Content-Type": "application/json",
    "x-app-key": "b6b0b0be59e9c60a4e9194119834deca",
    "x-app-id": "e527beec",
    "x-remote-user-id": "0"}

except KeyError:
   try:
      cluster_name = os.environ["CLUSTER_NAME"]
      dataUrl = "https://data." + cluster_name + ".hasura-app.io/v1/query"
      dataHeaders = {"Content-Type": "application/json"}

      # URL and headers for the nutrition info api call
      dataUrl_nutrition = "https://trackapi.nutritionix.com/v2/natural/nutrients"
      dataheaders_nutrition = {
    "Content-Type": "application/json",
    "x-app-key": "b6b0b0be59e9c60a4e9194119834deca",
    "x-app-id": "e527beec",
    "x-remote-user-id": "0"}
   except KeyError:
      print(  " Please set the name of your cluster as an environment variable using 'export CLUSTER_NAME=<cluster-name>', where <cluster-name> is the name of your cluster" )
      os.exit(1)
