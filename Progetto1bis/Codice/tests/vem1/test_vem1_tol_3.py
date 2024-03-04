import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Vem1Tol3(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/vem1.mtx")
        tol = 10 ** -8
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 3552)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 0.5)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 1778)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 9)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 2336)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 0.4)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 53)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 0.1)
