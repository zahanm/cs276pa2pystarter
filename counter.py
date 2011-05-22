
class Counter:

  def __init__(self):
    self.counts = {}

  def inc_count(self, elem):
    try:
      self.counts[elem] += 1
    except KeyError:
      self.counts[elem] = 1

