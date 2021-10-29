# Message formatter

#### Subscriber basted system used for formatting encoded ASCII messages into the desired type.

#### Currently supported formats:
- Decimal
- Hexadecimal
- Binary
- HTML

#### Expected output:  
```
python3 main.py

[ASCII Formatter] received message from [Code Broadcast]: ""SELECT * FROM Users WHERE UserId = " + txtUserId;"
[Binary Formatter] received message from [Code Broadcast]: "0010001001010011010001010100110001000101010000110101010000100000001010100010000001000110010100100100111101001101001000000101010101110011011001010111001001110011001000000101011101001000010001010101001001000101001000000101010101110011011001010111001001001001011001000010000000111101001000000010001000100000001010110010000001110100011110000111010001010101011100110110010101110010010010010110010000111011"
[Hex Formatter] received message from [Code Broadcast]: "0x220x530x450x4C0x450x430x540x200x2A0x200x460x520x4F0x4D0x200x550x730x650x720x730x200x570x480x450x520x450x200x550x730x650x720x490x640x200x3D0x200x220x200x2B0x200x740x780x740x550x730x650x720x490x640x3B"
[Html Formatter] received message from [Code Broadcast]: "&#34;&#83;&#69;&#76;&#69;&#67;&#84;&#32;&#42;&#32;&#70;&#82;&#79;&#77;&#32;&#85;&#115;&#101;&#114;&#115;&#32;&#87;&#72;&#69;&#82;&#69;&#32;&#85;&#115;&#101;&#114;&#73;&#100;&#32;&#61;&#32;&#34;&#32;&#43;&#32;&#116;&#120;&#116;&#85;&#115;&#101;&#114;&#73;&#100;&#59;"

[ASCII Formatter] received message from [Decimal Broadcast]: "$1,000,000"
[Decimal Formatter] received message from [Decimal Broadcast]: "036049044048048048044048048048"
```