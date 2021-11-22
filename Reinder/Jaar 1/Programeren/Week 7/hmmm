#!/usr/bin/python3
#
# $Id: hmmm,v 2.5 2018-02-22 19:18:43-08 geoff Exp $
#
# hmmm.py: Harvey Mudd Miniature Machine assembler and simulator
#
# Geoff Kuenning, 2016
#
# Based on hmmmAssembler.py and hmmmSimulator.py
# Ran Libeskind-Hadas, 2006
# modified by Peter Mawhorter, June 2006
# Extensively modified by Geoff Kuenning, October 2007
# modified by Kaya Woodall, June 2012

"""Assemble and execute Hmmm programs.

Usage:
    hmmm [-o FILE] [--] [HMMM-SOURCE]
    hmmm [-d] [--] [HMMM-SOURCE]
    hmmm [-d] [--] [HMMM-BINARY]
    hmmm (--help|--version)

HMMM-SOURCE is a source file in the Hmmm assembly language.
HMMM-BINARY is a Hmmm binary file produced by the -o switch.

If no input file name is given, the user will be prompted for one.

Options:
    -o, --output FILE           Write assembled binary to FILE; don't simulate.
    -d, --debug                 Enter debug mode when simulating.
    -h, --help                  Print this help message.
    --version                   Show version.
"""

import sys, string, re
have_docopt = True
try:
    import docopt
except ImportError:
    # BOO HISS!
    have_docopt = False

#
# opcodes encodes the preferred opcode translations.  Each entry is a
# triple: match, mask, translation.  If the binary word matches
# "match" under the mask, the translated opcode is given by that
# entry.  Blanks are ignored in the match and mask fields.  The table
# is order-dependent; the first match is used.  Note that at present
# the masks are either 0x0 or 0xF in each hex digit, although the code
# doesn't enforce that restriction.
#
# This table is shared directly between the assembler and simulator.
# The assembler doesn't use all the fields.
#
opcodes = (
        ("0000 0000 0000 0000", "1111 1111 1111 1111", "halt"),
        ("0000 0000 0000 0001", "1111 0000 1111 1111", "read"),
        ("0000 0000 0000 0010", "1111 0000 1111 1111", "write"),
        ("0000 0000 0000 0011", "1111 0000 1111 1111", "jumpr"),
        ("0001 0000 0000 0000", "1111 0000 0000 0000", "setn"),
        ("0010 0000 0000 0000", "1111 0000 0000 0000", "loadn"),
        ("0011 0000 0000 0000", "1111 0000 0000 0000", "storen"),
        ("0100 0000 0000 0000", "1111 0000 0000 1111", "loadr"),
        ("0100 0000 0000 0001", "1111 0000 0000 1111", "storer"),
        ("0100 0000 0000 0010", "1111 0000 0000 1111", "popr"),
        ("0100 0000 0000 0011", "1111 0000 0000 1111", "pushr"),
        ("0101 0000 0000 0000", "1111 0000 0000 0000", "addn"),
        ("0110 0000 0000 0000", "1111 1111 1111 1111", "nop"),
        ("0110 0000 0000 0000", "1111 0000 0000 1111", "copy"),
        ("0110 0000 0000 0000", "1111 0000 0000 0000", "add"),
        ("0111 0000 0000 0000", "1111 0000 1111 0000", "neg"),
        ("0111 0000 0000 0000", "1111 0000 0000 0000", "sub"),
        ("1000 0000 0000 0000", "1111 0000 0000 0000", "mul"),
        ("1001 0000 0000 0000", "1111 0000 0000 0000", "div"),
        ("1010 0000 0000 0000", "1111 0000 0000 0000", "mod"),
        ("1011 0000 0000 0000", "1111 1111 0000 0000", "jumpn"),
        ("1011 0000 0000 0000", "1111 0000 0000 0000", "calln"),
        ("1100 0000 0000 0000", "1111 0000 0000 0000", "jeqzn"),
        ("1101 0000 0000 0000", "1111 0000 0000 0000", "jnezn"),
        ("1110 0000 0000 0000", "1111 0000 0000 0000", "jgtzn"),
        ("1111 0000 0000 0000", "1111 0000 0000 0000", "jltzn"),
        ("0000 0000 0000 0000", "0000 0000 0000 0000", "data"),
        )
#
# The assembler would prefer a dictionary for the opcodes; that's not
# possible in the simulator because ordering matters.  Convert the
# table above into a dictionary that translates opcodes into encodings.
#
opcodeDict = {}
for i in range(len(opcodes)):
    opcodeDict[opcodes[i][2]] = opcodes[i][0]

