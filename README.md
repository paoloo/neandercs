# neandercs
compilador / simulador de assembly para arquitetura NEANDER
===========================================================
```
Uso: neandercs.py [opcoes] -f arquivo.asm / -

Compilador e simulador de assembly para arquitetura NEANDER. Usado na
disciplina de Arquitetura de Computadores no IFCE.

Options:
  --version             Mostra versão da aplicação
  -h, --help            Mostra ajuda
  -d, --debug           Habilita o modo de depuracao
  -f ARQUIVO, --file=ARQUIVO
                        Arquivo contendo assembly neander. Use - para
                        redirecionar por pipe/stdin.

Exemplos:

$ python neandercs.py teste.asm

ou

$ echo -e 'LDI 13\nSTA 50\nLDI 20\nSTA 51\nLDI 7\nSTA 52\nLDA 52\nADD 50\nADD 51\nSTA 53\nHLT\n' | python neandercs.py -f -

```
