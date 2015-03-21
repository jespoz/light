$(function () {

    $(document).on('ready', main);

    function main(){

        cargar_circular_kilo();
        cargar_circular_neto();
        graficos_acumulados();

        $("div[id^='cuenta']").each(function(){
            var element = $(this);
            var count = element.data('numero');
            var classAdd = element.data('clase');
            for( i = 0; i < count; i++ ){
                element.append("<i class='fa fa-male " + classAdd + "'></i>");
            }
        });

    }

    function cargar_circular_kilo(){

        var el = document.getElementById('graph-kilos');

        var options = {
            percent:  el.getAttribute('data-percent') || 25,
            size: el.getAttribute('data-size') || 80,
            lineWidth: el.getAttribute('data-line') || 10,
            rotate: el.getAttribute('data-rotate') || 0
        };

        var canvas = document.createElement('canvas');
        var span = document.createElement('span');
        span.textContent = options.percent + '%';

        if(options.percent < 0){
            span.className = 'valor_porc danger';
        }else{
            span.className = 'valor_porc success';
        }

        if (typeof(G_vmlCanvasManager) !== 'undefined') {
            G_vmlCanvasManager.initElement(canvas);
        }

        var ctx = canvas.getContext('2d');
        canvas.width = canvas.height = options.size;

        el.appendChild(span);
        el.appendChild(canvas);

        ctx.translate(options.size / 2, options.size / 2); // change center
        ctx.rotate((-1 / 2 + options.rotate / 180) * Math.PI); // rotate -90 deg

        //imd = ctx.getImageData(0, 0, 240, 240);
        var radius = (options.size - options.lineWidth) / 2;

        var drawCircle = function(color, lineWidth, percent) {
                percent = Math.min(Math.max(0, percent || 1), 1);
                ctx.beginPath();
                ctx.arc(0, 0, radius, 0, Math.PI * 2 * percent, false);
                ctx.strokeStyle = color;
                ctx.lineCap = 'round'; // butt, round or square
                ctx.lineWidth = lineWidth;
                ctx.stroke();
        };

        drawCircle('#CCC', options.lineWidth - 6, 100 / 100);

        if(options.percent < 0){
            drawCircle('#AC291F', options.lineWidth, -options.percent / 100);
        }else{
            drawCircle('#4D9379', options.lineWidth, options.percent / 100);
        }

    }

    function cargar_circular_neto(){

        var el = document.getElementById('graph-netos');

        var options = {
            percent:  el.getAttribute('data-percent') || 25,
            size: el.getAttribute('data-size') || 80,
            lineWidth: el.getAttribute('data-line') || 10,
            rotate: el.getAttribute('data-rotate') || 0
        };

        var canvas = document.createElement('canvas');
        var span = document.createElement('span');
        span.textContent = options.percent + '%';

        if(options.percent < 0){
            span.className = 'valor_porc danger';
        }else{
            span.className = 'valor_porc success';
        }

        if (typeof(G_vmlCanvasManager) !== 'undefined') {
            G_vmlCanvasManager.initElement(canvas);
        }

        var ctx = canvas.getContext('2d');
        canvas.width = canvas.height = options.size;

        el.appendChild(span);
        el.appendChild(canvas);

        ctx.translate(options.size / 2, options.size / 2); // change center
        ctx.rotate((-1 / 2 + options.rotate / 180) * Math.PI); // rotate -90 deg

        //imd = ctx.getImageData(0, 0, 240, 240);
        var radius = (options.size - options.lineWidth) / 2;

        var drawCircle = function(color, lineWidth, percent) {
                percent = Math.min(Math.max(0, percent || 1), 1);
                ctx.beginPath();
                ctx.arc(0, 0, radius, 0, Math.PI * 2 * percent, false);
                ctx.strokeStyle = color;
                ctx.lineCap = 'round'; // butt, round or square
                ctx.lineWidth = lineWidth;
                ctx.stroke();
        };

        drawCircle('#CCC', options.lineWidth - 6, 100 / 100);

        if(options.percent < 0){
            drawCircle('#AC291F', options.lineWidth, -options.percent / 100);
        }else{
            drawCircle('#4D9379', options.lineWidth, options.percent / 100);
        }

    }

    function graficos_acumulados(){

        var id_periodo = '';
        var loc = document.location.href;
        id_periodo = loc.substr((loc.length + 1) - 5);
        id_periodo = id_periodo.replace(/\//g, '');

        chart_kilos = new Highcharts.Chart({
            chart: {
                backgroundColor: '',
                borderColor: '#a2a2a1',
                borderWidth: 0,
                borderRadius: 0,
                renderTo: 'kilos-graph',
                type: 'column',
                plotBackgroundColor: ''
            },
            colors: ['#4D9379'],
            credits:{
                enabled: false
            },
            legend: {
                enabled: false
            },
            plotOptions: {
                series: {
                    pointWidth: 15
                }
            },
            title: {
                text: ''
            },
            tooltip: {
                pointFormat: '{point.y:,.0f} TON'
            },
            xAxis:{
                labels:{
                    enabled: false
                }
            },
            yAxis: {
                labels:{
                    enabled: false
                },
                title:{
                    enabled: false
                },
                gridLineWidth: 0,
                minorGridLineWidth: 0
            }
        });

        chart_netos = new Highcharts.Chart({
            chart: {
                backgroundColor: '',
                borderColor: '#a2a2a1',
                borderWidth: 0,
                borderRadius: 0,
                renderTo: 'netos-graph',
                type: 'column',
                plotBackgroundColor: ''
            },
            colors: ['#4D9379'],
            credits:{
                enabled: false
            },
            legend: {
                enabled: false
            },
            plotOptions: {
                series: {
                    pointWidth: 15
                }
            },
            title: {
                text: ''
            },
            tooltip: {
                pointFormat: '{point.y:,.0f} $M'
            },
            xAxis:{
                labels:{
                    enabled: false
                }
            },
            yAxis: {
                labels:{
                    enabled: false
                },
                title:{
                    enabled: false
                },
                gridLineWidth: 0,
                minorGridLineWidth: 0
            }
        });

        chart_precio = new Highcharts.Chart({
            chart: {
                backgroundColor: '',
                borderColor: '#a2a2a1',
                borderWidth: 0,
                borderRadius: 0,
                renderTo: 'acum_pp',
                type: 'line',
                plotBackgroundColor: ''
            },
            colors: ['#FFF'],
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
                lineWidth: 1,
                lineColor: '#FFF'
            },
            yAxis: {
                labels:{
                    enabled: false
                },
                title:{
                    enabled: false
                },
                gridLineWidth: 0,
                minorGridLineWidth: 0,
                lineWidth: 1,
                lineColor: '#FFF'
            },
            tooltip: {
                pointFormat: '${point.y:,.0f}'
            }
        });

        chart_locales = new Highcharts.Chart({
            chart: {
                backgroundColor: '',
                borderColor: '#a2a2a1',
                borderWidth: 0,
                borderRadius: 0,
                renderTo: 'acum_locales',
                type: 'line',
                plotBackgroundColor: ''
            },
            colors: ['#FFF'],
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
                lineWidth: 1,
                lineColor: '#FFF'
            },
            yAxis: {
                labels:{
                    enabled: false
                },
                title:{
                    enabled: false
                },
                gridLineWidth: 0,
                minorGridLineWidth: 0,
                lineWidth: 1,
                lineColor: '#FFF'
            },
            tooltip: {
                pointFormat: '{point.y:,.0f}'
            }
        });

        chart_frecuencia = new Highcharts.Chart({
            chart: {
                backgroundColor: '',
                borderColor: '#a2a2a1',
                borderWidth: 0,
                borderRadius: 0,
                renderTo: 'acum_frecuencia',
                type: 'line',
                plotBackgroundColor: ''
            },
            colors: ['#FFF'],
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
                lineWidth: 1,
                lineColor: '#FFF'
            },
            yAxis: {
                labels:{
                    enabled: false
                },
                title:{
                    enabled: false
                },
                gridLineWidth: 0,
                minorGridLineWidth: 0,
                lineWidth: 1,
                lineColor: '#FFF'
            },
            tooltip: {
                pointFormat: '{point.y:,.2f}'
            }
        });

        chart_ticket = new Highcharts.Chart({
            chart: {
                backgroundColor: '',
                borderColor: '#a2a2a1',
                borderWidth: 0,
                borderRadius: 0,
                renderTo: 'acum_ticket',
                type: 'line',
                plotBackgroundColor: ''
            },
            colors: ['#FFF'],
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
                lineWidth: 1,
                lineColor: '#FFF'
            },
            yAxis: {
                labels:{
                    enabled: false
                },
                title:{
                    enabled: false
                },
                gridLineWidth: 0,
                minorGridLineWidth: 0,
                lineWidth: 1,
                lineColor: '#FFF'
            },
            tooltip: {
                pointFormat: '{point.y:,.1f}'
            }
        });

        var datosApi = '';

        if(!isNaN(id_periodo)) {
            datosApi = '/data/carga_venta_acumulada_filtro/' + id_periodo + '/';
        }else{
            datosApi = '/data/carga_venta_acumulada/';
        }


        $.getJSON(datosApi, function (data) {
            var semanas = [];
            var kilos = [];
            var netos = [];
            var precios = [];
            var locales = [];
            var frecuencia = [];
            var ticket = [];
            $.each(data.semanas, function (key, val) {
                semanas.push(val.periodo__periodo);
            });
            $.each(data.ventas, function (key, val) {
                kilos.push(val.fields['kilo']);
                netos.push(val.fields['neto']);
                precios.push(val.fields['precio']);
                locales.push(val.fields['locales']);
                frecuencia.push(val.fields['frecuencia']);
                ticket.push(val.fields['ticket']);
            });
            chart_kilos.xAxis[0].setCategories(semanas);
            chart_netos.xAxis[0].setCategories(semanas);
            chart_precio.xAxis[0].setCategories(semanas);
            chart_locales.xAxis[0].setCategories(semanas);
            chart_frecuencia.xAxis[0].setCategories(semanas);
            chart_ticket.xAxis[0].setCategories(semanas);
            var series = {data: kilos};
            chart_kilos.addSeries(series);
            series = {data: netos};
            chart_netos.addSeries(series);
            series = {data: precios};
            chart_precio.addSeries(series);
            series = {data: locales};
            chart_locales.addSeries(series);
            series = {data: frecuencia};
            chart_frecuencia.addSeries(series);
            series = {data: ticket};
            chart_ticket.addSeries(series);
        });

    }

});
