import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Vem1Tol1(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/vem1.mtx")
        tol = 10 ** -4
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 1314)
        self.assertLess(self.it.percentageError(), 0.5)
        self.assertLess(self.it.time, 0.5)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 659)
        self.assertLess(self.it.percentageError(), 0.5)
        self.assertLess(self.it.time, 5)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 890)
        self.assertLess(self.it.percentageError(), 0.5)
        self.assertLess(self.it.time, 0.5)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 38)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 2)
