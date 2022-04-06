class Model():

    def fit(self, data):
        #Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        #Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def predict(self, data):
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
                
        prediction=data[-1]+Num/Den #calcolo il valore di predizione
        return prediction

#-------fin qui ho creato il modello-----#

#-------ora gli do in pasto una lista e vedo se funziona-----#
lista=[50, 52, 60]
modello=IncrementModel()
print(modello.predict(lista))