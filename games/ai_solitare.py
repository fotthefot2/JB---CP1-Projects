import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
RED_SUITS = ['♥', '♦']

class Card:
    def __init__(self, suit, rank, face_up=False):
        self.suit = suit
        self.rank = rank
        self.face_up = face_up

    @property
    def value(self):
        return RANKS.index(self.rank) + 1

    @property
    def color(self):
        return 'red' if self.suit in RED_SUITS else 'black'

    def __str__(self):
        if not self.face_up:
            return "[ ░░░ ]"
        return f"[{self.rank:>2}{self.suit}]"

class Solitaire:
    def __init__(self):
        self.deck = [Card(s, r) for s in SUITS for r in RANKS]
        random.shuffle(self.deck)
        
        self.stock = []
        self.waste = []
        self.foundations = {s: [] for s in SUITS}
        self.tableau = [[] for _ in range(7)]
        
        self.setup_game()

    def setup_game(self):
        for i in range(7):
            for j in range(i + 1):
                card = self.deck.pop()
                if j == i:
                    card.face_up = True
                self.tableau[i].append(card)
        self.stock = self.deck

    def display(self):
        print("\n" + "=" * 50)
        
        stock_str = f"[{len(self.stock)} cards]" if self.stock else "[Empty]"
        waste_str = str(self.waste[-1]) if self.waste else "[Empty]"
        
        print(f" Stock: {stock_str:<12} Waste: {waste_str}")
        print("-" * 50)
        
        found_str = "  ".join([
            f"{s}: {self.foundations[s][-1] if self.foundations[s] else '[   ]'}" 
            for s in SUITS
        ])
        print(f" Foundations:  {found_str}")
        print("=" * 50)
        
        print(" Tableau:")
        max_height = max(len(col) for col in self.tableau)
        headers = "    ".join([f"({i+1})" for i in range(7)])
        print(f"   {headers}")
        
        for row in range(max_height):
            row_cards = []
            for col in self.tableau:
                if row < len(col):
                    row_cards.append(str(col[row]))
                else:
                    row_cards.append("       ")
            print("   " + "  ".join(row_cards))
        print("=" * 50)

    def draw_card(self):
        if self.stock:
            card = self.stock.pop()
            card.face_up = True
            self.waste.append(card)
        elif self.waste:
            while self.waste:
                card = self.waste.pop()
                card.face_up = False
                self.stock.append(card)
            print("Recycled waste pile back to stock.")
        else:
            print("No cards left in stock or waste!")

    def move_waste_to_foundation(self, suit):
        if not self.waste:
            print("Waste pile is empty!")
            return False
            
        card = self.waste[-1]
        if card.suit != suit:
            print(f"Card {card} does not match foundation suit {suit}.")
            return False
            
        target_f = self.foundations[suit]
        expected_val = len(target_f) + 1
        
        if card.value == expected_val:
            self.foundations[suit].append(self.waste.pop())
            return True
        else:
            print(f"Cannot place {card} on {suit} foundation.")
            return False

    def move_waste_to_tableau(self, col_idx):
        if not self.waste:
            print("Waste pile is empty!")
            return False
            
        card = self.waste[-1]
        target_col = self.tableau[col_idx]
        
        if self._can_place_on_tableau(card, target_col):
            target_col.append(self.waste.pop())
            return True
        return False

    def move_tableau_to_tableau(self, src_col, src_row, dest_col):
        source = self.tableau[src_col]
        destination = self.tableau[dest_col]
        
        if src_row >= len(source) or not source[src_row].face_up:
            print("Invalid source card position.")
            return False
            
        moving_cards = source[src_row:]
        first_moving = moving_cards[0]
        
        if self._can_place_on_tableau(first_moving, destination):
            destination.extend(moving_cards)
            self.tableau[src_col] = source[:src_row]
            if self.tableau[src_col] and not self.tableau[src_col][-1].face_up:
                self.tableau[src_col][-1].face_up = True
            return True
        return False

    def move_tableau_to_foundation(self, col_idx, suit):
        col = self.tableau[col_idx]
        if not col:
            print("Column is empty!")
            return False
            
        card = col[-1]
        if card.suit != suit:
            print(f"Card {card} does not match foundation suit {suit}.")
            return False
            
        target_f = self.foundations[suit]
        if card.value == len(target_f) + 1:
            self.foundations[suit].append(col.pop())
            if col and not col[-1].face_up:
                col[-1].face_up = True
            return True
        else:
            print(f"Cannot place {card} on {suit} foundation.")
            return False

    def _can_place_on_tableau(self, card, target_column):
        if not target_column:
            return card.rank == 'K'
        
        top_card = target_column[-1]
        return (card.color != top_card.color) and (card.value == top_card.value - 1)

    def is_won(self):
        return sum(len(f) for f in self.foundations.values()) == 52

def run_game():
    game = Solitaire()
    
    while not game.is_won():
        game.display()
        print("\nCommands:")
        print("  d             - Draw card from stock")
        print("  wf <suit>     - Move waste to foundation (e.g., 'wf ♠')")
        print("  wt <col>      - Move waste to tableau column (1-7)")
        print("  tt <s_col> <s_row> <d_col> - Move tableau stack")
        print("  tf <col> <suit> - Move tableau top card to foundation")
        print("  q             - Quit")
        
        cmd = input("\nEnter command: ").strip().lower().split()
        if not cmd:
            continue
            
        action = cmd[0]
        
        try:
            if action == 'q':
                print("Thanks for playing!")
                break
            elif action == 'd':
                game.draw_card()
            elif action == 'wf' and len(cmd) == 2:
                game.move_waste_to_foundation(cmd[1])
            elif action == 'wt' and len(cmd) == 2:
                game.move_waste_to_tableau(int(cmd[1]) - 1)
            elif action == 'tt' and len(cmd) == 4:
                game.move_tableau_to_tableau(int(cmd[1]) - 1, int(cmd[2]) - 1, int(cmd[3]) - 1)
            elif action == 'tf' and len(cmd) == 3:
                game.move_tableau_to_foundation(int(cmd[1]) - 1, cmd[2])
            else:
                print("Invalid command syntax.")
        except (IndexError, ValueError):
            print("Invalid parameters provided.")

    if game.is_won():
        print("\n🎉 Congratulations! You solved Solitaire! 🎉")

if __name__ == "__main__":
    run_game()