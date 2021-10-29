from formatters.asciiFormatter import ASCIIFormatter
from formatters.binaryFormatter import BinaryFormatter
from formatters.hexFormatter import HexFormatter
from formatters.decimalFormatter import DecimalFormatter
from formatters.htmlFormatter import HtmlFormatter
from producer import Producer


p1 = Producer('Code Broadcast')
p2 = Producer('Decimal Broadcast')

s1 = ASCIIFormatter('ASCII Formatter')
s2 = BinaryFormatter('Binary Formatter')
s3 = HexFormatter('Hex Formatter')
s4 = DecimalFormatter('Decimal Formatter')
s5 = HtmlFormatter('Html Formatter')

s1.subscribe(p1)
s2.subscribe(p1)
s3.subscribe(p1)
s5.subscribe(p1)

s1.subscribe(p2)
s4.subscribe(p2)

p1.broadcast('"SELECT * FROM Users WHERE UserId = " + txtUserId;')
print()
p2.broadcast('$1,000,000')