#
# Encodings of the registers into binary.
#
register_encodings = {"r0":"0000", "r1":"0001", "r2":"0010", "r3":"0011",
    "r4":"0100", "r5":"0101", "r6":"0110", "r7":"0111",
    "r8":"1000", "r9":"1001", "r10":"1010", "r11":"1011",
    "r12":"1100", "r13":"1101", "r14":"1110", "r15":"1111", 
    "R0":"0000", "R1":"0001", "R2":"0010", "R3":"0011",
    "R4":"0100", "R5":"0101", "R6":"0110", "R7":"0111",
    "R8":"1000", "R9":"1001", "R10":"1010", "R11":"1011",
    "R12":"1100", "R13":"1101", "R14":"1110", "R15":"1111"}

#
# arguments encodes the required arguments for each operation.  "r"
# means a register; "s" means a signed 8-bit number in decimal; "u"
# means an unsigned 8-bit number in decimal, and "n" means a signed or
# unsigned 16-bit number in hex (0x notation) or decimal.  Actually,
# all numbers are accepted in all bases.
#
# In addition, "z" means insert four bits of zeros without swallowing
# an argument.
#
arguments = {
        "halt":   "",
        "read":   "r",
        "write":  "r",
        "jumpr":  "r",
        "setn":   "rs",
        "loadn":  "ru",
        "storen": "ru",
        "loadr":  "rr",
        "storer": "rr",
        "popr":   "rr",
        "pushr":  "rr",
        "addn":   "rs",
        "add":    "rrr",
        "copy":   "rr",
        "nop":    "",
        "sub":    "rrr",
        "neg":    "rzr",
        "mul":    "rrr",
        "div":    "rrr",
        "mod":    "rrr",
        "jumpn":  "zu",
        "calln":  "ru",
        "jeqzn":  "ru",
        "jgtzn":  "ru",
        "jltzn":  "ru",
        "jnezn":  "ru",
        "data":   "n",
        }

######################################################################
######################################################################
#
# DRIVER PROGRAM FOR THE ASSEMBLER AND SIMULATOR
#
######################################################################
######################################################################

def main(program = None):
    """Hmmm assembler and simulator.  Normally called by running the file.
       If it is called internally, will assemble and run "program"."""
    global debug

    revision = '$Revision: 2.5 $'
    version = re.search(r'Revision: ([0-9.]*)', revision).group(1)
    if program is not None:
        args = {
          '--debug': False,
          '--output': None,
          }
        program = convertStringToProgram(program)
    else:
        if have_docopt:
            args = docopt.docopt(__doc__, version = 'hmmm version ' + version)
        else:
            #
            # This sucks.  We have to deal with the arguments ourselves.
            # To simplify the task, we don't support most of the switches;
            # only -d and -n are allowed, and we don't do a lot of checking.
            # Install docopt!!!
            #
            args = {
              'HMMM-SOURCE': None,
              'HMMM-BINARY': None,
              '--debug': False,
              '--output': None,
              }
            if len(sys.argv) > 1  and  sys.argv[1] == '-d':
                print("Debug")
                args['--debug'] = True
                sys.argv = sys.argv[0:1] + sys.argv[2:]
            if len(sys.argv) > 1:
                args['HMMM-SOURCE'] = sys.argv[1]
        if args['HMMM-SOURCE'] is None:
            args['HMMM-SOURCE'] = args['HMMM-BINARY']
        if args['HMMM-SOURCE'] is None:
            args['HMMM-SOURCE'] = input('Enter input file name: ')
        program = readFile(args['HMMM-SOURCE'])

    if not isMachineCode(program):
        program = hmmmAssembler(program)
        if program is None:
            sys.exit(1)

        if args['--output']:
            writeMachineCode(program, args['--output'])
            sys.exit(0)

        program = programToMachineCode(program)

    #
    # We have either assembled the file or read a binary file.  We're
    # ready to run it.
    #
    convertMachineCode(program)
    if args['--debug']:
        debug = True
    try:
        runHmmm()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user, halting program execution...\n",
          file = sys.stderr)
        sys.exit(1)
    except EOFError:
        print("\n\nEnd of input, halting program execution...\n",
          file = sys.stderr)
        sys.exit(1)
    sys.exit(0)

