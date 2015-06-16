# -*- coding: utf-8 -*-
#    _ ____       Instituto Federal de
#   (_) __/        Educação, Ciência e
#  / / _/          Tecnologia do Ceará
# /_/_/   COMPILADOR/SIMULADOR NEANDER
# +------------------------------------------+
# |         ARQUITETURA NEANDER              |
# +---------+---------+----------------------+
# | OPCODE  |INSTRUCAO|     EFEITO           |
# +---------+---------+----------------------+
# 0b00000000, NOP    , no operation          |
# 0b00010000, STA end, MEM[end] <- AC        |
# 0b00100000, LDA end, AC <- MEM[end]        |
# 0b00110000, ADD end, AC <- MEM[end] + AC   |
# 0b01000000, OR  end, AC <- MEM[end] OR AC  |
# 0b01010000, AND end, AC <- MEM[end] AND AC |
# 0b01100000, NOT    , AC <- NOT AC          |
# 0b01110000, SUB end, AC <- MEM[end] - AC   |
# 0b10000000, JMP    , PC <- end             |
# 0b10010000, JN  end, IF N=1: PC <- end     |
# 0b10100000, JZ  end, IF Z=1: PC <- end     |
# 0b10110000, JNZ end, IF Z=0: PC <- end     |
# 0b11000000, IN  end,                       |
# 0b11010000, OUT end,                       |
# 0b11100000, LDI val, AC <- val             |
# 0b11110000, HLT    , halt                  |
# -------------------------------------------+

_mnemonics = ['NOP', 'STA', 'LDA', 'ADD', 'OR', 'AND', 'NOT', 'SUB', 'JMP', 'JN', 'JZ', 'JNZ', 'IN', 'OUT', 'LDI', 'HLT']
_opcodes = dict(zip(_mnemonics, [k<<4 if _mnemonics[k]!='' else -1 for k in range(len(_mnemonics))]))
_internals = ['EQU', 'ORG']
_AC = 0
_PC = 0
_flags=type('Enum',(),{'Z':0,'N':0})
_MEMORIA = [0] * 256
_VARIAVEIS={}
_arquivo = lambda(x): open(x,'r').read()

def _compila(_dado):
  global _MEMORIA
  global _opcodes
  global _internals
  global _VARIAVEIS
  _indice=0
  _instrucoes = _dado.split('\n')
  for _linha in _instrucoes:
    if len(_linha)!=0:
      _i = _linha.split(' ')
      if _i[0] in _internals:
        if _i[0]==_internals[1] and len(_i)==2: # ORG
          _indice = int(_i[1])
        else:
          print "[ERRO 0x01] Funcao inexistente. Seguindo..."
      elif _i[0] in _mnemonics: # ############ FUNCOES ######
        if _i[0]==_mnemonics[0x00]: # NOP
          _MEMORIA[_indice]=_opcodes[_i[0]]
        if _i[0]==_mnemonics[0x01]: # STA
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x02]: # LDA
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x03]: # ADD
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x04]: # OR
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x05]: # AND
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x06]: # NOT
          _MEMORIA[_indice]=_opcodes[_i[0]]
        if _i[0]==_mnemonics[0x07]: # SUB
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x08]: # JMP
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x09]: # JN
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x0a]: # JZ
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x0b]: # JNZ
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x0c]: # IN
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x0d]: # OUT
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x0e]: # LDI
          _MEMORIA[_indice]=_opcodes[_i[0]]
          _indice+=1
          if _i[1].isdigit(): # --- valor direto
            _MEMORIA[_indice]=int(_i[1])
          else: # ----------------- variavel
            _MEMORIA[_indice]=_VARIAVEIS[_i[1]]
        if _i[0]==_mnemonics[0x0f]: # HLT
          _MEMORIA[_indice]=_opcodes[_i[0]]
        else:
          pass
        _indice+=1
      elif _i[0].isdigit():
        print "[ERRO 0x02] variavel nao pode iniciar por numero"
      else:
        if len(_i)==3 and _i[1]==_internals[0] and _i[2].isdigit(): # EQU
          _VARIAVEIS[_i[0]]=int(_i[2])
        else:
          print "[ERRO 0x03] Esta chamada esta incorreta"

