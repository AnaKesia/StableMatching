def stableMatching(n, menPreferences, womenPreferences):
    # Inicialmente, todos os n homens estão solteiros
    unmarriedMen = list(range(n))
    # Nenhum dos homens tem cônjuge ainda, denotado por None
    manSpouse = [None] * n
    # Nenhuma das mulheres tem cônjuge ainda, denotado por None
    womanSpouse = [None] * n
    # Cada homem fez 0 propostas, então sua próxima proposta será para a primeira mulher em sua lista
    nextManChoice = [0] * n

    # Enquanto houver homens solteiros:
    while unmarriedMen:
        print(f"Solteiros: {unmarriedMen}")
        # Escolha o primeiro homem solteiro
        he = unmarriedMen.pop(0)
        print(f"Homem {he} faz proposta")
        # Suas preferências
        hisPreferences = menPreferences[he]
        # A mulher para quem ele vai propor
        she = hisPreferences[nextManChoice[he]]
        print(f"Homem {he} propõe para mulher {she}")
        # Preferências dela
        herPreferences = womenPreferences[she]
        # O marido atual dela (se houver)
        currentHusband = womanSpouse[she]

        # Se a mulher não tem marido, ela aceita o homem
        if currentHusband is None:
            print(f"Mulher {she} aceita proposta de homem {he}")
            manSpouse[he] = she
            womanSpouse[she] = he
        # Se a mulher já tem marido, verifica se ela prefere o novo pretendente
        else:
            currentHusbandRank = herPreferences.index(currentHusband)
            newManRank = herPreferences.index(he)
            # Se ela prefere o novo homem, ela troca de marido
            if newManRank < currentHusbandRank:
                print(f"Mulher {she} prefere homem {he} ao invés do marido {currentHusband}")
                manSpouse[he] = she
                womanSpouse[she] = he
                unmarriedMen.append(currentHusband)  # O marido anterior volta a ser solteiro
                manSpouse[currentHusband] = None
            else:
                print(f"Mulher {she} rejeita homem {he}")
                unmarriedMen.append(he)  # Ela rejeita o novo pretendente, ele continua solteiro
        
        # Próxima mulher para quem o homem vai propor (se necessário)
        nextManChoice[he] += 1

    print(f"Resultado final: {manSpouse}")
    return manSpouse

# Testes
assert(stableMatching(1, [[0]], [[0]]) == [0])
assert(stableMatching(2, [[0,1], [1,0]], [[0,1], [1,0]]) == [0, 1])
