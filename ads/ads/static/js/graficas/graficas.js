document.addEventListener("DOMContentLoaded", (event) => {
    principal();
})

async function principal(){
    const gobierno = await obtenerDatos("egobierno_general");
    console.log('gobierno: ', gobierno);

    const ia = await obtenerDatos("eia_general");
    console.log('ia: ', ia);

    const norte = await obtenerDatos("enorte_general");
    console.log('norte: ', norte);

    const sur = await obtenerDatos("esur_general");
    console.log('sur: ', sur);


    GraficoAvance(gobierno, norte, sur, ia);
    GraficoPresupuesto(gobierno, norte, sur, ia);
    GraficoMateriales();
    GraficoTrabajadores();
}

async function obtenerDatos(parametro) {
    const url = 'http://127.0.0.1:8000/api/v2/'+parametro;
    const respuesta = await fetch(url);
    if (!respuesta.ok) {
        throw new Error(`HTTP error! status: ${respuesta.status}`);
    }
    const datos = await respuesta.json();
    
    return datos['items']['0'];
}

function GraficoAvance(gobierno, norte, sur, ia) {
    google.charts.load("current", { packages: ["corechart"] });
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Edificio');
        data.addColumn('number', 'Completado');
        data.addColumn('number', 'Incompleto');

        data.addRows([
            ['Gobierno', gobierno['progreso'], 100-gobierno['progreso']],
            ['Norte', norte['progreso'], 100-norte['progreso']],
            ['Sur', sur['progreso'], 100-sur['progreso']],
            ['IA', ia['progreso'], 100-ia['progreso']],
        ]);

        var options = {
            isStacked: true,
            // legend: { position: 'none' },
            title: 'Progreso'
        };
        var chart = new google.visualization.BarChart(document.getElementById("chart_avance"));
        chart.draw(data, options);
    }
}



function GraficoPresupuesto(gobierno, norte, sur, ia) {
    google.charts.load("current", { packages: ["corechart"] });
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Edificio');
        data.addColumn('number', 'Usado');
        data.addColumn('number', 'Sin usar');

        data.addRows([
            ['Gobierno', gobierno['progreso'], 100-gobierno['progreso']],
            ['Norte', norte['progreso'], 100-norte['progreso']],
            ['Sur', sur['progreso'], 100-sur['progreso']],
            ['IA', ia['progreso'], 100-ia['progreso']],
        ]);

        var options = {
            isStacked: true,
            // legend: { position: 'none' },
            title: 'Presupuesto'
        };

        var chart = new google.visualization.BarChart(document.getElementById('chart_presupuesto'));
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