#
# Version of hmmm that can be run from inside iPython.
#
def hmmm(filename = None):
    """Assemble a Hmmm program from a given file and run it."""
    if filename is None:
        filename = input('Enter input file name: ')
    program = readFile(filename)
    if not isMachineCode(program):
        program = hmmmAssembler(program)
        program = programToMachineCode(program)

    convertMachineCode(program)
    try:
        runHmmm()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user, halting program execution...\n",
          file = sys.stderr)
    except EOFError:
        print("\n\nEnd of input, halting program execution...\n",
          file = sys.stderr)

######################################################################
######################################################################
#
# HMMM ASSEMBLER
#
######################################################################
######################################################################

# Maximum output line width
outputLineMax = 78

#
# insertBits performs a logical "OR" on A and B
#
def insertBits(a, b):
    """Perform logical OR on a and b, preserving blanks in a.  Both a and
       b must consist exclusively of blanks, 0s, and 1s."""
    if a == ''  or  b == '':
        return a
    elif a[0] == ' ':
        return ' ' + insertBits(a[1:], b)
    elif b[0] == ' ':
        return insertBits(a, b[1:])
    elif a[0] == '1'  or  b[0] == '1':
        return '1' + insertBits(a[1:], b[1:])
    else:
        return '0' + insertBits(a[1:], b[1:])

def numToTwosComplement(value, width):
    """Convert value to a twos-complement binary number of the given width."""
    if value < 0:
        return numToTwosComplement(2**width + value, width)
    fmt = '{:0' + str(width) + 'b}'
    return fmt.format(value)

def translate(flds):
    try:
        operation = flds[0]
        opval = opcodeDict[operation]
    except KeyError:
        print("\nOPERATION ERROR:")
        print("'{} IS NOT A VALID OPERATION.".format(flds[0]))
        return "***OPERATION ERROR HERE***"
    encoding = opval
    extraBits = '0000'
    argsRequired = arguments[flds[0]]
    parts  = re.split(r'[,\s]+', flds[1].strip())    # split args into parts
    argc = len(parts)
    if argc == 1  and  parts[0] == '':
        argc = 0
        parts = []
    numArgsRequired = 0
    for i in argsRequired:
        if i != 'z':
            numArgsRequired += 1
    if argc != numArgsRequired:
        print("\nARGUMENT ERROR:")
        print("WRONG NUMBER OF ARGUMENTS.")
        print("DETECTED {} ARGUMENTS, EXPECTED {} ARGUMENTS"
          .format(argc, numArgsRequired))
        print(flds[0], flds[1])
        return "***ARGUMENT ERROR HERE***"
    for p in parts:
        if p == '':
            print("\nARGUMENT ERROR:")
            print("EMPTY ARGUMENT.")
            return "***ARGUMENT ERROR HERE***"

        arg = re.match(r'([Rr][0-9]+|-?[0-9]+|-|0[xX][0-9a-fA-F]+)$', p)
        if arg is None:
            print("\nARGUMENT ERROR:")
            print("'{}' IS NEITHER A REGISTER NOR A NUMBER.".format(p))
            return "***ARGUMENT ERROR HERE***"
        code = argsRequired[0]
        argsRequired = argsRequired[1:]
        while code == 'z':
            extraBits += '0000'
            code = argsRequired[0]
            argsRequired = argsRequired[1:]
        if code == 'r':
            try:
                bits = register_encodings[p]
            except KeyError:
                print("\nREGISTER ERROR:")
                print("'{}' IS NOT A VALID REGISTER.".format(p))
                return "***REGISTER ERROR HERE***"
            extraBits += bits
        else:
            try:
                value = int(p)
            except ValueError:
                print("\nARGUMENT ERROR:")
                print("'{}' IS NOT A VALID NUMBER.".format(p))
                return "***ARGUMENT ERROR HERE***"
            if code == 's':
                ok = -128 <= value <= 127
                width = 8
            elif code == 'u':
                ok = 0 <= value <= 255
                width = 8
            elif code == 'n':
                ok = -32768 <= value <= 65535
                width = 16
                extraBits = ''          # No padding in this case
            else:
                print("\nINTERNAL ERROR:")
                print("HMMMASSEMBLER ENCOUNTERED AN UNEXPECTED SITUATION.")
                return "***INTERNAL ERROR HERE***"
            if not ok:
                print("\nARGUMENT ERROR:")
                print("'{}' IS OUT OF RANGE FOR THE ARGUMENT.".format(p))
                return "***ARGUMENT ERROR HERE***"
            extraBits += numToTwosComplement(value, width)

    return insertBits(encoding, extraBits)

