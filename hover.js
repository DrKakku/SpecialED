var $learn = $('.learn');
$learn.on('mousepointer', function() {
    $learn.get(0).play();

});

$learn.on('mouseout', function() {
    $learn.get(0).pause();
});