#!/usr/bin/python

import os,sys,time
import logging

def initialize(params):
	print >>sys.__stdout__,"Metric Client initialized with parameters %s" % str(params)

def add_metric(name,value,timestamp):
	print >>sys.__stdout__,"Metric - name is %s value is %s timestamp is %s" % (name,value,timestamp)

def done():
	print >>sys.__stdout__,"Metric client done"

