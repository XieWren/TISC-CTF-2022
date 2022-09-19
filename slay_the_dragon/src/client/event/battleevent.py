from typing import Optional

from client import GameClient
from client.error import Error
from client.ui import screens
from core.models import Boss, Command, Result


class BattleEvent:
    def __init__(self, client: GameClient) -> None:
        self.client = client
        self.player = client.player

    def run(self):
        self.boss: Boss = self.client.fetch_next_boss()

        while True:
            self.__display()

            match self.__get_battle_command():
                case Command.ATTACK:
                    self.__attack_boss()
                    if self.boss.is_dead:
                        break
                case Command.HEAL:
                    self.__use_potion()
                case Command.RUN:
                    self.client.send_command(Command.RUN)
                    return
                case _:
                    continue
                    
            # self.player.receive_attack_from(self.boss)                # Edited!
            if self.player.is_dead:
                break
        
        print(self.boss.hp)                                             # Edited!
        self.client.send_command_string("ATTACK "*self.boss.max_hp)     # Edited!
        self.client.send_command(Command.VALIDATE)
        print("Validated")                                              # Edited!

        if self.player.is_dead:
            self.__handle_death()
        print("Not dead")                                               # Edited!

        match self.client.fetch_result():
            case Result.VALIDATED_OK:
                screens.display_boss_slain_screen()
                return
            case Result.OBTAINED_FLAG:
                screens.display_flag_screen(self.client.fetch_flag())
                self.client.exit()
            case _:
                screens.display_error(Error.RECEIVED_MALFORMED_RESULT)
                self.client.exit(1)

    def __use_potion(self):
        self.client.send_command(Command.HEAL)
        self.player.use_potion()

    def __attack_boss(self):
        # self.client.send_command(Command.ATTACK)                      # Edited!
        self.boss.receive_attack_from(self.player)

    def __handle_death(self):
        screens.display_game_over_screen()
        self.client.exit()

    def __display(self):
        screens.display_battle_screen(player=self.player, boss=self.boss)

    def __get_battle_command(self) -> Optional[Command]:
        match input():
            case "1":
                return Command.ATTACK
            case "2":
                return Command.HEAL
            case "3":
                return Command.RUN
            case _:
                return None
