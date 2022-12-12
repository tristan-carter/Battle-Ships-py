import time

BOARDSIZE = 10

class Coord:
  x = None
  y = None
  def __init__(self, init_x, init_y):
    self.x = init_x
    self.y = init_y

  def __add__(self, other_coord):
    new_coord = Coord(self.x + other_coord.x, self.y + other_coord.y)
    return(new_coord)

  def __eq__(self, other_coord):
    return(self.x == other_coord.x and self.y == other_coord.y)

  def __str__(self):
    return(str(self.x) + ", " + str(self.y))

class Ship:
  lives = None
  squares = None
  type = None
  name = None
  
  def __init__(self, start_x, start_y, facingD):
    self.squares = []
    for i in range(self.lives):
      if facingD.lower() == "n":
        self.squares.append(Coord(start_x, start_y+i))
        
      elif facingD.lower() == "e":
        self.squares.append(Coord(start_x+i, start_y))
        
      elif facingD.lower() == "s":
        self.squares.append(Coord(start_x, start_y-i))
        
      elif facingD.lower() == "w":
        self.squares.append(Coord(start_x-i, start_y))


class Carrier(Ship):
  def __init__(self, start_x, start_y, facingD):
    self.lives = 5
    self.type = "Carrier"
    self.name = "C"

    Ship.__init__(self, start_x, start_y, facingD)

class Battleship(Ship):
  def __init__(self, start_x, start_y, facingD):
    self.lives = 4
    self.type = "Battleship"
    self.name = "B"

    Ship.__init__(self, start_x, start_y, facingD)
  
class Destroyer(Ship):
  def __init__(self, start_x, start_y, facingD):
    self.lives = 3
    self.type = "Destroyer"
    self.name = "D"

    Ship.__init__(self, start_x, start_y, facingD)

class Submarine(Ship):
  def __init__(self, start_x, start_y, facingD):
    self.lives = 3
    self.type = "Submarine"
    self.name = "S"

    Ship.__init__(self, start_x, start_y, facingD)

class PatrolBoat(Ship):
  def __init__(self, start_x, start_y, facingD):
    self.lives = 2
    self.type = "PatrolBoat"
    self.name = "P"

    Ship.__init__(self, start_x, start_y, facingD)

class BoardCell:
  coord = None
  ship = None
  def __init__(self, init_coord):
    self.coord = init_coord

