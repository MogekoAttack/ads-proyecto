document.addEventListener("DOMContentLoaded", (event) => {
    
})

async function principal(){
    await obtenerDatos();

    GraficoAvance();
    GraficoPresupuesto();
    GraficoMateriales();
    GraficoTrabajadores();
}

function GraficoAvance() {
    google.charts.load("current", { packages: ["corechart"] });
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = google.visualization.arrayToDataTable([
            ['Edificio', 'Porcentaje de avance', 'No completado'],
            ['Edificio Gobierno', 10, 90],
        ]);

        var options = {
            isStacked: true,
            legend: { position: 'none' },
        };
        var chart = new google.visualization.BarChart(document.getElementById("chart_avance"));
        chart.draw(data, options);
    }
}

async function obtenerDatos(parametro) {
    const url = 'http://127.0.0.1:8000/api/v2/'+parametro;
    const respuesta = await fetch(url);
    if (!respuesta.ok) {
        throw new Error(`HTTP error! status: ${respuesta.status}`);
    }
    const datos = await respuesta.json();
    console.log('datos: ', datos);
    
    return datos;
}

function GraficoPresupuesto() {
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Concepto');
        data.addColumn('number', 'Cantidad');
        data.addRows([
            ['Mano de obra', 33],
            ['Material', 50],
        ]);

        var options = {
            title: 'Presupuesto',
            sliceVisibilityThreshold: .2
        };

        var chart = new google.visualization.PieChart(document.getElementById('chart_presupuesto'));
        chart.draw(data, options);
    }
}

function GraficoMateriales() {
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Concepto');
        data.addColumn('number', 'Sin usar');
        data.addColumn('number', 'Usado');
        data.addRows([
            ['Ladrillo', 33,20],
            ['Cable', 50,70],
        ]);

        var options = {
            isStacked: true,
            title: 'Materiales',
        };

        var chart = new google.visualization.ColumnChart(document.getElementById('chart_materiales'));
        chart.draw(data, options);
    }
}

function GraficoTrabajadores(){
    google.charts.load('current', {packages:["orgchart"]});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');

        // For each orgchart box, provide the name, manager, and tooltip to show.
        data.addRows([
          [{'v':'Leonardo', 'f':'Mike<div style="color:red; font-style:italic">President</div>'},
           '', 'Super intendente'],
           [{'v':'Donatello', 'f':'Jim<div style="color:red; font-style:italic">Indendente</div>'},
           'Mike', 'VP'],
           [{'v':'Miguel Angel', 'f':'Jim<div style="color:red; font-style:italic">Indendente x2</div>'},
           'Mike', 'VP'],
          ['Bob', 'Jim', 'Bob Sponge'],
          ['Carol', 'Bob', '']
        ]);

        // Create the chart.
        var chart = new google.visualization.OrgChart(document.getElementById('chart_jerarquia_gobierno'));
        // Draw the chart, setting the allowHtml option to true for the tooltips.
        chart.draw(data, {'allowHtml':true});
      }
}