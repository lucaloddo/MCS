import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Vem1Tol2(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/vem1.mtx")
        tol = 10 ** -6
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 2433)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 2)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 1218)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 6)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 1612)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 1)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 45)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 1)