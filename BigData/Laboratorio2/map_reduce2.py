'''
2. El salario promedio por Empleado
'''

import csv
from mrjob.job import MRJob
from mrjob.step import MRStep


class salprom(MRJob):
    
    def avgmapper(self, _, line):

        (idemp, economic_sector, salary, year) = line.split(',')

        yield (idemp, int(salary))

    def avgreducer(self, idemp, values):

        s = list(values)

        promedio = sum(s) / len(s)

        yield (idemp, promedio) 

    def steps(self):
        return [
            MRStep(mapper=self.avgmapper,
                   reducer=self.avgreducer) 
                   ]


if __name__ == '__main__':
    salprom.run()
