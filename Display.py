from Room import *

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

    # With beautification
    def play_room(self, room_num):
        a = self.rooms.pop(room_num)
        red = Room(a.mmr, a.number)
        blue = Room(a.mmr, a.number)
        urutan = [red, blue, blue, red, red, blue, blue, red, red, blue]
        b = a.balancing_player()
        beautiful = display.beautification(b);
        for i in urutan:
            i.push(beautiful.pop(0))
        new = Playing_room(red, blue)
        self.playing_room.append(new)

    def end_game(self, room):
        for ruang in self.playing_room:
            if ruang.number == room:
                print(f'\nRoom {room} ended!\n')
                newroom = Room(0, ruang.number)
                self.recycle_room.append(newroom)
                self.playing_room.remove(ruang)


class display:
    @staticmethod
    def display_current():
        for servers in Server.serverlist:
            print("================================")
            print("Server: " + str(servers.id))
            print("================================")

            for team in servers.playing_room:
                print("[Room", str(team.number) + "]", "MMR: " + str(team.mmr - 100), "-",
                      str(team.mmr + 100) + ' (Playing...)')
                print("Red Team:")
                team.red.display_player()
                print("\nBlue Team:")
                team.blue.display_player()
                print("================================")

            for room in servers.rooms:
                a = room.balancing_player()
                a = display.beautification(a);
                room.game_ended()
                for i in a:
                    room.push(i)
                print("[Room " + str(room.number) + ']', "MMR: " + str(room.mmr - 100), "-",
                      str(room.mmr + 100) + ' (Waiting...)')
                room.display_player()
                print("================================")

    @staticmethod
    def beautification(list):
        panjang = 0
        for i in list:
            if len(i.name) > 15:
                i.name = i.name[0:15] + "..."
            if len(i.name) >= panjang:
                panjang = len(i.name)
        for k in list:
            if len(k.name) < panjang:
                k.name += (" " * (panjang - len(k.name)))
        return list