class table:

    def __init__(self):

        self.valores = []
        self.xi =[]
        self.frabsoluta= []
        self.frabsolutaacum =[]
        self.frerel =[]
        self.frerelper =[]
        self.frerelacumm =[]
        self.frerelacummper =[]
        self.muestra = int(input('por favor digite el numero total de datos de la muestra'))-1
        #print('el valor de la muestra es: ' , self.muestra)
        self.agregar_Valores()
        self.mostrar_valores()
        self.all_calcules()
        self.frrelativee()
        self.frepercent()
        self.frepercentacum()
        #self.Shows()
        self.datfr()
        self.piee()
        self.barr()
        self.media()
        self.mediana()
        self.moda()


    def agregar_Valores(self):
        self.i = 0
        while   (self.i<=self.muestra):
            self.valor = int(input('por favor digite el valor '))
            self.valores.append(self.valor)
            self.i+=1


    def mostrar_valores(self):
        import collections
        self.howw = collections.Counter(self.valores)


    def all_calcules(self):
        self.x= 0
        self.frrelativa = 0
        for self.xii,self.frabs in self.howw.items():
            self.x = self.x + self.frabs
            self.xi.append(self.xii)
            self.frabsoluta.append(self.frabs)
            self.frabsolutaacum.append(self.x )

    def frrelativee(self):
        self.frrelative = 0
        self.frrelativeacum = 0
        for y in self.frabsoluta:
            self.frrelative = (y/(self.muestra+1))
            self.frrelativeacum = self.frrelativeacum +  self.frrelative
            self.frerel.append(self.frrelative)
            self.frerelacumm.append(self.frrelativeacum)

    def frepercent(self):
        for g in self.frerel:
            self.frpercent = g *100
            #print('geeee', self.frpercent)
            self.frerelper.append(self.frpercent)

    def frepercentacum(self):
        for f in  self.frerelacumm:
            self.facuper = f * 100
            self.frerelacummper.append(self.facuper)



    def Shows(self):
        print('total de la muestra: ' ,self.valores)
        print ("xi",self.xi)
        print ("frecuencia absoluta ",self.frabsoluta)
        print ("frecuencia absoluta acumulada" ,self.frabsolutaacum)
        print ("frecuencia relativa : " , self.frerel)
        print ("frecuencia relativa en porcentaje: " , self.frerelper)
        print ("frecuencia relativa acumulada : " , self.frerelacumm)
        print ("frecuencia relativa acumulada en porcentaje: " , self.frerelacummper)



    def datfr(self):
        import pandas as pd
        #import matplotlib.pyplot as plt
        zippedList =  list(zip(self.xi,self.frabsoluta, self.frabsolutaacum, self.frerel,self.frerelper,self.frerelacumm,self.frerelacummper))
        self.table = pd.DataFrame(zippedList, columns = ['xi','FRecuencia absoluta','Frecuencia acumulada','Frecuencia relativa','Frecuencia relativa %','Frecuencia relativa acumulada','Frecuencia relativa acumulada %'], index= self.xi)
        #print(zippedList)
        print(self.table)

    def piee(self):
        import matplotlib.pyplot as plt
        myl=self.table['xi']
        size = self.table['Frecuencia relativa %']
        fig1, ax1 = plt.subplots()
        ax1.pie(size, labels=myl, autopct='%1.1f%%',
        shadow=True, startangle=90)
        ax1.axis('equal')
        plt.show()

    def barr (self):
        import matplotlib.pyplot as plt
        myl=self.table['xi']
        size = self.table['Frecuencia relativa %']
        fig, ax = plt.subplots()
        ax.set_ylabel('Porcentaje')
        ax.set_title('Porcentaje de frecuencia relativa')
        plt.bar(myl, size)
        plt.savefig('percentfrecuenciarelativa.png')
        plt.show()

    def media(self):
        self.media = (( sum(self.valores)) / len(self.valores))
        print ("la media es: " , self.media)

    def mediana (self):
        self.howlist = len(self.valores)
        self.mitad = 0
        self.medianaa = 0
        #es par:
        if (self.howlist % 2 ==0 ):
            self.mitad =  int(self.howlist/ 2)-1
            self.medianaa = (self.valores[self.mitad] + self.valores[self.mitad+1])/2
            print("la mediana es: " ,self.medianaa)
        else:
            self.mitad = int((self.howlist +1)/2)-1
            self.medianaa = self.valores[self.mitad]
            print("valores ",self.valores)
            print("la mediana es: " ,self.medianaa)

    def moda (self):
        self.keyy=[]
        self.valuee=[]
        for value, repeat in self.howw.items():
            self.keyy.append(value)
            self.valuee.append(repeat)

        self.diction  = zip(self.keyy,self.valuee)
        self.di=dict(self.diction)
        self.mayor = 0
        self.who=0
        for k,v in self.di.items():
            if(self.mayor < v):
                self.mayor= v
                self.who=k

        print("La moda es: {},con una repetición de  {} veces.".format(self.who, self.mayor))






f=table()