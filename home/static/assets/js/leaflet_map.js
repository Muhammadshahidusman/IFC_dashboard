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

var esriTopoLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Topo/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles © Esri'
});

var stamenTonerLayer = L.tileLayer('https://{s}.tile.stamen.com/toner/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.'
});

// Add the GeoServer WMS layer
var geoServerLayer = L.tileLayer.wms('http://34.209.210.215:8080/geoserver/IFC/wms', {
    layers: 'IFC:home_surveyprogress', // Replace with your GeoServer workspace and layer name
    format: 'image/png',
    transparent: true,
    attribution: "GeoServer"
});

// Layer control to toggle base and overlay layers
var baseLayers = {
    "OpenStreetMap": osmLayer,
    "Google Satellite": googleSatLayer,
    "Google Streets": googleStreetsLayer,
    // "Esri Topographic": esriTopoLayer,
    // "Stamen Toner": stamenTonerLayer
};

var overlayLayers = {
    "Building Points": geoServerLayer
};

// Add the default base layer
googleStreetsLayer.addTo(map);
geoServerLayer.addTo(map);

// Add layer control
L.control.layers(baseLayers, overlayLayers).addTo(map);