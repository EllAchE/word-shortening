import csv

def writeXml():
    row1 = '<?xml version="1.0" encoding="UTF-8"?>'
    row2 = '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">'
    row3 = '<plist version="1.0">'
    row4 = '<array>'
    secondToLast = '</array>'
    lastRow = '</plist>'

    dictLine = '	<dict>'
    phraseLine = '		<key>phrase</key>'
    shortcutLine = '		<key>shortcut</key>'
    closingDictLine = '	</dict>'

    def getStringLine(val):
        return '		<string>' + val + '</string>'

    def constructChunk(pair):
        # reversed bc of order
        return [dictLine, phraseLine, getStringLine(pair[1]), shortcutLine, getStringLine(pair[0]), closingDictLine]

    path = 'shortcuts.plist'

    lines = [row1, row2, row3, row4]
    with open('./mappings.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            nr = constructChunk(row)
            for i in nr:
                lines.append(i)

    lines.append(secondToLast)
    lines.append(lastRow)

    lines = list(map(lambda a : a + '\n', lines))

    with open(path, 'w') as f:
        f.writelines(lines)
