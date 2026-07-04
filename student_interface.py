import requests

def run_student_cli():
    print("   STUDENT ATTENDANCE SYSTEM  ")
    
    # 1. Enters Student ID and Name
    user_id = input("Enter Student ID: ").strip()
    user_name = input("Enter Student Name: ").strip()
    
    if not user_id or not user_name:
        print("\n[Error] ID and Name cannot be empty!")
        return

    # Base URL pointing to the Flask App server
    server_ip = "127.0.0.1"
    server_port = "5000"
    target_url = f"http://{server_ip}:{server_port}/mark/{user_id}/{user_name}"
    
    print(f"\n[Connecting] Submitting details to server...")
    
    # Clear local network proxies to avoid connection blocks
    bypass_proxies = {"http": None, "https": None}
    
    try:
        # 2. Clicks "Submit" / Sends data 
        response = requests.get(target_url, proxies=bypass_proxies)
        
        # 3. Success page with details returned from system 
        print(f"Status Code: {response.status_code}")
        print(f"Server Response: {response.text}")
        
    except requests.exceptions.ConnectionError:
        print("\n[NETWORK ERROR] Could not connect to the Attendance Server.")

if __name__ == "__main__":
    run_student_cli()