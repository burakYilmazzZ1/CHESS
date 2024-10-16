
import pygame

pygame.init()
WIDTH=1000
HEIGHT=900
screen=pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('To player Pygame Chess!')
font=pygame.font.Font('freesansbold.ttf',20)
big_font=pygame.font.Font('freesansbold.ttf',50)
timer=pygame.time.Clock()
fps=60
#game variables and images

white_pieces=['rook','knight','bishop','king','queen','bishop','knight','rook',
              'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']

white_location=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),
                (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1)]


black_pieces=['rook','knight','bishop','king','queen','bishop','knight','rook',
              'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_location=[(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),
                (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6)]

captured_pieces_white=[]
captured_pieces_black=[]

turn_step=0
selection=100
valid_moves=[]

black_queen=pygame.image.load('images/black queen.png')
black_queen=pygame.transform.scale(black_queen,(80,80))
black_queen_small=pygame.transform.scale(black_queen,(45,45))

black_king=pygame.image.load('images/black king.png')
black_king=pygame.transform.scale(black_king,(80,80))
black_king_small=pygame.transform.scale(black_king,(45,45))

black_rook=pygame.image.load('images/black rook.png')
black_rook=pygame.transform.scale(black_rook,(80,80))
black_rook_small=pygame.transform.scale(black_rook,(45,45))

black_bishop=pygame.image.load('images/black bishop.png')
black_bishop=pygame.transform.scale(black_bishop,(80,80))
black_bishop_small=pygame.transform.scale(black_bishop,(45,45))

black_knight=pygame.image.load('images/black knight.png')
black_knight=pygame.transform.scale(black_knight,(80,80))
black_knight_small=pygame.transform.scale(black_knight,(45,45))

black_pawn=pygame.image.load('images/black pawn.png')
black_pawn=pygame.transform.scale(black_pawn,(65,65))
black_pawn_small=pygame.transform.scale(black_pawn,(45,45))

white_queen=pygame.image.load('images/white queen.png')
white_queen=pygame.transform.scale(white_queen,(80,80))
white_queen_small=pygame.transform.scale(white_queen,(45,45))

white_king=pygame.image.load('images/white king.png')
white_king=pygame.transform.scale(white_king,(80,80))
white_king_small=pygame.transform.scale(white_king,(45,45))

white_rook=pygame.image.load('images/white rook.png')
white_rook=pygame.transform.scale(white_rook,(80,80))
white_rook_small=pygame.transform.scale(white_rook,(45,45))

white_bishop=pygame.image.load('images/white bishop.png')
white_bishop=pygame.transform.scale(white_bishop,(80,80))
white_bishop_small=pygame.transform.scale(white_bishop,(45,45))

white_knight=pygame.image.load('images/white knight.png')
white_knight=pygame.transform.scale(white_knight,(80,80))
white_knight_small=pygame.transform.scale(white_knight,(45,45))

white_pawn=pygame.image.load('images/white pawn.png')
white_pawn=pygame.transform.scale(white_pawn,(65,65))
white_pawn_small=pygame.transform.scale(white_pawn,(45,45))

white_images= [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images= [white_pawn_small,white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]

black_images= [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images= [black_pawn_small,black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]

piece_list=['pawn','queen','king','knight','rook','bishop']
#check variables/flashing counter


def draw_board():
    for i in range(32):
        column= i%4
        row= i//4

        if row%2==0:
            pygame.draw.rect(screen,'light gray',[480-(column*160), row*80,80,80])

        else:
            pygame.draw.rect(screen,'light gray',[560-(column*160),row*80,80,80])
        
        pygame.draw.rect(screen,'gray',[0,640,WIDTH,80])
        pygame.draw.rect(screen, 'gold', [0,640,WIDTH, 80],2)
        pygame.draw.rect(screen, 'gray', [640,0,160,HEIGHT],2)
        status_text=['White select a piece to move!','White: Select a Destination!',
                     'Black: Select a piece to move!', 'White: Select a Destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20,660))

        for i in range(9):
            pygame.draw.line(screen,'black',(0,80*i),(640,80*i),2)
            pygame.draw.line(screen,'black',(80*i,0),(80*i,640),2)
            
def draw_pieces():
    for i in range(len(white_pieces)):
        index=piece_list.index(white_pieces[i])
        if white_pieces[i]=='pawn':
            screen.blit(white_pawn,(white_location[i][0]*80+3,white_location[i][1]*80+6))
        else:
            screen.blit(white_images[index],(white_location[i][0]*80+1,white_location[i][1]*80+1))
        
        if turn_step<2:
            if selection==1:
                pygame.draw.rect(screen,'red',[white_location[i][0]*80+1,white_location[i][1]*80+1,80,80],2)
    for i in range(len(black_pieces)):
        index=piece_list.index(black_pieces[i])
        if black_pieces[i]=='pawn':
            screen.blit(black_pawn,(black_location[i][0]*80+3,black_location[i][1]*80+6))
        
        else:
            screen.blit(black_pawn,(black_location[i][0]*80+1,black_location[i][1]*80+1))
        
        if turn_step<2:
            if selection==1:
                pygame.draw.rect(screen,'blue',[black_location[i][0]*80+1,black_location[i][1]*80+1,80,80],2)


def check_option():
    pass


#main game loop
run=True
while run:
    timer.tick(fps)
    screen.fill('dark gray')

    draw_board()

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                x_coard=event.pos[0]//80
                y_coard=event.pos[1]//80
                click_coards=(x_coard,y_coard)

                if turn_step<=1:
                    if click_coards in white_location:
                        selection=white_location.index(click_coards)
                        if turn_step==0:
                            turn_step=1
                    
                    if click_coards in valid_moves and selection!=80:
                        white_location[selection]=click_coards
                        if click_coards in black_location:
                            black_piece=black_location.index(click_coards)
                            captured_pieces_white.append(black_pieces[black_piece])
                            black_pieces.pop(black_piece)
                            black_location.pop(black_piece)
                        black_options=check_option(black_pieces,black_location,'black')
                        white_options=check_option(white_pieces,white_location,'white')
                        turn_step=2
                        selection=80
                        valid_moves=[]
                if turn_step>1:
                    if click_coards in black_location:
                        selection=black_location.index(click_coards)
                        if turn_step==0:
                            turn_step=1
                    
                    if click_coards in valid_moves and selection!=80:
                        black_location[selection]=click_coards
                        if click_coards in white_location:
                            white_piece=white_location.index(click_coards)
                            captured_pieces_black.append(white_pieces[white_piece])
                        white_pieces.pop(white_piece)
                        white_location.pop(white_piece)
                        black_options=check_option(black_pieces,black_location,'black')
                        white_options=check_option(white_pieces,white_location,'white')
                        turn_step=2
                        selection=80
                        valid_moves=[]


    
    pygame.display.flip()
pygame.quit()