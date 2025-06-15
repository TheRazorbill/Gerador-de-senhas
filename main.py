import random as rnd
import string as strg

def faz_snh(tam):
    letras = strg.ascii_letters + strg.digits + strg.punctuation
    senha = ''.join(rnd.choice(letras) for i in range(tam))
    return senha

def checa_snh(senha):
    min = any(c.islower() for c in senha)
    mai = any(c.isupper() for c in senha)
    num = any(c.isdigit() for c in senha)
    espec = any(not c.isalnum() for c in senha)
    tamanho = len(senha) >= 8

    if min and mai and num and espec and tamanho:
        return True
    else:
        return False

def faz_varias_snh(num, tam):
    senhas = []
    for _ in range(num):
        senhas.append(faz_snh(tam))
    return senhas

def mostra_info(senha):
    min = any(c.islower() for c in senha)
    mai = any(c.isupper() for c in senha)
    num = any(c.isdigit() for c in senha)
    espec = any(not c.isalnum() for c in senha)
    tamanho = len(senha) >= 8

    print(f"Min: {min}")
    print(f"Mai: {mai}")
    print(f"Num: {num}")
    print(f"Esp: {espec}")
    print(f"Tam: {tamanho}")

def comeca():
    print("Gerar e Ver Senha Simples.")

    while True:
        try:
            acao = input("1-Fazer Senhas, 2-Ver Senhas, 3-Sair: ")
            if acao == '1':
                tam = int(input("Tamanho da senha (min 8): "))
                if tam < 8:
                    print("Tamanho muito curto.")
                    continue
                num = int(input("Quantas senhas: "))
                senhas_feitas = faz_varias_snh(num, tam)
                print("\nSenhas Feitas:")
                for s in senhas_feitas:
                    print(s)
                print("\n")
            elif acao == '2':
                senha_dada = input("Digite a senha: ")
                ok = checa_snh(senha_dada)
                print(f"Senha OK: {ok}")
                mostra_info(senha_dada)
                print("\n")
            elif acao == '3':
                print("Até!")
                break
            else:
                print("Escolha errada.")
        except ValueError:
            print("Entrada errada. Tente de novo.")
        except Exception as e:
            print(f"Um erro deu: {e}")

if __name__ == "__main__":
    comeca()

# Termos usados

# faz_snh:          Fazer Senha
# checa_snh:        Checar Senha
# faz_varias_snh:   Fazer Várias Senhas
# mostra_info:      Mostrar Info
# comeca:           Começa (função principal)
# tam:              Tamanho
# letras:           Letras (caracteres)
# senha:            Senha
# min:              Minúscula
# mai:              Maiúscula
# num:              Número (dígito)
# espec:            Especial
# num:              Número (quantidade)
# acao:             Ação (opção)
# senha_dada:       Senha Dada (entrada)
# ok:               OK (válida)
# curto:            Curto (pequeno)
# simples:          Simples
# novo:             Novo (novamente)
# deu:              Deu (ocorreu)