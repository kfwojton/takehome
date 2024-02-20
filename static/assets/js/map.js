!(function (o) {
    Array.prototype.forEach ||
        (o.forEach =
            o.forEach ||
            function (o, e) {
                for (var t = 0, r = this.length; t < r; t++) t in this && o.call(e, this[t], t, this);
            });
})(Array.prototype);
var mapObject,
    marker,
    markers = [],
    markersData = {
        Marker: [
            {
                location_latitude: 48.866024,
                location_longitude: 2.340041,
                locationURL: "single-property-2.html",
                locationImg: "https://via.placeholder.com/800x500",
                propertypricebed: "$220 + 2Bed",
                propertyname: "#204 Green Vally Resort",
                propertylocation: "Montreal, Canada",
				contactURL: "single-property-2.html",
            },
            {
                location_latitude: 48.86856,
                location_longitude: 2.349427,
                locationURL: "single-property-2.html",
                locationImg: "https://via.placeholder.com/800x500",
                propertypricebed: "$220 + 2Bed",
                propertyname: "#204 Green Vally Resort",
                propertylocation: "Montreal, Canada",
				contactURL: "single-property-2.html",
            },
            {
                location_latitude: 48.870824,
                location_longitude: 2.333005,
                locationURL: "single-property-2.html",
                locationImg: "https://via.placeholder.com/800x500",
                propertypricebed: "$220 + 2Bed",
                propertyname: "#204 Green Vally Resort",
                propertylocation: "Montreal, Canada",
				contactURL: "single-property-2.html",
            },
            {
                location_latitude: 48.864642,
                location_longitude: 2.345837,
                locationURL: "single-property-2.html",
                locationImg: "https://via.placeholder.com/800x500",
                propertypricebed: "$220 + 2Bed",
                propertyname: "#204 Green Vally Resort",
                propertylocation: "Montreal, Canada",
				contactURL: "single-property-2.html",
            },
            {
                location_latitude: 48.861753,
                location_longitude: 2.338402,
                locationURL: "single-property-2.html",
                locationImg: "https://via.placeholder.com/800x500",
                propertypricebed: "$220 + 2Bed",
                propertyname: "#204 Green Vally Resort",
                propertylocation: "Montreal, Canada",
				contactURL: "single-property-2.html",
            },
            {
                location_latitude: 48.872111,
                location_longitude: 2.345151,
                locationURL: "single-property-2.html",
                locationImg: "https://via.placeholder.com/800x500",
                propertypricebed: "$220 + 2Bed",
                propertyname: "#204 Green Vally Resort",
                propertylocation: "Montreal, Canada",
				contactURL: "single-property-2.html",
            },
            {
                location_latitude: 48.865881,
                location_longitude: 2.341507,
                locationURL: "single-property-2.html",
                locationImg: "https://via.placeholder.com/800x500",
                propertypricebed: "$220 + 2Bed",
                propertyname: "#204 Green Vally Resort",
                propertylocation: "Montreal, Canada",
				contactURL: "single-property-2.html",
            },
            {
                location_latitude: 48.867236,
                location_longitude: 2.34361,
                locationURL: "single-property-2.html",
                locationImg: "https://via.placeholder.com/800x500",
                propertypricebed: "$220 + 2Bed",
                propertyname: "#204 Green Vally Resort",
                propertylocation: "Montreal, Canada",
				contactURL: "single-property-2.html",
            },
        ],
    },
    mapOptions = {
        zoom: 15,
        center: new google.maps.LatLng(48.867236, 2.34361),
        mapTypeId: google.maps.MapTypeId.satellite,
        mapTypeControl: !1,
        mapTypeControlOptions: { style: google.maps.MapTypeControlStyle.DROPDOWN_MENU, position: google.maps.ControlPosition.LEFT_CENTER },
        panControl: !1,
        panControlOptions: { position: google.maps.ControlPosition.TOP_RIGHT },
        zoomControl: !0,
        zoomControlOptions: { position: google.maps.ControlPosition.RIGHT_BOTTOM },
        scrollwheel: !1,
        scaleControl: !1,
        scaleControlOptions: { position: google.maps.ControlPosition.TOP_LEFT },
        streetViewControl: !0,
        streetViewControlOptions: { position: google.maps.ControlPosition.LEFT_TOP },
    };
for (var key in ((mapObject = new google.maps.Map(document.getElementById("map"), mapOptions)), markersData))
    markersData[key].forEach(function (o) {
        (marker = new google.maps.Marker({ position: new google.maps.LatLng(o.location_latitude, o.location_longitude), map: mapObject, icon: "assets/img/marker.png" })),
            void 0 === markers[key] && (markers[key] = []),
            markers[key].push(marker),
            google.maps.event.addListener(marker, "click", function () {
                closeInfoBox(), getInfoBox(o).open(mapObject, this), mapObject.setCenter(new google.maps.LatLng(o.location_latitude, o.location_longitude));
            });
    });
function hideAllMarkers() {
    for (var o in markers)
        markers[o].forEach(function (o) {
            o.setMap(null);
        });
}
function closeInfoBox() {
    $("div.infoBox").remove();
}
function getInfoBox(o) {
    return new InfoBox({
        content:
            '<div class="map-popup-wrap"><div class="map-popup"><div class="_RentUP_proprty_grid"><div class="_RentUP_prt_grid_thumb"><a href="' +o.locationURL +'"><img src="' +o.locationImg +'" class="img-fluid" alt="" /></a><div class="rhomy_abs_caption"><h4 class="rhomy_pr_name verify">' + o.propertypricebed +'</h4></div></div><div class="_RentUP_prt_grid_caption"><div class="_RentUP_prt_head"><h5 class="_RentUP_prt_title">' +o.propertyname +'</h5><span class="_RentUP_prt_location"><i class="ti-location-pin mr-1"></i>' +o.propertylocation +'</span></div><div class="_RentUP_prt_bot"><div class="_RentUP_prt_bot_flex"><ul class="featur_5269"><li><div class="ft_th" data-toggle="tooltip" data-placement="top" title="" data-original-title="Pet Allowed"><img src="assets/img/pet.svg" alt=""></div></li><li><div class="ft_th" data-toggle="tooltip" data-placement="top" title="" data-original-title="Air Conditions"><img src="assets/img/cooling.svg" alt=""></div></li><li><div class="ft_th" data-toggle="tooltip" data-placement="top" title="" data-original-title="Wifi Avaialable"><img src="assets/img/wifi.svg" alt=""></div></li><li><div class="ft_th" data-toggle="tooltip" data-placement="top" title="" data-original-title="Gym Center"><img src="assets/img/gym.svg" alt=""></div></li><li><div class="ft_th" data-toggle="tooltip" data-placement="top" title="" data-original-title="Car Parking"><img src="assets/img/car.svg" alt=""></div></li></ul></div><div class="_RentUP_prt_bot_left"><a href=""' +o.contactURL +'"" class="mp_rhomy_btn"><i class="fa fa-envelope mr-1"></i>Contact</a></div></div></div></div></div></div>',
        disableAutoPan: !1,
        maxWidth: 0,
        pixelOffset: new google.maps.Size(10, 92),
        closeBoxMargin: "",
        closeBoxURL: "assets/img/close.png",
        isHidden: !1,
        alignBottom: !0,
        pane: "floatPane",
        enableEventPropagation: !0,
    });
}
function onHtmlClick(o, e) {
    google.maps.event.trigger(markers[o][e], "click");
}
new MarkerClusterer(mapObject, markers[key]);
