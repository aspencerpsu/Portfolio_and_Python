     1	import time
     2	import re
     3	import subprocess
     4	import math
     5	import datetime
     6	
     7	from django.utils.html import strip_tags
     8	
     9	class SendMailTo(object):
    10	  
    11	  def __init__(self, user, attachment):
    12	    self.user = user #The user we are sending mail to
    13	    self.attachment = attachment
    14	
    15	  def sendmail(self, message, subject, cmd):
    16	    if self.attachment:
    17		recv = subprocess.check_output("{cmd} {message} | mail -vv -a {attachment} -s {subject} {user}".format(attachment=self.attachment, 
    18			subject=subject, 
    19			cmd=cmd,
    20			message = message,
    21			user=self.user), shell=True)	
    22	    print recv 
    23	
    24	def main():
    25	  the_user = str(raw_input("Hello, who are we sending this message to? : "))
    26	  the_subject = str(raw_input("What's the subject within this document? (please use '\"\"'s): "))
    27	  the_message = str(raw_input("What would you like to say? "))
    28	  the_input = str(raw_input("What's the type? "))
    29	
    30	  if re.match("/(@\w+\.(com|edu|org|eu|cu|io))$/", the_user):
    31	    print "Sorry The From: Header is an inappropriate receiver"
    32	  else:
    33	    print "You're message has been sent"
    34	  
    35	  maildelivering = SendMailTo(the_user, "./products.html")
    36	  maildelivering.sendmail(the_message, the_subject, the_input)
    37	  print "delivery complete" 
    38	
    39	def count_words(html_string):
    40		"""
    41		E.G.
    42		the html you're parsing as shown underneath
    43	
    44		---<h1>this is a title</h1>"""
    45		word_string = strip_tags(html_string)
    46		count = len(re.findall(r'\w+', word_string)) #joincfe.com/projects/
    47		return count
    48	
    49	
    50	def get_read_time(html_string):
    51		count = count_words(html_string)
    52		readtime_min = int(math.ceil((count/200.0))) #assuming 200wpm reading comprehension
    53	
    54		# read_time_sec = readtime_min * 60
    55	
    56		read_time = str(datetime.timedelta(minutes=readtime_min))
    57		return read_time
    58	
