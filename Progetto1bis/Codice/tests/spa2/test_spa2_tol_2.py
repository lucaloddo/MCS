import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Spa2Tol2(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/spa2.mtx")
        tol = 10 ** -6
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 57)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 2)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 8)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 30)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 1949)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 20)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 122)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 3)
