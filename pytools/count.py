import os, sys

def countFile(filename):
    lines, words, chars = 0, 0, 0
    fin = open(filename,'r')
    for l in fin:
        lines+=1
        chars+=len(l)
        words+=len(l.strip().split())
    
    print lines,'\t',words,'\t',chars,'\t',filename
    return (lines,words,chars)

def countPattern(pattern):
    import glob
    files, lines, words, chars = 0, 0, 0, 0
    for fname in glob.glob(pattern):
        try:
            l,w,c = countFile(fname)
            files+=1
            lines+=l
            words+=w
            chars+=c
        except Exception as e:
            pass # do not show errors
    return files,lines,words,chars

def usage():
    print 'Usage:',sys.argv[0],'<file>'
    sys.exit(1)

if __name__=='__main__':
    if len(sys.argv) < 2:
        usage()
    print 'line\tword\tchar\tfilename'
    print '-'*60
    f,l,w,c = 0,0,0,0
    for i,argv in enumerate(sys.argv):
        if i != 0:
            f1,l1,w1,c1 = countPattern(argv)
            f,l,w,c=(f+f1,l+l1,w+w1,c+c1)
    print '-'*60
    print f,'file(s) in total:'
    print l,'\t',w,'\t',c

