import subprocess
import time

def download_urls(file_path):
    with open(file_path, "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    
    for index, url in enumerate(urls, start=233):
        prefix = f"{index:03d}"
        command = [
            "gallery-dl",
            "--filename", f"{prefix} {{num:03d}}.{{extension}}",
            url
        ]
        
        print(f"Downloading {url} with prefix {prefix}...")
        process = subprocess.run(command)
        if process.returncode != 0:
            print(f"Error downloading {url}")
        
        time.sleep(1)  # Small delay to avoid potential rate limiting

if __name__ == "__main__":
    download_urls("gallery-dl.txt")