def assemble(program):
    output = []
    lineNum = -1
    for line in program:
        lineNum += 1
        # nasty regular expression to parse line number, instruction,
        # and arguments
        if len(re.findall(r'^([0-9]+)[\s]+([a-z]+)[\s]*(([-r0-9xXa-fA-F]+[,\s]*)*)([\s]+(#.*)*)*$', line)) != 1:
            print("\nSYNTAX ERROR ON LINE {}:".format(lineNum))
            print(line)
            output.append([lineNum, "***SYNTAX ERROR HERE***", line])
            continue

        flds = re.sub(r'^([0-9]+)[\s]+([a-z]+)[\s]*(([-r0-9xXa-fA-F]+[,\s]*)*)([\s]+(#.*)*)*$', r'\1~\2~\3', line).split('~')

        try:
            userLine = int(flds[0])
        except ValueError:
            print("\nMISSING LINE NUMBER AT LINE {}:".format(lineNum))
            print("FOUND:", flds[0])
            output.append([lineNum, "***MISSING LINE NUMBER HERE***", line])
            continue

        instruction = translate(flds[1:])
        triplet = [lineNum, instruction, line]

        if instruction[0] != '*' and lineNum != userLine:
            print("\nBAD LINE NUMBER AT LINE {}:".format(lineNum))
            print("LINE NUMBER: {} EXPECTED {}".format(flds[0], lineNum))
            output.append([lineNum, "***BAD LINE NUMBER HERE***", line])
            continue

        output.append(triplet)
    return output


def readFile(filename):
    try:
        f = open(filename,"r")          # file with machine code
    except IOError:
        print("Cannot open file: ", filename)
        sys.exit(1)
    program = []
    while True:
        line = f.readline()
        if line == "":                  # End of file
            break
        line = line.strip()             # Strip white space from front and end
        if line != ""   and  line[0] != '#': # If it's not a comment...
            program.append(line)        # ... then it's part of the program
    f.close()
    return program

def convertStringToProgram(s):
    """Convert the string "s" to the internal representation of a program.
       This function is not used by Hmmm itself, but is available to programs
       that wish to import Hmmm and use it internally."""
    program = []
    linesOfString = s.split("\n")
    for line in linesOfString:
        if line == "":
            continue
        line = line.strip()             # Strip white space from front and end
        if line != ""   and  line[0] != '#': # If it's not a comment...
            program.append(line)        # ... then it's part of the program
    return program

def isMachineCode(program):
    """Returns True if the program appears to be machine code, False if it
       appears to be Hmmm source code."""
    return re.match(r'([01]{4} ){3}[01]{4}$', program[0]) is not None

def writeMachineCode(machineCode, filename):
    """Write the internal representation of machine code to a file."""
    f = open(filename, "w")
    for triplet in machineCode:
        f.write(triplet[1] + "\n")

def programToMachineCode(program):
    """Convert the result of an assembled program into internal machien code."""
    return [triplet[1] for triplet in program]

def hmmmAssembler(program):
    """Assemble the given program and return it as a string.  If an assembly
       error occurs, returns None.  Error messages are printed directly to
       stdout (this is because the program listing also goes to stdout)."""
    machineCode = assemble(program)

    # check whether there are any errors
    failure = False
    for triplet in machineCode:
        if triplet[1][0] == '*':
            failure = 1
            break
    if failure:
        print("\n***** ASSEMBLY TERMINATED UNSUCCESSFULLY *****")
        print("              ASSEMBLY RESULTS:\n")
    else:
        print("\n" + "-"*22)
        print("| ASSEMBLY SUCCESSFUL |")
        print("-"*22 + "\n")
    try:
        nWidth = max([len(str(x[0])) for x in machineCode])
    except ValueError:
        print("                <EMPTY PROGRAM>\n")
        return None
    # Create a format for the output.
    fmt = "{:<" + str(nWidth) + "}: {:<31} {}"
    for triplet in machineCode:
        # Print each line with tabs expanded, and with the width limited
        # to outputLineMax.
        line = fmt.format(triplet[0], triplet[1], triplet[2].expandtabs())
        print(line[:outputLineMax])
    print("")
    if failure:
        print("***** ASSEMBLY FAILED, SEE ABOVE FOR ERRORS *****")
        return None
    else:
        return machineCode

######################################################################
######################################################################
#
# HMMM SIMULATOR
#
######################################################################
######################################################################

memory = [0]*256        # 256 words of memory.  Instructions are represented
                        # ..in string form; data is integer
registers = [0]*16      # 16 integer registers
pc = 0                  # program counter initialized to 0
instruction = 0         # instruction register
debug = False           # debug mode?
ask = True              # for fast debug mode
lastPC = 0              # where the program counter was 1 instruction ago
codeSize = 0            # can't execute past this or read/write before this
displayNext = 1         # display next instruction?

