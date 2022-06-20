from Balancing import balancing

class Room:
    def __init__(self, mmr, number):
        self.number = number
        self.mmr = mmr
        self.top = None
        self.bottom = None
        self.totalPlayer = 0

    def push(self, player):
        self.totalPlayer += 1
        if self.top == None:
            self.bottom = player
        else:
            player.next = self.top
        self.top = player

    def pop(self):
        self.totalPlayer -= 1
        if self.top == None:
            print("Error")
        elif self.top == self.bottom:
            self.top = None
            self.bottom = None
        else:
            self.top = self.top.next

    def game_ended(self):
        p = self.top
        while p:
            self.top.room = None
            a = p.next
            self.pop()
            p = a

    def display_player(self):
        p = self.top
        while p:
            print(p.description())
            p = p.next

    def balancing_player(self):
        list_p = []
        p = self.top
        while p:
            a = p.next
            p.next = None
            list_p.append(p)
            p = a
        balancing.balance(list_p, 0, len(list_p) - 1)
        return list_p


class Playing_room:
    def __init__(self, red, blue):
        self.number = red.number
        self.mmr = red.mmr
        self.red = red
        self.blue = blue