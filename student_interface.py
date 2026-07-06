import requests

def run_student_cli():
    print("====================================")
    print("   STUDENT ATTENDANCE SYSTEM (CLI)  ")
    print("====================================")
    
    # 1. Ask student for input and trim accidental spaces
    user_id = input("Enter Student ID: ").strip()
    user_name = input("Enter Student Name: ").strip()
    
    # Stop early if inputs are empty so the system doesn't crash
    if not user_id or not user_name:
        print("\n[Error] ID and Name cannot be empty!")
        return

    # Server connection settings
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = "5000"
    target_url = f"http://{SERVER_IP}:{SERVER_PORT}/mark/{user_id}/{user_name}"
    
    print(f"\n[Connecting] Submitting details to server...")
    
    # Clear system proxies to ensure smooth local communication
    bypass_proxies = {"http": None, "https": None}
    
    try:
        # Send data to the main Flask app
        response = requests.get(target_url, proxies=bypass_proxies)
        
        print("\n==============================")
        print(f"Status Code: {response.status_code}")
        print(f"Server Response: {response.text}")
        print("==============================")
        
    except requests.exceptions.ConnectionError:
        # This safety block only triggers if the main app.py server is turned off
        print("\n[NETWORK ERROR] Could not connect to the Attendance Server.")

if __name__ == "__main__":
    run_student_cli()