$('.modal').on('hidden.bs.modal', function () {
    $('video').each(function () { this.pause(); });    
});

$('#console_video_modal').on('shown.bs.modal', function () {
    $('#console').get(0).play();
});

$('#gs_video_modal').on('shown.bs.modal', function () {
    $('#groundstation').get(0).play();
});