import re
COUNT = 0

def updateCount():
    fin = open(__file__, 'r')
    code = fin.read()
    fin.close()

    second_line = code.split('\n')[1]
    second_line_parts = second_line.split(' ')
    second_line_parts[2] = str(int(second_line_parts[2])+1)

    second_line = ' '.join(second_line_parts)
    lines = code.split('\n')
    lines[1] = second_line
    code = '\n'.join(lines)

    fout = open(__file__, 'w')
    fout.write(code)
    fout.close()



    
      
# print ("socket binded to %s", %(port) )
  


if __name__ == '__main__':
    print('This script has run {} times'.format(COUNT))
    updateCount()