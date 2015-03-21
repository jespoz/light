$(function() {

    var loc = document.location.href;
    var id_periodo = loc.substr((loc.length + 1) - 5);
    id_periodo = id_periodo.replace(/\//g, '');

    chart_crudo = new Highcharts.Chart({
        chart: {
            type: 'scatter',
            renderTo: 'graph-crudo',
            zoomType: 'xy'
        },
        credits:{
            enabled: false
        },
        title: {
            text: 'Dispersión de precios CRUDOS'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            title: {
                enabled: true,
                text: 'Unidades x Transacción'
            },
            min: 0
        },
        yAxis: {
            title: {
                text: 'Diferencia ($)'
            },
            labels: {
                format: '{value}'
            }
        },
        legend: {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom',
            floating: false,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
        },
        plotOptions: {
            scatter: {
                marker: {
                    radius: 5,
                    states: {
                        hover: {
                            enabled: true,
                            lineColor: 'rgb(100,100,100)'
                        }
                    }
                },
                states: {
                    hover: {
                        marker: {
                            enabled: false
                        }
                    }
                },
                tooltip: {
                    headerFormat: '<b>{series.name}</b><br>',
                    pointFormat: '{point.dataLabels}'
                }
            }
        }
    });

    chart_procesado = new Highcharts.Chart({
        chart: {
            type: 'scatter',
            renderTo: 'graph-procesado',
            zoomType: 'xy'
        },
        credits:{
            enabled: false
        },
        title: {
            text: 'Dispersión de precios PROCESADOS'
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            title: {
                enabled: true,
                text: 'Unidades x Transacción'
            },
            min: 0
        },
        yAxis: {
            title: {
                text: 'Diferencia ($)'
            },
            labels: {
                format: '{value}'
            }
        },
        legend: {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom',
            floating: false,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
        },
        plotOptions: {
            scatter: {
                marker: {
                    radius: 5,
                    states: {
                        hover: {
                            enabled: true,
                            lineColor: 'rgb(100,100,100)'
                        }
                    }
                },
                states: {
                    hover: {
                        marker: {
                            enabled: false
                        }
                    }
                },
                tooltip: {
                    headerFormat: '<b>{series.name}</b><br>',
                    pointFormat: '{point.dataLabels}'
                }
            }
        }
    });

    if(!isNaN(id_periodo)) {
        var url = '/actions/accionables/precios/dispersion/' + id_periodo + '/';
    }

    $.getJSON(url, function (data) {
        var series = {data: data.preventa_crudo, name: 'Preventa', color:"#4D9379"};
        chart_crudo.addSeries(series);
        series = {data: data.vendedor_crudo, name: 'Vendedor', color: "#E3713B"};
        chart_crudo.addSeries(series);
        series = {data: data.preventa_proc, name: 'Preventa', color: "#4D9379"};
        chart_procesado.addSeries(series);
        series = {data: data.vendedor_proc, name: 'Vendedor', color: "#E3713B"};
        chart_procesado.addSeries(series);
    });

    $("#btn_crudos").on('click', function(){
        if($.fn.DataTable.isDataTable("#ver")){
            $("#ver").dataTable().fnDestroy();
        }
        var $element = $("#body_table");
        $element.html('');
        var url = '/actions/accionables/precios/negocio/' + $(this).data('periodo') + '/1/';
        $.getJSON(url, function(data){
            $.each(data.listado, function(key, val){
                $element.append('<tr><td>' + val.sector__sector + '</td><td>' + val.codigoMaterial + '</td><td>' + val.material + '</td><td>' + val.conDescuento + '</td><td>' + val.sinDescuento + '</td><td>' + val.sobreprecio + '</td><td class="ultimo"><button data-mat="' + val.material + '" data-material="' + val.codigoMaterial + '" class="apertura btn btn-success btn-xs" data-toggle="modal" data-target="#myModal"><i class="fa fa-plus-square-o"></i></button></td></tr>');
            });
            destroyDataTable();
        });
        $("#tabla_material").removeClass('hidden');
    });

    $("#btn_procesados").on('click', function(){
        if($.fn.DataTable.isDataTable("#ver")){
            $("#ver").dataTable().fnDestroy();
        }
        var $element = $("#body_table");
        $element.html('');
        var url = '/actions/accionables/precios/negocio/' + $(this).data('periodo') + '/2/';
        $.getJSON(url, function(data){
            $.each(data.listado, function(key, val){
                $element.append('<tr><td>' + val.sector__sector + '</td><td>' + val.codigoMaterial + '</td><td>' + val.material + '</td><td>' + val.conDescuento + '</td><td>' + val.sinDescuento + '</td><td>' + val.sobreprecio + '</td><td class="ultimo"><button data-mat="' + val.material + '" data-material="' + val.codigoMaterial + '" class="apertura btn btn-success btn-xs" data-toggle="modal" data-target="#myModal"><i class="fa fa-plus-square-o"></i></button></td></tr>');
            });
            destroyDataTable();
        });
        $("#tabla_material").removeClass('hidden');
    });

    function destroyDataTable(){
        $("#ver").dataTable({
            searching: false,
            paging: false,
            info: false,
            "order": [[3, "desc"]]
        });
    }

    $("#myModal").on("hidden.bs.modal", function(e) {
        $("#listado").dataTable().fnDestroy();
    });

    $("#myModal").on("show.bs.modal", function(e) {
        var material = $(e.relatedTarget).data('material');
        $("#tituloModal").text('Detalle de locales con descuento en ' + $(e.relatedTarget).data('mat'));
        $(".primera_cab").text($(e.relatedTarget).data('mat'));
        var $element = $("#apertura_tabla_modal");
        $element.html('');
        var url = '/actions/accionables/precios/negocio/apertura/' + id_periodo + '/' + material + '/';
        $.getJSON(url, function(data){
            $.each(data.listado, function(key, val){
                var uno = val.uno;
                if(uno == 0){
                    uno = '';
                }else{
                    uno = uno + '%'
                }
                var dos = val.dos;
                if(dos == 0){
                    dos = '';
                }else{
                    dos = dos + '%'
                }
                var tres = val.tres;
                if(tres == 0){
                    tres = '';
                }else{
                    tres = tres + '%'
                }
                var cuatro = val.cuatro;
                if(cuatro == 0){
                    cuatro = '';
                }else{
                    cuatro = cuatro + '%'
                }
                var cinco = val.cinco;
                if(cinco == 0){
                    cinco = '';
                }else{
                    cinco = cinco + '%'
                }
                var seisAdiez = val.seisAdiez;
                if(seisAdiez == 0){
                    seisAdiez = '';
                }else{
                    seisAdiez = seisAdiez + '%'
                }
                var onceAveinte = val.onceAveinte;
                if(onceAveinte == 0){
                    onceAveinte = '';
                }else{
                    onceAveinte = onceAveinte + '%'
                }
                var mayorVeinte = val.mayorVeinte;
                if(mayorVeinte == 0){
                    mayorVeinte = '';
                }else{
                    mayorVeinte = mayorVeinte + '%'
                }
                $element.append('<tr><td>' + val.supervisor + '</td><td>' + val.preventa + '</td><td>' + val.codLocal + '</td><td>' + val.clienteLocal + '</td><td>' + val.categoria__categoria + '</td><td>' + val.responsable + '</td><td>' + uno + '</td><td>' + dos + '</td><td>' + tres + '</td><td>' + cuatro + '</td><td>' + cinco + '</td><td>' + seisAdiez + '</td><td>' + onceAveinte + '</td><td>' + mayorVeinte + '</td></tr>');
            });

            $("#listado").dataTable({
                "aLengthMenu": [[25, 50, 75, 100, -1],[25, 50, 75, 100, "All"]],
                "iDisplayLength": 100,
                "order": [[0, "desc"]]
            });

            var $elementimp = document.createElement('a');
            $elementimp.className = 'btn btn-primary btn-sm';
            $elementimp.id = 'csv';
            $elementimp.onclick = imprimir_csv;

            var $icono = document.createElement('i');
            $icono.className = 'fa fa-download';

            $elementimp.appendChild($icono);

            $("#listado_filter").append($elementimp);

        });

    });

    function imprimir_csv(){

        $("#listado").tableExport({
            type: 'excel',
            escape: 'false'
        });

    }

});
