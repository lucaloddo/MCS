import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Vem2Tol4(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/vem2.mtx")
        tol = 10 ** -10
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 7174)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 2)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 3589)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 35)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 4696)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 2)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 74)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 1)
