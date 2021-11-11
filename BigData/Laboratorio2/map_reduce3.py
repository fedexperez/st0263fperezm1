'''
3. Número de sector_economico por Empleado que ha tenido a lo largo de la estadística
La instruccion no se entiende muy bien, aquí se muestra por sector economico cuales son los empleados que ha tenido
'''

import csv
from mrjob.job import MRJob
from mrjob.step import MRStep

class salprom(MRJob):
    
    def semapper(self, _, line):

        (idemp, economic_sector, salary, year) = line.split(',')

        yield (idemp, economic_sector)

    def sereducer(self, idemp, values):

        s = list(values)

        yield (idemp, s) 

    def steps(self):
        return [
            MRStep(mapper=self.semapper,
                   reducer=self.sereducer) 
                   ]


if __name__ == '__main__':
    salprom.run()
