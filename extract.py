import datefinder
from commonregex import CommonRegex
import geograpy
import re


class Extractor(object):
  """docstring for ClassName"""
  path = ""
  parsed_text=""
  contents=""

  def setPath(p):
    this.path = p
    this.parsedContent()

  def parsedContent(this):
    openObject=open(this.path, "r")
    this.contents = openObject.read()
    this.parsed_text = CommonRegex(contents)
   
  def findUserName():
    return "Shubhi Lohani"
    
  def findDate():
    date = this.parsed_text.dates
    return date[0]

  def findTIme():
    time = this.parsed_text.times
    return time[0]

  def findAddress():
    address=[]      
    regexp1 = "venue[ ]?[:-][ ]?[a-zA-Z0-9,&. -]+"
    if "venue" in this.contents:
      address =re.findall(regexp1, contents.lower())
      address[0] = address[0][5:]
      address[0].strip()
      address[0] = s[1:]
      address[0].strip();
    if not address:
      regexp = "[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}"
      #"[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}"
      address = re.findall(regexp, contents)
    if not address:
      regexp = "\d+.+(?=AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)[A-Z]{2}[, ]+\d{5}(?:-\d{4})?"
      #"[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}"
      address = re.findall(regexp, contents)
    return address[0]    