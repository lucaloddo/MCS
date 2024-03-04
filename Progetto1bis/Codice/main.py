import logging
import os
import sys

import iterativeMethod as itM
import readMatrix


def configLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # create console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(ch)


def buildMatrixPathsList(directory):
    matrici = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            matrici.append(f)
    return matrici


def main():
    configLogger()
    logging.info("Program started")
    directory = "dati"
    methods = ["Jacobi", "GaussSeidel", "Gradiente", "GradienteConiugato"]
    tolerances = [10 ** -4, 10 ** -6, 10 ** -8, 10 ** -10]
    matrices = buildMatrixPathsList(directory)
    for matrix in matrices:
        logging.info("--------------------------------------------------")
        logging.info("Solving linear system with matrix A at path: " + matrix)
        matrixA = readMatrix.read(matrix)
        for tol in tolerances:
            logging.info("--------------------------------------------------")
            logging.info("Tolerance selected: " + str(tol))
            for method in methods:
                logging.info("--------------------------------------------------")
                logging.info("Iterative method selected: " + method)
                iterativeObj = itM.IterativeMethod(matrixA, tol)
                iterativeObj.solve(method)


main()
