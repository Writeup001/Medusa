#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.BugFree import BugFreeFileContains
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(BugFreeFileContains.medusa, Url, Values, UnixTimestamp)
    Prompt("BugFree")