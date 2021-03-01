
// Global Font Awesome Icons & Variables
var heartIcon = `<i class="fas fa-heart"></i>`;
var hearIconOutline = `<i class="far fa-heart"></i>`;
var carIcon = `<i class="fas fa-car"></i>`;
var meet, night, pass, type, vehicle;
var listingItem;



/**Function to intialize card views of listings. Once clicked, listings will display
more detailed information **/
function init() {

    console.log('working');
    //Grab DOM element
    var listingDom = document.getElementById('listings2');
    // listingDom.innerHTML = <p>Hello World!</p>

    

    console.log("Listings Page");
 
    //if file exists, open and process
    if('../../static/all_listings.txt'){
        fetch('../../static/all_listings.txt')
            .then(response => response.json())
            .then(data => {
                
                console.log(data)

                console.log(Object.keys(data).length)
                var count = 0;

                //Get each Listing object
                while(count < Object.keys( data ).length){
                    
                    //Grab Booleans: Meet Renter
                    if (data[count].meet_Renter === true) {
                        meet = "Yes";
                    } else {
                        meet = "No";
                    }
                    //Overnight Parking
                    if (data[count].overNight === true) {
                        night = "Yes";
                    } else {
                        night = "No";
                    }
                    //Parking Pass Needed
                    if (data[count].parking_Pass === true) {
                        pass = "Yes";
                    } else {
                        pass = "No";
                    }

                    //Listing's Parking Type. Loop through array
                    var i = 0;
                    while(i < data[count].parking.length) {
                        if(data[count].parking[i] === "R"){
                            type += "Residential/Private ";
                        }
                        if(data[count].parking[i] === "G"){
                            type += "Garage ";
                        }
                        if(data[count].parking[i] === "L"){
                            type += "Parking Lot";
                        }
                        if(data[count].parking[i] === "S"){
                            type += "Street Parking";
                        }
                        if(data[count].parking[i] === "O"){
                            type += "Other/Misc";
                        }
                        i++;
                    }
                     
                    //Listing's Vehicle Accomodations. Loop through array
                    var x = 0;
                    while(x < data[count].vehicles.length) {
                        if(data[count].vehicles[x] === "C"){
                            vehicle += "Compact/Sedan ";
                        }
                        if(data[count].vehicles[x] === "T"){
                            vehicle += "Truck/SUV";
                        }
                        if(data[count].vehicles[x] === "V"){
                            vehicle += "Vans";
                        }
                        if(data[count].vehicles[x] === "M"){
                            vehicle += "Motocycles/Mopeds";
                        }
                        if(data[count].vehicles[x] === "O"){
                            vehicle += "Motorhomes or Oversized";
                        }
                        x++;
                    }


                    //add HTML content and display
                    listingItem = `
                        <div id="${data[count].listing_id}" class="listing" style="width: 18rem;">
                            <img src="${data[count].images_id}" id="imageProp">
                            <p>${hearIconOutline}</p>
                            <div id="listHead">
                                <h2 class="card-title">${data[count].title}</h2>
                            </div>
                            <div id="details">
                                <p>${data[count].description}</p>
                            </div>
                            <div id="parkSec">
                                <p>${carIcon}Parking Type: ${type}</p>
                                <p>${carIcon}Vehicles Accomodated: ${vehicle}</p>
                            </div>
                                <p id="price"><b>Hourly Price: $${data[count].hourly_Rate}</b> $USD</p>
                                <p>Day Price: $${data[count].day_Rate}</p>
                            <div>
                                <p class="lead"><a class="btn btn-outline-light btn-lg" href="${data[count].listing_id}" role="button">Details</a></p>
                            </div>
                        </div>   
                    `;

                    //display to HTML
                    listingDom.innerHTML+= listingItem;

                    //increment listing counter
                    count++;
                }
        });
    }
}

// Function to filter listings by parking type
// function filterParking(parking){

// }

// Function to filter listings by location
// function filterLocations(address){

// }


window.onload = init;