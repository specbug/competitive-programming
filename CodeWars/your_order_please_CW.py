def order(sentence):
  # code here
  if len(sentence) == 0:
      return ''
      
  return ' '.join(sorted([i for i in sentence.split()], key=lambda x: [int(c) for c in x if c.isnumeric()][0]))