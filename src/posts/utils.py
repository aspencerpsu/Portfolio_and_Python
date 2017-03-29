import time
import re
import subprocess
import math
import datetime

from django.utils.html import strip_tags

class SendMailTo(object):
  
  def __init__(self, user, attachment):
    self.user = user #The user we are sending mail to
    self.attachment = attachment

  def sendmail(self, message, subject, cmd):
    if self.attachment:
	recv = subprocess.check_output("{cmd} {message} | mail -vv -a {attachment} -s {subject} {user}".format(attachment=self.attachment, 
		subject=subject, 
		cmd=cmd,
		message = message,
		user=self.user), shell=True)	
    else:
        recv = subprocess.check_output("{cmd} {message} | mail -vv -s {subject} {user}".format(subject=subject,
												cmd=cmd,
												message=message,
												user=self.user), shell=True)
    print recv 

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

