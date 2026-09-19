#Chess Game

import turtle as trtl
wn = trtl.Screen()

root = wn.getcanvas().winfo_toplevel()
root.state("zoomed")

#sets the colors of the board
even_color="dark gray"
odd_color="light gray"
bgcolor="light blue"

#default font to be used
font_default=("Arial",12,"bold")
#must reset the file, as you start a new game
def reset_file():
    #create list, which will have the correct values
    correct_filevalues=[]

    #open file
    correct_file=open("chess_unedited.txt", "r")

    #iterate through file, append to list
    for value in correct_file:
        correct_filevalues.append(value)

    #open old file, and write each value in the correct file
    incorrect_file=open("chesslocations.txt","w")
    for value in correct_filevalues:
        incorrect_file.write(value)

#BOARD START-----------------------------------------------------------
def create_board():
    #set starting variables
    square_x=-270
    square_y=210
    square_counter=0
    #tracer
    wn.tracer(False)
    for _ in range(8):
        #each time a new column is created
        square_x+=60
        square_y=210
        #to get the alternating color look
        square_counter+=1
        for _ in range(8):
            #creating square
            square=trtl.Turtle(shape="square")
            square.penup()
            square.shapesize(3)
            #choosing color
            if square_counter % 2 == 0:
                square.color(even_color)
            else:
                square.color(odd_color)
            #changing counter
            square_counter+=1
            #moving square
            square.goto(square_x,square_y)
            #choosing where the next square goes
            square_y-=60
    #updates to show board
    wn.update()
#BOARD END--------------------------------------------------------------------------------
#CREATE PIECES -------------------------------
def create_pieces_start():
    pieces_shapes=[]
    piece_turtles=[]

    #list of names to create pieces easier
    list_whitepieces=["white_rook.gif","white_knight.gif","white_bishop.gif","white_queen.gif","white_king.gif"]
    list_blackpieces=["black_rook.gif","black_knight_smiley.gif","black_bishop.gif","black_queen.gif","black_king.gif","black_knight.gif"]
    #lists above are to create the shapes, and lists under are to make turtles, you cannot make a shape twice
    list_whitepieces_all=["white_rook.gif","white_knight.gif","white_bishop.gif","white_queen.gif","white_king.gif", "white_bishop.gif","white_knight.gif","white_rook.gif"]
    list_blackpieces_all=["black_rook.gif","black_knight_smiley.gif","black_bishop.gif","black_queen.gif","black_king.gif","black_bishop.gif","black_knight.gif","black_rook.gif"]

    #append to shape list
    pieces_shapes.append(list_whitepieces)
    pieces_shapes.append(list_blackpieces)
    #append to turtle list
    piece_turtles.append(list_whitepieces_all)
    piece_turtles.append(list_blackpieces_all)
    #create the shapes
    for piece_list in pieces_shapes:
        for piece in piece_list:
        #create the shape
            wn.addshape(piece)
    #starting cords
    piece_x=-210
    piece_y=-210
    #get all of the files
    for piece_list in piece_turtles:
        for piece in piece_list:
        #add a turtle that shape
                pieceTurtle=trtl.Turtle(shape=piece)
                pieceTurtle.goto(piece_x,piece_y)
                pieceTurtle.stamp()
                #move to the right
                piece_x+=60
                #when you get to the end of the board, move up
                if piece_x > 210:
                    piece_x = -210
                    piece_y = 210
    #pawns below
    pawn_x=-210
    pawn_y=-150
    #add shapes for pawns
    wn.addshape("white_pawn.gif")
    wn.addshape("black_pawn.gif")
    #iterate through colors
    pawn_shapes=["white_pawn.gif","black_pawn.gif"]
    for pawn in pawn_shapes:
        #repeat 8 times
        for _ in range(8):
            #create the turtle
            pawnTurtle=trtl.Turtle(shape=pawn)
            #go to position
            pawnTurtle.goto(pawn_x,pawn_y)
            pawnTurtle.stamp()
            #go right
            pawn_x+=60
            #if you get off the board, move up and to the left
            if pawn_x > 210:
                pawn_x=-210
                pawn_y=150

#GET PIECE NAMES FOR ALL PIECES CURRENTLY
def get_pieces():
    #setting new list to blank
    piece_name_list=[]
    boardfile=open("chesslocations.txt", "r")
    for value in boardfile:
         #set index to 0, name to none, for each new piece
        piece_name=""
        index=0
        #for each letter before the comma, add that letter to a string, which is then added to the list when getting to the comma
        while value[index] != ",":
            piece_name+=value[index]
            index+=1
        piece_name_list.append(piece_name)
    #returns names of all pieces, in format of ex: w_pawn
    return piece_name_list

#GET LOCATIONS OF ALL PIECES CURRENTLY
def get_locations():
    #setting new list to blank
    piece_cord_list=[]
    #open file
    boardfile=open("chesslocations.txt", "r")
    for value in boardfile:
        #iterate through letters on the file
        index=0
        piece_cords=""
        #while we are still at the letters, skip them
        while value[index] != ",":
            index+=1
        #extra index to get through the comma
        index+=1
        #add first number
        piece_cords+=value[index]
        #skip to, and then add second number
        index+=1
        piece_cords+=value[index]
        piece_cord_list.append(piece_cords)
    return piece_cord_list

#determine where the click was, in board cords, using canvas cords
def determine_cords(xvalue,yvalue):
    counter=0
    #if the click is off the board:
    if xvalue < -240 or xvalue>240 or yvalue<-240 or yvalue>240:
            return None
    #iterates through for both values, x and y
    values=[xvalue,yvalue]
    for value in values:
        #checks to see whether it is x or y value for later
        if counter == 0:
            counter+=1
            isx= True
        else:
            isx=False
        #create starting value to check from, in increments of 60 (board square size)
        starting_value=-240
        #checks to see what block the click was on
        for index in range(8):
            #checks to see if the x value
            if (value >= starting_value) and (value <= starting_value+60):
                #if this is the x value we are checking...
                if isx == True:
                    #x_onboard is the x cord on board
                    x_onboard=index+1
                    #this variable below is the canvas cord of the center of the square clicked
                    x_click_middle_square=starting_value+30
                    break
                #isx is False if we are checking the y value
                if isx == False:
                    #identical variables as above, but for y value
                    y_onboard=index+1
                    y_click_middle_square=starting_value+30
                    break
            else:
                #iterate through all board pieces until we find the correct click location
                starting_value+=60
    return [x_onboard,y_onboard,x_click_middle_square,y_click_middle_square]