def validInteger(x):
    if type(x) == int:
        return -32768 <= x <= 32767
    else:
        return False

def disassemble(line):
    """Disassemble a binary line, returning a 3-element tuple.  The
       first tuple element is a string giving the assembly code, the
       second is the mnemonic opcode alone, and the third is a list of
       arguments, if any, in binary encoding.  Failures result in an
       error tuple."""
    if type(line) != type(''):
        return ('***UNTRANSLATABLE INSTRUCTION!***', '***UNTRANSLATABLE***', \
          [])
    hex = int(line.replace(' ', ''), 2)
    for tuple in opcodes:
        proto = int(tuple[0].replace(' ', ''), 2)
        mask = int(tuple[1].replace(' ', ''), 2)
        if hex & mask == proto:
            # We have found the proper instruction.  Decode the arguments.
            opcode = tuple[2]
            translation = opcode
            hex <<= 4
            args = []
            separator = ' '
            for arg in arguments[opcode]:
                # r s u n z
                if arg == 'r':
                    val = (hex & 0xf000) >> 12
                    translation += separator + 'r' + str(val)
                    separator = ', '
                    hex <<= 4
                    args += [val]
                elif arg == 'z':
                    hex <<= 4
                elif arg == 's'  or  arg == 'u':
                    val = (hex & 0xff00) >> 8
                    if arg == 's'  and  (val & 0x80) != 0:
                        val -= 256
                    translation += separator + str(val)
                    separator = ', '
                    hex <<= 8
                    args += [val]
                elif arg == 'u':
                    val = (hex & 0xff00) >> 8
                    translation += separator + str(val)
                    separator = ', '
                    hex <<= 8
                    args += [val]
                elif arg == 'n':
                    # In the absence of other information, always unsigned
                    val = hex & 0xffff
                    translation += separator + str(val)
                    separator = ', '
                    hex <<= 16
                    args += [val]
            return (translation, opcode, args)
    return ('***UNTRANSLATABLE INSTRUCTION!***', '***UNTRANSLATABLE***', [])

def simulationError(message):
    """Issue an error message (to stdout) and halt program execution."""
    print("\n\n")
    print(message)
    print("Halting program execution.")
    sys.exit(1)

def validPC(pc):
    return 0 <= pc < codeSize

def validAddr(addr):
    return codeSize <= addr < 256

def runHmmm():
    """Execute a program that has previously been loaded into Hmmm's memory."""
    global pc, instruction, memory, loop_check, lastPC, codeSize
    while pc != -1:         # fetch/execute cycle
        if not validPC(pc):
            simulationError("Memory Out of Bounds Error.\n"
              + "Program attempted to execute memory location " + str(pc))
        instruction = memory[pc]
                            # Fetch and store into instruction register
        lastPC = pc
        pc = pc+1           # increment pc
        try:
            execute(instruction)
        except KeyboardInterrupt:
            print("\n\nInterrupted by user, halting program execution...\n")
            sys.exit()
        except EOFError:
            print("\n\nEnd of input, halting program execution...\n")
            sys.exit()

def checkOverflow(register, instruction, lastPC):
    """Check a register value for overflow; if it is illegal issue error
       information, including a disassembly of the offending instruction,
       to stdout."""
    if not validInteger(register):
        parts = instruction.split()
        translation, opcode, args = disassemble(memory[lastPC])
        print("\n  Program Counter:", lastPC)
        print("  Instruction: {}   Arguments: {}".format(
          opcode,", ".join(parts[1:])))
        print("  Translation:", translation, end=' ')
        simulationError( \
          "Integer Overflow Error: Result " + str(register) \
            + " was larger than 16 bits.\n")

