class Model():

    def fit(self, data):
        #Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        #Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    
    def compute_avg_increment(self, data):
        #sanitizzazione dati
        if len(data)<2:
            raise Exception('Errore: devo avere almeno 2 valori per fare una differenza, invece ne ho solo {}'.format(len(data)))
        #inizializzo Num e Den e indice i
            Num=Den=0 #posso creare anche così più variabili che hanno stesso valore
            i=-1 #parte da -1 così quando entro nel ciclo parto da i=0
            #Logica per la predizione
            for item in data:
                i=i+1
                if i==0:  #se sto trattando il primo elemento della lista non faccio nulla
                    Num=Num
                    Den=Den
                else:  #se tratto un qualsiasi altro elemento della lista
                    Num=Num+(data[i]-data[i-1]) #cumulo le differenze sulla variabile Num
                    Den=Den+1 #cumulo sul Den il numero di differenze analizzate
                        
                    avg_increment=Num/Den

        
    def predict(self, data):
        self.compute_avg_increment(self, data)
        prediction=data[-1]+avg_increment #calcolo il valore di predizione
        return prediction

class FitIncrementModel(IncrementModel):
    
    def fit(self, data):
        self.compute_avg_increment(self, data)
        self.global_avg_increment=avg_increment
        return self.global_avg_increment

    def predict(self, data):
        self.compute_avg_increment(self, data)
        self.local_avg_increment=avg_increment
        prediction=data[-1]+(self.global_avg_increment+self.local_avg_increment)/2
        return prediction
        
#-------fin qui ho creato il modello------#

#-------ora gli do in pasto una lista e vedo se funziona-----#
lista_fit=[8, 19, 31, 41]
lista_predict=[50, 52, 60]
shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]



modello=FitIncrementModel()
print(modello.fit(lista_fit))
print(modello.predict(lista_predict))