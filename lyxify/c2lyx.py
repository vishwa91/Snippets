import sys

def namer(filename):
    name = ''
    for i in filename:
        if i == '.':
            break
        name += i
    return name

try:
    f = open(sys.argv[1])
    print 'Opened ' + f.name
except:
    print "usage: python c2lyx file"
    sys.exit('Exit due to invalid parameters')

name = namer(f.name)

output = file(name+'.lyx','wd')

start = '''
#LyX 2.0 created this file. For more info see http://www.lyx.org/
\\lyxformat 345
\\begin_document
\\begin_header
\\textclass literate-article
\\use_default_options true
\\language english
\\inputencoding auto
\\font_roman default
\\font_sans default
\\font_typewriter default
\\font_default_family default
\\font_sc false
\\font_osf false
\\font_sf_scale 100
\\font_tt_scale 100

\\graphics default
\\paperfontsize default
\\spacing single
\\use_hyperref false
\\papersize default
\\use_geometry false
\\use_amsmath 1
\\use_esint 1
\\cite_engine basic
\\use_bibtopic false
\\paperorientation portrait
\\secnumdepth 3
\\tocdepth 3
\\paragraph_separation indent
\\defskip medskip
\\quotes_language english
\\papercolumns 1
\\papersides 1
\\paperpagestyle default
\\tracking_changes false
\\output_changes false
\\author ""
\\end_header
'''
output.writelines(start)

output.writelines('\\begin_body\n')
output.writelines('\\begin_layout Scrap\n\n')
output.writelines('<<*>>=\n')
output.writelines('\\begin_inset Newline newline\n')
output.writelines('\\end_inset\n\n')

for line in f.readlines():
    line = line.replace('\\','\n\\backslash\n')
    output.writelines(line)
    output.writelines('\n')
    output.writelines("\\begin_inset Newline newline\n")
    output.writelines("\\end_inset\n\n")

output.writelines('@\n')
output.writelines('\\end_layout\n')
output.writelines('\\end_body\n')
output.writelines('\\end_document\n')

print 'Created the lyx file '+name+'.lyx'
print 'Thank you for using c2lyx'

f.close()
output.close()