#this is called after every click
#this function understands clicks on pieces, requested moves
#restart game requests, checkmate checking requests, every click possible
def understand_request(x,y):
    #get global variables
    global retry_button_current
    global piece_click_loc_board
    global piece_click_loc_canvas
    global pawn_promote_current_white,pawn_promote_current_black
    #if the click was on the checkmate button
    if check_for_checkmatebutton_click(x,y)==True:
        #get the result of the game
        ending_result=check_forcheck_mate()
        #if the game is over
        if ending_result != False:
            #create the ending screen
            create_game_over_screen(ending_result[0],ending_result[1])
    #if the endgame button is there
    if retry_button_current == True:
        #check for the click on the restart game button
        if checkfor_retrybutton_click(x,y)==True:
            #restart the game
            start_game()
    #if there is any pawn promotion
    if pawn_promote_current_white==True or pawn_promote_current_black == True:
        initiate_pawnpromotion(x,y)
        return None
    #figure out where was clicked, on the board and middle square
    click_cords=(determine_cords(x,y))
    #ignore clicks outside of board
    if click_cords is None:
        clear_all_grays()
        return None

    #get variables from determine_cords
    click_cords_board_unformatted=[click_cords[0],click_cords[1]]
    click_cords_canvas=[click_cords[2],click_cords[3]]

    #format previously determined cords correctly
    xcord=click_cords_board_unformatted[0]
    ycord=click_cords_board_unformatted[1]
    click_cords_board=(str(xcord)+str(ycord))
    #get the list of locations of current pieces, to tell if a piece was clicked on
    piece_locations_list=get_locations()
    #checks for move
    if check_forgrayclick(click_cords_canvas) == True:
        #process requested move
        on_move_request(click_cords_canvas,click_cords_board)
    #if a piece was clicked on, and a gray was not
    elif check_forgrayclick(click_cords_canvas) == False:
        if click_cords_board in piece_locations_list:
            on_gray_request(click_cords_board,click_cords_canvas)    
    #if a piece was not clicked on, meaning a blank square was
    else:
        clear_all_grays()

#check to see what was clicked on
def check_forgrayclick(click_cords_canvas):
    global turtle_graylist
    if turtle_graylist == []:
        return False
    #iterate through every "gray turtle"
    for turtle in turtle_graylist:
        #find position of gray
        cords_ofgray_unformatted=turtle.pos()
        #format gray cords
        cords_ofgray=(list(cords_ofgray_unformatted))
        #if the location clicked is the same as a gray
        if click_cords_canvas == cords_ofgray:
            return True

def on_move_request(click_cords_canvas,click_cords_board):
    #get rid of grays
    clear_all_grays()
    #make a new piece there
    make_movedpiece(click_cords_canvas,click_cords_board)
    update_file(click_cords_canvas)
    add_square_aftermove()
    #update which pieces can castle
    update_castling_eligible_pieces(click_cords_board)
    #check for castle, get rook cords, and move both rook and king on a castle
    move_rook_oncastle(getrook_cords_castle(click_cords_board))
    #check for a draw by insufficient material
    check_for_insufficient_material(determine_ifturn())

def on_gray_request(click_cords_board,click_cords_canvas):
    global piece_click_loc_board, piece_click_loc_canvas
    #get the names of pieces and locations
    piece_name_list=get_pieces()
    piece_locations_list=get_locations()
    #clear all the grays existing
    clear_all_grays()
    #get piece description from the lists
    index_piecename=piece_locations_list.index(click_cords_board)
    piece_clicked=piece_name_list[index_piecename]
    #get the name and color
    color_and_name=determine_name_and_color(piece_clicked)
    #if it is their turn
    if determine_ifturn() == color_and_name[1]:
        #get the click location on canvas, and board
        #these variables will not update on a move, only on a request of grays
        #this allows the code to have values for the extra squares that must go onto locations after a move
        piece_click_loc_canvas=[click_cords_canvas[0],click_cords_canvas[1]]
        piece_click_loc_board=[click_cords_board[0],click_cords_board[1]]
        #uses name, color, and location to determine where the piece clicked can move
        eligible_grays=determine_spaces(color_and_name[0],color_and_name[1],click_cords_board)
        #get the legal moves, compared to the possible moves
        legalgrays=get_legalmoves(eligible_grays,color_and_name,click_cords_board)
        #adding castling for clicking on kings
        if color_and_name[0] == "king":
            #determine the castling squares
            castling_squares=determine_castling_eligibility(color_and_name[1],click_cords_board)
            #if they can castle, add the castling squares
            if castling_squares is not None:
                for square in castling_squares:
                    legalgrays.append(square)
        #resets these variables, as they change when checking for check
        piece_click_loc_canvas=[click_cords_canvas[0],click_cords_canvas[1]]
        piece_click_loc_board=[click_cords_board[0],click_cords_board[1]]
        #if there is any spot for the piece to move
        if eligible_grays is not None:
            #legalgrays is formatted like [[3,3],[3,4]], which are the board cords
            #we need canvas cords, so we can direct the grays where to go using turtles canvas
            #graylocations_canvas will be legalgrays, but in canvas cord form
            graylocations_canvas=determine_graylocations_canvas(legalgrays)     
            #create the grays
            create_grays(graylocations_canvas)    
   
def make_movedpiece(location_goto,click_cords_board):
    global en_p_pawnlocs_w,en_p_pawnlocs_b,en_p_grays_b,en_p_grays_w
    #get the cords of the new square make a new square to overlap the existing piece on a potential take
    cords_unformatted=determine_cords(location_goto[0],location_goto[1])
    cords_board=[cords_unformatted[0],cords_unformatted[1]]
    #determine the color
    if ((cords_board[0])+(cords_board[1])) % 2 == 0:
        color=even_color
    else:
        color=odd_color
    #create the square, and stamp on spot, when the spot is the square we are moving to
    square=trtl.Turtle(shape="square")
    square.shapesize(3)
    square.color(color)
    square.goto(location_goto)
    square.stamp()
    #get color and name of piece
    locations_list=get_locations()
    names_list=get_pieces()
    index=locations_list.index(str(piece_click_loc_board[0])+str(piece_click_loc_board[1]))
    name_andcolor_unformatted=names_list[index]
    name_andcolor=determine_name_and_color(name_andcolor_unformatted)
    name=name_andcolor[0]
    color=name_andcolor[1]
    #formats click cords board in the same way as en_p_gray lists
    en_passant_format_ccb=[int(str(click_cords_board)[0]),int(str(click_cords_board)[1])]
    #checks the name and color, and sets the file accordingly
    if name == "pawn":
        #if the move was not a capture of an en passant, remove everything from those lists
        if en_passant_format_ccb not in en_p_grays_w:
            en_p_grays_w=[]
            en_p_pawnlocs_w=[]
        if en_passant_format_ccb not in en_p_grays_b:
            en_p_grays_b=[]
            en_p_pawnlocs_b=[]
        #only for pawn, to add en passant in, must identify the times a pawn moves 2 squares
        note_en_passant(location_goto,piece_click_loc_canvas,color,click_cords_board)
        #identifies an en passant capture
        identify_en_passant(location_goto)
        if color == "white":
            #identify when they have reached a promotion
            if cords_board[1] == 8:
                create_options_promotion(color,location_goto)
                piece_filename="white_pawn.gif"
            else:
                piece_filename="white_pawn.gif"
        else:
            if cords_board[1] == 1:
                create_options_promotion(color,location_goto)
            piece_filename="black_pawn.gif"
    if name == "rook":
        if color == "white":
            piece_filename="white_rook.gif"
        else:
            piece_filename="black_rook.gif"
    if name == "knight":
        if color == "white":
            piece_filename="white_knight.gif"
        else:
            piece_filename="black_knight_smiley.gif"
    if name == "bishop":
        if color == "white":
            piece_filename="white_bishop.gif"
        else:
            piece_filename="black_bishop.gif"
    if name == "queen":
        if color == "white":
            piece_filename="white_queen.gif"
        else:
            piece_filename="black_queen.gif"
    if name == "king":
        if color == "white":
            piece_filename="white_king.gif"
        else:
            piece_filename="black_king.gif"
    #make turtle visible in correct spot
    piece_turtle=trtl.Turtle(shape=piece_filename)
    piece_turtle.goto(location_goto)
    piece_turtle.stamp()


