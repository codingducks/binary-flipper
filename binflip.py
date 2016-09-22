#Simple Binary Flipper
 
inp = raw_input(">")
 
print '\n'
 
inp1 = inp.replace('1', 'x').replace('0', 'y')
inp2 = inp1.replace('x', '0').replace('y', '1')
print "normal binary\n", inp, '\n'
print "middle step\n", inp1, '\n'
print 'result\n', inp2, '\n'
