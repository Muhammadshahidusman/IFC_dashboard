// Initialize the map
var map = L.map('map').setView([24.8607, 67.0011], 10); // Center the map (adjust coordinates for your region)

// Base map layers
var osmLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors',
    maxZoom: 18
});

var googleSatLayer = L.tileLayer('https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    attribution: '© Google Maps'
});

var googleStreetsLayer = L.tileLayer('https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
    attribution: '© Google Maps'
});

// GeoServer WFS URL (Modify accordingly)
var wfsUrl = 'http://34.209.210.215:8080/geoserver/IFC/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=IFC:home_karachi_buildings&outputFormat=application/json';

// Fetch GeoJSON from GeoServer WFS
fetch(wfsUrl)
    .then(response => response.json())
    .then(data => {
        var geojsonLayer = L.geoJSON(data, {
            pointToLayer: function (feature, latlng) {
                return L.circleMarker(latlng, {
                    radius: 6,
                    fillColor: "#ff7800",
                    color: "#000",
                    weight: 1,
                    opacity: 1,
                    fillOpacity: 0.8
                });
            },
            onEachFeature: function (feature, layer) {
                layer.bindPopup("<b>ID:</b> " + feature.id + "<br><b>Name:</b> " + (feature.properties.name || "N/A"));
            }
        });
        geojsonLayer.addTo(map);
    })
    .catch(error => console.log("Error loading WFS data: ", error));

// Layer control to toggle base layers
var baseLayers = {
    "OpenStreetMap": osmLayer,
    "Google Satellite": googleSatLayer,
    "Google Streets": googleStreetsLayer
};

// Add default base layer
googleStreetsLayer.addTo(map);

// Add layer control
L.control.layers(baseLayers).addTo(map);
