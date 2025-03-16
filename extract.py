import re

def extract_lat_lon(google_maps_url):
    # ใช้ Regular Expression เพื่อดึงค่า Latitude และ Longitude จาก URL
    pattern = r"@([-.\d]+),([-.\d]+)"
    match = re.search(pattern, google_maps_url)
    
    if match:
        latitude = float(match.group(1))
        longitude = float(match.group(2))
        return latitude, longitude
    else:
        return None, None

# ตัวอย่างการใช้งาน
google_maps_url = "https://www.google.com/maps/@13.7563,100.5018,15z"
lat, lon = extract_lat_lon(google_maps_url)

if lat and lon:
    print(f"Latitude: {lat}, Longitude: {lon}")
else:
    print("ไม่พบพิกัดใน URL ที่ให้มา")