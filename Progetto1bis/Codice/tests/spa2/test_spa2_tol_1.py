import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Spa2Tol1(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/spa2.mtx")
        tol = 10 ** -4
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 36)
        self.assertLess(self.it.percentageError(), 0.2)
        self.assertLess(self.it.time, 0.6)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 5)
        self.assertLess(self.it.percentageError(), 0.3)
        self.assertLess(self.it.time, 20)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 161)
        self.assertLess(self.it.percentageError(), 1.9)
        self.assertLess(self.it.time, 3)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 42)
        self.assertLess(self.it.percentageError(), 0.99)
        self.assertLess(self.it.time, 2)
