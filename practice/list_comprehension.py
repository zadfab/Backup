import numpy

book = "this is a book about zaid's anxiety and depression.we are going to talk about the cause(Root) of the problem ,symptoms amd the cure of the problem"

set = sorted(set(book))
print(len(set),len(book))
li = {char:i for i,char in enumerate(set)}
arr = numpy.array(set)
print(li)

encodeing = [li[i] for i in book]
encodeing = numpy.array(encodeing)
print(encodeing)