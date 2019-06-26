from random import randint
from BaseAI_3 import BaseAI
from Grid_3 import Grid
import copy
class PlayerAI(BaseAI):
    def getMove(self, grid):
        e,s = PlayerAI.next_move(grid,depth=2,max_depth=2)
        moves = [UP, DOWN, LEFT, RIGHT] = range(4)
        return e
    def evaluate(grid,ratio=0.25):
        max_head = max(grid.map[0][0],grid.map[0][3],grid.map[3][0],grid.map[3][3])
            ##第一圈
        Weighter_value_1 = 0
        verse = False
        weight = 1.0
        position_1 = (-1,-1)
        if(grid.map[0][0]==max_head):
            for y in range(0,4):
                for x in range(0,4):
                    x_vain=x
                    y_vain=y
                    if verse:
                        x_vain = 3-x
                    val=grid.map[x_vain][y_vain]
                    if(position_1 == (-1,-1) and val == 0 ):     ##第一个为0的点
                        position_1 = (x_vain,y_vain)
                    Weighter_value_1 = Weighter_value_1 + val*weight
                    weight = weight*ratio
                verse = not verse
            

        ##第二圈
        Weighter_value_2 = 0
        verse = False
        weight = 1.0
        position_2 = (-1,-1)
        if(grid.map[0][0]==max_head):
            for x in range(0,4):
                for y in range(0,4):
                    x_vain=x
                    y_vain=y
                    if verse:
                        y_vain = 3-y
                    val=grid.map[x_vain][y_vain]
                    if(position_2 == (-1,-1) and val == 0 ):
                        position_2 = (x_vain,y_vain)
                    Weighter_value_2 = Weighter_value_2 + val*weight
                    weight = weight*ratio
                verse = not verse
            
        ##第三圈
        Weighter_value_3 = 0
        verse = False
        weight = 1.0
        position_3 = (-1,-1)
        if(grid.map[0][3]==max_head):
            for y in range(0,4):
                for x in range(0,4):
                    x_vain=x
                    y_vain = 3-y
                    if verse:
                        x_vain = 3-x
                    val=grid.map[x_vain][y_vain]
                    if(position_3 == (-1,-1) and val == 0):
                        position_3 = (x_vain,y_vain)
                    Weighter_value_3 = Weighter_value_3 + val*weight
                    weight = weight*ratio
                verse = not verse
        ##第四圈
        Weighter_value_4 = 0
        verse = False
        weight = 1.0
        position_4 = (-1,-1)
        if(grid.map[3][0]==max_head):
            for x in range(0,3):
                for y in range(0,4):
                    x_vain = 3-x
                    y_vain = y
                    if verse:
                        y_vain = 3-y
                    val=grid.map[x_vain][y_vain]
                    if( position_4 == (-1,-1) and val == 0):
                        position_4 = (x_vain,y_vain)
                    Weighter_value_4 = Weighter_value_4 + val*weight
                    weight = weight*ratio
                verse = not verse

        ##第五圈
        Weighter_value_5 = 0
        verse = True
        weight = 1.0
        position_5 = (-1,-1)
        if(grid.map[3][0]==max_head):
            for y in range(0,4):
                for x in range(0,4):
                    x_vain = x
                    y_vain = y
                    if verse:
                        x_vain = 3-x
                    val=grid.map[x_vain][y_vain]
                    if(position_5 == (-1,-1) and val == 0):
                        position_5 = (x_vain,y_vain)
                    Weighter_value_5 = Weighter_value_5 + val*weight
                    weight = weight*ratio
                verse = not verse
                
        ##第六圈
        Weighter_value_6 = 0
        verse = True
        weight = 1.0
        position_6 = (-1,-1)
        if(grid.map[0][3]==max_head):
            for x in range(0,3):
                for y in range(0,4):
                    x_vain = x
                    y_vain = y
                    if verse:
                        y_vain = 3-y
                    val=grid.map[x_vain][y_vain]
                    if(position_6 == (-1,-1) and val == 0):
                        position_6 = (x_vain,y_vain)
                    Weighter_value_6 = Weighter_value_6 + val*weight
                    weight = weight*ratio
                verse = not verse

        ##第七圈
        Weighter_value_7 = 0
        verse = True
        weight = 1.0
        position_7 = (-1,-1)
        if(grid.map[3][3]==max_head):
            for y in range(0,4):
                for x in range(0,4):
                    x_vain = x
                    y_vain = 3-y
                    if verse:
                        x_vain =3-x
                    val=grid.map[x_vain][y_vain]
                    if(position_7 == (-1,-1) and val == 0):
                        position_7 = (x_vain,y_vain)
                    Weighter_value_7 = Weighter_value_7 + val*weight
                    weight = weight*ratio
                verse = not verse

        ##第八圈：
        Weighter_value_8 = 0
        verse = True
        weight = 1.0
        position_8 = (-1,-1)
        if(grid.map[3][3]==max_head):
            for x in range(0,4):
                for y in range(0,4):
                    x_vain=3-x
                    y_vain = y
                    if verse:
                        y_vain = 3-y
                    val=grid.map[x_vain][y_vain]
                    if(position_8 == (-1,-1) and val == 0):
                        position_8 = (x_vain,y_vain)
                    Weighter_value_8 = Weighter_value_8 + val*weight
                    weight = weight*ratio
                verse = not verse

        max_Val = max(Weighter_value_1,Weighter_value_2,Weighter_value_3,Weighter_value_4,Weighter_value_5,Weighter_value_6,Weighter_value_7,Weighter_value_8)
##
##        position = position_1
##        W_value  = Weighter_value_1
        if(max_Val == Weighter_value_1):
            position = position_1
            return max_Val , position
        if(max_Val == Weighter_value_2):
            position = position_2
            return max_Val , position
        if(max_Val == Weighter_value_3):
            position = position_3
            return max_Val , position
        if(max_Val == Weighter_value_4):
            position = position_4
            return max_Val , position
        if(max_Val == Weighter_value_5):
            position = position_5
            return max_Val , position
        if(max_Val == Weighter_value_6):
            position = position_6
            return max_Val , position
        if(max_Val == Weighter_value_7):
            position = position_7
            return max_Val , position
        if(max_Val == Weighter_value_8):
            position = position_8
            return max_Val , position

        
        return max_Val , position


    def next_move(grid,depth,max_depth,base=0.9):
        best_score = 0
        best_move = -1
        valid_move = grid.getAvailableMoves()
        for e in range(0,4):
            if( e in valid_move):
                copy_grid = copy.deepcopy(grid)
                copy_grid.move(e)

                score,position = PlayerAI.evaluate(copy_grid)
                copy_grid.map[position[0]][position[1]]=2

                if depth != 0:
                    new_e,new_s = PlayerAI.next_move(copy_grid,depth-1,max_depth)
                    score += new_s * pow(base,max_depth-depth+1)

                if(score >best_score):
                    best_score = score
                    best_move = e

        return best_move,best_score


                    
            
