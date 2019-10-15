# Lesson 4 - Map Visualization and Filters

## Outline
* GeoJSON
* Map Visualization
* Data Filtering
* Nesting

## GeoJSON
Inspect the `D3_4_1_inspect_this.htm` file and analyze what it does. Add the `debugger` after the SVG line and oen it on Chrome to inspect the information loaded from the `world_countries.json`. Inspect the `geo_data` variable logged. More about the GeoJSON format [here](https://mygeodata.cloud/converter/geojson-to-latlong).

## Map Visualization
The json file will be used to visualize the polygons associated with the world countries. For this, we'll start selecting a projection:
``` javascript
let projection = d3.geoMercator();
```

The projections tranforms a `latitude,longitude` pair of points in the pixel coordinates display to the SVG element. Next we'll draw the polygons using the `path` element.
``` javascript
let path = d3.geoPath().projection(projection);

svg.append("path")
  	.attr("d", path(geo_data));
```
The `path` function returns a path of each country. Verify this with the `debugger` function after the path line and see what happens when the argument is a GeoJSON object (`path(geo_data.features[0]))`).  
Modify the scale and position of the map using the `transform` scale and translate functions in the mercator object. Adjust the scale to 170 (default scale value is 150, try woth values ranging between 100 and 500). Center the map in the middle of SVG.  
Modify