def update_file(new_loc_unformatted,promotion=False):
    global move_counter
    global piece_click_loc_board
    global en_p_white, en_p_black
    #need the old location, name, and new location to change the file
    #format the location of the new loc
    new_cords=determine_cords(new_loc_unformatted[0],new_loc_unformatted[1])
    new_loc=str(new_cords[0])+str(new_cords[1])
    new_loc_canvas=[new_cords[2],new_cords[3]]
    locations_list=get_locations()
    names_list=get_pieces()
    #modifies the old click location for promotion
    if promotion!=False:
        #get the piece and color through the file
        name_andcolor=(get_name_andcolor_fromfile(promotion))
        color_promotion_fullword=name_andcolor[0]
        name_promotion=name_andcolor[1]
        #changes the color to just the first letter
        color_promotion_letter=color_promotion_fullword[0]
        piece_identity=str(color_promotion_letter+"_"+ name_promotion)
        piece_click_loc_board=new_loc
    #format location of old loc
    old_loc=(str(piece_click_loc_board[0])+str(piece_click_loc_board[1]))
    #get name
    index_in_namelist=locations_list.index(old_loc)
    name=names_list[index_in_namelist]
    #removes old values from list
    locations_list.pop(index_in_namelist)
    names_list.pop(index_in_namelist)
    #if the move is an en passant capturing white
    if en_p_white == True:
        update_game_enpassant("white",new_loc,locations_list,names_list,new_loc_canvas)
        #resets, so this if statement will only evaluate to true on another en passant
        en_p_white=False
    #same thing, for black        
    if en_p_black == True:
        update_game_enpassant("black",new_loc,locations_list,names_list,new_loc_canvas)
        en_p_black=False
    #if you are taking a piece
    if new_loc in locations_list:
        #figure out what piece is at the place we want to move
        index_oftaken_piece=locations_list.index(new_loc)
        #"take" the piece
        locations_list.pop(index_oftaken_piece)
        names_list.pop(index_oftaken_piece)
    #edits the name on a promotion
    if promotion != False:
        name=piece_identity
        #edit move counter, as it will increase on the promotion
        move_counter-=1
    #adds new values to list
    locations_list.append(new_loc)
    names_list.append(name)
    #update file
    pieces_file=open("chesslocations.txt", "w")
    for index in range(len(locations_list)):
        pieces_file.write(names_list[index]+","+locations_list[index]+"\n")
    pieces_file.close()
    #increment move counter
    move_counter+=1


#after a move, needs to remove the piece
def add_square_aftermove(en_passant_addsquareloc=False,pawn_promote=False):
    global piece_click_loc_board
    global piece_click_loc_canvas
    global ul_rookmove,ur_rookmove,dl_rookmove,dr_rookmove,wking_move,bking_move
    #make the square
    square=trtl.Turtle(shape="square")
    square.penup()
    square.shapesize(3)
    #set variables
    square_loc_canvas=piece_click_loc_canvas[0],piece_click_loc_canvas[1]
    location=piece_click_loc_board[0],piece_click_loc_board[1]
    #check to see if the move is a king move that prevents a castle, and updates variables accordingly
    if location == ("5","1"):
        wking_move=True
    if location == ("5","8"):
        bking_move=True
    #during an en passant
    if en_passant_addsquareloc != False:
        #change variables of square loc on board and canvas
        square_loc_canvas=en_passant_addsquareloc
        unformatted_location=determine_cords(square_loc_canvas[0],square_loc_canvas[1])
        location=unformatted_location[0],unformatted_location[1]
    #during a pawn promotion
    if pawn_promote != False:
        #change variables
        square_loc_canvas=pawn_promote
        unformatted_location=determine_cords(square_loc_canvas[0],square_loc_canvas[1])
        location=unformatted_location[0],unformatted_location[1]
    #determine square color
    if (int(location[0]) + int(location[1])) % 2 == 0:
        squarecolor=even_color
    else:
        squarecolor=odd_color
    square.color(squarecolor)
    #move and stamp square
    square.goto(square_loc_canvas)
    square.stamp()

#get [king,white] from w_king, or similar
def determine_name_and_color(name):
    #determine color
    if name[0] == "w":
        color="white"
    else:
        color="black"
    #determine piece
    piece_name=""
    counter=0
    #for every letter..
    for letter in name:
        #skips to name
        counter+=1
        #adds letter to name, only after the b_ (indexes 0 and 1)
        if counter>2:
            piece_name+=letter
    return [piece_name,color]

def determine_ifturn():
    global move_counter
    white_turn=False
    black_turn=False
    #if the move counter is even, white turn
    if move_counter % 2 == 0:
        white_turn=True
    else:
        black_turn=True
    if white_turn==True:
        return "white"
    if black_turn==True:
        return "black"

