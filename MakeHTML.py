import io
import re

def main():
    with io.open('queneau_novel.txt','r',encoding='utf-8') as f:
        lines = f.readlines()
    
    print '<html>'
    print '<link rel="stylesheet" href="slate.css" media="screen">'
    print '<body>'
    
    make_title()
    make_toc(lines)
    make_body(lines)
    
    print '</body>'
    print '</html>'

def make_title():
    print '<center>'
    print '<h1>Riverrun</h1>'
    print '<p class="lead">An automatically generated NaNoGenMo 2016 submission. Based on James Joyce\'s <u>Ulysses</u></p>'
    print '</center>'
    print '<p>&nbsp;</p>'
    print '<p>&nbsp;</p>'


def make_toc(lines):

    print '<center>'
    print '<h3>Table of Contents</h3>'
    print '<p>&nbsp;</p>'
    chapter = 1
    for line in lines:
        m=re.search('\[ ([0-9][0-9].*) \].*',line)
        if m is not None:
            print '<p><a href="#' + str(chapter) + '">' + m.groups(0)[0] + '</a></p>'
            chapter += 1

    print '</center>'
    print '<p>&nbsp;</p>'
    print '<p>&nbsp;</p>'
    print '<p>&nbsp;</p>'



def make_body(lines):

    for line in lines:
        chapter = 1
        if( re.search('\[.*\].*',line) ):
            print '<a name="' + str(chapter) + '"></a>'
            print "<h2>"
            print line
            print "</h2>"
            chapter += 1 
        elif( re.search('   ',line) ):
            print "<blockquote><i>"
            print line.encode('ascii', 'xmlcharrefreplace')
            print "</i></blockquote>"
        else:
            print "<p>"
            print line.encode('ascii', 'xmlcharrefreplace')
            print "</p>"

if __name__=="__main__":
    main()