def debugMode():
    """Implement debugging mode."""
    global memory, registers, pc, debug, ask
    if not debug  or  not ask:
        return
    while True:
        command = input("\nDebugging Mode Command (h for help): ")
        if command in ("c", "continue"):
            ask = False
            return
        elif command in ("d", "dump"):
            print("Memory Contents:")
            for addr in range(codeSize):
                print('{:3d}: {}'.format(addr, memory[addr]))
            c_len = (len(memory) - codeSize + 5) // 6
            for i in range(c_len):
                try:
                    for addr in range(codeSize + i,
                            codeSize + i + 6 * c_len, c_len):
                        print('{:3d}: {:<7d}'.format(addr,
                            memory[addr]),
                          end = ' ')
                except IndexError:
                    pass
                print("")
        elif command in ("h", "help"):
            print("\nDebugging Mode Commands:")
            print("  'c' or 'continue': run through the rest of the program"
              + " (in debugging mode)")
            print("  'd' or 'dump': print the non-empty portions of memory")
            print("  'h' or 'help': display this message")
            print("  'p' or 'print': print the contents of the registers")
            print("  'q' or 'quit': halt the program and exit")
            print("  'r' or 'run': run through the rest of the program"
              + " (exit debugging mode)")
            print("  default: execute the next instruction")
        elif command in ("p", "print"):
            print("Registers:")
            for i in range(len(registers)):
                print("  {:2d}: {}".format(i, registers[i]))
            print("")
        elif command in ("q", "quit"):
            print("Aborting Program...")
            sys.exit()
        elif command in ("r", "run"):
            print("Continuing program...")
            debug = False
            return
        else:
            return

#
# Hmmm instruction implementations.  These must precede the instruction
# dispatch table, since the functions are referenced there.
#
def op_halt(args):
    global debug, pc
    pc = -1                 # This terminates the run loop
    if debug:
        print("halt\n")

def op_read(args):
    global registers
    try:
        sys.stdout.flush()
        sys.stderr.flush()
    except:
        # If those can't be flushed, no problem... .
        # I think those lines help in IDLE, but
        # break the code at the terminal, so perhaps
        # this try/except approach will make it work
        # in both situations!
        pass

    while True:
        userInput = input("Enter number (q to quit): ")
        if userInput == 'q':
            sys.exit()
        try:
            registers[args[0]] = int(userInput)
            if validInteger(registers[args[0]]):
                break
        except ValueError:
            pass
        print("\nIllegal input: number must be in [-32768,32767]\n")

def op_write(args):
    global registers
    print(registers[args[0]])

def op_jumpr(args):
    global registers, pc, lastPC
    pc = registers[args[0]]
    if not validPC(pc):
        simulationError("Invalid jump target at pc " + str(lastPC) \
          + ": " + str(pc))

def op_setn(args):
    global registers
    registers[args[0]] = args[1]

def op_loadn(args):
    global registers, memory, lastPC
    if not validAddr(args[1]):
        simulationError("Invalid load target at pc " + str(lastPC) \
          + ": " + str(args[1]))
    registers[args[0]] = memory[args[1]]

def op_storen(args):
    global registers, memory, lastPC
    if not validAddr(args[1]):
        simulationError("Invalid store target at pc " + str(lastPC) \
          + ": " + str(args[1]))
    memory[args[1]] = registers[args[0]]

def op_loadr(args):
    global registers, memory, lastPC
    if not validAddr(registers[args[1]]):
        simulationError("Invalid load target at pc " + str(lastPC) \
          + ": " + str(registers[args[1]]))
    registers[args[0]] = memory[registers[args[1]]]

def op_storer(args):
    global registers, memory, lastPC
    if not validAddr(registers[args[1]]):
        simulationError("Invalid store target at pc " + str(lastPC) \
          + ": " + str(registers[args[1]]))
    memory[registers[args[1]]] = registers[args[0]]

def op_popr(args):
    global registers, memory, lastPC
    registers[args[1]] -= 1
    if not validAddr(registers[args[1]]):
        simulationError("Invalid pop target at pc " + str(lastPC) \
          + ": " + str(registers[args[1]]))
    registers[args[0]] = memory[registers[args[1]]]

def op_pushr(args):
    global registers, memory, lastPC
    if not validAddr(registers[args[1]]):
        simulationError("Invalid push target at pc " + str(lastPC) \
          + ": " + str(registers[args[1]]))
    memory[registers[args[1]]] = registers[args[0]]
    registers[args[1]] += 1

def op_addn(args):
    global registers, instruction, lastPC
    registers[args[0]] += args[1]
    checkOverflow(registers[args[0]], instruction, lastPC)

def op_add(args):
    global registers, instruction, lastPC
    registers[args[0]] = registers[args[1]] + registers[args[2]]
    checkOverflow(registers[args[0]], instruction, lastPC)

def op_copy(args):
    op_add(args + [0])

def op_nop(args):
    op_add([0, 0, 0])

def op_sub(args):
    global registers, instruction, lastPC
    registers[args[0]] = registers[args[1]] - registers[args[2]]
    checkOverflow(registers[args[0]], instruction, lastPC)

def op_neg(args):
    op_sub([args[0], 0, args[1]])

def op_mul(args):
    global registers, instruction, lastPC
    registers[args[0]] = registers[args[1]] * registers[args[2]]
    checkOverflow(registers[args[0]], instruction, lastPC)

