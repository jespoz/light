$(".tooltip-a").hover(function(){
    var $span = $(this).children("span");
    var $img = $(this).children("img");
    $span.css('display', 'block');
    $img.css('display', 'block');
});
$(".tooltip-a").mouseout(function(){
    var $span = $(this).children("span");
    var $img = $(this).children("img");
    $span.css('display', 'none');
    $img.css('display', 'none');
});