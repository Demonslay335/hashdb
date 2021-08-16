#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Malware hash library.
"""
import algorithms

class AlgorithmError(Exception):
    pass

def get_algorithms():
    return list(algorithms.modules.keys())

def get_algorithm_hash(algorithm_name, data):
    if algorithm_name not in list(algorithms.modules.keys()):
        raise AlgorithmError("Algorithm not found")
    if type(data) == str:
        data = data.encode('utf-8')
    return algorithms.modules[algorithm_name].get_hash(data)
