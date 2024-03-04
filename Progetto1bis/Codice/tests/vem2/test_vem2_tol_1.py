import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Vem2Tol1(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/vem2.mtx")
        tol = 10 ** -4
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 1927)
        self.assertLess(self.it.percentageError(), 0.6)
        self.assertLess(self.it.time, 1)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 965)
        self.assertLess(self.it.percentageError(), 0.6)
        self.assertLess(self.it.time, 8)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 1308)
        self.assertLess(self.it.percentageError(), 0.5)
        self.assertLess(self.it.time, 1)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 47)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 1)
