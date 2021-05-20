import re

def RegexStrip(string, strip=None):
    leftSideWhite = re.compile(r'^([\s]+)')
    rightSideWhite = re.compile(r'([\s]+)$')
    if strip == None:
        leftStrip = leftSideWhite.sub('', string)
        strippedString = rightSideWhite.sub('', leftStrip)
    else:
        for i in strip:
            passedStrip = re.compile(i)
            strippedString = passedStrip.sub('', string)
            string = strippedString
    return strippedString

output = RegexStrip('            adfffsayuotooklmri79nmbbylpffff(aaaggu)8966            ', 'fugn680 d9olkymb7a')
print(output)