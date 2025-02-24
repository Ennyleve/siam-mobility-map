var latlngs = [
    [13.74588, 100.530489],
    [13.74600, 100.53100]
];
var polyline = L.polyline(latlngs, {color: 'blue'}).addTo(map_f583aefe328f879114063c58f137aa6f);

// ฟังก์ชันที่จะรับข้อมูลพิกัดใหม่และเพิ่มลงในแผนที่
function updateRoute(newLat, newLng) {
    var newLatLng = [newLat, newLng];
    polyline.addLatLng(newLatLng); // เพิ่มพิกัดใหม่ลงในเส้นทาง
    map.setView(newLatLng, 18); // เคลื่อนแผนที่ไปที่พิกัดใหม่
}

marker.bindPopup("<b>Location:</b> Siam Square").openPopup();