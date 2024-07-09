def principal():
    print("Executando principal")

    def funcao_interna():
        print("Executando funcao interna")

    def funcao_interna2():
        print("Executando funcao interna 2")

    funcao_interna()
    funcao_interna2()

principal()