#determines the spaces a piece can move, must check for every piece individually
def determine_spaces(name,color,location_click_board):
    location_xval=int(location_click_board[0])
    location_yval=int(location_click_board[1])
    eligible_grays=[]
    #starts with king, pawn, and knight, because those pieces do not need to be in a loop
    if name == "knight":
        #get all knight movements
        move_up_vert=location_yval+2
        move_down_vert=location_yval-2
        move_left_vert=location_xval-1
        move_right_vert=location_xval+1
        move_up_horiz=location_yval+1
        move_down_horiz=location_yval-1
        move_right_horiz=location_xval+2
        move_left_horiz=location_xval-2
        #add all knight movements to a list
        knight_moves=[]

        #add every knight move to a list, all 8
        #right 1 up 2
        knight_moves.append([move_right_vert,move_up_vert])
        #left 1 up 2
        knight_moves.append([move_left_vert,move_up_vert])
        #right 1 down 2
        knight_moves.append([move_right_vert,move_down_vert])
        #left 1 down 2
        knight_moves.append([move_left_vert,move_down_vert])
        #right 2 down 1
        knight_moves.append([move_right_horiz,move_down_horiz])
        #right 2, up 1
        knight_moves.append([move_right_horiz,move_up_horiz])
        #left 2, down 1
        knight_moves.append([move_left_horiz,move_down_horiz])
        #left 2, up 1
        knight_moves.append([move_left_horiz,move_up_horiz])
        #let the code know the knights moves need to be checked
        eligible_grays=knight_moves
    #PAWN--------------------------------------------------------------------
    if name == "pawn":
        #get global list for en passant
        global en_p_grays_b, en_p_grays_w
        #assume the pawn can't move forward 2
        move_2=False
        if color=="white":
            #sets the differential, which is used to determine the space the pawn can move, because not all pawns can move the same spaces, even if they're on the same square
            colored_differential=1
            #set en passant list, based on color
            current_enp_list=en_p_grays_b
        #same for black
        if color=="black":
            colored_differential=-1
            current_enp_list=en_p_grays_w
            #only checking for when it returns true, and not != False
            #this is because pawns can only move forward when there is nothing there, so a value
            #should only be appended when there is nothing there
            #for all other pieces, a value must be added when there is a piece, that is not the same color,
            #which is when the function returns "take", or false if there is nothing there
            #this is why we must call determine_ifpossible_move so many times for pawns, because some of their moves are illegal
            #due to another piece being there, but other moves aren't

        #check forward 1 for a pawn
        if determine_ifpossible_move(location_xval,(location_yval+colored_differential),color) == True:
            eligible_grays.append([location_xval,location_yval+colored_differential])
            #determine the position for the pawn, and if moving 2 is legal
            #this code only runs when you can move 1 space legally, to prevent pawns from being able to jump pieces
            if color == "white" and location_yval == 2:
                move_2=True
            if color == "black" and location_yval == 7:
                move_2=True
            if move_2==True:
                #check forward 2 for a pawn
                if determine_ifpossible_move(location_xval,(location_yval+(colored_differential*2)),color) == True:
                    eligible_grays.append([location_xval,(location_yval+(colored_differential*2))])
        #add left and right cords to a list, to make the follow code shorter
        left_and_right_cords=[location_xval-1,location_xval+1]
        for new_xcord in left_and_right_cords:
            #check for a take
            if determine_ifpossible_move(new_xcord,(location_yval+colored_differential),color) == "take":
                eligible_grays.append([new_xcord,(location_yval+colored_differential)])
            #check to see if the square is available en passant
            if [new_xcord,(location_yval+colored_differential)] in current_enp_list:
                eligible_grays.append([new_xcord,(location_yval+colored_differential)])
    #king==================================================================================
    if name == "king":
        #get global list for king moves and rook moves
        global dl_rookmove,dr_rookmove,ul_rookmove,ur_rookmove, wking_move,bking_move
        #get all of the kings movement options
        left_movement=location_xval-1
        right_movement=location_xval+1
        up_movement=location_yval+1
        down_movement=location_yval-1
        king_moves=[]
        #get every king move
        #up 1
        king_moves.append([location_xval,up_movement])
        #up 1, left 1
        king_moves.append([left_movement,up_movement])
        #up 1, right 1
        king_moves.append([right_movement,up_movement])
        #left 1
        king_moves.append([left_movement,location_yval])
        #right 1
        king_moves.append([right_movement,location_yval])
        #down 1
        king_moves.append([location_xval,down_movement])
        #down 1 left 1
        king_moves.append([left_movement,down_movement])
        #down 1 right 1
        king_moves.append([right_movement,down_movement])
        eligible_grays=king_moves
    #variables for bishop/queen not to jump over pieces
    upleft=True
    upright=True
    downleft=True
    downright=True
    #variables for rook/queen not to jump over pieces
    up=True
    down=True
    left=True
    right=True
    movements_jumping_list_rook=[up,down,left,right]
    movements_jumping_list_bishop=[upleft,upright,downleft,downright]
    #must do 8 times, so we can get the pieces to move all over the board
    for index in range(8):
        #get the movement, based on index and starting loc
        left_movement=location_xval-(index+1)
        right_movement=location_xval+(index+1)
        up_movement=location_yval+(index+1)
        down_movement=location_yval-(index+1)
    #ROOK####################################################################################
        if name == "rook" or name == "queen":
            #get list of all moves
            potential_moves=[]
            #up 
            potential_moves.append([location_xval,up_movement])
            #down 
            potential_moves.append([location_xval,down_movement])
            #left 
            potential_moves.append([left_movement,location_yval])
            #right
            potential_moves.append([right_movement,location_yval])
            for iteration_index in range(len(potential_moves)):
                #check for every move
                move=potential_moves[iteration_index]
                #get the jumping check, essentially stopping a piece from jumping over another
                current_jumpingcheck=movements_jumping_list_rook[iteration_index]
                #if you can move there, and you can still move in that direction without jumping
                if determine_ifpossible_move(move[0],move[1],color) != False and current_jumpingcheck == True:
                    eligible_grays.append([move[0],move[1]])
                    #if moving there is a take
                    if determine_ifpossible_move(move[0],move[1],color) == "take":
                        #tell the code to never check that direction again
                        movements_jumping_list_rook[iteration_index]=False
                #if you can't move there
                else:
                    #never check that direction
                    movements_jumping_list_rook[iteration_index]=False

    #BISHOP##############################################################################
        if name=="bishop" or name == "queen":
            #get the potential directions
            potential_moves=[]
            potential_moves.append([left_movement,up_movement])
            potential_moves.append([right_movement,up_movement])
            potential_moves.append([left_movement,down_movement])
            potential_moves.append([right_movement,down_movement])
            for iteration_index in range(len(potential_moves)):
                #check for every move
                move=potential_moves[iteration_index]
                #get the jumping check
                current_jumpingcheck=movements_jumping_list_bishop[iteration_index]
                #if you can move there, and you can still move in that direction
                if determine_ifpossible_move(move[0],move[1],color) != False and current_jumpingcheck == True:
                    eligible_grays.append([move[0],move[1]])
                    #if moving there is a take
                    if determine_ifpossible_move(move[0],move[1],color) == "take":
                        #tell the code to never check that direction again
                        movements_jumping_list_bishop[iteration_index]=False
                #if you can't move there
                else:
                    #never check that direction
                    movements_jumping_list_bishop[iteration_index]=False

    if eligible_grays==[]:
        return None
    else:
        #knights and kings moves not checked for other pieces yet
        if name == "knight" or name == "king":
            real_grays=[]
            #iterate through all the moves
            for potential_move in eligible_grays:
                #only append when there is no same color piece there
                if determine_ifpossible_move(potential_move[0],potential_move[1],color) != False:
                    real_grays.append(potential_move)
            return real_grays
        else:
            return eligible_grays


#determines the real spaces that you can move to, without thinking about checks
def determine_ifpossible_move(cordx,cordy,color):
    names_list=get_pieces()
    locations_list=get_locations()

    #determines if cords are on the board
    #if any of these conditions are true, that cord cannot be moved to
    if cordx <= 0 or cordx >= 9 or cordy <= 0 or cordy >= 9:
        return False

    #formats list of piece locations from file
    formatted_locations=[]
    for cord in locations_list:
        formatted_locations.append(int(cord))

    #formats cords of click
    cords=int(str(cordx)+str(cordy))

    #if the clicked cord has a piece on it
    if cords in formatted_locations:
        #get the name (with color) of the piece
        index_oflocation=formatted_locations.index(cords)
        name_piece_onspot=(names_list[index_oflocation])
 
        #if the colors match return false, for no move
        if name_piece_onspot[0]==color[0]:
            return False
        #if there is a piece, but the colors do not match
        #this needs to be different from true/false, because pawns, rooks, bishops, and queens legal moves
        #all can change depending on it
        else:
            return "take"
    #if there is not any piece there
    else:
        return True


