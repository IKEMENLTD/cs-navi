import os
import requests
import time

# Target directory
target_dir = r"d:\cardloanmedia-b-2\assets\images\thumbnails"
os.makedirs(target_dir, exist_ok=True)

# Keywords for "Japanese Business Person" vibe
keywords_list = [
    "japanese,business,man",
    "japanese,business,woman",
    "japanese,office,working",
    "japanese,business,smile",
    "japanese,meeting,business"
]

print(f"Downloading {len(keywords_list)} thumbnails to {target_dir}...")

for i, keywords in enumerate(keywords_list):
    filename = f"thumbnail-{i+1}.png"
    filepath = os.path.join(target_dir, filename)
    
    # Using LoremFlickr
    # Adding lock=i to ensure different images if the service supports it, or just random
    # LoremFlickr redirects to an image.
    url = f"https://loremflickr.com/640/480/{keywords}?lock={i}"
    
    try:
        print(f"[{i+1}/{len(keywords_list)}] Downloading for '{keywords}'...")
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"  -> Saved to {filename}")
        else:
            print(f"  -> Failed: Status {response.status_code}")
    except Exception as e:
        print(f"  -> Error: {e}")
    
    # Sleep to be nice
    time.sleep(1)

print("Download complete.")
