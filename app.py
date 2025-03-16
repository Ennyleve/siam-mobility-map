import openrouteservice
import folium
from flask import Flask, render_template
import os

app = Flask(__name__)

# API Key ของคุณ
api_key = '5b3ce3597851110001cf62489e6e8f7493b94012af59a9bd4d8889eb'
client = openrouteservice.Client(key=api_key)

# ✅ พิกัดต้องเป็น (longitude, latitude)
start = (100.5284337, 13.7446961)  # National Stadium (lon, lat)
end = (100.5309092, 13.7444913)    # SIAMSCAPE (lon, lat)

# คำนวณเส้นทางจาก National Stadium ไป SIAMSCAPE
route_1 = client.directions(
    coordinates=[start, end],
    profile='driving-car',
    format='geojson'
)

# คำนวณเส้นทางจาก SIAMSCAPE ไป National Stadium
route_2 = client.directions(
    coordinates=[end, start],
    profile='driving-car',
    format='geojson'
)

# สร้างแผนที่
m = folium.Map(location=[13.7447, 100.529], zoom_start=15)

# วาดเส้นทางแรก (National Stadium -> SIAMSCAPE) ด้วยสีแดง
folium.GeoJson(route_1, style_function=lambda x: {'color': 'red'}).add_to(m)

# วาดเส้นทางที่สอง (SIAMSCAPE -> National Stadium) ด้วยสีฟ้า
folium.GeoJson(route_2, style_function=lambda x: {'color': 'blue'}).add_to(m)

# เปรียบเทียบและหาจุดทับซ้อน
coordinates_1 = route_1['features'][0]['geometry']['coordinates']
coordinates_2 = route_2['features'][0]['geometry']['coordinates']

# ✅ ต้องสลับตำแหน่งพิกัดก่อนเปรียบเทียบ (lon, lat) → (lat, lon)
overlap_points = set(map(lambda p: (p[1], p[0]), coordinates_1)) & set(map(lambda p: (p[1], p[0]), coordinates_2))

# วาดจุดทับซ้อนเป็นสีเขียว
for i, (lat, lon) in enumerate(overlap_points):
    if i == 2:
        popup_text = "Siam Scape"  # ชื่อจุดแรก
        image_url = "https://www.pmcuproperty.com/uploads/bu_index/313477896.jpg"
    elif i == len(overlap_points) - 1:
        popup_text = "National Stadium"  # ชื่อจุดสุดท้าย
        image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/National_Stadium_Bangkok_%2835559665256%29.jpg/250px-National_Stadium_Bangkok_%2835559665256%29.jpg"
    else:
        popup_text = "MBK Center"  # จุดที่เหลือ
        image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/MBK_CENTER_%288%29.jpg/300px-MBK_CENTER_%288%29.jpg"

    folium.Marker([lat, lon], popup=popup_text, icon=folium.Icon(color="green")).add_to(m)
    
# สร้าง HTML สำหรับ Popup
    popup_html = f"""
    <h4>{popup_text}</h4>
    <img src="{image_url}" width="200px">
    <p>Latitude: {lat}, Longitude: {lon}</p>
    """

    folium.Marker(
        [lat, lon],
        popup=folium.Popup(popup_html, max_width=250),
        icon=folium.Icon(color="green")
    ).add_to(m)


# route สำหรับหน้าแสดงแผนที่
@app.route('/')
def map_view():
    # บันทึกแผนที่ลงใน static directory
    map_path = os.path.join(app.static_folder, 'map_with_routes.html')
    m.save(map_path)
    return render_template('map_view.html', map_path='map_with_routes.html')

if __name__ == "__main__":
    app.run(debug=True)
