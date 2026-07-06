import requests

def run_student_cli():
    print("==============================")
    print(" STUDENT ATTENDANCE SYSTEM (CLI)")
    print("==============================")

    user_id = input("Enter Student ID: ").strip()
    user_name = input("Enter Student Name: ").strip()

    if not user_id or not user_name:
        print("Error: ID and Name cannot be empty.")
        return

    # Change to server IP shown at startup for network access
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = "5000"
    url = f"http://{SERVER_IP}:{SERVER_PORT}/mark/{user_id}/{user_name}"

    print(f"\nConnecting to server...")

    try:
        response = requests.get(url, proxies={"http": None, "https": None})
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the attendance server.")

if __name__ == "__main__":
    run_student_cli()