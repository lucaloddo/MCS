import os
import unittest

import readMatrix
from iterativeMethod import IterativeMethod


class Vem1Tol4(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        matrix = readMatrix.read(path + "/dati/vem1.mtx")
        tol = 10 ** -10
        self.it = IterativeMethod(matrix, tol)

    def testJacobi(self):
        self.it.solve("Jacobi")
        self.assertEqual(self.it.nIterations, 4671)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 1)

    def testGaussSeidel(self):
        self.it.solve("GaussSeidel")
        self.assertEqual(self.it.nIterations, 2338)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 12)

    def testGradiente(self):
        self.it.solve("Gradiente")
        self.assertEqual(self.it.nIterations, 3058)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 2)

    def testGradienteConiugato(self):
        self.it.solve("GradienteConiugato")
        self.assertEqual(self.it.nIterations, 59)
        self.assertLess(self.it.percentageError(), 0.1)
        self.assertLess(self.it.time, 1)
