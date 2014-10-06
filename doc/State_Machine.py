# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# 
# State Machine

# <markdowncell>

# Design the worlds simplest state machine for a recording controller.

# <codecell>

print 'State Machine'

# <codecell>

states = { 'off'   : { 'begin':'idle' },
           'idle'  : { 'end'  :'off',   'start':'record' } ,
           'record': { 'pause':'pause', 'stop' :'idle',  'no_chunks':'error' },
           'pause' : { 'resume':'record', 'stop':'idle' },
           'error' : {'chunks':'record'}}
print states

# <codecell>

def next_state(s,e):
    print 'Event:',e
    if states[s].has_key(e):
        s = states[s][e]
        print "Next state:", s
    return s

events = [ 'begin', 'end', 'begin', 'start', 'xxx', 'stop', 'start', 'no_chunks','chunks','pause','resume',
          'pause', 'resume', 'stop', 'end' ]
s = 'off'

for e in events:
    s = next_state(s,e)s

