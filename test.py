
import sys


def main():
    file=r"C:\Temp\docs\Countries.txt"

    with open(file, 'r') as fh:

        print ( [ line.split(',')[3] for line in fh ] )
        '''
        
        for index,line in enumerate(fh):
            try:
                country =  line.split(',')
                #print( type( country) )
                print( country[3])
            except:
                print(f"data missing in:{line} and index:{index}")
        '''


if __name__ == '__main__':
    sys.exit(main() )
