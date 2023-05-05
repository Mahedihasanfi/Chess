# xy-coordinate, where x-letter & y-digit
x =["a","b","c","d","e","f","g","h"]   
y=["1","2","3","4","5","6","7","8"]

# request user to input the white piece
white_piece = []
def add_white_piece():
    while white_piece==[]:   
        global white_coordinates 
        user_input1 = input("please take one white piece out of pawn or rook and coordinates (e.g. 'rook a5'): ").lower()
        if user_input1.startswith(('pawn','rook')) and len(user_input1.split()) == 2:
            piece, white_coordinates = user_input1.split()            
            if white_coordinates[0] in x and white_coordinates[1] in y:
                print(f"White {piece} was successfully added at {white_coordinates}.")                
                white_piece.append(user_input1) 
                print("white piece", white_piece)
            else:
                print("Invalid input. Please enter a valid coordinates.")
        else:
            print("Invalid input. Please enter a valid white piece and its coordinates.")

# request user to input the black piece
black_pieces = []
black_coordinates=[]
def add_black_piece():    
    while len(black_coordinates)<17:
        user_input2 = input("please take black piece from pawn, rook or king and its coordinates(e.g.'pawn b2'), or write 'done' to finish: ").lower()
        if user_input2 == "done":
            print(black_pieces)
            print(f'{len(black_pieces)} black piece(s) added successfully.')
            break
        elif user_input2.startswith(('pawn','rook', 'king')) and len(user_input2.split()) == 2:
            bpiece, coordinates = user_input2.split()
            if coordinates[0] in x and coordinates[1] in y:
                if coordinates != white_coordinates:
                    if coordinates not in black_coordinates:
                        print(f"Black {bpiece} was successfully added at {coordinates}.")
                        black_pieces.append(user_input2)
                        black_coordinates.append(coordinates)
                        print(black_pieces)
                        print(f'{len(black_pieces)} black piece(s) added successfully.')                                               
                    else:
                        print("There is another BLACK piece in SAME coordinate")              
                else:
                    print("There is another WHITE piece in SAME coordinate")
            else:
                print("There enter valid coordinate")
        else:
            print("Invalid input. Please enter a valid black piece and its coordinates, or 'done' to finish.")


add_white_piece()      
add_black_piece()      

# Function to check if the white piece can take any black pieces
def can_take(white, black):   
    if white[0:4] == 'pawn':
        # if the pawn can take the black piece diagonally
        white_row, white_col = int(white[6]), ord(white[5]) - ord('a')
        black_row, black_col = int(black[6]), ord(black[5]) - ord('a')
        return (abs(white_row - black_row) == 1 and abs(white_col - black_col) == 1)    
    elif white[0:4] == 'rook':
        # if the rook can take the black piece horizontally or vertically        
        white_row, white_col = int(white[6]), ord(white[5]) - ord('a')
        black_row, black_col = int(black[6]), ord(black[5]) - ord('a')
        return (white_row == black_row or white_col == black_col)
    else:
        return False

# The white piece can take 
white_piece_string = ", ".join(white_piece)
can_take_list = [black for black in black_pieces if can_take(white_piece_string, black)]

# Print the result
if can_take_list:
    print(f'The white {white_piece_string} can take the following black piece(s): {", ".join(can_take_list)}.')
else:
    print(f'The white {white_piece_string} cannot take any black piece.')