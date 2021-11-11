'''
1. El salario promedio por Sector Económico (SE)
'''

import csv
from mrjob.job import MRJob
from mrjob.step import MRStep


class salprom(MRJob):

    def mapper_sect(self, _, line):

        (idemp, economic_sector, salary, year) = line.split(',')

        yield (economic_sector, int(salary))

    def reducer_sect(self, sector, values):

        s = list(values)

        promedio = sum(s) / len(s)

        yield (sector, promedio)
    

    def steps(self):
        return [
            MRStep(mapper=self.mapper_sect,
                   reducer=self.reducer_sect)
                   ]


if __name__ == '__main__':
    salprom.run()
