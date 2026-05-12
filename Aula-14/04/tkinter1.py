import pygame
import sys
import os

# 1. Configurações Iniciais
pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Login Animado - Pygame")
clock = pygame.time.Clock()

# Fontes para os textos
fonte_titulo = pygame.font.SysFont("Roboto", 32, bold=True)
fonte_input = pygame.font.SysFont("Roboto", 24)

# 2. Carregar a sua imagem (Fundo Animado)
caminho_imagem = os.path.join(os.path.dirname(__file__), "background.png")

try:
    imagem_original = pygame.image.load(caminho_imagem)
    imagem = pygame.transform.scale(imagem_original, (150, 150))
    rect_imagem = imagem.get_rect()
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")
    pygame.quit()
    sys.exit()

# 3. Variáveis de Movimento da Imagem
velocidade = [4, 4]

# 4. Variáveis da Interface de Login
# Posições dos campos (Retângulos)
painel_login = pygame.Rect(250, 120, 300, 360)
input_usuario = pygame.Rect(290, 240, 220, 35)
input_senha = pygame.Rect(290, 310, 220, 35)
botao_entrar = pygame.Rect(290, 380, 220, 40)

# Estados do teclado e strings de texto
texto_usuario = ""
texto_senha = ""
campo_ativo = None  # Pode ser 'usuario' ou 'senha'

# Cores
COR_PAINEL = (45, 45, 48, 240)    # Cinza escuro com leve transparência
COR_INPUT_PADRAO = (60, 60, 63)
COR_INPUT_ATIVO = (0, 122, 204)   # Azul destacado
COR_BOTAO = (0, 122, 204)
COR_TEXTO = (255, 255, 255)

# Loop principal
while True:
    # Captura de Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Detectar cliques do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if input_usuario.collidepoint(evento.pos):
                campo_ativo = "usuario"
            elif input_senha.collidepoint(evento.pos):
                campo_ativo = "senha"
            elif botao_entrar.collidepoint(evento.pos):
                print(f"Tentativa de Login!\nUsuário: {texto_usuario}\nSenha: {'*' * len(texto_senha)}")
            else:
                campo_ativo = None
        
        # Detectar digitação do teclado
        if evento.type == pygame.KEYDOWN and campo_ativo is not None:
            if evento.key == pygame.K_BACKSPACE:
                if campo_ativo == "usuario":
                    texto_usuario = texto_usuario[:-1]
                elif campo_ativo == "senha":
                    texto_senha = texto_senha[:-1]
            elif evento.key == pygame.K_TAB:
                campo_ativo = "senha" if campo_ativo == "usuario" else "usuario"
            elif evento.key == pygame.K_RETURN:
                print(f"Tentativa de Login!\nUsuário: {texto_usuario}\nSenha: {'*' * len(texto_senha)}")
            else:
                # Evita estourar o limite visual da caixa de texto
                if evento.unicode.isprintable():
                    if campo_ativo == "usuario" and len(texto_usuario) < 15:
                        texto_usuario += evento.unicode
                    elif campo_ativo == "senha" and len(texto_senha) < 15:
                        texto_senha += evento.unicode

    # 5. Mover a imagem de fundo
    rect_imagem = rect_imagem.move(velocidade)

    # Lógica de Colisão da Imagem (Quicar nas bordas)
    if rect_imagem.left < 0 or rect_imagem.right > largura:
        velocidade[0] = -velocidade[0]
    if rect_imagem.top < 0 or rect_imagem.bottom > altura:
        velocidade[1] = -velocidade[1]

    # 6. Desenhar elementos na tela (A ordem importa!)
    tela.fill((25, 25, 25))  # Limpa a tela com fundo escuro
    
    # Desenha a imagem quicando por baixo de tudo
    tela.blit(imagem, rect_imagem) 

    # Desenha o painel central de login
    pygame.draw.rect(tela, COR_PAINEL, painel_login, border_radius=10)
    
    # Título do Painel
    txt_titulo = fonte_titulo.render("Bem-vindo", True, COR_TEXTO)
    tela.blit(txt_titulo, (largura // 2 - txt_titulo.get_width() // 2, 150))

    # Caixas de entrada (muda de cor se clicada)
    cor_u = COR_INPUT_ATIVO if campo_ativo == "usuario" else COR_INPUT_PADRAO
    cor_s = COR_INPUT_ATIVO if campo_ativo == "senha" else COR_INPUT_PADRAO
    pygame.draw.rect(tela, cor_u, input_usuario, border_radius=5)
    pygame.draw.rect(tela, cor_s, input_senha, border_radius=5)
    
    # Botão de entrar
    pygame.draw.rect(tela, COR_BOTAO, botao_entrar, border_radius=5)
    txt_btn = fonte_input.render("Entrar", True, COR_TEXTO)
    tela.blit(txt_btn, (botao_entrar.centerx - txt_btn.get_width() // 2, botao_entrar.centery - txt_btn.get_height() // 2))

    # Renderizar os textos digitados na tela
    # Usuário
    surf_u = fonte_input.render(texto_usuario if texto_usuario else "Usuário...", True, (180, 180, 180) if not texto_usuario else COR_TEXTO)
    tela.blit(surf_u, (input_usuario.x + 10, input_usuario.y + 7))
    
    # Senha (exibe asteriscos para segurança)
    exibicao_senha = "*" * len(texto_senha)
    surf_s = fonte_input.render(exibicao_senha if texto_senha else "Senha...", True, (180, 180, 180) if not texto_senha else COR_TEXTO)
    tela.blit(surf_s, (input_senha.x + 10, input_senha.y + 7))

    pygame.display.flip()  # Renderiza o quadro atualizado
    clock.tick(60)         # Mantém 60 FPS
