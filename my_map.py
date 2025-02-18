import folium

# พิกัดที่คุณต้องการ
location = [13.745880, 100.530489]  # จาก OpenStreetMap

# สร้างแผนที่
m = folium.Map(location=location, zoom_start=18)

# เพิ่ม Marker สำหรับพิกัดที่ต้องการ
folium.Marker(location).add_to(m)

# บันทึกแผนที่เป็น HTML
m.save("siam_square_map.html")