class player():
  def __init__(self, mmr, id, name, server):
      self.mmr = mmr
      self.id = id
      self.name = name
      self.server = server
      self.next = None

  def description(self):
    return f'[{str(self.id)}] {self.name}\t MMR: ({str(self.mmr)})'