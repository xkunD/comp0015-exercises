##
#  This program is from: Python for Everyone by Horstmann and Necaise
#  The program processes a file containing a count followed by data values.
#  If the file doesn't exist or the format is incorrect, you can specify another file.
#

def main() :
   done = False
   while not done :
      try :
         filename = input("Please enter the file name: ")
         data = readFile(filename)
         
         # As an example for processing the data, we compute the sum.
         total = 0
         for value in data :
            total = total + value
            
         print("The sum is", total)
         done = True
         
      except IOError :
         print("Error: file not found.")
         
      except ValueError : 
         print("Error: file contents invalid.")
         
      except RuntimeError as error :
         print("Error:", str(error))

## Opens a file and reads a data set.
#  @param filename the name of the file holding the data
#  @return a list containing the data in the file
#
def readFile(filename) :
   inFile = open(filename, "r")   
   try :
      return readData(inFile)
   finally :
      inFile.close()

## Reads a data set.
#  @param inFile the input file containing the data
#  @return the data set in a list
#
def readData(inFile) :
   line = inFile.readline()
   numberOfValues = int(line)  # May raise a ValueError exception.
   data = []
   
   for i in range(numberOfValues) :
      line = inFile.readline()
      value = int(line)        # May raise a ValueError exception.               
      data.append(value)
      
   # Make sure there are no more values in the file.
   line = inFile.readline()
   if line != "" :          
      raise RuntimeError("End of file expected.")
   
   return data
   
# Start the program.
main()
