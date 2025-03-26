from random import randint

lista_npcs = []

player = {
    'name': 'Azhariel',
    'level': 1,
    'exp': 0,
    'exp_max': 30,
    'hp': 100,
    'hp_max': 100,
    'damage': 25,
}


def criar_npc(level):

    novo_npc = {
        'name': f'Monster #{level}',
        'level': level,
        'damage': 5 * level,
        'hp': 100 * level,
        'hp_max': 100 * level,
        'exp': 7 * level,
    }
    return novo_npc


def gerar_npcs(n_npcs):

    # o RANGE é útil pois poderemos, depois, gerar N npcs, apenas passando o número para a função
    for x in range(n_npcs):
        novo_npc = criar_npc(x + 1)
        lista_npcs.append(novo_npc)


def exibir_npc():
    for npc in lista_npcs:
        exibir_npc()


def exibir_npc(npc):
    for npc in lista_npcs:
        print(
            f"Name: {npc['name']} // Level: {npc['level']} // Damage: {npc['damage']} // HP: {npc['hp']} // EXP: {npc['exp']}"
        )


def exibir_player():
    print(
        f"Name: {player['name']} // Level: {player['level']} // Damage: {player['damage']} // HP: {player['hp']}/{player['hp_max']} //EXP: {player['exp']}//{player['exp_max']}"
    )


def reset_player():
    player['hp'] = player['hp_max']


def reset_npc(npc):
    npc['hp'] = npc['hp_max']


def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] = player['exp_max'] * 2
        player['hp_max'] = + 20
        player['damage'] = player['damage'] * 1.5


def iniciar_batalha(npc):
    while npc['hp'] > 0 and player['hp'] > 0:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)

    if player['hp'] > 0:
        print(f'{player['name']} WINS! + {npc['exp']} EXP!')
        player['exp'] += npc['exp']
        exibir_player()
    else:
        print(f'{npc['name']} WINS! YOU DIED...')
        exibir_npc(npc)

    level_up()
    reset_player()
    reset_npc(npc)


def atacar_npc(npc):
    npc['hp'] -= player['damage']


def atacar_player(npc):
    player['hp'] -= npc['damage']


def exibir_info_batalha(npc):
    print(f'Player: HP: {player["hp"]} / HP MAXIMO: {player["hp_max"]} ')
    print(
        f'NPC: {npc['name']} / HP: {npc["hp"]} / HP MAXIMO: {npc["hp_max"]} ')
    print('-' * 20)


gerar_npcs(5)

npc_selected = lista_npcs[0]
iniciar_batalha(npc_selected)
iniciar_batalha(npc_selected)
iniciar_batalha(npc_selected)
iniciar_batalha(npc_selected)
iniciar_batalha(npc_selected)
exibir_player()
