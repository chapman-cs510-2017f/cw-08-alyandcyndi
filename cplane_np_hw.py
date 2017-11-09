#!/usr/bin/env python3

###
# Name: Cynthia Parks
# Student ID: 2303535
# Email: cparks@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Homework 6
###

import cplane_np
from cplane_np import ArrayComplexPlane
import numpy as np
import pandas as pd

def julia(c, max=100):
    """
    Takes in a complex number and returns the number of times it takes for the magnitude of 
    the complex number to be greater than 2.
    
    Args:
        c (complex): Complex parameter for function
    
    Returns:
        algfunc (function): Function to see how many iterations are needed for |z|>2
    """
    
    def algfunc(z):
        """
        Function used to track iterations needed for |z|>2
        """
        n=1
        
        while n < max:
            if abs(z) > 2:
                return n
            else:
                n += 1
                z = z**2 + c
        return 0
    return algfunc


class JuliaPlane(ArrayComplexPlane):
    """
    Class that subclasses the ArrayComplexPlane class.  It applies the julia function to the plane.  
    
    Args:
        c (complex): Complex parameter for the julia function
        
    Attributes:
        plane []: List of complex points (see __create_plane)
        fs []: List of functions applied to plane
    """
    def __init__(self, c):
        """
        Initializes plane with the julia applied to the points and new min/max set
        """
        self.c = c
        ArrayComplexPlane.__init__(self, -2, 2, 1000, -2, 2, 1000)
        self.apply(julia(c))
        
    def refresh(self, c):
        """
        Refreshes plane and applies the julia function to the points
        """
        self.c = c
        self.fs = []
        self.plane = self._ArrayComplexPlane__create_plane()
        self.apply(julia(c))
        
    def toCSV(self, filename):
        """
        Exports transformed plane to a .cvs file
        """
        attribute_id = ['xmin', 'xmax', 'xlen', 'ymin', 'ymax', 'ylen', 'c']
        attribute = [self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen, self.c]