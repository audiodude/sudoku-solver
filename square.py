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

class Square:
    '''
    classdocs
    '''

    def __init__(self, x, y, groups, value=None):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        
        if value:
            self.value = [value]
        else:
            self.value = [1,2,3,4,5,6,7,8,9]
        
        self.groups = groups
        
    def update_groups(self):
        if len(self.value) == 1:
            val = self.value[0]
            for gp in self.groups:
                for sq in gp:
                    if sq == self:
                        continue
                        
                    if val in sq.value:
                        sq.value.remove(val)
                        if len(sq.value) == 0:
                            raise Exception('Empty value array')
                        if len(sq.value) == 1:
                            sq.update_groups()
            return True
        else:
            return False
            
    def __repr__(self):
        return '%s:%s' % (self.x, self.y) 