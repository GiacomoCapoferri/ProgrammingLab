#istanzio la classe
class CSVFile():

    #definisco attributo che contenga il nome
    def __init__(self,name):
        #setto il nome
        self.name = name
        #check se name è stringa
        if not isinstance(self.name, str):
            raise Exception('Il nome non è una stringa')
        
    
    #definisco metodo per che torni dati csv come lista di liste
    def get_data(self, start ,stop):
        if start==None:
            self.start = 0
        else:
            self.start = 3
        
        self.stop = 9
        #inizializzo lista
        list = []

        #inizializzo variabile che mi dice se file è leggibile o meno
        file_leggibile=True

        #inizio il try-except
        try:
            my_file = open(self.name, 'r')
        except:
            print('Errore: non riesco a leggere il file')
            file_leggibile=False

        #se il file è leggibile
        if file_leggibile:
            my_file_sliced = slice(self.start,self.stop,1)
            print(my_file[my_file_sliced])
            #for line in my_file[my_file_sliced]:
                
                #elements = line.split(',')
                #elimino l'ultimo elemento che mi da \n
                #elements[-1] = elements[-1].strip()
                #if elements[0] != 'Date':
                    #date = elements[0]
                    #value = elements[1]
                    #list.append(line)
        #return list


csvfile=CSVFile('shampoo_sales.csv')
print(csvfile.get_data(3, 6))