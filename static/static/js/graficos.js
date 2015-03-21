$(function () {

    $(document).on('ready', main);

    function main(){

        var id_periodo;
        var loc = document.location.href;
        id_periodo = loc.substr((loc.length + 1) - 5);
        id_periodo = id_periodo.replace(/\//g, '');

        if(!isNaN(id_periodo)) {
            $.get('/infographic/carga_margen_acumulado_filtro/' + id_periodo + '/', cargar_grafico);
        }else{
            $.get('/infographic/carga_margen_acumulado/', cargar_grafico);
        }

        if(document.getElementById('hash_tipoCliente')){
            cargar_hash_tipoCliente();
        }
        if(document.getElementById('hash_sector')){
            cargar_hash_sector();
        }
        if(document.getElementById('hash_tipoClienteSector')){
            cargar_hash_tipoClienteSector();
        }
        if(document.getElementById('hash_num_sectores')){
            cargar_hash_sectores();
        }

        cargar_circular_pedido();
        cargar_circular_facturado();

        if(!isNaN(id_periodo)) {
            $.get('/infographic/carga_costo_venta_filtro/' + id_periodo + '/', cargar_grafico_pie);
        }else{
            $.get('/infographic/carga_costo_venta/', cargar_grafico_pie);
        }
    }

    function cargar_hash_tipoCliente(){

        var id_periodo;
        var loc = document.location.href;
        id_periodo = loc.substr((loc.length + 1) - 5);
        id_periodo = id_periodo.replace(/\//g, '');

        var datosApi = '';

        if(!isNaN(id_periodo)) {
            datosApi = '/infographic/hash_tipoCliente_filtro/' + id_periodo + '/';
        }else{
            datosApi = '/infographic/hash_tipoCliente/';
        }

        tipos = '';

        $.getJSON(datosApi, function (data) {
            $.each(data.hash, function (key, val) {
                tipos = tipos + ', ' + val.fields['valor']
            });
            $('#hash_tipoCliente').replaceWith('<b>' + tipos.substr(1) +  '</b>');
        });

    }

    function cargar_hash_sector(){

        var id_periodo;
        var loc = document.location.href;
        id_periodo = loc.substr((loc.length + 1) - 5);
        id_periodo = id_periodo.replace(/\//g, '');

        var datosApi = '';

        if(!isNaN(id_periodo)) {
            datosApi = '/infographic/hash_sector_filtro/' + id_periodo + '/';
        }else{
            datosApi = '/infographic/hash_sector/';
        }

        tiposSec = '';

        $.getJSON(datosApi, function (data) {
            $.each(data.hash, function (key, val) {
                tiposSec = tiposSec + ', ' + val.fields['valor']
            });
            $('#hash_sector').replaceWith('<b>' + tiposSec.substr(1) +  '</b>');
        });

    }

    function cargar_hash_tipoClienteSector(){

        var id_periodo;
        var loc = document.location.href;
        id_periodo = loc.substr((loc.length + 1) - 5);
        id_periodo = id_periodo.replace(/\//g, '');

        var datosApi = '';

        if(!isNaN(id_periodo)) {
            datosApi = '/infographic/hash_tipoClienteSector_filtro/' + id_periodo + '/';
        }else{
            datosApi = '/infographic/hash_tipoClienteSector/';
        }

        tiposTCSec = '';

        $.getJSON(datosApi, function (data) {
            $.each(data.hash, function (key, val) {
                tiposTCSec = tiposTCSec + ', ' + val.fields['valor']
            });
            $('#hash_tipoClienteSector').replaceWith('<b>' + tiposTCSec.substr(1) +  '</b>');
        });

    }

    function cargar_hash_sectores(){

        var id_periodo;
        var loc = document.location.href;
        id_periodo = loc.substr((loc.length + 1) - 5);
        id_periodo = id_periodo.replace(/\//g, '');

        var datosApi = '';

        if(!isNaN(id_periodo)) {
            datosApi = '/infographic/hash_sectores_filtro/' + id_periodo + '/';
        }else{
            datosApi = '/infographic/hash_sectores/';
        }

        tiposSecs = '';

        $.getJSON(datosApi, function (data) {
            $.each(data.hash, function (key, val) {
                tiposSecs = tiposSecs + ', ' + val.fields['valor']
            });
            $('#hash_num_sectores').replaceWith('<b>' + tiposSecs.substr(1) +  '</b>');
        });

    }

    function cargar_circular_pedido(){

        var el = document.getElementById('graph-pedido'); // get canvas

        var options = {
            percent:  el.getAttribute('data-percent') || 25,
            size: el.getAttribute('data-size') || 70,
            lineWidth: el.getAttribute('data-line') || 10,
            rotate: el.getAttribute('data-rotate') || 0
        };

        var canvas = document.createElement('canvas');
        var info = document.createElement('div');
        var span = document.createElement('span');
        span.textContent = options.percent + '%';
        info.className ='div_info_circular_progress';

        var span_info = document.createElement('span');
        var span_valor = document.createElement('span');
        span_info.className = 'info_circular';
        span_info.textContent = 'Diferencia entre el precio vigente y el precio del pedido';

        span_valor.className = 'valor_circular';
        span_valor.textContent = el.getAttribute('data-valor');

        info.appendChild(span_info);
        info.appendChild(span_valor);

        if (typeof(G_vmlCanvasManager) !== 'undefined') {
            G_vmlCanvasManager.initElement(canvas);
        }

        var ctx = canvas.getContext('2d');
        canvas.width = canvas.height = options.size;

        el.appendChild(span);
        el.appendChild(canvas);
        el.appendChild(info);

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
        drawCircle('#AC291F', options.lineWidth, options.percent / 100);
    }

    function cargar_circular_facturado(){

        var el = document.getElementById('graph-facturado'); // get canvas

        var options = {
            percent:  el.getAttribute('data-percent') || 25,
            size: el.getAttribute('data-size') || 70,
            lineWidth: el.getAttribute('data-line') || 10,
            rotate: el.getAttribute('data-rotate') || 0
        };

        var canvas = document.createElement('canvas');
        var info = document.createElement('div');
        var span = document.createElement('span');
        span.textContent = options.percent + '%';
        info.className ='div_info_circular_progress';

        var span_info = document.createElement('span');
        var span_valor = document.createElement('span');
        span_info.className = 'info_circular';
        span_info.textContent = 'Diferencia entre el precio del pedido y el precio facturado';

        span_valor.className = 'valor_circular';
        span_valor.textContent = el.getAttribute('data-valor');

        info.appendChild(span_info);
        info.appendChild(span_valor);

        if (typeof(G_vmlCanvasManager) !== 'undefined') {
            G_vmlCanvasManager.initElement(canvas);
        }

        var ctx = canvas.getContext('2d');
        canvas.width = canvas.height = options.size;

        el.appendChild(span);
        el.appendChild(canvas);
        el.appendChild(info);

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
        drawCircle('#AC291F', options.lineWidth, options.percent / 100);
    }

    function cargar_grafico(){

        var id_periodo = '';
        var loc = document.location.href;
        id_periodo = loc.substr((loc.length + 1) - 5);
        id_periodo = id_periodo.replace(/\//g, '');

        chart_answer = new Highcharts.Chart({
            chart: {
                backgroundColor: '',
                borderColor: '#a2a2a1',
                borderWidth: 0,
                borderRadius: 0,
                renderTo: 'margen-graph',
                type: 'area',
                plotBackgroundColor: ''
            },
            credits:{
                enabled: false
            },
            colors: ['#AC291F'],
            legend: {
                enabled: true
            },
            title: {
                text: ''
            },
            tooltip: {
                borderRadius: 0,
                borderWidth: 0,
                shadow: false,
                style: {
                    fontSize: '7pt',
                    color: '#000000'
                },
                pointFormat: '{point.y:.2f} %'
            },
            plotOptions: {
                series: {
                    fillOpacity: 0.2
                }
            },
            yAxis:{
                title: '',
                lineColor: '#4D9379',
                lineWidth: 2,
                minorGridLineDashStyle: 'longdash',
                minorTickInterval: 'auto',
                minorTickWidth: 0,
                labels:{
                    format: '{value:.1f} %',
                    enabled: false
                }
            },
            xAxis:{
                lineColor: '#4D9379',
                lineWidth: 2
            }
        });

        chart_unitario = new Highcharts.Chart({
            chart: {
                backgroundColor: '',
                borderColor: '#a2a2a1',
                borderWidth: 0,
                borderRadius: 0,
                renderTo: 'unitario-graph',
                type: 'area',
                plotBackgroundColor: ''
            },
            credits:{
                enabled: false
            },
            colors: ['#AC291F'],
            legend: {
                enabled: true
            },
            title: {
                text: ''
            },
            tooltip: {
                borderRadius: 0,
                borderWidth: 0,
                shadow: false,
                style: {
                    fontSize: '7pt',
                    color: '#000000'
                },
                pointFormat: '{point.y:.1f} CLP/KG'
            },
            plotOptions: {
                series: {
                    fillOpacity: 0.2
                }
            },
            yAxis:{
                title: '',
                lineColor: '#4D9379',
                lineWidth: 2,
                minorGridLineDashStyle: 'longdash',
                minorTickInterval: 'auto',
                minorTickWidth: 0,
                labels:{
                    format: '{value:.1f} CLP/KG',
                    enabled: false
                }
            },
            xAxis:{
                lineColor: '#4D9379',
                lineWidth: 2
            }
        });

        chart_costos = new Highcharts.Chart({
            chart: {
                backgroundColor: '',
                borderColor: '#a2a2a1',
                borderWidth: 0,
                borderRadius: 0,
                renderTo: 'costos-graph',
                type: 'line',
                plotBackgroundColor: '',
                height: 140
            },
            credits:{
                enabled: false
            },
            colors: ['#AC291F'],
            legend: {
                enabled: true,
                itemStyle: {
                    fontSize: '10px',
                    fontFamily: 'Open Sans Light',
                    fontWeight: 'normal',
                    color: 'grey'
                },
                margin: 0
            },
            title: {
                text: ''
            },
            tooltip: {
                borderRadius: 0,
                borderWidth: 0,
                shadow: false,
                style: {
                    fontSize: '7pt',
                    color: '#000000'
                },
                pointFormat: '{point.y:.2f} %'
            },
            plotOptions: {
                series: {
                    fillOpacity: 0.2
                }
            },
            yAxis:{
                title: '',
                lineColor: '#4D9379',
                lineWidth: 2,
                minorGridLineDashStyle: 'longdash',
                minorTickInterval: 'auto',
                minorTickWidth: 0,
                labels:{
                    format: '{value:.1f} %',
                    enabled: false
                }
            },
            xAxis:{
                lineColor: '#4D9379',
                lineWidth: 2
            }
        });

        chart_distr_sec = new Highcharts.Chart({
            chart: {
                backgroundColor: '',
                borderColor: '#a2a2a1',
                borderWidth: 0,
                borderRadius: 0,
                renderTo: 'distr_sec_graph',
                type: 'line',
                plotBackgroundColor: '',
                height: 140
            },
            credits:{
                enabled: false
            },
            colors: ['#AC291F'],
            legend: {
                enabled: true,
                itemStyle: {
                    fontSize: '10px',
                    fontFamily: 'Open Sans Light',
                    fontWeight: 'normal',
                    color: 'grey'
                },
                margin: 0
            },
            title: {
                text: ''
            },
            tooltip: {
                borderRadius: 0,
                borderWidth: 0,
                shadow: false,
                style: {
                    fontSize: '7pt',
                    color: '#000000'
                },
                pointFormat: '{point.y:.1f} CLP/KG'
            },
            plotOptions: {
                series: {
                    fillOpacity: 0.2
                }
            },
            yAxis:{
                title: '',
                lineColor: '#4D9379',
                lineWidth: 2,
                minorGridLineDashStyle: 'longdash',
                minorTickInterval: 'auto',
                minorTickWidth: 0,
                labels:{
                    format: '{value}',
                    enabled: true
                }
            },
            xAxis:{
                lineColor: '#4D9379',
                lineWidth: 2
            }
        });

        chart_merchandising = new Highcharts.Chart({
            chart: {
                backgroundColor: '',
                borderColor: '#a2a2a1',
                borderWidth: 0,
                borderRadius: 0,
                renderTo: 'merchandising_graph',
                type: 'line',
                plotBackgroundColor: '',
                height: 140
            },
            credits:{
                enabled: false
            },
            colors: ['#AC291F'],
            legend: {
                enabled: true,
                itemStyle: {
                    fontSize: '10px',
                    fontFamily: 'Open Sans Light',
                    fontWeight: 'normal',
                    color: 'grey'
                },
                margin: 0
            },
            title: {
                text: ''
            },
            tooltip: {
                borderRadius: 0,
                borderWidth: 0,
                shadow: false,
                style: {
                    fontSize: '7pt',
                    color: '#000000'
                },
                pointFormat: '{point.y:.1f} %'
            },
            plotOptions: {
                series: {
                    fillOpacity: 0.2
                }
            },
            yAxis:{
                title: '',
                lineColor: '#4D9379',
                lineWidth: 2,
                minorGridLineDashStyle: 'longdash',
                minorTickInterval: 'auto',
                minorTickWidth: 0,
                labels:{
                    format: '{value}',
                    enabled: true
                }
            },
            xAxis:{
                lineColor: '#4D9379',
                lineWidth: 2
            }
        });

        var datosApi = '';

        if(!isNaN(id_periodo)) {
            datosApi = '/infographic/carga_margen_acumulado_filtro/' + id_periodo + '/';
        }else{
            datosApi = '/infographic/carga_margen_acumulado/';
        }

        $.getJSON(datosApi, function (data) {
            var arr = [];
            var ciclos = [];
            var acum = [];
            var ingreso = [];
            var gasto = [];
            var sucursal = [];
            var zonal = [];
            var nacional = [];
            var sucursal_distr = [];
            var zonal_distr = [];
            var nacional_distr = [];
            var sucursal_merch = [];
            var zonal_merch = [];
            var nacional_merch = [];
            var max = [];
            $.each(data.meses, function (key, val) {
                ciclos.push(val.periodo__periodo.substring(0, 3).toUpperCase());
                max.push(val.periodo__periodo);
            });
            var ultimo = max[max.length-1];
            ultimo = ultimo.substr(ultimo.length-4, 4);
            $.each(data.ciclo, function (key, val) {
                acum.push(val.fields['aa']);
                arr.push(val.fields['ac']);
            });
            $.each(data.unitario, function (key, val) {
                ingreso.push(val.fields['ingreso']);
                gasto.push(val.fields['gasto']);
            });
            $.each(data.costo, function (key, val) {
                sucursal.push(val.fields['sucursal']);
                zonal.push(val.fields['zonal']);
                nacional.push(val.fields['nacional']);
            });
            $.each(data.distr_sec, function (key, val) {
                sucursal_distr.push(val.fields['sucursal']);
                zonal_distr.push(val.fields['zonal']);
                nacional_distr.push(val.fields['nacional']);
            });
            $.each(data.merchandising, function (key, val) {
                sucursal_merch.push(val.fields['sucursal']);
                zonal_merch.push(val.fields['zonal']);
                nacional_merch.push(val.fields['nacional']);
            });

            chart_answer.xAxis[0].setCategories(ciclos);
            chart_unitario.xAxis[0].setCategories(ciclos);
            chart_costos.xAxis[0].setCategories(ciclos);
            chart_distr_sec.xAxis[0].setCategories(ciclos);
            chart_merchandising.xAxis[0].setCategories(ciclos);
            var series = {data: arr, name: ultimo};
            chart_answer.addSeries(series);
            series = {data: acum, name: ultimo-1, color: '#4D9379'};
            chart_answer.addSeries(series);
            series = {data: gasto, name: 'GASTO'};
            chart_unitario.addSeries(series);
            series = {data: ingreso, name: 'INGRESO', color: '#4D9379'};
            chart_unitario.addSeries(series);
            series = {data: nacional, name: 'NAC', color: '#E3713B'};
            chart_costos.addSeries(series);
            series = {data: zonal, name: 'ZON', color: '#E5C730'};
            chart_costos.addSeries(series);
            series = {data: sucursal, name: 'SUC', color: '#4D9379'};
            chart_costos.addSeries(series);
            series = {data: nacional_distr, name: 'NAC', color: '#E3713B'};
            chart_distr_sec.addSeries(series);
            series = {data: zonal_distr, name: 'ZON', color: '#E5C730'};
            chart_distr_sec.addSeries(series);
            series = {data: sucursal_distr, name: 'SUC', color: '#4D9379'};
            chart_distr_sec.addSeries(series);
            series = {data: nacional_merch, name: 'NAC', color: '#E3713B'};
            chart_merchandising.addSeries(series);
            series = {data: zonal_merch, name: 'ZON', color: '#E5C730'};
            chart_merchandising.addSeries(series);
            series = {data: sucursal_merch, name: 'SUC', color: '#4D9379'};
            chart_merchandising.addSeries(series);
        });

    }

    function cargar_grafico_pie(){

        var id_periodo = '';
        var loc = document.location.href;
        id_periodo = loc.substr((loc.length + 1) - 5);
        id_periodo = id_periodo.replace(/\//g, '');

        var options = {
            chart: {
                renderTo: '',
                plotBackground: null,
                plotBorderWidth: null,
                plotShadow: false,
                backgroundColor: '',
                marginTop: 0,
                spacing: 0,
                height: 300,
                width: 270,
                type: 'column'
            },
            credits: {
                enabled: false
            },
            colors: [
                '#E3713B',
                '#E5C730',
                '#4D9379',
                '#86663E'
            ],
            legend: {
                align: 'center',
                verticalAlign: 'bottom',
                margin: 0
            },
            title: {
                text: ''
            },
            tooltip: {
                formatter: function(){
                    return '<b>' + this.xAxis.categories + '</b>: ' + this.percentage + ' %';
                }
            },
            plotOptions: {
                column: {
                    stacking: 'percent'
                }
            },
            xAxis:{
                categories: []
            },
            series: [{
                data: []
            }]
        };

        var datosApi = '';

        if(!isNaN(id_periodo)) {
            datosApi = '/infographic/carga_costo_venta_filtro/' + id_periodo + '/';
        }else{
            datosApi = '/infographic/carga_costo_venta/';
        }

        $.getJSON(datosApi, function (data) {
            var datos = [];
            var names = [];
            $.each(data.costo, function (key, val) {
                names.push(val.claseCoste__clasecoste);
                datos.push({
                    name: val.claseCoste__clasecoste,
                    y: Math.round(val.costo),
                    color: val.claseCoste__color
                });
            });
            options.series[0].data = datos;
            chart = new Highcharts.Chart(options);
        });

        $('#costo-graph').highcharts({
            chart: {
                type: 'column'
            },
            title: {
                text: ''
            },
            xAxis: {
                categories: ['SUC', 'ZON', 'NAC']
            },
            yAxis: {
                min: 0,
                title: {
                    text: ''
                }
            },
            tooltip: {
                pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
                shared: true
            },
            plotOptions: {
                column: {
                    stacking: 'percent'
                }
            },
            series: [{
                name: 'John',
                data: [5, 3, 4, 7, 2]
            }, {
                name: 'Jane',
                data: [2, 2, 3, 2, 1]
            }, {
                name: 'Joe',
                data: [3, 4, 4, 2, 5]
            }]
        });

    }

});