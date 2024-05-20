def consulta(categoria, lancamento, sub_genero):
    categoria = categoria if categoria in ['Ação', 'Comedia', 'Romance', 'Terror', 'Ficção cientifica', 'Aventura', 'Novela', 'Fantasia'] else 'Nulo'
    sub_genero = categoria if categoria in ['FPS','Hack and Slash','Party', 'Adventura', 'Visual Novel', 'RPG', 'Survival', 'Psicológico', 'RPG', 'Shooter', 'Mundo Aberto', 'Platforma', 'Drama', 'Mistério', 'Ação'] else 'Nulo'
    lancamento = lancamento if type(lancamento) == int and (lancamento < 2012 or lancamento > 2012) else 'Nulo'

    if categoria == 'Nulo' or lancamento == 'Nulo' or sub_genero == 'Nulo':
        return 'Erro'

    if categoria == "Ação":
        if sub_genero == 'FPS':
            if lancamento > 2012:
                return 'DOOM (2016)'
            if lancamento < 2012:
                return 'Call of Duty: Modern Warfare'
        if sub_genero == 'Hack and Slash':
            if lancamento > 2012:
                return 'Devil May Cry 5'
            if lancamento < 2012:
                return 'Bayonetta'

    if categoria == "Comedia":
        if sub_genero == 'Party':
            if lancamento > 2012:
                return 'Overcooked'
            if lancamento < 2012:
                return 'Mario Party 9'
        if sub_genero == 'Aventura':
            if lancamento > 2012:
                return 'Untitled Goose Game'
            if lancamento < 2012:
                return 'Psychonauts'

    if categoria == "Romance":
        if sub_genero == 'Visual Novel':
            if lancamento > 2012:
                return 'Doki Doki Literature Club'
            if lancamento < 2012:
                return 'Clannad'
        if sub_genero == 'RPG':
            if lancamento > 2012:
                return 'Persona 5'
            if lancamento < 2012:
                return 'Final Fantasy IX'

    if categoria == "Terror":
        if sub_genero == 'Survival':
            if lancamento > 2012:
                return 'Resident Evil 7'
            if lancamento < 2012:
                return 'Resident Evil 4'
        if sub_genero == 'Psicológico':
            if lancamento > 2012:
                return 'Outlast'
            if lancamento < 2012:
                return 'Silent Hill 2'

    if categoria == "Ficção cientifica":
        if sub_genero == 'RPG':
            if lancamento > 2012:
                return 'The Outer Worlds'
            if lancamento < 2012:
                return 'Mass Effect 2'
        if sub_genero == 'Shooter':
            if lancamento > 2012:
                return 'Destiny 2'
            if lancamento < 2012:
                return 'Halo: Reach'

    if categoria == "Aventura":
        if sub_genero == 'Mundo Aberto':
            if lancamento > 2012:
                return 'Assassin\'s Creed Odyssey'
            if lancamento < 2012:
                return 'Red Dead Redemption'
        if sub_genero == 'Platform':
            if lancamento > 2012:
                return 'Super Mario Odyssey'
            if lancamento < 2012:
                return 'Super Mario Galaxy 2'

    if categoria == "Novel":
        if sub_genero == 'Drama':
            if lancamento > 2012:
                return 'Life is Strange'
            if lancamento < 2012:
                return 'The Walking Dead: Season One'
        if sub_genero == 'Mistério':
            if lancamento > 2012:
                return 'Oxenfree'
            if lancamento < 2012:
                return 'Heavy Rain'

    if categoria == "Fantasia":
        if sub_genero == 'RPG':
            if lancamento > 2012:
                return 'The Witcher 3: Wild Hunt'
            if lancamento < 2012:
                return 'The Elder Scrolls V: Skyrim'
        if sub_genero == 'Ação':
            if lancamento > 2012:
                return 'Dark Souls III'
            if lancamento < 2012:
                return 'Dark Souls'

# Exemplos de função
print(consulta('Ação', 2015, 'FPS'))  # Output: DOOM (2016)
print(consulta('Romance', 2010, 'RPG'))  # Output: Final Fantasy IX
