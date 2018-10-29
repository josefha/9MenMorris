import unittest
from TournamentManager.tournament import Player
from GamePlatform.GameManager import GameManager
from GamePlatform.TerminalRenderer import TerminalRenderer
import TournamentManager.tournament


class IntegrationTests(unittest.TestCase):

    def test_player_list(self):
        player1 = Player(1, "arvid", 99, True, 3, 3)
        player2 = Player(1, "victor", 99, True, 3, 3)
        player_list = []
        player_list.append(player1)
        player_list.append(player2)
        game_manager = GameManager(TerminalRenderer(), player_list)

        self.assertEqual(game_manager.tournament_players, player_list)

    def test_winner(self):
        player1 = Player(1, "arvid", 99, True, 3, 3)
        player2 = Player(1, "victor", 99, True, 3, 3)
        player_list = []
        player_list.append(player1)
        player_list.append(player2)
        game_manager = GameManager(TerminalRenderer(), player_list)
        winner = game_manager.start_game()

        self.assertEqual(winner, game_manager.winner)