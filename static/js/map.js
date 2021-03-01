// Initialize and add the map
let map, infoWindow;

function initMap() {
    console.log("Map Page");

    // The location of Uluru
    // const uluru = { lat: -25.344, lng: 131.036 };
    
    // The map, centered at Uluru
    map = new google.maps.Map(document.getElementById("map"), {
      zoom: 17,
      // center: uluru,
    });
    infoWindow = new google.maps.InfoWindow();

     
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            const pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            };
            infoWindow.setPosition(pos);
            infoWindow.setContent("Location found.");
            infoWindow.open(map);
            map.setCenter(pos);
          },
          () => {
            handleLocationError(true, infoWindow, map.getCenter());
          }
        );
      } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
      }
  
  //});
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  );
  infoWindow.open(map);
}

