import email
from email import policy
from email.parser import BytesParser
import glob
import os


import os, pandas as pd, glob
from bs4 import BeautifulSoup as bs
import json
import re
import codecs
root='Sent/'
allFiles = []
for path, subdirs, files in os.walk(root):
    for name in files:
        allFiles.append(os.path.join(path, name))
print(len(allFiles))
list_of_mails=[]
for eml_file in allFiles:
    with open(eml_file, 'rb') as fp:  # select a specific email file from the list
        name = fp.name # Get file name
        msg = BytesParser(policy=policy.default).parse(fp)
    try:
        text = msg.get_body(preferencelist=('plain')).get_content()
    except:
        text = ''
    fp.close()
    #clean_text = preg_replace('/(^\w.+:\n)?(^>.*(\n|$))+/mi', '', text);
    clean_text = re.sub(r'/(^\w.+:\n)?(^>.*(\n|$))+/mi', "", text)
    #print(clean_text)
    text = text.split("\n")
    #print (name) # Get name of eml file
    list_of_mails.append([name,clean_text])

print(len(list_of_mails))
