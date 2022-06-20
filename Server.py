from Room import *
import Display

class Server:
    serverlist = []
    numb = 0
    def __init__(self, id):
        self.rooms = []
        self.playing_room = []
        Server.serverlist.append(self)
        self.id = id
        self.recycle_room = []

    def add_room(self, room):
        self.rooms.append(room)

    #With beautification
    def play_room(self, room_num):
        a = self.rooms.pop(room_num)
        red = Room(a.mmr, a.number)
        blue = Room(a.mmr, a.number)
        urutan = [red,blue,blue,red,red,blue,blue,red,red,blue]
        b = a.balancing_player()
        beautiful = Display.display.beautification(b);
        for i in urutan:
          i.push(beautiful.pop(0))
        new = Playing_room(red,blue)
        self.playing_room.append(new)

    def end_game(self, room):
      for ruang in self.playing_room:
        if ruang.number == room:
          print(f'\nRoom {room} ended!\n')
          ruang.game_ended()
          self.recycle_room.append(ruang)
          self.playing_room.remove(ruang)