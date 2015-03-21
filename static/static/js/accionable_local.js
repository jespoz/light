$(function(){

    $(".box_client").on('click', function () {

        $("#generar i").removeClass('fa-file-text-o');
        $("#generar i").addClass('fa-spinner fa-spin');

        $("#contenedor_list").html('');
        str = '<table id="listado" class="table table-bordered table-striped table-responsive hidden"><thead><th>Supervisor</th><th>Preventa</th><th>Cod. Local</th><th>Cliente Local</th><th>Categoría</th><th>Sector</th><th>Promedio</th><th>Mínimo</th><th>Máximo</th><th>Vta. Prom. $M</th><th>Semanas</th></thead><tbody id="table-list"></tbody></table>';
        $("#contenedor_list").append(str);

        var $idTipoCliente = $(this).data('id');
        var $idPeriodo = $(this).data('periodo');
        var $element1 = $("#table-categories");
        var $element2 = $("#table-list");
        var url = '/actions/accionables/locales/' + $idPeriodo + '/' + $idTipoCliente + '/';

        $.getJSON(url, function(data){
            $element1.empty();
            $element2.empty();
            $.each(data.totales, function(key, val){
                $element1.append('<tr><td>' + val.categoria__categoria + '</td><td>' + val.dcount + '</td><td>' + formatNumber(Math.round(val.prom, 0)) + ' $M </td></tr>');
            });
            $.each(data.listado, function(key, val){
                venta = Math.round(val.ventaPromedio);
                $element2.append('<tr><td>' + val.supervisor + '</td><td>' + val.preventa + '</td><td>' + val.codLocal + '</td><td>' + val.clienteLocal + '</td><td>' + val.categoria__categoria + '</td><td>' + val.sector__sector + '</td><td>' + val.promedio + '</td><td>' + val.minimo + '</td><td>' + val.maximo + '</td><td>' + venta + '</td><td>' + val.semCalculo + '</td></tr>');
            });
            $("#generar i").removeClass('fa-spinner fa-spin');
            $("#generar i").addClass('fa-file-text-o');
        });

        $("#generar").removeClass('hidden');

        if($("#listado").hasClass('hidden')){

        }else{
            $("#listado").addClass('hidden');
        }

    });

    function formatNumber (num) {
        return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1.")
    }

    $("#generar").on('click', function () {

        $("#listado").dataTable({
            "aLengthMenu": [[25, 50, 75, 100, -1],[25, 50, 75, 100, "All"]],
            "iDisplayLength": 100,
            "order": [[9, "desc"]]
        });
        $("#listado").removeClass('hidden');

        var $element = document.createElement('a');
        $element.className = 'btn btn-primary btn-sm';
        $element.id = 'csv';
        $element.onclick = imprimir_csv;

        var $icono = document.createElement('i');
        $icono.className = 'fa fa-download';

        $element.appendChild($icono);

        $("#listado_filter").append($element);

    });

    function imprimir_csv(){

        $("#listado").tableExport({
            type: 'excel',
            escape: 'false'
        });

    }

});
