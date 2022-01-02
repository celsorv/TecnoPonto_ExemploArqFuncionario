# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   TECNO PONTO
#   Exemplo de gravação de arquivo de funcionários
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[ exemplo.py ]

salto_linha = '\n'

with open('arq.txt', 'w') as f:

    # números fictícios
    # https://www.4devs.com.br/gerador_de_pis_pasep
    pis = ["077067201928", "095372910293", "076673432947"]

    for i in range(3):

        f.write('TPONTO')
        f.write('matricula' + str(i + 1))
        f.write('CRACHA--FUNCIONARIO' + str(i + 1))
        f.write('nome-completo-do-funcionario-contratado-da-empresa')
        f.write('NUMERO--CARTEIRA-TRABALHO')
        f.write(pis[i])         # inscrição PIS (12 dígitos zero à esquerda)
        f.write('10012020')     # Admissão DDMMAAAA
        f.write('M')            # Forma Pagto M ou H
        f.write('220')          # Horas Mês
        f.write('N')            # Cálculo Proporcional
        f.write('00001')        # Código Cargo
        f.write('00001')        # Código Departamento
        f.write('00001')        # Código Turno
        f.write('00001')        # Código Parâmetros
        f.write('N')            # Compensa Extras S ou N
        f.write('N')            # Compensa Faltas S ou N
        f.write('3')            # Ação ao Mudar Data (vide layout)

        # campos opcionais
        # ---------------------------------------------
        # f.write( 'CAMINHO-NOME-DO-ARQUIVO-COM-A-FOTO-DO--FUNCIONARIO' )
        # f.write( 'nome-logradouro-e-nro-da-residencia-do-funcionario' )
        # f.write( 'NOME--CIDADE--FUNCIONARIO' )
        # f.write( 'SP' )                     # UF
        # f.write( '05311000' )               # CEP
        # f.write( 'NUMEROS-DE-TELEFONES-FIXO-E-CELULAR-DO-FUNCIONARIO' )
        # f.write( '10032001' )               # Nascimento DDMMAAAA
        # f.write( 'Naturalidade-Funcion' )
        # f.write( 'S' )                      # Estado Civil
        # f.write( '000003000.00' )           # Salário
        # f.write( 'CIC-CPF--FUNCIONARIO' )
        # f.write( 'carteira-funcionario' )
        # f.write( 'TITULO-ELEITOR-FUNCI' )
        # ---------------------------------------------

        f.write(salto_linha)
