import json


def read_from_file(file_path: str) -> dict:
    with open(file_path) as my_file:
        data: dict = json.load(my_file)
    return data


def put_from_file(file_path: str, db: dict):
    data = read_from_file(file_path)


def put_function(pair, db: dict):
    print("PUT ", pair)

    data: dict = json.loads(pair)

    db["6TT"] = {"name": "first item"}
    db["Hritwik"] = "Test"
    db["Integer"] = 6
    print(db["Hritwik"])
