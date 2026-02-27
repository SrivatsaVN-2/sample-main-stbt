from sample-api.hello_api import hello_world


def call_api():
    message = hello_world()
    print(message)


if __name__ == "__main__":
    call_api()