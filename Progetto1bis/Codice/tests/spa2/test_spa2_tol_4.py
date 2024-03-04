import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Spa2Tol4(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/spa2.mtx")
        tol = 10 ** -10
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 99)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 2)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 15)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 40)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 8285)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 80)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 240)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 6)
