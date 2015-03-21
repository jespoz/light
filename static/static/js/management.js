$(document).ready(function(){

    $("[id*=button]").click(function(e){
        var $id = $(this).data('id');
        var $status = $("#circle-status-" + $id);
        if($status.hasClass('text-rojo')){
            dialog_message('No se puede realizar la carga, ya que el periodo se encuentra cargado', 0);
        }else{
            ajax_loading();
            $("#form-" + $id).submit();
        }
    });

    $("#close").click(function(e){
        hidden_message();
        e.preventDefault();
    });

    $("#boton-aceptar").click(function(e){
        hidden_message();
        e.preventDefault();
    });

    $("#back-message").click(function(e){
        hidden_message();
        e.preventDefault();
    });

    $.each($(".form"), function(){
        $(this).trigger('reset');
    });

    $.each($(".btn"), function(){
        $(this).prop('disabled', true);
    });

    function habilitarCargar(id){
        var $boton = $("#button-" + id);
        var $archivo = $("#comp-archivo-" + id);
        var $periodo = $("#comp-periodo-" + id);
        if($archivo.hasClass('label-success') && $periodo.hasClass('label-success')){
            $boton.removeAttr('disabled');
            $boton.addClass('btn-primary');
        }else{
            $boton.prop('disabled', true);
            $boton.removeClass('btn-primary');
        }
    }

    $(".file").on('change', handleFileSelect);

    $(".periodo").on('change', function(){
        var id = $(this).data('id');
        var $comprobacion = $("#comp-periodo-" + id);
        var $elemento = $("#circle-status-" + id);
        if($(this).val() == 0){
            $comprobacion.removeClass("label-success");
            $comprobacion.addClass("label-danger");
            $elemento.removeClass('text-verde');
            $elemento.removeClass('text-rojo');
        }else{
            $comprobacion.removeClass("label-danger");
            $comprobacion.addClass("label-success");
            var url = '/imports/reports/data_exist/' + id + '/' + $(this).val() + '/';
            $.getJSON(url, function(data){
                $elemento.removeClass('text-verde');
                $elemento.removeClass('text-rojo');
                if(data.retorno == 0 || data.retorno == ''){
                    $elemento.addClass('text-verde');
                }else{
                    $elemento.addClass('text-rojo');
                }
            });

        }
        habilitarCargar(id);
    });

    function handleFileSelect(evt){
        var file = evt.target.files[0];
        var ident = $(this).data('id');
        Papa.parse(file, {
            header: true,
            dynamicTyping: true,
            delimited: ';',
            complete: function(results) {
                doStuff(results.data, ident);
            },
            error: function(err, file, inputElem, reason){
                console.log(reason);
            }
        });
    }

    function doStuff(data, id) {
        var $comprobacion = $("#comp-archivo-" + id);
        if (id == '1') {
            if(data.length == 1){
                dialog_message('Archivo no contiene datos', 0);
            }else {
                if (data[0].Kilos && data[0].Venta && data[0].Margen && data[0]['Oficina de ventas'] && data[0]['Total Ingresos'] && data[0]['Total Gastos'] && data[0]['Margen %']) {
                    $comprobacion.removeClass("label-danger");
                    $comprobacion.addClass("label-success");
                } else {
                    $comprobacion.removeClass("label-success");
                    $comprobacion.addClass("label-danger");
                    dialog_message('Archivo Incorrecto...');
                }
            }
        } else if (id == '2') {
            if(data.length == 1){
                dialog_message('Archivo no contiene datos', 0);
            }else {
                if (data[0]['Tipo de cliente'] && data[0]['Oficina de ventas'] && data[0]['Kilos Venta']) {
                    $comprobacion.removeClass("label-danger");
                    $comprobacion.addClass("label-success");
                } else {
                    $comprobacion.removeClass("label-success");
                    $comprobacion.addClass("label-danger");
                    dialog_message('Archivo Incorrecto...', 0);
                }
            }
        } else if (id == '3') {
            if(data.length == 1){
                dialog_message('Archivo no contiene datos', 0);
            }else {
                if (data[0]['Tipo de cliente'] && data[0]['Oficina de ventas'] && data[0].Sector && data[0]['Kilos Venta'] && data[0]['Venta Neta']) {
                    $comprobacion.removeClass("label-danger");
                    $comprobacion.addClass("label-success");
                } else {
                    $comprobacion.removeClass("label-success");
                    $comprobacion.addClass("label-danger");
                    dialog_message('Archivo Incorrecto...', 0);
                }
            }
        } else if(id == '4'){
            if(data.length == 1){
                dialog_message('Archivo no contiene datos', 0);
            }else {
                if (data[0]['Tipo de Cliente'] && data[0]['Oficina de ventas'] && data[0].Sector && data[0].Cadena && data[0]['Rut'] && data[0]['Tipo Pedido'] && data[0]['Kilos  Facturados'] && data[0]['P.Base'] && data[0]['P.Especial'] && data[0]['P.Vigente'] && data[0]['P.Pedido'] && data[0]['P.Facturado']) {
                    $comprobacion.removeClass("label-danger");
                    $comprobacion.addClass("label-success");
                } else {
                    $comprobacion.removeClass("label-success");
                    $comprobacion.addClass("label-danger");
                    dialog_message('Archivo Incorrecto...', 0);
                }
            }
        } else if(id == '5'){
            if(data.length == 1){
                dialog_message('Archivo no contiene datos', 0);
            }else {
                if (data[0]['Oficina de ventas'] && data[0]['Clase de coste'] && data[0].Sector && data[0].Monto) {
                    $comprobacion.removeClass("label-danger");
                    $comprobacion.addClass("label-success");
                } else {
                    $comprobacion.removeClass("label-success");
                    $comprobacion.addClass("label-danger");
                    dialog_message('Archivo Incorrecto...', 0);
                }
            }
        } else if(id == '6'){
            if(data.length == 1){
                dialog_message('Archivo no contiene datos', 0);
            }else {
                if (data[0].Referencia && data[0]['Unidades Venta'] && data[0]['Oficina de ventas'] && data[0]['Tipo de cliente'] && data[0]['Categoria Cliente'] && data[0].Sector && data[0]['Cod Local'] && data[0]['Supervisor_BP-CL'] && data[0]['Preventa_BP-CL'] && data[0]['Dia natural'] && data[0]['Cod Material'] && data[0].Material && data[0]['Nivel 2'] && data[0]['Nivel 3'] && data[0].Marca && data[0]['Kilos Venta'] && data[0]['Venta Neta']) {
                    $comprobacion.removeClass("label-danger");
                    $comprobacion.addClass("label-success");
                } else {
                    $comprobacion.removeClass("label-success");
                    $comprobacion.addClass("label-danger");
                    dialog_message('Archivo Incorrecto...', 0);
                }
            }
        }else{
            dialog_message('Importe no programado...', 0);
        }
        habilitarCargar(id);
    }

    function ajax_loading(){
        var $back = $("#back-message-loading");
        $back.removeClass('hidden');
        $back.addClass('in');
    }

    function dialog_message(message, question) {
        var $back = $("#back-message");
        var $modal = $("#modal-message");
        var $message = $("#message");
        $back.removeClass('hidden');
        $back.addClass('in');
        $modal.attr('aria-hidden', false).show();
        $modal.css('display', 'block');
        $modal.addClass('in');
        $message.text(message);
        if(question == 0){
            $("#boton-cancelar").addClass('hidden');
        }else{
            $("#boton-cancelar").removeClass('hidden');
        }
    }

    function hidden_message(){
        var $back = $("#back-message");
        var $modal = $("#modal-message");
        $back.addClass('hidden');
        $back.removeClass('in');
        $modal.removeAttr('aria-hidden');
        $modal.removeAttr('style');
        $modal.removeClass('in');
    }

});
