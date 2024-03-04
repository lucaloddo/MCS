import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Vem2Tol3(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/vem2.mtx")
        tol = 10 ** -8
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 5425)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 1.2)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 2714)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 24)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 3566)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 0.7)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 66)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 0.1)
