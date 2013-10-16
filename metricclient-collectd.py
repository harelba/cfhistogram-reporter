#!/usr/bin/python

import os,sys,time
import logging

def initialize(params):
	pass
	#print >>sys.__stdout__,"Metric Client initialized with parameters %s" % str(params)

def add_metric(name,value,timestamp):
	print >>sys.__stdout__,"Here you should write the output in collectd format"

def done():
	pass
	#print >>sys.__stdout__,"Metric client done"

