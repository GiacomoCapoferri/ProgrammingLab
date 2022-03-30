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
    def get_data(self, start, end):
        
        self.start = 3  
        self.stop = 7
        
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
            for line in range(self.start,self.stop,1):
                elements = line.split(',')
                #elimino l'ultimo elemento che mi da \n
                elements[-1] = elements[-1].strip()
                if elements[0] != 'Date':
                    #date = elements[0]
                    #value = elements[1]
                    list.append(elements)
        return list

class NumericalCSVFile(CSVFile):
    def get_data():
        
        #inizializzo la lista con valori numerici float
        num_list=[]

        #inizializzo la lista con valori stringa (risultato del get data padre)
        str_list = super().get_data()

        #ciclo su ogni riga
        for line in str_list:
            #faccio le mie operazioni
            try:
                line[1]=float(line[1])
                num_list.append(line)
            #se ho errore lo segnalo con un print
            except Exception as err:
                print ('Ho avuto questo Errore: "{}"'.format(err))
        #restituisco tutta la lista con valori float e bonificata di valori sporchi
        return num_list

csvfile=NumericalCSVFile('shampoo_sales.csv')
print(csvfile.get_data())