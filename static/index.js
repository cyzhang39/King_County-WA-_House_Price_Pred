function zipcode() {
    var target = document.getElementById("zipcode");
    return target.value;
}

function area() {
    var target = document.getElementById("area");
    return target.value;
}

function above() {
    var target = document.getElementById("above");
    return target.value;
}

function basement() {
    var target = document.getElementById("basement");
    return target.value;
}

function yrBuilt() {
    var target = document.getElementById("built");
    return target.value;
}

function yrRenovated() {
    var target = document.getElementById("renovated");
    return target.value;
}

function beds() {
    var target = document.getElementById("beds");
    return target.value;
}

function baths() {
    var target = document.getElementById("baths");
    return target.value;
}

function floor() {
    var target = document.getElementById("floors");
    return target.value;
}


function submitInfo(){
    console.log("Predicting price based on your info...");
    var zip = document.getElementById("zipcode").value;
    var bedrooms = document.getElementById("beds").value;
    var bathrooms = document.getElementById("baths").value;
    var sqft = document.getElementById("area").value;
    var floors = document.getElementById("floors").value;
    var above = document.getElementById("above").value;
    var base = document.getElementById("basement").value;
    var built = document.getElementById("built").value;
    var reno = document.getElementById("renovated").value;

    var result = document.getElementById("result");
  
    var url = "http://127.0.0.1:5000/predict";
  
    $.post(url, {
        zipcode: zip.toString(),
        bedrooms: parseInt(bedrooms),
        bathrooms: parseInt(bathrooms),
        sqft_living: parseInt(sqft),
        floors: parseInt(floors),
        sqft_above: parseInt(above),
        sqft_basement: parseInt(base),
        yr_built: parseInt(built),
        yr_renovated: parseInt(reno),
        
    },function(data, status) {
        console.log(data.price);
        result.innerHTML = "<h1>$" + data.price.toString() + " </h1>";
        console.log(status);
    });
}