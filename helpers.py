import sys

class SetUp:

    def __init__(self):
        pass

    @classmethod
    def get_input_filename(cls):
        for i in range(len(sys.argv)):
            if(sys.argv[i] == '-i' and i < (len(sys.argv) -1)):
                inputFileName = sys.argv[i + 1]

        return inputFileName

    @classmethod
    def get_output_filename(cls):

        for i in range(len(sys.argv)):
            if (sys.argv[i] == '-o' and i < (len(sys.argv) -1)):
                outputFileName = sys.argv[i + 1]

        return outputFileName


    @classmethod
    def import_data_file(cls):

        for i in range(len(sys.argv)):
            if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
                inputFileName = sys.argv[i + 1]

        try:
            instructions = [line.rstrip() for line in open(inputFileName, 'r')]
        except IOError:
            print("Could not open input file, is path correct?")

        return instructions

    @classmethod
    def imm_bit_to_32_bit_converter(cls,num, bitsize):

        if (negBitMask & num) > 0:
            num = num | extendMask
            num = num ^ 0xFFFFFFFF
            num = num + 1
            num = num * -1
        return num