def _executa(_debug=False):
  global _PC
  global _AC
  global _MEMORIA
  global _opcodes
  global _flags
  _PC=0
  while 1:
    _atual = int(_MEMORIA[_PC]) >> 4
    if _atual==0x00:   # NOP
      pass
    elif _atual==0x01: # STA
      _PC+=1
      _MEMORIA[int(_MEMORIA[_PC])]=int(_AC)
    elif _atual==0x02: # LDA
      _PC+=1
      _AC=int(_MEMORIA[_MEMORIA[_PC]])
    elif _atual==0x03: # ADD
      _PC+=1
      _AC+=int(_MEMORIA[_MEMORIA[_PC]])
    elif _atual==0x04: # OR
      _PC+=1
      _AC|=int(_MEMORIA[_PC])
    elif _atual==0x05: # AND
      _PC+=1
      _AC&=int(_MEMORIA[_PC])
    elif _atual==0x06: # NOT
      _AC=~_AC
    elif _atual==0x07: # SUB
      _PC+=1
      _AC-=int(_MEMORIA[_MEMORIA[_PC]])
    elif _atual==0x08: # JMP
      _PC+=1
      _PC+=int(_MEMORIA[_PC])
    elif _atual==0x09: # JN
      _PC+=1
      if _flags.N==1:
        _PC+=int(_MEMORIA[_PC])
    elif _atual==0x0a: # JZ
      _PC+=1
      if _flags.Z==1:
        _PC+=int(_MEMORIA[_PC])
    elif _atual==0x0b: # JNZ
      _PC+=1
      if _flags.Z==0:
        _PC+=int(_MEMORIA[_PC])
    elif _atual==0x0c: # IN
      pass
    elif _atual==0x0d: # OUT
      pass
    elif _atual==0x0e: # LDI
      _PC+=1
      _AC=int(_MEMORIA[_PC])
    elif _atual==0x0f: # HLT
      break
    else:
      print '[ERRO 0x04] OPCODE desconhecido %d' % _atual
      break
    _flags.Z = (0,1)[_AC==0]
    _flags.N = (0,1)[_AC<0]
    _PC+=1
    if _debug:
      _hexdump()

def _hexdump():
  global _PC
  global _AC
  global _MEMORIA
  global _flags
  _end=0
  _hex='%04x  ' % _end
  for i in range(len(_MEMORIA)):
    _hex += '%02x ' % _MEMORIA[i]
    if (i+1)>0 and (i+1)%16==0 and (i+1)<len(_MEMORIA):
      _end+=16
      _hex +='\n%04x  ' % _end
  print 'ENDR  -- -- -- -- -- -- - MEMORIA - -- -- -- -- -- --'
  print _hex
  print '      AC=%d    PC=%d    Z=%d    N=%d\n' % (_AC, _PC, _flags.Z, _flags.N)


from optparse import OptionParser
import sys
desc='Compilador e simulador de assembly para arquitetura NEANDER. Usado na disciplina de Arquitetura de Computadores no IFCE.'
uso='%prog [opcoes] arquivo.asm / -'
parser = OptionParser(usage=uso, version="%prog IFCE-0.3-alpha", description=desc)
parser.add_option('-d', '--debug', action='store_true', dest='debug', help='Habilita o modo de depuracao')
parser.add_option('-f', '--file', dest='arquivo', help='Arquivo contendo assembly neander. Use - para redirecionar por pipe/usar stdin.')

(opts,args)=parser.parse_args()

if opts.arquivo:
  if opts.arquivo == '-':
    infile = sys.stdin.read()
  else:
    infile = open(opts.arquivo, "r").read()
  _compila(infile)
  _executa(opts.debug)
  _hexdump()
else:
  print 'Nenhum arquivo para ler.\n-h para ajuda.'
  exit(0)
