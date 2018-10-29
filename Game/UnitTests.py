import unittest
from unittest.mock import patch
from TournamentManager.tournament import Player
import TournamentManager.tournament as tt


class TestMethods(unittest.TestCase):
    def test_player_creation(self):
        player = Player(1, "Arvid", 99, True, 3, 3)
        self.assertEqual(player.__repr__(), "(1, 'Arvid', 99, True, 3, 3)")

    def test_player_set_item(self):
        player = Player(2, "Victor", 0, False, 0, 0)
        player.__setitem__(2, 3)
        self.assertEqual(player.__getitem__(2), 3)

    def test_update_score(self):
        player = Player(2, "Victor", 0, False, 0, 0)
        i = 0
        while(i < 10):
            i += 2
            player.update_score(1)
        self.assertEqual(player.points, 5)

    @patch('TournamentManager.tournament.select_game_type', return_value='1')
    def test_game_type1(self, input):
        self.assertEqual(tt.select_game_type(), '1')

    @patch('TournamentManager.tournament.select_game_type', return_value='2')
    def test_game_type2(self, input):
        self.assertEqual(tt.select_game_type(), '2')

    @patch('TournamentManager.tournament.select_game_type', return_value='3')
    def test_game_type3(self, input):
        self.assertEqual(tt.select_game_type(), '3')

    @patch('TournamentManager.tournament.select_game_type', return_value='4')
    def test_game_type4(self, input):
        self.assertEqual(tt.select_game_type(), '4')

    @patch('TournamentManager.tournament.select_game_type', return_value='5')
    def test_game_type5(self, input):
        self.assertEqual(tt.select_game_type(), '5')

    @patch('TournamentManager.tournament.input_players', return_value='3')
    def test_input_players3(self, input):
        self.assertEqual(tt.input_players(), '3')

    @patch('TournamentManager.tournament.input_players', return_value='4')
    def test_input_players4(self, input):
        self.assertEqual(tt.input_players(), '4')

    @patch('TournamentManager.tournament.input_players', return_value='5')
    def test_input_players5(self, input):
        self.assertEqual(tt.input_players(), '5')

    @patch('TournamentManager.tournament.input_players', return_value='6')
    def test_input_players6(self, input):
        self.assertEqual(tt.input_players(), '6')

    @patch('TournamentManager.tournament.input_players', return_value='7')
    def test_input_players7(self, input):
        self.assertEqual(tt.input_players(), '7')

    @patch('TournamentManager.tournament.input_players', return_value='8')
    def test_input_players8(self, input):
        self.assertEqual(tt.input_players(), '8')

    @patch('TournamentManager.tournament.select_cpu_level', return_value='1')
    def test_select_cpu_level1(self, input):
        self.assertEqual(tt.select_cpu_level(), '1')

    @patch('TournamentManager.tournament.select_cpu_level', return_value='2')
    def test_select_cpu_level2(self, input):
        self.assertEqual(tt.select_cpu_level(), '2')

    @patch('TournamentManager.tournament.select_cpu_level', return_value='3')
    def test_select_cpu_level3(self, input):
        self.assertEqual(tt.select_cpu_level(), '3')

    @patch('TournamentManager.tournament.select_cpu', return_value='True')
    def test_if_cpu_True(self, input):
        self.assertEqual(tt.select_cpu(), 'True')

    @patch('TournamentManager.tournament.select_cpu', return_value='False')
    def test_if_cpu_False(self, input):
        self.assertEqual(tt.select_cpu(), 'False')

    def test_name_width(self):

        players = []

        new_player = Player(0, "Test1", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(1, "TestingALongName", 0, False, 0, 0)
        players.append(new_player)

        self.assertEqual(tt.name_width(players), 16)

    def test_name_width2(self):
        players = []
        self.assertEqual(tt.name_width(players), 4)

    def test_name_width3(self):
        players = []

        new_player = Player(0, "", 0, False, 0, 0)
        players.append(new_player)

        self.assertEqual(tt.name_width(players), 4)

    def test_name_width4(self):
        players = []

        new_player = Player(0, "Arvid", 0, False, 0, 0)
        players.append(new_player)

        self.assertEqual(tt.name_width(players), 5)

    def test_sort_played1(self):

        players = []

        new_player1 = Player(0, "Test1", 8, False, 0, 2)
        players.append(new_player1)
        new_player2 = Player(1, "TestingALongName", 9, False, 0, 4)
        players.append(new_player2)
        new_player3 = Player(2, "test3", 5, False, 0, 6)
        players.append(new_player3)
        new_player4 = Player(3, "test4", 2, False, 0, 7)
        players.append(new_player4)
        new_player5 = Player(4, "test5", 6, False, 0, 5)
        players.append(new_player5)
        new_player6 = Player(5, "test6", 10, False, 0, 0)
        players.append(new_player6)
        new_player7 = Player(6, "test7", 3, False, 0, 0)
        players.append(new_player7)
        new_player8 = Player(7, "test8", 4, False, 0, 0)
        players.append(new_player8)

        self.assertEqual(tt.update_list(players), [new_player6, new_player2, new_player1, new_player5, new_player3,
                                                   new_player8, new_player7, new_player4])

    def test_sort_played2(self):
        players = []

        new_player = Player(0, "Test1", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(1, "TestingALongName", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(2, "test3", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(3, "test4", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(4, "test5", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(5, "test6", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(6, "test7", 0, False, 0, 0)
        players.append(new_player)
        new_player = Player(7, "test8", 0, False, 0, 0)
        players.append(new_player)

        self.assertEqual(tt.sort_played(players), )
if __name__ == '__main__':
    unittest.main()
