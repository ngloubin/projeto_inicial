# Space Invaders Versão Ngloubin

## Descrição

Space Invaders do Matheus N é um jogo clássico de tiro no estilo Space Invaders, desenvolvido com Pygame. O jogo apresenta uma série de inimigos que o jogador deve destruir com lasers enquanto evita ser atingido.

## Estrutura do Projeto

O projeto é modularizado para facilitar a manutenção e o desenvolvimento. A estrutura de diretórios é a seguinte:

```bash
projeto_inicial/
├── space_invaders/
│   ├── __init__.py
│   ├── assets.py
│   ├── entities.py
│   ├── settings.py
│   ├── utils.py
│   └── main.py
└── assets/
    ├── pixel_ship_red_small.png
    ├── pixel_ship_green_small.png
    ├── pixel_ship_blue_small.png
    ├── pixel_ship_yellow.png
    ├── pixel_laser_red.png
    ├── pixel_laser_green.png
    ├── pixel_laser_blue.png
    ├── pixel_laser_yellow.png
    └── background-black.png
└── sounds/
    ├── space-laser.mp3
    └── explosion.mp3
```
## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/space_invaders.git
   cd space_invaders
    ```

- Instale as dependências usando o Poetry:

Primeiro, certifique-se de ter o Poetry instalado. Caso não tenha, instale-o seguindo as instruções em Poetry.

Em seguida, instale as dependências:
```bash
peotry install
```
## Execução do Jogo
Para iniciar o jogo, execute o comando:
```bash
poetry run python main.py
```