#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):
        #a:integer, b:integer
        def test_sample01 (self):
                self.assertEqual (21, calc(3,7))
        #a:0, b:integer
        def test_sample02 (self):
                self.assertEqual (-1, calc(0,150))
        #a:letter, b:letter
        def test_sample03 (self):
                self.assertEqual (-1, calc('a','b'))
        #a:not integer, b:integer
        def test_sample04 (self):
                self.assertEqual (-1, calc(0.1,999))

# add testcase EP
        #a:letter, b:integer
        def test_sample05 (self):
                self.assertEqual (-1, calc('a',2))
        #a:integer, b:not integer
        def test_sample06 (self):
                self.assertEqual (-1, calc(999,0.1))
        #a:not integer, b:not integer
        def test_sample07 (self):
                self.assertEqual (-1, calc(0.1,0.1))
        #a:letter, b:not integer
        def test_sample08 (self):
                self.assertEqual (-1, calc('a',0.1))
        #a:integer, b:letter
        def test_sample09 (self):
                self.assertEqual (-1, calc(2,'b'))
        #a:not integer, b:letter
        def test_sample10 (self):
                self.assertEqual (-1, calc(0.1,'b'))
        
# add testcase BV  
        #a:1, b:integer
        def test_sample11 (self):
                self.assertEqual (2, calc(1,2))
        #a:999, b:integer
        def test_sample12 (self):
                self.assertEqual (1998, calc(999,2)) 
        #a:1000, b:integer
        def test_sample13 (self):
                self.assertEqual (-1, calc(1000,2)) 
        #a:integer, b:0
        def test_sample14 (self):
                self.assertEqual (-1, calc(2,0)) 
        #a:integer, b:1
        def test_sample15 (self):
                self.assertEqual (150, calc(2,1)) 
        #a:integer, b:999
        def test_sample16 (self):
                self.assertEqual (1998, calc(2,999)) 
        #a:integer, b:1000
        def test_sample17 (self):
                self.assertEqual (-1, calc(2,1000)) 