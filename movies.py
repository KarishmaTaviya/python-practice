class movies:

    counter=0;
    
    def __init__(self):
         self.mov=[]
         

    #display all the movies in list
    def display_mv(self):
        print('\nMovie List is : ',self.mov,end='')

    #add movie   
    def store_mv(self):
        l1=[];
        num=int(input('\nEnter the number of movies you want to add: '))
        
        for i in range(num):
            #self.mov.append([])
            mvnm=input('\nSpecify movie : ')
            l1.append(mvnm)
            mvdt=input('\nRelease date : ')
            l1.append(mvdt)
            mvdic=input('\nDirector : ')
            l1.append(mvdic)
            mvcon=input('\nCountry : ')
            l1.append(mvcon)
            mvlang=input('\nLanguage : ')
            l1.append(mvlang)

            for j in range(i):
                self.mov[i].append(l1)

            movies.counter+=1

    #remove movie
    def remove_mv(self,mvnm):
        self.mov.remove(mvnm)
        movies.counter-=1

    @classmethod
    def tot_mv(cls):
        print('\nNumber of movies is : ',cls.counter)



m=movies()

#display all the movies in list
m.display_mv()

#add movie
m.store_mv()

m.display_mv()

#remove movie
m.remove_mv(input('\nSpecify the movie you want to remove: '))

m.display_mv()
m.tot_mv()
