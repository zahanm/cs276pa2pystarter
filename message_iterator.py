
from __future__ import print_function

import cPickle as pickle
import sys

class MessageIterator:
  
  def __init__(self, inp_filename):
    self.inpfile = open(inp_filename, 'rb')
    self.reader = pickle.Unpickler(self.inpfile)
    self.numgroups = self.reader.load()

  def __iter__(self):
    return self

  def next(self):
    try:
      return self.reader.load()
    except EOFError:
      self.close()
      raise StopIteration

  def close(self):
    """
    Not necessary to call this if MessageIterator is used as an iterator in a
    for loop
    See how __next__() handles EOFError
    """
    self.inpfile.close()

def main():
  if len(sys.argv) != 2:
    print('Usage: python message_iterator <input_file>', file=sys.stderr)
    sys.exit(-1)
  mi = MessageIterator(sys.argv[1])

  for mf in mi:
    print("{0} ({1})".format(mf.filename,mf.newsgroupnum))
    print("Subject:")
    for subj,count in mf.subject.counts:
      print("Count for "+subj+" is "+count)
    for word,count in mf.body.counts:
      print("Count for "+word+" is "+count)

if __name__ == '__main__':
  main()

