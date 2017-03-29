'''
Below shows a simple example how using a directed acyclic graph (DAG) can help with maintaining order
of execution steps, and also by tracking what all is needing to be calculated from the root
to display of a given function. This is most useful when you might have many iterative
computations before receiving a final output
'''

import pickle

executionResults = {}
states = []


def DAGFunction(f):
  '''
  Decorator that allows an execution of a given function to be tracked with various metrics
  '''
  global states
  def trace(*args, **kwargs):
    result = f(*args, **kwargs)
    states.append(pickle.dumps(result))
    executionResults.update([(f.__name__, result)])
    return result, states, executionResults
  return trace

'''
Create three random functions where the 2nd and 3rd have connections
'''

@DAGFunction
def Test1(a):
  return a + 1
  
@DAGFunction
def Test2(a):
  return Test1(a)[0] + 2
  
@DAGFunction
def Test3(a):
  return Test2(a)[0] + 3

'''
Example evaluation of Test3(10):

(16, ['I11\n.', 'I13\n.', 'I16\n.'], {'Test1': 11, 'Test3': 16, 'Test2': 13})

16 is the return value of function Test3(10).
List in the middle is pickled versions of each result through the path to root.
Dictionary on right represents the names of all functions executed and what their values were. You can see from this
the path of the graph. Test 1 = 11, 11 + 2 in Test2 results in 13, and finally, Test2 + 3 = 16.
'''
