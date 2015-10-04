'''
Author: Youssef Elasser

Reads csv file and writes to an xsl file in the form of 
<xsl:when test="$code='lang"'>Language</xsl:when>
'''

import csv

if __name__ == '__main__':

    with open('languages.csv','rb') as csv_file:
        # creates a csv reader object
        lang = csv.reader(csv_file, dialect='excel', quotechar = '|')

        # opens output xsl file to be written to
        f = open('ccd.xsl','w')

        for row in lang:
            f.write('<xsl:when test="$code=\'' + row[0] + '\'">' + row[1]
            		+ '</xsl:when>\n')