import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Spa1Tol4(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/spa1.mtx")
        tol = 10 ** -10
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 313)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 0.6)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 31)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 11)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 12919)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 16)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 200)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 0.5)
