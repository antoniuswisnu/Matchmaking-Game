from Display import *
from Queue import queue
from Player import player

if __name__ == "__main__":
  server1 = Server(1)
  server2 = Server(2)
  queue.add_player(player(2000, "xxx001", "Sondong", 1))
  queue.add_player(player(2025, "xxx002", "Darkness of Raven", 1))
  queue.add_player(player(2080, "xxx003", "Nope", 1))
  queue.add_player(player(2020, "xxx001", "Sekiper", 1))
  queue.add_player(player(2010, "xxx002", "AyamRenggo", 1))
  queue.add_player(player(2090, "xxx003", "LYF", 1))
  queue.add_player(player(2045, "xxx001", "Boboho", 1))
  queue.add_player(player(2050, "xxx002", "Cah Angon", 1))
  queue.add_player(player(2073, "xxx003", "aracnoid", 1))
  queue.add_player(player(2033, "xxx003", "Supardi", 1))
  queue.add_player(player(2308, "xxx003", "Yanto", 1))
  queue.add_player(player(5000, "xxx003", "Brown-Sham", 1))
  queue.add_player(player(5090, "xxx003", "Farmingan", 2))
  queue.add_player(player(5100, "xxx003", "Habaneroh", 2))
  queue.add_player(player(2308, "xxx003", "Kindred", 1))
  queue.run()
  display.display_current()

  server1.end_game(server1.playing_room[0].number)
  # display.display_current()
  queue.add_player(player(2000, "xxx001", "Sondong", 1))
  display.display_current()