def op_div(args):
    global registers, lastPC
    try:
        registers[args[0]] = registers[args[1]] // registers[args[2]]
    except ZeroDivisionError:
        simulationError("Division by Zero Error at pc " + str(lastPC) + ".")

def op_mod(args):
    global registers
    try:
        registers[args[0]] = registers[args[1]] % registers[args[2]]
    except ZeroDivisionError:
        simulationError("Division by Zero Error at pc " + str(lastPC) + ".")

def op_calln(args):
    global registers, pc, lastPC
    registers[args[0]] = pc
    pc = args[1]
    if not validPC(pc):
        simulationError("Invalid jump/call target at pc " + str(lastPC) \
          + ": " + str(pc))

def op_jumpn(args):
    op_calln([0] + args)

def op_jeqzn(args):
    global registers, pc, lastPC
    if registers[args[0]] == 0:
        pc = args[1]
    if not validPC(pc):
        simulationError("Invalid jump target at pc " + str(lastPC) \
          + ": " + str(pc))

def op_jltzn(args):
    global registers, pc, lastPC
    if registers[args[0]] < 0:
        pc = args[1]
    if not validPC(pc):
        simulationError("Invalid jump target at pc " + str(lastPC) \
          + ": " + str(pc))

def op_jgtzn(args):
    global registers, pc, lastPC
    if registers[args[0]] > 0:
        pc = args[1]
    if not validPC(pc):
        simulationError("Invalid jump target at pc " + str(lastPC) \
          + ": " + str(pc))

def op_jnezn(args):
    global registers, pc, lastPC
    if registers[args[0]] != 0:
        pc = args[1]
    if not validPC(pc):
        simulationError("Invalid jump target at pc " + str(lastPC) \
          + ": " + str(pc))

def op_unimp(args):
    global lastPC, instruction
    simulationError("Unimplemented opcode at pc " + str(lastPC) + ": "
      + instruction[0])

#
# Instruction dispatch table.  This table pairs each opcode with the
# function that implements it.
#
# We take advantage of Python introspection here.  The following loop
# walks through the opcode table.  For each entry in that table, we
# look up the corresponding function in Python's globals table and
# enter it into the implementations dictionary.  The result is that
# implementations contains things like {'add': op_add, ...}.
#
implementations = {}
for triplet in opcodes:
    op = triplet[2]
    func = 'op_' + op
    if func in globals():
        implementations[op] = globals()[func]
    else:
        implementations[op] = op_unimp

def execute(instruction):
    """Execute a single Hmmm instruction.  As part of that, offer the
       debugging menu."""
    global memory, registers, pc, debug, ask, lastPC

    if instruction == "" or validInteger(instruction):
        simulationError("Bad instruction at memory location " + lastPC)

    parts = instruction.split()      # parse instruction

    # Do debug mode, if needed
    debugMode()

    # Disassemble the current instruction in case we need its information
    translation, opcode, args = disassemble(memory[lastPC])

    if debug:  # this is necessary because of the 'run' command
        print("\n  Program Counter:", lastPC)
        print("  Instruction:", opcode, "  Arguments:", ", ".join(parts[1:]))
        print("  Translation:", translation)
        if displayNext:
            print("  Next Target:", pc)
            print("  Next Instruction:", disassemble(memory[pc])[0], "\n")

    # Register 0 is always forced to zero
    registers[0] = 0

    if opcode in implementations:
        implementations[opcode](args)
    else:
        simulationError("Invalid operation code at pc " + str(pc))

    # Re-force register 0 to zero so register dumps will be correct.
    registers[0] = 0