def update_castling_eligible_pieces(new_loc_str):
    global ul_rookmove,ur_rookmove,dl_rookmove,dr_rookmove
    global piece_click_loc_board

    #format our locs
    old_loc=int(str(piece_click_loc_board[0])+str(piece_click_loc_board[1]))
    new_loc=int(new_loc_str)

    #if we are moving to, or from any corner, that corner cannot be castled to anymore
    #and global variables need updating accordingly
    if old_loc == 11 or new_loc == 11:
        dl_rookmove=True
    if old_loc == 18 or new_loc == 18:
        dr_rookmove=True
    if old_loc == 81 or new_loc == 81:
        ul_rookmove=True
    if old_loc == 88 or new_loc == 88:
        ur_rookmove=True
    
def determine_castling_eligibility(color,kingloc):
    #get global list for king moves and rook moves
    global dl_rookmove,dr_rookmove,ul_rookmove,ur_rookmove, wking_move,bking_move
    castling_squares=[]
    #set variables based on color of request
    if color == "white":
        #left and right rookmoves
        left_rookmove=dl_rookmove
        right_rookmove=dr_rookmove
        king_move=wking_move
        #variable for updating file for later
        color_andname_fileformatted="w_king"
        #check_forcheck takes opposite color of the king you need to check for check on
        opposite_color="black"
    #same for black
    else:
        left_rookmove=ul_rookmove
        right_rookmove=ur_rookmove
        king_move=bking_move
        color_andname_fileformatted="b_king"
        opposite_color="white"
    #if the king has moved, end the function
    if king_move == True:
        return None
    #end the function if the king is in check currently
    if check_forcheck(opposite_color) == True:
        return None
    
    #get which directions are still valid
    list_legaldirections=[]
    #copy of list_legaldirections, and will be used for direction in iteration of the loop
    #list_legaldirections must be modified during the running of the loop that depends on it, so it cannot be used
    list_legaldirections_beforeloop_copy=[]
    #if that direction of castling is still valid, append to lists
    if left_rookmove == False:
        list_legaldirections.append("left")
        list_legaldirections_beforeloop_copy.append("left")
    if right_rookmove == False:
        list_legaldirections.append("right")
        list_legaldirections_beforeloop_copy.append("right")
    if list_legaldirections == []:
        return None
    #check for each direction of castling
    for direction in list_legaldirections_beforeloop_copy:
        #distance in between king and where we are checking set to 0
        piece_distance=0
        #set variables for leftside castle
        if direction == "left":
            loopingnum=3
            difference=-1
        #same for right
        else:
            loopingnum=2
            difference=1
        #check for each space the castle will involve
        for _ in range(loopingnum):
            #add to the piece distance
            piece_distance+=difference
            #get the new kingloc we are testing for
            new_kingloc=[int(kingloc[0])+piece_distance,int(kingloc[1])]
            #essentially, if there is a same-color piece at this new loc, we cannot castle there
            if determine_ifpossible_move(new_kingloc[0],new_kingloc[1],color) == False:
                list_legaldirections.remove(direction)
                break
            #update the file, as if the king had moved
            update_file_check_forchecks(color_andname_fileformatted,kingloc,new_kingloc)
            #check for check on the king in this new spot, if true, we cannot castle there
            if check_forcheck(opposite_color) == True:
                #update the file back, given there is a check
                update_file_check_forchecks(color_andname_fileformatted,new_kingloc,kingloc,resetting=True)
                list_legaldirections.remove(direction)
                break
            #update the file back, on no check
            update_file_check_forchecks(color_andname_fileformatted,new_kingloc,kingloc,resetting=True)
    #after this ^ loop, only valid castling directions will remain in list_legaldirections

    if "left" in list_legaldirections:
        #add a left king castle loc
        castling_squares.append([int(kingloc[0])-2,int(kingloc[1])])
    if "right" in list_legaldirections:
        #add a right king castle loc
        castling_squares.append([int(kingloc[0])+2,int(kingloc[1])])
    return castling_squares


#move the king, and get the rook cords, on a castle
def getrook_cords_castle(new_cords):
    #get names a locations of all pieces
    locs=get_locations()
    names=get_pieces()
    #format cords of old click
    old_cords=str(piece_click_loc_board[0])+str(piece_click_loc_board[1])
    if new_cords not in locs:
        return None
    #get the name of the piece we moved
    index_ofpiece=locs.index(new_cords)
    name_ofpiece=names[index_ofpiece]
    #get the name and color
    color_and_name= determine_name_and_color(name_ofpiece)
    name=color_and_name[0]
    color=color_and_name[1]
    #if we didn't click on a king, return nothing
    if name != "king":
        return None
    #format x vals
    new_xval=int(new_cords[0])
    old_xval=int(old_cords[0])
    #get the difference in xvals
    difference_in_xvals=new_xval-old_xval
    #if the move wasn't a castle, return none
    if abs(difference_in_xvals) != 2:
        return None
    #if it was a rightside castle, get the rook cords board and canvas
    if difference_in_xvals > 0:
        rook_currentcords_board=[int(new_xval+1),int(new_cords[1])]
        rook_newcords_board=[int(new_xval-1),int(new_cords[1])]
        #add x value of canvas cords, we do not know the y cords on the canvas yet\
        #we will determine that later using color
        rook_currentcords_canvas=[210]
        rook_newcords_canvas=[90]
    #same for leftside castle
    if difference_in_xvals < 0:
        rook_currentcords_board=[int(new_xval-2),int(new_cords[1])]
        rook_newcords_board=[int(new_xval+1),int(new_cords[1])]
        rook_currentcords_canvas=[-210]
        rook_newcords_canvas=[-30]
    #we know the y cord of the rook on a white castle, and black, so append those to the lists accordingly
    if color == "white":
        rook_currentcords_canvas.append(-210)
        rook_newcords_canvas.append(-210)
    else:
        rook_currentcords_canvas.append(210)
        rook_newcords_canvas.append(210)
    return(rook_currentcords_board,rook_newcords_board,rook_currentcords_canvas,rook_newcords_canvas)


def move_rook_oncastle(rookcords_list):
    global move_counter
    #if we aren't castling
    if rookcords_list==None:
        return None
    #understand variables from other function passed in one larger list
    board_old_rook=rookcords_list[0]
    board_new_rook_unformatted=rookcords_list[1]
    canvas_old_rook=rookcords_list[2]
    canvas_new_rook=rookcords_list[3]
    #simulate a new move and past click, to move the rook
    global piece_click_loc_board,piece_click_loc_canvas
    piece_click_loc_board=board_old_rook
    piece_click_loc_canvas=canvas_old_rook
    #format board cords 
    board_new_rook=str(board_new_rook_unformatted[0])+str(board_new_rook_unformatted[1])
    #subtract from move counter, as this will technically be two moves, taking away the others turn
    move_counter-=1
    #this tells the code there was a new click, on the cords of where we want the rook to go
    on_move_request(canvas_new_rook,board_new_rook)


def get_kinglocs():
    #get locations of all pieces
    king_locations=[]
    locations=get_locations()
    names=get_pieces()
    #find each king in list of pieces
    king_nameslist=["w_king","b_king"]
    for name in king_nameslist:
        #index of king
        king_index=names.index(name)
        #get location
        king_location=locations[king_index]
        king_locations.append(king_location)
    #locations of kings, in string 44 format
    king_w_location_unformat=king_locations[0]
    king_b_location_unformat=king_locations[1]
    #change format of king locations to match eligible_grays
    king_w_loc=[int(king_w_location_unformat[0]),int(king_w_location_unformat[1])]
    king_b_loc=[int(king_b_location_unformat[0]),int(king_b_location_unformat[1])]
    return [king_w_loc,king_b_loc]


