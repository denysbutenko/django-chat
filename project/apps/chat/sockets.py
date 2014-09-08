# -*- coding: utf-8 -*-
import logging

from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from socketio.sdjango import namespace
import datetime


@namespace('/chat')
class ChatNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):
    nicknames = []

    def initialize(self):
        self.logger = logging.getLogger("socketio.chat")
        self.log("Socketio session started")

    def log(self, message):
        self.logger.info("[{0}] {1}".format(
            datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S"),
            message)
        )

    def on_join(self, channel):
        self.channel = channel
        self.join(channel)
        self.on_nickname(self.request.user.username or 'Anonymous')
        return True

    def on_nickname(self, nickname):
        self.log('Nickname: {0}'.format(nickname))
        self.nicknames.append(nickname)
        self.socket.session['nickname'] = nickname
        self.broadcast_event('announcement', '%s has connected' % nickname)
        self.broadcast_event('nicknames', self.nicknames)
        return True, nickname

    def recv_disconnect(self):
        # Remove nickname from the list.
        nickname = self.socket.session['nickname']
        self.log('Disconnected: {0}'.format(nickname))
        self.nicknames.remove(nickname)
        self.broadcast_event('announcement', '%s has disconnected' % nickname)
        self.broadcast_event('nicknames', self.nicknames)
        self.disconnect(silent=True)
        return True

    def on_user_message(self, msg):
        nickname = self.socket.session['nickname']
        self.log('{0} said: {1}'.format(nickname, msg))
        self.emit_to_room(self.channel, 'msg_to_room',
                          nickname, msg)
        return True
