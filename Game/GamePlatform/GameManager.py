from GamePlatform.GameBoard import GameBoard
from GamePlatform.GameRules import detect_mill, is_blocked, who_has_less_than_three
from GamePlatform.Player import Player
from GamePlatform.StdinController import StdinController
from TournamentManager.MatchResult import MatchResult

from GameEngine.ComputerController import ComputerController
from time import sleep

TURNS_FOR_DRAW = 400
DEFAULT_STONES = 9


class GameManager:
    def __init__(self, renderer, tournament_players):
        self.renderer = renderer
        self.players = []
        self.tournament_players = tournament_players

        # Convert
        stone_type = "black"
        for tournament_player in tournament_players:
            player = Player(stone_type, tournament_player, DEFAULT_STONES)
            if(tournament_player.cpu == True):
                player.set_controller(ComputerController(player, complexity = tournament_player.cpu_level))
            else:
                player.set_controller(StdinController(player))
            self.players.append(player)
            stone_type = "white"

        self.board = GameBoard()

        self.phase = 1
        self.step_count = 0

    def start_game(self):
        winner = self.game_step()
        self.renderer.render_winner(winner)
        if winner is not None:
            return winner.tournament_player
        else:
            return None

    def game_step(self):
        is_game_over = False
        winner = None

        while not is_game_over:
            sleep(0.2) # For CPU Agains CPU
            if self.step_count > TURNS_FOR_DRAW:
                winner = None
                return winner

            current_player = self.players[self.step_count % len(self.players)]

            self.renderer.begin_render()
            self.renderer.render_phase(self.phase)
            self.renderer.print_player_stones(self.players)
            self.renderer.render(self.board)
            self.renderer.print_player_turn(current_player)

            move = current_player.controller.make_move(self.board, self.phase)
            n_mills = detect_mill(self.board, move)
            if n_mills > 0:
                self.renderer.begin_render()
                self.renderer.render_phase(self.phase)
                self.renderer.print_player_stones(self.players)
                self.renderer.render(self.board)
                self.renderer.print_player_turn(current_player)
                current_player.controller.remove_stone(self.board)

            other_players = [
                player for player in self.players
                if player is not current_player
            ]

            if self.phase == 1:
                move.player.n_stones -= 1
            if self.phase == 1 and self.should_start_phase2():
                self.phase = 2

            if self.phase == 2:
                if is_blocked(self.board, other_players[0]):
                    winner = current_player
                    return winner
                has_less_than_three = who_has_less_than_three(
                    self.board, self.players)
                if (has_less_than_three is not None):
                    other_players = [
                        player for player in self.players
                        if player is not has_less_than_three
                    ]
                    winner = other_players[0]
                    return winner

            self.step_count += 1

    def should_start_phase2(self):
        return all(player.n_stones == 0 for player in self.players)