class Board:
  board = None
  enemyHitsBy7u6oard = None
  enemyBoard = None
  
  userName = None
  enemyUserName = None
  userShips = None
  
  def __init__(self, initUserName, initEnemyUserName):
    self.userName = initUserName
    self.enemyUserName = initEnemyUserName

    self.enemyHitsBoard = [["□" for x in range(BOARDSIZE)] for y in range(BOARDSIZE)]
    self.board = [[BoardCell(Coord(x, y)) for x in range(BOARDSIZE)] for y in range(BOARDSIZE)]

    self.userShips = self.initiate_ships()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

  def initiate_ships_input(self, shipType, lives):
    while True:
      init_ship_xyd = input(self.userName + " please enter your " + shipType + "'s x y (from 1-10) and which way it will face from that point (N, E, S, W) e.g '2 5 N' ").split()
      #checks if it is a valid input
      start_x = int(init_ship_xyd[0])-1
      start_y = int(init_ship_xyd[1])-1
      facingD = init_ship_xyd[2].lower()
      if start_x <= 9 and start_x >= 0 and start_y <= 9 and start_y >= 0 and (facingD == "n" or facingD == "e" or facingD == "s" or facingD == "w"):
        #checks if the ship will overlap with another ship
        ship_squares = []
        for i in range(lives):
          if facingD == "n":
            ship_squares.append(Coord(start_x, start_y+i))
            
          elif facingD == "e":
            ship_squares.append(Coord(start_x+i, start_y))
            
          elif facingD == "s":
            ship_squares.append(Coord(start_x, start_y-i))
            
          elif facingD == "w":
            ship_squares.append(Coord(start_x-i, start_y))

        ship_collides = False
        for ship_square in ship_squares:
          if self.board[ship_square.x][ship_square.y].ship != None:
            ship_collides = True

        if not ship_collides:
          return start_x, start_y, facingD
        else:
          print("This ship position collides with another already placed ship, please try again")
      else:
        print("This ship position is invalid, please remember the correct format and try again")

  def place_new_ship(self, new_ship):
    for ship_coord in new_ship.squares:
        self.board[ship_coord.x][ship_coord.y].ship = new_ship
    print("\n")
    print(self)
      
  def initiate_ships(self):
    carrier_start_x, carrier_start_y, carrier_facingD = self.initiate_ships_input("Carrier", 5)
    new_carrier = Carrier(carrier_start_x, carrier_start_y, carrier_facingD)
    self.place_new_ship(new_carrier)
    
    battleship_start_x, battleship_start_y, battleship_facingD = self.initiate_ships_input("Battleship", 4)
    new_battleship = Battleship(battleship_start_x, battleship_start_y, battleship_facingD)
    self.place_new_ship(new_battleship)

    destroyer_start_x, destroyer_start_y, destroyer_facingD = self.initiate_ships_input("Destroyer", 3)
    new_destroyer = Destroyer(destroyer_start_x, destroyer_start_y, destroyer_facingD)
    self.place_new_ship(new_destroyer)
    
    submarine_start_x, submarine_start_y, submarine_facingD = self.initiate_ships_input("Submarine", 3)
    new_submarine = Submarine(submarine_start_x, submarine_start_y, submarine_facingD)
    self.place_new_ship(new_submarine)
    
    patrolboat_start_x, patrolboat_start_y, patrolboat_facingD = self.initiate_ships_input("Patrol Boat", 2)
    new_patrolboat = PatrolBoat(patrolboat_start_x, patrolboat_start_y, patrolboat_facingD)
    self.place_new_ship(new_patrolboat)
    
    new_ships = [new_carrier,
    new_battleship,
    new_destroyer,
    new_submarine,
    new_patrolboat]
    
    return(new_ships)

  def check_lives(self):
    total_lives = 0
    for y in range(BOARDSIZE):
      for x in range(BOARDSIZE):
        ship = self.board[x][y].ship
        if ship != None and ship != "X" and ship != "■":
          total_lives += ship.lives

    if total_lives == 0:
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
      print("GAME OVER")
      print(self.enemyUserName + " has won!")
      
      return False
    else:
      return True
  
  def enemy_destroy_square(self, square_coord):
    coord_cell = self.board[square_coord.x][square_coord.y]
    cell_ship = coord_cell.ship
    if cell_ship == None:
      cell_ship = "■"
      self.enemyHitsBoard[square_coord.x][square_coord.y] = "■"
      self.board[square_coord.x][square_coord.y].ship = "■"
      print("MISS")
      
    elif cell_ship != "■":
      cell_ship.lives -= 1

      for ship_square in cell_ship.squares:
        if ship_square == coord_cell.coord:
          cell_ship.squares.remove(ship_square)
      cell_ship = "X"
      self.enemyHitsBoard[square_coord.x][square_coord.y] = "X"
      self.board[square_coord.x][square_coord.y].ship = "X"
      print("HIT")
    else:
      print("MISS")
    
  def enemy_play_turn(self):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Enemy Board:")
    for y in range(BOARDSIZE-1, -1, -1):
      row = ""
      for x in range(BOARDSIZE):
        row += " "
        row += self.enemyHitsBoard[x][y]
      print(row)
    print("")
    print("Your Board:")
    print(self.enemyBoard)

    chosen_square = None
    square_coord = None
    while True:
      chosen_square = input(self.enemyUserName + " please enter a square to attack from 1-10 (e.g 1 5) ").split()
      target_x = int(chosen_square[0])
      target_y = int(chosen_square[1])
      
      if target_x <= 10 and target_x >= 1 and target_y <= 10 and target_y >= 1:
        square_coord = Coord(target_x-1, target_y-1)
        if self.enemyHitsBoard[square_coord.x][square_coord.y] != "■" and self.enemyHitsBoard[square_coord.x][square_coord.y] != "X":
          break
        else:
          print("you have already attacked this square, please try again and choose a different one")
      else:
        print("The square you entered to attack is invalid, please remember the correct format and try again")
      
    self.enemy_destroy_square(square_coord)

    return self.check_lives()
      
  def __str__(self):
    for y in range(BOARDSIZE-1, -1, -1):
      row = ""
      for x in range(BOARDSIZE):
        boardCell = self.board[x][y]
        row += " "
        if boardCell.ship != None and boardCell.ship != "X" and boardCell.ship != "■":
          row += boardCell.ship.name
        elif boardCell.ship == None:
          row += "□"
        else:
          row += boardCell.ship
      print(row)
    return ""

def main():
  user1Name = input("User1 please enter your username ")
  user2Name = input("User2 please enter your username ")
  
  user1Board = Board(user1Name, user2Name)
  user2Board = Board(user2Name, user1Name)
  
  user1Board.enemyBoard = user2Board
  user2Board.enemyBoard = user1Board
  
  gamePlaying = True
  while gamePlaying:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Hand over to " + user2Name)
    time.sleep(3)
    gamePlaying = user1Board.enemy_play_turn()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if not gamePlaying:
      break
    
    print("Hand over to " + user1Name)
    time.sleep(3)
    gamePlaying = user2Board.enemy_play_turn()

if __name__ == "__main__":
    main()