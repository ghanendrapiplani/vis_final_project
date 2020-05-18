var countries = ["IN", "CN", "KZ", "US"]
    am4core.ready(function() {
    
    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end
    
    // Create map instance
    var chart = am4core.create("chartdiv", am4maps.MapChart);
    
    // Set map definition
    chart.geodata = am4geodata_worldLow;
    
    // Set projection
    chart.projection = new am4maps.projections.NaturalEarth1();
    
    // Create map polygon series
    var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
    polygonSeries.mapPolygons.template.strokeWidth = 0.5;
    
    // Exclude Antartica
    polygonSeries.exclude = ["AQ"];
    
    // Make map load polygon (like country names) data from GeoJSON
    polygonSeries.useGeodata = true;
    
    // Configure series
    var polygonTemplate = polygonSeries.mapPolygons.template;
    polygonTemplate.tooltipText = "{name}";
    polygonTemplate.fill = chart.colors.getIndex(0);
    
    // Create hover state and set alternative fill color
    var hs = polygonTemplate.states.create("hover");
    hs.properties.fill = chart.colors.getIndex(2);
    
    // Create active state
    var activeState = polygonTemplate.states.create("active");
    activeState.properties.fill = chart.colors.getIndex(4);
    
    polygonTemplate.sele

    // Create an event to toggle "active" state
    polygonTemplate.events.on("hit", function(ev) {
      ev.target.isActive = !ev.target.isActive;
      id = ev.target.dataItem.dataContext.id
      if(countries.indexOf(id) === -1) {
        countries.push(id);
        console.log(id);
        console.log(countries)
      }else{
        countries.splice( countries.indexOf(id), 1 );
        console.log(countries)
      }
      ajax_fx("http://127.0.0.1:5000/radar");
      ajax_fx("http://127.0.0.1:5000/parallelcord");
      ajax_fx("http://127.0.0.1:5000/scatter");
    })
    
    chart.events.on("ready", function(ev) {
      for(var i = 0; i < countries.length; i++) {
        var country = polygonSeries.getPolygonById(countries[i]);
        country.isActive = true;
        
    }
    });


    var graticuleSeries = chart.series.push(new am4maps.GraticuleSeries());
    
    });

    function ajax_fx(url){
      console.log("ajax for url"+url)

//      $(".loader").show();
//      d3.select("svg").remove();
      $.ajax({url: url, data : {data:countries.join(", ")}, success: function(result){
        console.log(url)
//              $(".loader").hide();
//              $("#div1").html(result);
      }});
}