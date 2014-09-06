$(function() {
    var socket = io.connect("/chat");

    socket.on('connect', function () {
        $('.fa-logo').addClass('text-success');
        socket.emit('join', window.channel_id);
        console.log('Connected to ' + window.channel_id);
    });

    socket.on('disconnect', function(){
        console.log('Disconnected from ' + window.channel_id);
    });

    socket.on('announcement', function(msg) {
        $('#lines').append($('<p>').append($('<em>').text(msg)));
    });

    socket.on('nicknames', function (nicknames) {
        $('#users-list').empty();
        for (var i in nicknames) {
            $('#users-list').append($('<li class="list-group-item">').text(nicknames[i]));
        }
    });

    socket.on('reconnect', function () {
        $('#lines').remove();
        message('System', 'Reconnected to the server');
    });

    socket.on('reconnecting', function () {
        message('System', 'Attempting to re-connect to the server');
    });

    socket.on('error', function (e) {
        message('System', e ? e : 'A unknown error occurred');
    });

    socket.on('msg_to_room', message);

    function message(from, msg) {
        $('#lines').append($('<p>').append($('<b>').text(from + ': '), msg));
    }

    $(function () {
        $('#sendMessageForm').submit(function () {
            message('me', $('#message').val());
            socket.emit('user message', $('#message').val());
            clear();
            $('#lines').get(0).scrollTop = 10000000;
            return false;
        });

        function clear () {
            $('#message').val('').focus();
        };
    });
});
