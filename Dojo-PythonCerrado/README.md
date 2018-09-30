# Coding Dojo UnB

## Problema: Interpretador de BrainFuck

Brainfuck é uma linguagem de programação cujo funcionamento é muito parecido com uma máquina de Turing. Essa máquina possui como componentes um vetor de 30000 bytes, indexado de 0 a 29999, e um ponteiro, que guarda uma posição desse vetor. Cada célula do vetor irá guardar um valor inteiro, que faz correspondência com um caractere da [Tabela ASCII](http://www.asciitable.com/). Em cada passo, a máquina realiza uma instrução de acordo com o byte armazenado na posição do vetor indicada pelo ponteiro.  

O conjunto de instruções válidas da linguagem é o seguinte:

Instrução | Descrição
------------|-------------
"<" | Incrementa o ponteiro.
">" | Decrementa o ponteiro.
"+" | Incrementa o byte na posição indicada pelo ponteiro.
"–" | Decrementa o byte na posição indicada pelo ponteiro.
"," | Lê um byte e armazena na posição indicada pelo ponteiro. Se não houver nada que possa ser lido (entrada acabou), armazenar zero.
"." | Imprime o valor do byte na posição indicada pelo ponteiro.
"[" | Início do loop: Executa o código delimitado até que o byte na posição indicada pelo ponteiro seja igual a zero.
"]" | Fim do loop: Volta para "[".

#### Informações úteis
- Brainfuck ignora qualquer caractere exceto os 8 acima
- Caso o valor do vetor na posição indicada pelo ponteiro passar de 255, volta a 0
- Caso o valor do vetor na posição indicada pelo ponteiro diminuir de 0, volta a 255

#### Casos de erro
- Comandos "[" e "]" não estão em quantidades iguais
- Ponteiro maior que 29999 ou menor que 0

#### Manipulação básica
Em Brainfuck, a memória tem estado, isto é, a cada operação o estado da memória altera-se de acordo com a ação, e todas as alterações são refletidas em operações futuras. A intenção é colocar valores em cada posição da memória com um valor inteiro correspondente a um caractere ASCII. Vamos ver um exemplo prático:

++++++++++   
++++++++++   
++++++++++    
++++++++++    
++++++++++    
++++++++++   
+++++.  

Segundo a tabela de operadores que já foi apresentada, o operador + serve para incrementar numa unidade (+1) o valor da posição atual da memória (inicializado internamente a zero). Temos então 65 operadores de incremento. Isto vai permitir colocar o valor 65 na primeira célula de memória, 65 é o valor do caractere "A" na table ASCII, a última linha contém o operador ".", que imprime o caractere correspondente, no nosso caso imprimirá a letra "A"!

Para visualizar um exemplo de como o brainfuck funciona: [Brainfuck](https://fatiherikli.github.io/brainfuck-visualizer/#KysrKysrKytbPisrKytbPisrPisrKz4rKys+Kzw8PDwtXT4rPis+LT4+K1s8XTwtXQo+Pi4+LS0tLisrKysrKysuLisrKy4+Pi48LS48LisrKy4tLS0tLS0uLS0tLS0tLS0uPj4rLj4rKy4=)


## Entregas ##


- Primeira entrega: Programa simples que aceite apenas os 6 comandos basicos +-<>,.

Casos de testes | Output
----------------|-------
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++. | A
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++<<.>.>. | ABC
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. | ZYXWVUTSRQPONMLKJIHGFEDCBA
,. | "Imprime o caracter digitado"
,-. | "Descrementa em 1 o numero digitado"
+++++Testando+++++++++++++++Outros+++++++++++++++++++++++++++++++++++++Caracteres++++++++++++++++++++++++e+++++++++.-.-.-.-.deixando.-.-.-.-.-.-a.-.-.-.-cadeia.-.-.-.-.-.-.-enorme.-.-.-. | ZYXWVUTSRQPONMLKJIHGFEDCBA


- Segunda entrega: Aceitar loops simples

Casos de testes |  Output   
----------------|---------   
++++++[>++++++++++<-]>+++++. |  A   
++++++[>++++++++++>++++++++++>++++++++++<<<-]>+++++.>++++++.>+++++++. | ABC
++++++[>++++++++++<-]>++++>++++++++++++++++++++++++++[<+.>-] | ABCDEFGHIJKLMNOPQRSTUVWXYZ
++++++++++[>++++++++>++++++++++>+++++++++++>++++++++++>++++++++++++>++++++++++>++++++++++>+++>++++++++>+++++<<<<<<<<<<-]>++++.>---.>--.>+++++.>----.>++++.>---.>++.>+++.>. | Talitha S2
,>,------------------------------------------------[<+>-]<. | "x-y"

- Terceira entrega: Aceitar loops encadeados

Casos de testes | Output
----------------|--------
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++. | Hello Word!
