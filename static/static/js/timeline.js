$(function () {

    $(document).on('ready', main);

    function main(){
        $(".graph-acum").each(function(){
            var $id = $(this).data('id');
            window['chart' + $id] = new Highcharts.Chart({
                chart: {
                    backgroundColor: '',
                    borderColor: '#CCC',
                    borderWidth: 0,
                    borderRadius: 0,
                    renderTo: 'graph-acum-' + $id,
                    type: 'area',
                    plotBackgroundColor: '',
                    width: 150,
                    height: 70
                },
                colors: ['#E3713B'],
                credits:{
                    enabled: false
                },
                legend: {
                    enabled: false
                },
                title: {
                    text: ''
                },
                xAxis:{
                    labels:{
                        enabled: false
                    },
                    lineWidth: 0,
                    lineColor: 'transparent'
                },
                plotOptions: {
                    series: {
                        fillOpacity: 0.2
                    }
                },
                yAxis: {
                    labels:{
                        enabled: false
                    },
                    title:{
                        enabled: false
                    },
                    gridLineWidth: 1,
                    gridLineColor: '#E3713B',
                    minorGridLineWidth: 0,
                    lineWidth: 1,
                    lineColor: 'transparent'
                },
                tooltip: {
                    pointFormat: '{point.y:,.1f}%'
                }
            });

            datosApi = '/design/acumulados/' + $id + '/';

            $.getJSON(datosApi, function (data) {
                var periodos = [];
                var valores = [];

                $.each(data.indicador, function (key, val) {
                    periodos.push(val.periodo__periodo);
                    console.log('ingreso');
                    console.log($id);
                    //if($id == 1) {
                        //console.log(1);
                        valores.push(val.ac);
                    //}else if($id == 6){
                        //console.log(2);
                        //valores.push(val.resultado);
                    //}
                    //console.log(3);
                });

                Array.max = function(array){
                  return Math.max.apply(Math, array);
                };

                Array.min = function(array){
                  return Math.min.apply(Math, array);
                };

                var min = Array.min(valores);
                var max = Array.max(valores);

                window['chart' + $id].xAxis[0].setCategories(periodos);
                window['chart' + $id].yAxis[0].setExtremes(min, max);
                var series = {data: valores};
                window['chart' + $id].addSeries(series);

            });

        });
    }
});
