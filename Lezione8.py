lista=[50, 52, 60]

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
        Num=0
        Den=-1
        #Logica per la predizione
        for item in data:
            if item==0:
                Num=Num
                Den=Den
            else:
                Num=Num+(data[item]-data[item-1])
                Den=Den+1
                
        prediction=data[-1]+Num/Den
        return prediction

modello=IncrementModel()
print(modello.predict(lista))