$(function () {
    var $body = $(".chat_body");
    var $content = $(".chat_content");
    $(".chat_heading").on('click', function(){
        $body.toggleClass('active');
        $body.slideToggle('slow');
        if($content.hasClass('active')){
            $content.slideToggle('slow');
        }
    });
    $(".analista").on('click', function(){
        var $analista = $(this).data('analista');
        $content.find('span.nom_an').text($analista);
        $content.toggleClass('active');
        $content.slideToggle('slow');
    });
    $(".close").on('click', function(){
        $content.toggleClass('active');
        $content.slideToggle('slow');
    });
});
