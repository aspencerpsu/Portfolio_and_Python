import time
import re
import math
import datetime

from django.utils.html import strip_tags

def count_words(html_string):
	"""
	E.G.
	the html you're parsing as shown underneath

	---<h1>this is a title</h1>"""
	word_string = strip_tags(html_string)
	count = len(re.findall(r'\w+', word_string)) #joincfe.com/projects/
	return count


def get_read_time(html_string):
	count = count_words(html_string)
	readtime_min = int(math.ceil((count/200.0))) #assuming 200wpm reading comprehension

	# read_time_sec = readtime_min * 60

	read_time = str(datetime.timedelta(minutes=readtime_min))
	return read_time