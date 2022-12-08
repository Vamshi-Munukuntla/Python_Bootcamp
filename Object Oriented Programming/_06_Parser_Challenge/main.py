from parser import Parser
from UK_Parser import UKParser

string1 = 'contact us via 111-222-2222 or info@appmillers.com'
string2 = 'contact us via +1-111-222-2222 or info@appmillers.com'
parser1 = Parser(string1)
print(parser1.parser())

parser2 = UKParser(string2)
print(parser2.parser())
