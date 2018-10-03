#!/usr/bin/env python
import os
import random

def main_header():
	ban = random.choice(os.listdir("banners"))
	banextenstion = "banners/%s" % (ban)
	ban_open = open(banextenstion, "r")
	print "\033[96m" + ban_open.read() + "\033[0m"
	ban_open.close()
