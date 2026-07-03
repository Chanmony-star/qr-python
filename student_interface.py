import requests
def run_student_interface():
    print("=== STUDENT ATTENDANCE SIMULATOR ===")
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")
    #  Set the address of the server
    server_ip = "127.0.0.1"
    port = "5000"
    # Glue everything together to make the website link (URL)
    url = f"http://{server_ip}:{port}/mark/{student_id}/{student_name}"
    print("\nConnecting to the server...")
    print(f"Sending data to: {url}")
    # Send the information over the network
    # We use 'proxies=None' to make sure your computer firewall doesn't block it
    response = requests.get(url, proxies={"http": None, "https": None})
    # Show the results from the server
    print("\n--- SERVER RESPONSE ---")
    print(f"Status Code: {response.status_code}")
    print(f"Server Message: {response.text}")
    print("-----------------------")
# This line tells Python to start the code above
if __name__ == "__main__":
    run_student_interface()