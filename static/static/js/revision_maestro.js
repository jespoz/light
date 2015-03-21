$(function(){
    $("#generar_no_clientes").on('click', function(){
        $(".fa-cogs").addClass('fa-spinner fa-spin');
        $(".fa-cogs").removeClass('fa-cogs');
        var $element = $("#contenido_nulos");
        var elements = 0;
        var url = '/masters/revision/update_locales_nulos/';
        $.getJSON(url, function(data){
            $.each(data.locales, function(key, val){
                $element.append('<tr><td>' + val.fields['cliente'] + '</td></tr>');
                elements += 1;
            });
            $("#generar_no_clientes").addClass('hidden');
            $("#salida").text('Se encontraron ' + elements + ' locales sin información en nuestras bases');
            $("#salida").removeClass('hidden');
            $("#csv").removeClass('hidden');
        });
    });

    $("#csv").on('click', function() {
        var $table = $("#copiable");
        var $rows = $table.find('tr:has(td)'),

            tmpColDelim = String.fromCharCode(11), // vertical tab character
            tmpRowDelim = String.fromCharCode(0), // null character

            // actual delimiter characters for CSV format
            colDelim = ';',
            rowDelim = '"\r\n"',

            // Grab text from table into CSV formatted string
            csv = '"' + $rows.map(function (i, row) {
                var $row = $(row),
                    $cols = $row.find('td');

                return $cols.map(function (j, col) {
                    var $col = $(col),
                        text = $col.text();

                    return text.replace('"', '""'); // escape double quotes

                }).get().join(tmpColDelim);

            }).get().join(tmpRowDelim)
                .split(tmpRowDelim).join(rowDelim)
                .split(tmpColDelim).join(colDelim) + '"',

            // Data URI
            csvData = 'data:application/csv;charset=utf-8,' + encodeURIComponent(csv);

        $(this)
            .attr({
            'download': 'export.csv',
                'href': csvData,
                'target': '_blank'
        });

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

    $("#button-knvp").prop('disabled', true);
    $("#button-kna1").prop('disabled', true);

    $("#button-kna1").on('click', function(){
        $(".form").submit();
    });

    $("#kna1").on('change', handleFileSelect);

    function handleFileSelect(evt){
        var file = evt.target.files[0];
        var ident = $(this).attr('id');
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
        var $boton = $("#button-" + id);
        if (data.length == 1) {
            dialog_message('Archivo no contiene datos', 0);
        } else {
            if (id == 'kna1'){
                if (data[0].Codigo && data[0]['Nombre 1'] && data[0]['Nombre 2'] && data[0].Poblacion && data[0].Fecha) {
                    $boton.removeAttr('disabled');
                    $boton.addClass('btn-primary');
                } else {
                    dialog_message('Archivo Incorrecto...', 0);
                }
            }
        }
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

    function ajax_loading(){
        var $back = $("#back-message-loading");
        $back.removeClass('hidden');
        $back.addClass('in');
    }

});
