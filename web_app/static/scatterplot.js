
function drawScatterPlot(data, chart_title) {
    console.log('test', data[0])
    console.log(typeof data[0])
    d3.select('#vizn').remove();
    console.log('data', data[0]);
    var array = [];
    var min = 0, max = 0;

    for(var i=0; i< data.length; ++i){
        obj = {}
        obj.x = data[i][Schooling];
        obj.y = data[i][Life expectancy ];
        obj.clusterid = data[i]['clusterid']
        array.push(obj);
    }

    data = array;
    console.log('array data', data);
    var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;
    var xValue = function(d) { return d.x;}, xScale = d3.scale.linear().range([0, width]),
        xMap = function(d) { return xScale(xValue(d));}, xAxis = d3.svg.axis().scale(xScale).orient("bottom");
    var yValue = function(d) { return d.y;}, yScale = d3.scale.linear().range([height, 0]),
        yMap = function(d) { return yScale(yValue(d));}, yAxis = d3.svg.axis().scale(yScale).orient("left");
    var cValue = function(d) { return d.clusterid;}
    var color = d3.scale.category10();
    var svg = d3.select("body").append("svg")
        .attr('id', 'vizn')
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    var tooltip = d3.select("body").append('div').style('position','absolute');
    xScale.domain([d3.min(data, xValue)-1, d3.max(data, xValue)+1]);
    yScale.domain([d3.min(data, yValue)-1, d3.max(data, yValue)+1]);
    svg.append("g")
          .attr("transform", "translate(0," + height + ")")
          .attr("class", "x_axis")
          .call(xAxis)
        .append("text")
          .attr("class", "label")
          .attr("y", -6)
          .attr("x", width)
          .text("Component 1")
          .style("text-anchor", "end");
    svg.append("g")
          .attr("class", "y_axis")
          .call(yAxis)
        .append("text")
          .attr("class", "label")
          .attr("y", 6)
          .attr("transform", "rotate(-90)")
          .attr("dy", ".71em")
          .text("Component 2")
          .style("text-anchor", "end");
    svg.selectAll(".dot")
          .data(data)
          .enter().append("circle")
          .attr("class", "dot")
          .attr("cx", xMap)
          .attr("r", 4)
          .attr("cy", yMap)
          .style("fill", function(d) { return color(cValue(d));})
    svg.append("text")
        .attr("x", (width / 2))
        .attr("y", 0 + (margin.top / 2))
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .style("text-decoration", "underline")
        .style("font-weight", "bold")
        .text(chart_title);
}