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

    function message(message) {
        $('#lines').append($('<p>').append(
            $('<span class="text-muted">').text(
                '[' + message.date + '] '
            ),
            $('<b>').text(message.from + ': '),
            message.text
        ));
    }

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

    $(function () {
        $('#sendMessageForm').submit(function () {
            sent_message = {
                date: moment().format("HH:mm:ss"),
                from: 'me',
                text: $('#message').val()
            }
            socket.emit('user message', sent_message);
            message(sent_message);
            clear();
            $('#lines').get(0).scrollTop = 10000000;
            return false;
        });

        function clear () {
            $('#message').val('').focus();
        };
    });
});