def check_forcheck_mate():
    #get color who's turn it is
    if determine_ifturn()=="white":
        color="white"
        opposite_color="black"
    else:
        color="black"
        opposite_color="white"
    #get all the moves of the color
    pieces_lists=format_pieces_separatelists(color)
    pieces_namelist=pieces_lists[0]
    pieces_locslist=pieces_lists[1]
    #set blank list for legal moves
    all_legalmoves=[]
    #for each piece in the list
    for index in range(len(pieces_namelist)):
        #get piece name and location
        name=pieces_namelist[index]
        loc=pieces_locslist[index]
        #get the moves, then legal moves
        moves=determine_spaces(name,color,loc)
        legalmoves=get_legalmoves(moves,[name,color],loc)
        #add legal moves, to a list
        all_legalmoves.append(legalmoves)

    #for each value in the list of legal moves
    for moves in all_legalmoves:
        #if any piece is not legal, the game is over
        if moves is not None and moves != []:
            #return false, there is no checkmate
            return False
    #if the code runs this, there are no moves
    #if the color is not in check, it is a stalemate
    if check_forcheck(opposite_color) == False:
        return [None,"Stalemate, "]
    #if the color is in check, and has no moves, checkmate
    return [opposite_color,"Checkmate! "]


def check_for_insufficient_material(color_tobechecked):
    global white_nomaterial,black_nomaterial
    #get list of names for that color
    names=format_pieces_separatelists(color_tobechecked)[0]
    #need to check for any queens, pawns, rooks, and less than 2 knights + bishops
    if "queen" in names:
        return False
    if "rook" in names:
        return False
    if "pawn" in names:
        return False
    if names.count("knight") + names.count("bishop") >= 2:
        return False
    #if they have gotten this far, that color has insufficient material, let the variables know
    if color_tobechecked == "white":
        white_nomaterial=True
    else:
        black_nomaterial=True
    #if there is no material, let the rest of the program know
    if white_nomaterial == True and black_nomaterial == True:
        create_game_over_screen(None,"Draw, ")
def check_for_checkmatebutton_click(x,y):
    #simple hard-coded elements, checking for the click of a button with turtle
    if y > 250 and y < 300:
        y_click=True
    else:
        y_click=False
    if x > -25 and x < 25:
        x_click=True
    else:
        x_click=False
    if x_click and y_click == True:
        return True
    else:
        return False

def format_pieces_separatelists(color):
    #get unformatted lists
    locations_list=get_locations()
    names_list=get_pieces()
    #create parallel lists
    namelist=[]
    loclist=[]
    #create a counter, so we can identify the parallel location to this piece name
    counter=0

    for name_unformatted in names_list:
        #determine the color and name from a value such as "w_knight"
        name_andcolor=determine_name_and_color(name_unformatted)
        #separate name and color
        piece_name=name_andcolor[0]
        piece_color=name_andcolor[1]
        #determine the location of this piece as well, through the parallel lists of the text file
        location_ofpiece=locations_list[counter]
        #add name to list
        if piece_color == color:
            namelist.append(piece_name)
            loclist.append(location_ofpiece)
        #increment counter to identify the next
        counter+=1
    #every piece name, and the parallel location
    return [namelist,loclist]

#ran twice, and check is checked for in between. First run is to move pieces, then check is checked for, then second
#iteration is for resetting all values, so the player can play and the code can know what is legal
def update_file_check_forchecks(name_andcolor,old_loc_unformatted,new_loc_unformatted,resetting=False):
    global takenpiece_loc,takenpiece_name,index_oftaken
    file_copy=[]
    #in some scenarios, locations are formatted wrong
    old_loc=str(old_loc_unformatted[0])+str(old_loc_unformatted[1])
    new_loc=str(new_loc_unformatted[0])+str(new_loc_unformatted[1])
    #open file
    file_values=open("chesslocations.txt", "r")
    for value in file_values:
        #removes our name and old loc from list
        if value != (name_andcolor+","+str(old_loc)+"\n"):
            file_copy.append(value)
    file_values.close()
    #remove piece we are moving
    names_list=[]
    locs_list=[]
    #file copy is a list of piece name, color, and locations
    for value in file_copy:
        name=""
        #get list of names
        index=0
        for _ in value:
            #extract piece name before comma
            if value[index] != ",":
                name+=value[index]
                index+=1
            else:
                break

        #the line underneath this set index at the index of the first number
        index+=1
        #append name to list
        names_list.append(name)
        #get location, append to list
        location=value[index]+value[index+1]
        locs_list.append(location)
    
    #temporarily taken piece, track details
    if resetting == False:
        #if this move is a take (or our new location is in the list), update the variables
        if new_loc in locs_list:
            index_oftaken=locs_list.index(new_loc)
            takenpiece_name=names_list[index_oftaken]
            takenpiece_loc=locs_list[index_oftaken]
            file_copy.pop(index_oftaken)
        #if the move is not a take, reset them
        else:
            takenpiece_loc=""
            takenpiece_name=""
    #if we are resetting the file, place back the piece that we "took"
    if resetting == True:
        #we only do this, if we took a piece in the first place
        if takenpiece_loc != "" and takenpiece_name != "":
            file_copy.append(takenpiece_name+","+takenpiece_loc+"\n")
    #add new value, of the original moving piece
    file_copy.append((name_andcolor+","+str(new_loc)+"\n"))
    #update the actual file
    file_needs_updating=open("chesslocations.txt","w")
    for value in file_copy:
        file_needs_updating.write(value)
    file_needs_updating.close()


def get_legalmoves(moves,color_and_name,old_loc):
    if moves is None:
        return None
    #format color and name for updating file
    file_colorandname=str(str((color_and_name[1][0]))+"_"+str((color_and_name[0])))
    #get opposite color
    if determine_ifturn() == "white":
        opposite_color="black"
    else:
        opposite_color="white"
    #iterate through moves, and check for check
    real_legalmoves=[]
    for move in moves:
        #update file like we did that move
        update_file_check_forchecks(file_colorandname,old_loc,move)
        #if there's no check, thats a legal move
        if check_forcheck(opposite_color) == False:
            real_legalmoves.append(move)
        #update the file back
        update_file_check_forchecks(file_colorandname,move,old_loc,resetting=True)
    return real_legalmoves

   
def check_forcheck(opposite_color):
    #get locations of every piece
    pieces_lists=format_pieces_separatelists(opposite_color)
    pieces_names=pieces_lists[0]
    pieces_locs=pieces_lists[1]
    #go through every piece name and location, and find their moves
    pieces_moves=[]
    for index in range(len(pieces_names)):
        name=pieces_names[index]
        oldloc=pieces_locs[index]
        piece_move=determine_spaces(name,opposite_color,oldloc)
        #append to list
        pieces_moves.append(piece_move)
    #get king locations, for the opposite color for color who's turn it is
    both_kinglocs=get_kinglocs()
    if opposite_color=="white":
        current_kingloc=both_kinglocs[1]
    else:
        current_kingloc=both_kinglocs[0]
    #get each individual list of piece moves
    for individual_piecemoves in pieces_moves:
        #if they have any moves
        if individual_piecemoves is not None:
            #if the king location is IN the list of moves
            if current_kingloc in individual_piecemoves:
                #return true, because there is a check
                return True
    #if that doesn't return true, return false     
    return False


