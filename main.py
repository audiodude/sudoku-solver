'''
Sudoku Solver : A Python program for solving sudoku puzzles.

Author: Travis Briggs, briggs.travis (at) gmail.com
===================================================
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

import sys
from puzzle import Puzzle

if __name__ == '__main__':
    if len(sys.argv) > 1:
        f = open(sys.argv[1], "r")
        ans = []
        for l in f.readlines():
            if l[0] != "#":
                ans.append(l.rstrip().split(" "))
          
        pz = Puzzle(ans)     
        pz.printout()
        
        pz.initial_update()
        while (pz.eliminate_singles() or pz.eliminate_doubles()) and (not pz.finished()):
            pass
        
        print
        print
        pz.printout()