import io
import re

with io.open('queneau_novel.txt','r',encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    if( re.search('\[.*\].*',line) ):
        print "<h2>"
        print line
        print "</h2>"
    elif( re.search('   ',line) ):
        print "<blockquote><i>"
        print line.encode('ascii', 'xmlcharrefreplace')
        print "</i></blockquote>"
    else:
        print "<p>"
        print line.encode('ascii', 'xmlcharrefreplace')
        print "</p>"