def convertMachineCode(program):
    """Convert the machine-coded string in "program" into a program
       in memory."""
    global memory, codeSize
    address = 0
    for line in program:
        for c in line:
            if c not in "01 \n":
                print("\nERROR: Not a valid binary file.\n")
                sys.exit(1)
        if line == "":
            break
        memory[address] = line
        address +=  1
    codeSize = address
    if codeSize == 0:
        print("\nERROR: Empty file.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()

# $Log: hmmm,v $
# Revision 2.5  2018-02-22 19:18:43-08  geoff
# REmove the -n (--no-debug) switch.  Now the only way to get debugging
# is to run hmmm with the -d or --debug switch; it never prompts to ask
# whether to enter debugging mode.
#
# Revision 2.4  2018-02-22 18:38:48-08  geoff
# Rename run to runHmmm so that it doesn't interfere with iPython's run
# command.  Add a hmmm() function that can be used to re-invoke hmmm without
# re-running it.
#
# Revision 2.3  2017-03-06 16:46:50-08  geoff
# Add minimal support for systems that don't have docopt.  Also change
# the name of the argument dictionary in main so it doesn't collide with
# the "arguments" global.
#
# Revision 2.2  2016-11-27 15:40:21-08  geoff
# Add pushr and popr to the instruction set.  As part of that, dynamically
# generate the implementations table so it doesn't have to be kept consistent
# by hand.  Also fix a couple of bugs: calling main with a program-as-string
# argument didn't work, and the --debug and --no-debug switches didn't work.
#
# Revision 2.1  2016-11-23 16:53:30-08  geoff
# Initial revision
#
#
# ***Old RCS log from hmmmAssembler.py:
#
# Revision 1.7  2016-11-12 15:04:48-08  geoff
# Explicitly invoke Python3.  Get rid of reload; it's not needed.  Get
# rid of some odd stylistic quirks.
#
# Revision 1.6  2016-11-12 14:03:31-08  geoff
# Convert to Python3 (using 2to3)
#
# Revision 1.5  2016-11-12 13:41:04-08  geoff
# Revisions (made in 2012) to the instruction set to make it more
# beginner-friendly.  In particular, any instruction that uses a
# constant in the instruction now has a "n" suffix; anything that uses a
# value from a register has "r".  "Mov" becomes "copy", which is what it
# actually does.  This version sort of supports the pre-2012 instruction
# set as well as the newer one (but you have to change the code to do
# so).  Add code to allow assembly and execution in the same run.
#
# Revision 1.5 2012/06/18 1:52:30 kaya
# Rewrote HMMM assembly code. New shortcuts can be found on the HMMM Directory page.
# Included dictionary so the program can be run in old or new mode, as internal commands
# remain unaltered.
#
# Revision 1.4  2007/10/08 08:10:11  geoff
# Add support for the neg instruction.  This required generalizing the
# "z" operand specifier.  Also get rid of the obsolete version of the
# opcodes table, which I neglected to delete earlier.
#
# Revision 1.3  2007/10/07 09:18:58  geoff
# Fix the masks on mov and data to correctly reflect the format of those
# two pseudo-operations.
#
# Revision 1.2  2007/10/07 07:47:14  geoff
# Major changes to improve the instruction architecture.  Unfortunately,
# as part of these changes I converted all tabs to blanks, so there are
# spurious diffs.  Modifications include:
#
# 1. Better table-driven encoding unified with simulator encoding tables.
# 2. Major rewrite of assembly code to use tables rather than if/elif.
#
# ***Old RCS log from hmmmSimulator.py:
#
# Revision 1.9  2016-11-12 15:04:48-08  geoff
# Explicitly invoke Python3.  Get rid of reload; it's not needed.  Get
# rid of some odd stylistic quirks.  Rewrite the input loop for the read
# instruction to use try/except.
#
# Revision 1.8  2016-11-12 14:04:32-08  geoff
# Fix valid_integer to reject non-integral types
#
# Revision 1.7  2016-11-12 14:03:31-08  geoff
# Convert to Python3 (using 2to3)
#
# Revision 1.6  2016-11-12 13:44:35-08  geoff
# Don't flush stdin, and get rid of some weird style quirks
#
# Revision 1.5  2016-11-12 13:41:04-08  geoff
# Revisions (made in 2012) to the instruction set to make it more
# beginner-friendly.  In particular, any instruction that uses a
# constant in the instruction now has a "n" suffix; anything that uses a
# value from a register has "r".  "Mov" becomes "copy", which is what it
# actually does.  Also improve a lot of error messages; ignore errors
# when flushing streams; don't use "file" as a variable name; assume
# output goes to "out.b".
#
# Revision 1.4  2007/10/08 08:10:12  geoff
# Add support for the neg instruction.
#
# Revision 1.3  2007/10/07 09:18:58  geoff
# Fix the masks on mov and data to correctly reflect the format of those
# two pseudo-operations.
#
# Revision 1.2  2007/10/07 07:47:14  geoff
# Major changes to improve the instruction architecture.  Unfortunately,
# as part of these changes I converted all tabs to blanks, so there are
# spurious diffs.  Modifications include:
#
# 1. Table-driven decoding unified with assembler encoding tables.
# 2. Error-checking and error-reporting functions to simplify the code.
# 3. Complete rewrite/replacement of disassembly/decoding.
# 4. Execute function rewritten to simplify structure and reflect new
#    architecture.
#
