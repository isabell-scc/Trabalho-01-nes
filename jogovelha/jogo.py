import numpy as np

class Tabuleiro:
    def __init__(self) -> None:
        """Inicializa um tabuleiro vazio.
        """
        #Lista com 9 casa vazias
        self.casas = [' '] * 9

    def pegar_tabuleiro(self) -> list[list[str]]:
        """Retorna o tabuleiro como uma lista de listas.
        """
        lista_tab = []
        for i in range(0,9,3):
            linha = [self.casas[i],self.casas[i+1] ,self.casas[i+2]]
            lista_tab.append(linha)
        return lista_tab

    def marcar_casa(self, linha: int, coluna: int, simbolo: str) -> bool:
        """Marca uma casa no tabuleiro, com o símbolo especificado.
        Retorna True se a casa foi marcada com sucesso, False caso já esteja marcada.

        Args:
            linha (int): A linha da casa a ser marcada.
            coluna (int): A coluna da casa a ser marcada.
            simbolo (str): O símbolo que vai ser usado para marcar a casa.
        """
        #Transforma os valores de linha e coluna, no indíce para o tabuleiro,Já que ele pode ser acessado por indices de 0 a 8 
        index = linha * 3 + coluna
        if self.casas[index] != ' ':
            print("Essa casa já foi marcada, escolha outra.")
            return False
        else:
            self.casas[index] = simbolo
            return True

    def imprimir_tabuleiro(self) -> None:
        """Imprime o tabuleiro para o usuário.
        """
        for i in self.pegar_tabuleiro():
            print(f"{i[0]} | {i[1]} | {i[2]}")
        print("*********************************")


class Jogador:
    def __init__(self, simbolo: str) -> None:
        """Inicializa a classe Jogador.

        Args:
            simbolo (str): O símbolo que o jogador vai usar para marcar casas,que o representa.
        """
        self.simbolo = simbolo

    def fazer_jogada(self, tabuleiro: Tabuleiro) -> tuple[int, int]:
        """Faz a jogada do jogador.

        Args:
            tabuleiro (Tabuleiro): O tabuleiro do jogo.

        Returns:
            tuple[int, int]: Uma tupla contendo a linha e a coluna da casa escolhida.
        """
        pass


class JogadorHumano(Jogador):
    def fazer_jogada(self, tabuleiro: Tabuleiro) -> tuple[int, int]:
        """Faz a jogada do jogador humano.
        """
        print(f"É a vez do jogador {self.simbolo}.")
        while True:
            linha = int(input("Digite a linha na qual você quer marcar (0-2): "))
            coluna = int(input("Digite a coluna na qual que você quer marcar (0-2): "))
            #Verificando se os valores estão dentro do intervalo correto e se a  casa escolhida está livre
            if 0 <= linha <= 2 and 0 <= coluna <= 2:
                if tabuleiro.marcar_casa(linha, coluna, self.simbolo):
                 return (linha,coluna)
                else:
                    print("Essa casa já foi marcada, escolha outra.")
                    continue
            else:
                print("Os valore de linha e coluna devem estar entre 0 e 2.")


class JogadorComputador(Jogador):
    def __init__(self, simbolo: str, estrategia: str = "aleatória")-> None:
        """Inicializa a classe JogadorComputador.

        Args:
            simbolo (str): O símbolo que o jogador vai usar para marcar casas,que o representa.
            estratégia (str, optional): A estratégia do computador,que por padrão é "aleatória".
        """
        super().__init__(simbolo)
        self.estratégia = estrategia
        if self.estratégia != "aleatória":
            raise ValueError("Essa estratégia não e válida, tente usar: 'aleatória'")

    def fazer_jogada(self, tabuleiro: Tabuleiro) -> tuple[int, int]:
        """Faz a jogada do jogador robô.
        """
        while True:
            #Irá escolher valores aleatórios de 0 a 2 para linha e coluna
            linha = np.random.randint(0, 3)
            coluna = np.random.randint(0, 3)

            #Verificando se as casas estão livres
            if tabuleiro.marcar_casa(linha, coluna, self.simbolo):
                return (linha,coluna)

class JogoVelha:
    def __init__(self, jogador1: Jogador, jogador2: Jogador) -> None:
        """Inicializa a classe JogoVelha.

        Args:
            jogador1 (Jogador): O primeiro jogador, que irá começar.
            jogador2 (Jogador): O segundo jogador.
        """
        self.jogadores = [jogador1, jogador2]
        #Instanciando um objeto Tabuleiro dentro de JogoVelha
        self.tabuleiro = Tabuleiro()
        self.turno_atual = 0

    def jogador_atual(self) -> Jogador:
        """Retorna o jogador que irá fazer a jogada da classe Jogador
        """
        #Como o turno é zero, retorna o jogador 1
        return self.jogadores[self.turno_atual]

    def jogar(self) -> None:
        """Inicia o jogo.
        """
        print("Vamos começar o jogo!")
        while True:
            jogador = self.jogador_atual()
            (linha,coluna) = jogador.fazer_jogada(self.tabuleiro)
            print(f" O Jogador {jogador.simbolo} jogou em ({linha}, {coluna}):\n")
            #Imprimindo o tabuleiro após a jogada
            self.tabuleiro.imprimir_tabuleiro()

            resultado = self.checar_fim_de_jogo()
            if resultado:
                print(resultado)
                break
             #Muda o jogador da vez, ser era 0, retorna 1 e vice-versa
            self.turno_atual = (self.turno_atual + 1) % 2  # Alterna o turno

    def checar_fim_de_jogo(self):
        """Verifica se o jogo acabou, ou seja se houve um vencedor ou se deu empate.
        """
         #Verificando as linhas horizontais
        if self.tabuleiro.casas[0] == self.tabuleiro.casas[1] == self.tabuleiro.casas[2] != ' ':
            return f" O jogador {self.tabuleiro.casas[0]} venceu!"
        elif self.tabuleiro.casas[3] == self.tabuleiro.casas[4] == self.tabuleiro.casas[5] != ' ':
            return f" O jogador {self.tabuleiro.casas[3]} venceu!"
        elif self.tabuleiro.casas[6] == self.tabuleiro.casas[7] == self.tabuleiro.casas[8] != ' ':
            return f" O jogador {self.tabuleiro.casas[6]} venceu!"

        #Verificando as linhas Verticais
        if self.tabuleiro.casas[0] == self.tabuleiro.casas[3] == self.tabuleiro.casas[6] != ' ':
            return f" O jogador {self.tabuleiro.casas[0]} venceu!"
        if self.tabuleiro.casas[1] == self.tabuleiro.casas[4] == self.tabuleiro.casas[7] != ' ':
            f" O jogador {self.tabuleiro.casas[1]} venceu!"
        if self.tabuleiro.casas[2] == self.tabuleiro.casas[5] == self.tabuleiro.casas[8] != ' ':
            return f" O jogador {self.tabuleiro.casas[2]} venceu!"

        #Verificando as diagonais
        if self.tabuleiro.casas[0] == self.tabuleiro.casas[4] == self.tabuleiro.casas[8] != ' ':
            return f" O jogador {self.tabuleiro.casas[0]} venceu!"
        elif self.tabuleiro.casas[2] == self.tabuleiro.casas[4] == self.tabuleiro.casas[6] != ' ':
            return f" O jogador {self.tabuleiro.casas[2]} venceu!"

        #Verificando empate:
        if all(casa != ' ' for casa in self.tabuleiro.casas):
            return "O jogo empatou!"
        return None