#translate a cord like 1,1 to -240,-240 for turtle to locate
def determine_graylocations_canvas(graylocations_board):
    cords_ofgrays=[]
    cords_of_canvasgrays=[]
    #graylocations is a list of lists, need to have a list of numbers like 44, not [4,4]
    for value in graylocations_board:
        cords_ofgrays.append(int(str(value[0])+str(value[1])))
    #for every location of gray, separate x and y
    for cords in cords_ofgrays:
        cord_x=int(str(cords)[0])
        cord_y=cords%10
        #make list to iterate easier through cords
        cords=[cord_x,cord_y]
        #make new variable so we can append later
        cords_of_thisgray=[]
        #turns 44 (44 is example) into canvas cords
        for cord in cords:
            #starting value, lowest
            starting_val=-210
            #iterate 8 times
            for index in range(8):
                #if the cord = index+1 (4=4)
                if cord == index+1:
                    #append the canvas cord
                    cords_of_thisgray.append(starting_val)
                    #break this loop
                    break
                else:
                    #add 60 (space between chess spaces in turtle units) each iteration
                    starting_val+=60
        cords_of_canvasgrays.append(cords_of_thisgray)
    return cords_of_canvasgrays


#create gray spots
def create_grays(cordlist):
    global turtle_graylist
    for cord in cordlist:
        gray=trtl.Turtle(shape="circle")
        turtle_graylist.append(gray)
        gray.shapesize(1)
        gray.color("white")
        gray.goto(cord[0],cord[1])
        gray.stamp()

def clear_all_grays():
    global turtle_graylist
    for turtle in turtle_graylist:
        turtle.clear()
    turtle_graylist=[]


#identify when a pawn moves up two squares, and append values to list for en passants
def note_en_passant(new_loc,old_loc,color,new_board_loc):
    global en_p_pawnlocs_w,en_p_pawnlocs_b,en_p_grays_b,en_p_grays_w
    #if the pawn moved two squares in one turn
    if abs(new_loc[1] - old_loc[1]) == 120:
        #get the location where a pawn would capture it in an en passant
        en_p_yval= int((new_loc[1]+piece_click_loc_canvas[1])/2)
        en_p_loc_canvas=[new_loc[0],en_p_yval]
        #format canvas cords into board cords
        en_p_loc_board_unformatted=determine_cords(en_p_loc_canvas[0],en_p_loc_canvas[1])
        en_p_loc_board=[en_p_loc_board_unformatted[0],en_p_loc_board_unformatted[1]]
        #append to lists for later use
        if color == "white":
            en_p_grays_w.append(en_p_loc_board)
            en_p_pawnlocs_w.append(new_board_loc)
        else:
            en_p_grays_b.append(en_p_loc_board)
            en_p_pawnlocs_b.append(new_board_loc)
#identify when a piece captures in en passant
def identify_en_passant(new_loc_canvas):
    global en_p_white
    global en_p_black
    #set variables
    new_loc_xval=new_loc_canvas[0]
    new_loc_yval=new_loc_canvas[1]
    #get board locs
    more_locs=determine_cords(new_loc_xval,new_loc_yval)
    new_board_locs=[more_locs[0],more_locs[1]]
    #if the move is an en passant, for black taking white
    if new_board_locs in en_p_grays_w:
        #get the index to remove from lists
        index_toremove=en_p_grays_w.index(new_board_locs)
        #remove from lists
        en_p_grays_w.pop(index_toremove)
        en_p_pawnlocs_w.pop(index_toremove)
        #this variable will be used in update_file, to let the function know that the piece that needs 
        #to be take is 1 space higher than the space the pawn moved to
        en_p_white=True
    #identical code, for black
    if new_board_locs in en_p_grays_b:
        #get the index to remove from lists
        index_toremove=en_p_grays_b.index(new_board_locs)
        #remove from lists
        en_p_grays_b.pop(index_toremove)
        en_p_pawnlocs_b.pop(index_toremove)
        #this variable will be used in update_file, to let the function know that the piece that needs to be take is 1 space higher than the space the pawn moved to
        en_p_black=True


def update_game_enpassant(color,new_loc,locations_list,names_list,new_loc_canvas):
    if color == "white":
        #identify the index of taken pawn in lists, to remove later
        #this y value is 1 higher, because its an en passant
        takenpawn_loc=str(new_loc[0]+str((int(new_loc[1])+1)))
        index_oftakenpawn=locations_list.index(takenpawn_loc)
        #identify the canvas cords of the taken pawn
        canvas_takenpawnloc=(new_loc_canvas[0],new_loc_canvas[1]+60)
    if color == "black":
        #identify same variables, but for black
        takenpawn_loc=str(new_loc[0]+str((int(new_loc[1])-1)))
        index_oftakenpawn=locations_list.index(takenpawn_loc)
        canvas_takenpawnloc=(new_loc_canvas[0],new_loc_canvas[1]-60)
    #remove that pawn from lists
    locations_list.pop(index_oftakenpawn)
    names_list.pop(index_oftakenpawn)
    #add square after move, indicate that it is an en passant capture
    add_square_aftermove(en_passant_addsquareloc=canvas_takenpawnloc)


def initiate_pawnpromotion(xcord_click,ycord_click):
    global pawn_promote_current_black, pawn_promote_current_white
    #check for individual colors, get the location (canvas), and file name of piece
    if pawn_promote_current_white==True:
        piece_clicked_promote=determine_pawnpromote_click(xcord_click,ycord_click,"white")
    else:
        piece_clicked_promote=determine_pawnpromote_click(xcord_click,ycord_click,"black")
    #account for when they do not click on any promotion options
    if piece_clicked_promote==None:
        return ""
    #add square on location of promotion, and add correct piece
    promote_filename=piece_clicked_promote[0]
    promote_xcord_canvas=piece_clicked_promote[1]
    promote_ycord_canvas=piece_clicked_promote[2]
    #add square to remove pawn that has been promoted
    add_square_aftermove(pawn_promote=[promote_xcord_canvas,promote_ycord_canvas])
    #add promoted piece
    promoted_piece=trtl.Turtle(shape=promote_filename)
    promoted_piece.goto(promote_xcord_canvas,promote_ycord_canvas)
    promoted_piece.stamp()


