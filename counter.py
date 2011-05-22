
class Counter:

  def __init__(self):
    self.counts = {}
    self.total = 0
  
  def contains_key(self, elem):
    return elem in self.counts

  def inc_count(self, elem):
    try:
      self.counts[elem] += 1
    except KeyError:
      self.counts[elem] = 1
    self.total += 1
  
  def inc_count_all(self, elems):
    for elem in elems:
      self.inc_count(elem)

  def get_count(self, elem):
    try:
      return self.counts[elem]
    except KeyError:
      return 0

  def set_count(self, elem, count):
    if elem in self.counts:
      self.total -= self.counts[elem]
    self.counts[elem] = count
    self.total += count
  
  def get_total(self):
    return self.total

  def arg_max(self):
    max_elem = None
    max_count = -float('inf')
    for elem, count in self.counts:
      if not max_elem or count > max_count:
        max_elem = elem
        max_count = count
    return max_elem

