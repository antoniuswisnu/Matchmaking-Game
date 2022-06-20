from Display import *
from Room import Room


class queue:
    player_list = []

    @staticmethod
    def add_player(player):
        queue.player_list.append(player)

    @staticmethod
    def check_player():
        for i in Server.serverlist:
            if queue.player_list[0].server == i.id:
                if len(i.rooms) < 1:
                    queue.create_room(i)
                    break
                else:
                    matched = False
                    for room in i.rooms:
                        if queue.player_list[0].mmr <= room.mmr + 100 and queue.player_list[0].mmr >= room.mmr - 100:
                            queue.player_list[0].room = room.number
                            room.push(queue.player_list.pop(0))
                            matched = True
                            queue.check_player_joined(room, i)
                            break
                    if not matched:
                        queue.create_room(i)
                        break
                    break

    @staticmethod
    def check_player_joined(room, i):
        if room.totalPlayer == 10:
            a = i.rooms.index(room)
            i.play_room(a)

    @staticmethod
    def create_room(i):
        if len(i.recycle_room) == 0:
            ruangbaru = Room(queue.player_list[0].mmr, Server.numb)
            i.rooms.append(ruangbaru)
            queue.player_list[0].room = ruangbaru.number
            Server.numb += 1
            ruangbaru.push(queue.player_list.pop(0))
        else:
            i.recycle_room[0].mmr = queue.player_list[0].mmr
            i.recycle_room[0].push(queue.player_list.pop(0))
            i.rooms.append(i.recycle_room.pop(0))

    @staticmethod
    def run():
        while len(queue.player_list) > 0:
            queue.check_player()