def create_options_promotion(color,pawn_loc):
    #variable for understand request function to understand what is going on
    global pawn_promote_current_white,pawn_promote_current_black
    global spot_turtlelist
    global spot_list
    global pieces_files_w
    global pieces_files_b
    if color=="white":
        pawn_promote_current_white=True
    else:
        pawn_promote_current_black=True
    #create list to append later
    spot_list=[]
    #list of piece options
    pieces_files_w=["white_queen.gif","white_knight.gif","white_bishop.gif","white_rook.gif"]
    pieces_files_b=["black_queen.gif","black_knight.gif","black_bishop.gif","black_rook.gif"]
    #decide variables based on color
    pawn_loc_xval=pawn_loc[0]
    if color == "white":
        #add 60 because our options for pawn promotion will be just above the board
        spotloc_yval=pawn_loc[1]+60
    else:
        spotloc_yval=pawn_loc[1]-60
    #make locations for options to go to, append to list
    for index in range(4):
        #spot is now the spot of each turtle, when each option on a promotion is the turtle
        spot=[pawn_loc_xval+(index*60),spotloc_yval]
        spot_list.append(spot)
    #determine what colors the options should be
    if color == "white":
        list_to_use=pieces_files_w
    else:
        list_to_use=pieces_files_b
    #use counter to count the file
    file_counter=0
    spot_turtlelist=[]
    for spot in spot_list:
        #creates turtle, goes to the spot, determines correct shape
        turtle=trtl.Turtle(shape="circle")
        turtle.shape(list_to_use[file_counter])
        turtle.goto(spot)
        turtle.stamp()
        #append the turtles to list, to clear later
        spot_turtlelist.append(turtle)
        #iterates through file counter so the shapes change
        file_counter+=1


def determine_pawnpromote_click(xcord,ycord,color):
    global spot_list
    global pawn_promote_current_white,pawn_promote_current_black
    global spot_turtlelist
    #determine where the click needs to be on y axis, based on color
    if color == "white":
        yval_correctspot=270
        #get location of pawn that is being promoted for later
        pawn_promote_ycord=(spot_list[0][1])-60
    else:
        yval_correctspot=-270
        pawn_promote_ycord=(spot_list[0][1])+60
    #if the click was on the correct y area
    if (ycord > yval_correctspot-30) and (ycord < yval_correctspot+30):
        #iterate through spotlist
        for spot in spot_list:
            spot_xcord=spot[0]
            #if the click is at that spot (approximately)
            if (xcord > spot_xcord - 30) and (xcord < spot_xcord + 30):
                #determine what index the spot is in spot list
                index_ofclickedspot=spot_list.index(spot)
                #determine what file list to use
                if color == "white":
                    use_filelist=pieces_files_w
                    #get makes us able to move afterwards
                    pawn_promote_current_white=False
                else:
                    use_filelist=pieces_files_b
                    pawn_promote_current_black=False
                #get the file of the space that was clicked on
                file_clicked=use_filelist[index_ofclickedspot]
                #clear spot_turtlelist
                for turtle in spot_turtlelist:
                    turtle.clear()
                spot_turtlelist=[]
                #get canvas locations of pawn that is being promoted
                pawn_promote_xcord=spot_list[0][0]
                #updates file about new piece
                update_file([pawn_promote_xcord,pawn_promote_ycord],promotion=file_clicked)
                return file_clicked,pawn_promote_xcord,pawn_promote_ycord  
               
def get_name_andcolor_fromfile(file_name):
    color=""
    name=""
    #get the name
    for index in range(len(file_name)):
        #for each value before the _ add to name
        if file_name[index] != "_":
            color+=file_name[index]
        else:
            index += 1
            break
    #index is already at beginning of the name
    for blank in file_name:
        if file_name[index] != ".":
            name+=file_name[index]
            index+=1
        else:
            break
    return color,name
   
def create_checkmate_button():
    button=trtl.Turtle(shape="square")
    button.penup()
    button.color("purple")
    button.goto(0,275)
    button.stamp()

def create_game_over_screen(color_winner, method_of_ending):
    create_gameover_backgroundscreen()
    write_winning_text(color_winner,method_of_ending)
    make_retry_button()

def create_gameover_backgroundscreen():
    #create the turtle
    background_square=trtl.Turtle()
    background_square.fillcolor("white")
    #move it to the right area
    background_square.penup()
    background_square.goto(-150,-350)
    background_square.pendown()
    #make a box with it
    background_square.begin_fill()
    for blank in range(2):
        background_square.forward(300)
        background_square.left(90)
        background_square.forward(100)
        background_square.left(90)
    background_square.end_fill()
    background_square.hideturtle()


def write_winning_text(color_winner,method_of_ending):
    if color_winner is None:
        color_winner = "Nobody"
    else:
        #turns color winner to White or Black instead of white/black
        color_winner_editing=list(color_winner)
        color_firstletter=color_winner_editing.pop(0)
        color_firstletter_upper=color_firstletter.upper()
        color_winner_editing.insert(0,color_firstletter_upper)
        color_winner=""
        for letter in color_winner_editing:
            color_winner+=letter
    writer=trtl.Turtle()
    writer.penup()
    writer.goto(-100,-275)
    writer.write(method_of_ending+color_winner+" Wins", font=font_default)
    writer.hideturtle()


def start_game():
    #set all of our global variables, and set them back to their starting values
    global piece_click_loc_board,black_nomaterial,white_nomaterial,takenpiece_loc,takenpiece_name,retry_button_current
    global dl_rookmove,dr_rookmove,ur_rookmove,ul_rookmove,wking_move,bking_move
    global en_p_pawnlocs_b,en_p_pawnlocs_w,en_p_grays_w,en_p_grays_b,en_p_white,en_p_black,pawn_promote_current_black,pawn_promote_current_white
    global move_counter,turtle_graylist
    #set variable to avoid reference before assignment
    piece_click_loc_board=""
    black_nomaterial=False
    white_nomaterial=False
    takenpiece_loc=""
    takenpiece_name=""
    retry_button_current=False
    #castling global variables
    dl_rookmove=False
    dr_rookmove=False
    ur_rookmove=False
    ul_rookmove=False
    wking_move=False
    bking_move=False
    #lists for en passant, so we can append later
    en_p_pawnlocs_w=[]
    en_p_pawnlocs_b=[]
    en_p_grays_w=[]
    en_p_grays_b=[]
    en_p_white=False
    en_p_black=False
    #pawn promote variables
    pawn_promote_current_white=False
    pawn_promote_current_black=False
    #more variables
    move_counter=0
    turtle_graylist=[]
    #reset the file, which moves pieces back to their starting squares
    reset_file()
    #creates the board
    create_board()
    #creates checkmate button
    create_checkmate_button()
    #creates the pieces
    create_pieces_start()


def make_retry_button():
    button=trtl.Turtle()
    button.penup()
    button.hideturtle()
    button.goto(-60,-335)
    button.fillcolor("dark gray")
    button.begin_fill()
    for blank in range(2):
        button.forward(120)
        button.left(90)
        button.forward(50)
        button.left(90)
    button.end_fill()
    button.hideturtle()
    redo_writer=trtl.Turtle()
    redo_writer.penup()
    redo_writer.hideturtle()
    redo_writer.goto(-45,-320)
    redo_writer.color("white")
    redo_writer.write("Play again?", font=font_default)

    global retry_button_current
    retry_button_current=True

def checkfor_retrybutton_click(xcord,ycord):
    if xcord >= -60 and xcord <= 60 and ycord <=-285 and ycord >=-335:
        clear_retrybutton_area()
        return True
    else:
        return False

def clear_retrybutton_area():
    cleaner=trtl.Turtle(shape="square")
    cleaner.color(bgcolor)
    cleaner.penup()
    cleaner.goto(0,-300)
    cleaner.shapesize(20)
    cleaner.stamp()
if __name__ == "__main__":
    start_game()
    #on click, run our main function
    wn.onclick(understand_request)
    wn.bgcolor(bgcolor)
    wn.mainloop()