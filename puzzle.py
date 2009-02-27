'''
Copyright (C) 2009 Travis Briggs

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from square import Square, eliminate_vals
from math import ceil
import pdb

def wsquare(x, y):
    if y > 8 or y < 0:
        raise Exception('y value out of range: ' + str(y))
    
    if x > 8 or x < 0:
        raise Exception('x value out of range: ' + str(x))
        
    if x in range(3):
        if y in range(3):
            return 0
        elif y in range(3,6):
            return 3
        else:
            return 6
            
    elif x in range(3,6):
        if y in range(3):
            return 1
        elif y in range(3,6):
            return 4
        else:
            return 7
                
    else:
        if y in range(3):
            return 2
        elif y in range(3,6):
            return 5
        else:
            return 8
                   
class Puzzle:
    '''
    classdocs
    '''


    def __init__(self, text_array):
        '''
        Constructor
        '''
        self.rows = [[] for i in range(9)]
        self.cols = [[] for i in range(9)]
        self.sqrs = [[] for i in range(9)]
        
        y = 0
        for row in text_array:
            x = 0
            for col in row:
                if col.find('.') != -1:
                    if len(col) == 2:
                        try:
                            for n in range(int(col[1:2])):
                                self.create_square(x, y)
                                x += 1
                            continue
                        except:
                            raise Exception('Non-integer value following a period in puzzle specification')
                    else:
                        self.create_square(x, y)
                else:
                    self.create_square(x, y, int(col))
                x += 1
            y += 1
    
    def initial_update(self):
        for row in self.rows:
            for s in row:
                s.update_groups()
                
    def eliminate_singles(self):
        update = False
        for grp in self.rows + self.cols + self.sqrs:
            if self.finished():
                return False
            nums = [[] for i in range(10)]
            for s in grp:
                if len(s.value) != 1:
                    for v in s.value:
                        nums[v].append(s)

            for i, num in enumerate(nums):
                if len(num) == 1:
                    update = True
                    num[0].value = [i]
                    num[0].update_groups()
        
        return update
    
    def eliminate_doubles(self):
        update = False
        for grp in self.rows + self.cols + self.sqrs:
            if self.finished():
                return False
            potentials = {}    
            for sq in grp:
                if len(sq.value) == 2:
                    print "Found a double"
                    val_tuple = (sq.value[0], sq.value[1])
                    if val_tuple in potentials:
                        print "### MATCHING DOUBLE ###"
                        update = True
                        eliminate_vals(grp, val_tuple, [sq, potentials[val_tuple]])
                    else:
                        potentials[val_tuple] = sq
                    print potentials
        
        return update
    
    def finished(self):
        for row in self.rows:
            for s in row:
                if len(s.value) > 1:
                    return False
        else:
            return True
                
    def print_values(self):
        for row in self.rows:
            for s in row:
                print s.value,
            print
                
    def create_square(self, x, y, val=None):
        s = Square(x, y, [self.rows[y], self.cols[x], self.sqrs[wsquare(x,y)]], val)
        self.rows[y].append(s)
        self.cols[x].append(s)
        self.sqrs[wsquare(x,y)].append(s)
        
    def printout(self):
        for row in self.rows:
          for s in row:
             if len(s.value) == 1:
               print s.value[0],
             else:
               print ".",
          print 