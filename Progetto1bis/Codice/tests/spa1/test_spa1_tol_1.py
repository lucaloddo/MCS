import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Spa1Tol1(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/spa1.mtx")
        tol = 10 ** -4
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 115)
        self.assertLess(self.it.percentageError(), 0.2)
        self.assertLess(self.it.time, 0.2)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 9)
        self.assertLess(self.it.percentageError(), 1.9)
        self.assertLess(self.it.time, 4)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 143)
        self.assertLess(self.it.percentageError(), 3.5)
        self.assertLess(self.it.time, 0.2)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 49)
        self.assertLess(self.it.percentageError(), 2.1)
        self.assertLess(self.it.time, 0.2)
