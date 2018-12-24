import connexion


api = connexion.App(__name__, specification_dir="./")
api.add_api("swagger.yml")


if __name__ == "__main__":
    api.run(host='0.0.0.0', port=8000, debug=True)