import openrouteservice
import folium
from flask import Flask, render_template
import os

app = Flask(__name__)

# API Key ของคุณ
api_key = '5b3ce3597851110001cf62489e6e8f7493b94012af59a9bd4d8889eb'
client = openrouteservice.Client(key=api_key)

# พิกัดของ National Stadium และ SIAMSCAPE
start = (100.5284337, 13.7446961)  # National Stadium
end = (100.5309092, 13.7444913)   # SIAMSCAPE

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
m = folium.Map(location=[13.745, 100.529], zoom_start=15)

# วาดเส้นทางแรก (National Stadium -> SIAMSCAPE) ด้วยสีแดง
folium.GeoJson(route_1, style_function=lambda x: {'color': 'red'}).add_to(m)

# วาดเส้นทางที่สอง (SIAMSCAPE -> National Stadium) ด้วยสีฟ้า
folium.GeoJson(route_2, style_function=lambda x: {'color': 'blue'}).add_to(m)

# เปรียบเทียบและหาจุดทับซ้อน
coordinates_1 = route_1['features'][0]['geometry']['coordinates']
coordinates_2 = route_2['features'][0]['geometry']['coordinates']
overlap_points = set(map(tuple, coordinates_1)) & set(map(tuple, coordinates_2))

# วาดจุดทับซ้อนเป็นสีเขียว
for point in overlap_points:
    folium.Marker([point[1], point[0]], popup="Overlap").add_to(m)

# route สำหรับหน้าแสดงแผนที่
@app.route('/')
def map_view():
    # บันทึกแผนที่ลงใน static directory
    map_path = os.path.join(app.static_folder, 'map_with_routes.html')
    m.save(map_path)
    return render_template('map_view.html', map_path='map_with_routes.html')

if __name__ == "__main__":
    app.run(debug=True)
