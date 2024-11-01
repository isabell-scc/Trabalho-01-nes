# Jogo da velha

Um jogo da velha tradicional, com a opção de jogar com um 'robô'.

## Instalação

Para instalar, execute:

```
python setup.py install
```

## Uso

Exemplo de uso:

```py
from jogovelha import JogoVelha, JogadorHumano, JogadorComputador, Tabuleiro

#Função para iniciar o jogo, definindo, cada componente
def comecar_jogo():
    jogador1 = JogadorHumano('X')
    jogador2 = JogadorComputador('O')
    jogo = JogoVelha(jogador1, jogador2)
    jogo.jogar()

# Inicia o jogo 
comecar_jogo()
```