var socket = io.connect("/chat");

socket.on('connect', function () {
    $('.fa-logo').addClass('text-success');
    socket.emit('join', window.channel_id);
});
