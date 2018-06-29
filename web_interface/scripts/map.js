// Create the mapo
var map = L.map('map', {
	minZoom: 2,
	maxZoom: 4,
	center: [-100, 220],
	zoom: 3,
	// Prevent user from dragging outside the bounds
	maxBoundsViscosity: 1.0,	
	// Tell Leaflet to use a 1-1 mapping btwn screen px
	// and its internal lat-long coord system
	crs: L.CRS.Simple 
});
// Disable double-click to zoom
map.doubleClickZoom.disable();

// Bookmarks
var control = new L.Control.Bookmarks().addTo(map);

// Drawing polygons on web interface
var drawnItems = new L.FeatureGroup();
map.addLayer(drawnItems);
var drawControl = new L.Control.Draw({
	draw: {
		marker: false,
		circlemarker: false,
		polyline: false,
	},
	edit: {
		featureGroup: drawnItems
	},	     	
});
map.addControl(drawControl);

map.on(L.Draw.Event.CREATED, function(e) {
	var type = e.layerType,
	    layer = e.layer;
	drawnItems.addLayer(layer);
	// Prompt user to enter a name for the drawn item		
	var itemName = prompt("Enter a name for the drawn object");
	drawnItems.bindPopup(itemName);	
	// TODO: Save drawn item
	var polygon = layer.toGeoJSON();
	alert(polygon); // Polygon object
	var polygon_string = JSON.stringify(polygon);
	console.log(polygon_string); // JSON string 
	polygon.name = itemName;
	alert(polygon.name + " has been created.");
   document.getElementById('textbox').value = polygon_string;
	document.getElementById('form').submit();
	// Send to DB	
	/*
	$.ajax({
		url: 'http://10.1.111.238:5000/send_polygon',
		type: 'post',
		data: polygon_string,
		contentType: 'application/json',
		dataType: 'string',
	});
	*/
});


// TODO: Adjust values from here on after map is available

// Image
var w = 2016,
	 h = 1036,
	 url = "https://upload.wikimedia.org/wikipedia/commons/f/fe/La_sanfernando_valley_wikivoyage_map.png"; 

// Calculate the edges of the image, in coordinate space
var southWest = map.unproject([0, h], map.getMaxZoom()-1);
var northEast = map.unproject([w, 0], map.getMaxZoom()-1);
var bounds = new L.LatLngBounds(southWest, northEast);

// Add the image overlay  
L.imageOverlay(url, bounds).addTo(map);

// Tell leaflet that the map is exactly as big as the image
map.setMaxBounds(bounds);

// Create marker and popup for BL
var beyondLimits = L.marker([-108,218]).addTo(map);
beyondLimits.bindPopup("Beyond Limits").openPopup();

// Create circle for DT Glendale area
var downtownGlendale = L.circle([-110.5,219], {
	color: 'green',
	fillColor: 'lime',
	fillOpacity: 0.3,
	radius: 11 
}).addTo(map);
downtownGlendale.bindPopup("Downtown Glendale");

// Create other markers and their popups
var portosBurbank = L.marker([-95.5,176.5]).addTo(map);
portosBurbank.bindPopup("Porto's Bakery and Cafe");
var universalStudios = L.marker([-111,174]).addTo(map);
universalStudios.bindPopup("Universal Studios Hollywood");

// Get coordinates of clicked location
/*
function onMapClick(e) {
	alert("You clicked the map at " + e.latlng.toString());
}
map.on('click', onMapClick);
*/

// Polygon
var park = L.polygon([
	[-72.875, 196.500434],
	[-72.625, 197.9956],
	[-73.5, 198.000115],
	[-74.75, 198.249956],
	[-74.75, 198.874557],
	[-73.125, 198.374876],
	[-72.625, 198.874557],
	[-71.75, 198.124716],
	[-71, 198.124716],
	[-71, 199.249318],
	[-72.125, 199.249318],
	[-72.125, 200.12376],
	[-69, 200.12376],
	[-69, 203.371687],
	[-73.375, 206.619613],
	[-73.375, 202.247404],
	[-76.75, 202.247404],
	[-77.75, 201.997564],
	[-76.75, 200.12376],
	[-79.875, 197.625354],
	[-78.875, 196.625992],
	[-75.375, 197.125673],
]).addTo(map);
park.setStyle({
	fillColor: "pink",
	color: "lightpink",
	fillOpacity: 0.5,
	opacity: 0.4,
});
park.bindPopup("Wildwood Canyon Park");

// Polyline/Path
var travel = L.polyline([beyondLimits.getLatLng(), universalStudios.getLatLng()]).addTo(map);

// Leaflet.PointInPolygon test
var p1 = new L.Marker([-78, 198]); // Point within the polygon
console.log(park.contains(p1.getLatLng())); // returns true
var p2 = new  L.Marker([-78, 180]); // Point outside and west of polygon
console.log(park.contains(p2.getLatLng())); // returns false

/*
// GeoJson test
var geoFeat = {
	"type": "Feature",
	"properties": {},
	"geometry": {
		"type":"Polygon",
		"coordinates":[[
			[126,-64.75],
			[140,-80],
			[200,-80],
		]]
	}
};
L.geoJSON(geoFeat).addTo(map);
*/


