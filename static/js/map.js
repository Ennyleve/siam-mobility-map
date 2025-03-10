let map;
let marker;
let geocoder;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 13.736717, lng: 100.523186 }, // Bangkok
        zoom: 12,
    });

    geocoder = new google.maps.Geocoder();

    marker = new google.maps.Marker({
        map: map,
        draggable: true,
    });

    const autocomplete = new google.maps.places.Autocomplete(document.getElementById("address-autocomplete"));
    autocomplete.addListener("place_changed", function () {
        let place = autocomplete.getPlace();
        if (!place.geometry) {
            console.error("No details available for input: '" + place.name + "'");
            return;
        }
        marker.setPosition(place.geometry.location);
        map.setCenter(place.geometry.location);
    });
}

function geocodeAddress(address) {
    geocoder.geocode({ address: address }, function (results, status) {
        if (status === "OK") {
            map.setCenter(results[0].geometry.location);
            marker.setPosition(results[0].geometry.location);
        } else {
            alert("Geocode was not successful for the following reason: " + status);
        }
    });
}

window.initMap = initMap;
