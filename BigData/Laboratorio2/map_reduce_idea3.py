'''
3. Número de SE por Empleado que ha tenido a lo largo de la estadística
La instruccion no se entiende muy bien, aquí se muestra por empleado cuantos en sectores economicos ha estado
'''

import csv
from mrjob.job import MRJob
from mrjob.step import MRStep

class salprom(MRJob):
    
    def semapper(self, _, line):

        (idemp, economic_sector, salary, year) = line.split(',')

        yield (economic_sector, 1)

    def sereducer(self, economic_sector, values):
        yield (economic_sector, sum(values)) 

    def steps(self):
        return [
            MRStep(mapper=self.semapper,
                   reducer=self.sereducer) 
                   ]


if __name__ == '__main__':
    salprom.run()
