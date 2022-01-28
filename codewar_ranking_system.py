# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method

class User:
    def __init__(self):
        self.index = 0
        self.rank = -8
        self.progress = 0
        
        
    def inc_progress(self, rank):
        possible_rank = [i for i in range(-8, 9) if i != 0]
        
        if rank not in possible_rank:
            raise "This is not a valid rank point!!"
        
        # if the user's rank is less than the highest possible rank
        if self.rank in possible_rank[:-1]:
            
            if self.rank == rank:
                self.progress += 3
                
            if possible_rank.index(self.rank) - possible_rank.index(rank) == 1:
                self.progress += 1
                
            if self.rank - rank == 2:
                pass
            
            if self.rank < rank:
                d = (possible_rank.index(rank)) - (possible_rank.index(self.rank))
                #d = rank - self.rank
                self.progress += (10 * d * d)
                
            if self.progress >= 100:
                mod = [self.progress // 100, self.progress % 100]

                self.index += mod[0]

                # assign the highest possible rank index to the index
                if self.index >= len(possible_rank):
                    self.index = len(possible_rank)-1

                self.progress = mod[1]

                self.rank = possible_rank[self.index]
            
            if self.rank == possible_rank[-1]:
                self.progress = 0
user = User()
user.inc_progress(8)
print(user.rank)
print(user.progress)
user.inc_progress(-3)
print(user.rank)
print(user.progress)
user.inc_progress(-6)
print(user.rank)
print(user.progress)                            # 8 -3 -6 -5 -3 -3 -3 4 8 -8
user.inc_progress(-5)
print(user.rank)
print(user.progress)
user.inc_progress(-3)
print(user.rank)
print(user.progress)
user.inc_progress(-3)
print(user.rank)
print(user.progress)
user.inc_progress(-3)
print(user.rank)
print(user.progress)
user.inc_progress(4)
print(user.rank)
print(user.progress)
user.inc_progress(8)
print(user.rank)
print(user.progress)
user.inc_progress(-8)
print(user.rank)
print(user.progress)


#-4 3 -8 5 2 -4 -3 7 5 -3