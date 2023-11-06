tabelaBrasileirao = ('Botafogo', 'Fortaleza', 'Palmeiras','internacional', 'Fluminense','Cruzeiro', 'Grêmio', 'São Paulo','Vasco'\
    ,'Atlético Mineiro', 'Santos', 'Red Bull Bragantino',   'Flamengo', 'Goiás', 'Athletico Paranaense', 'Corinthians', 'Cuiabá'\
    , 'Coritiba', 'Bahia', 'América Mineiro')
print(f'os 5 primeiros colocados {tabelaBrasileirao[0: 5]}')
print(f'os ultimos 4 do colocados {tabelaBrasileirao[-4:]}')
print(f'em ordem alfabetica {sorted(tabelaBrasileirao)}')
print(f'o palmeiras ta na {tabelaBrasileirao.index("Palmeiras")+1}ª')