#!/usr/bin/env python

from sys import argv
import os.path, csv

if len(argv) != 2 or argv[1] in ['-h', '--help', 'help']:
    exit('Usage: %s csvfile' % argv[0])

if not os.path.exists(argv[1]):
    exit('Error: named file (%s) does not exist' % argv[1])

srcfile = argv[1]
dstfile = 'todo.txt'

actions = []

f = open(srcfile, 'rU')
reader = csv.reader(f)

for row in reader:
    if len(row) != 12:
        print('BAD ROW: %s' + row)
        continue
    taskid,ttype,tname,tstatus,tproject,tcontext,tstart,tdue,tcompletion,tduration,tflagged,tnotes = row
    if ttype != 'Action':
        continue
    if not tproject == '':
        tproject = '+' + tproject.replace(' ','_')
    if not tcontext == '':
        tcontext = '@' + tcontext.replace(' ','_')
    if not tcompletion == '':
        tcompletion = 'x ' + tcompletion.split(' ')[0]
    action = ('%s %s %s %s %s' % (tcompletion, tcontext, tproject, tname, tnotes))
    actions.append(action.strip() + '\n')
        
open(dstfile, 'w').writelines(actions)
print('Number of items written to %s: %d' % (dstfile, len(actions)))

