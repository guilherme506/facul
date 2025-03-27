#peça que o usuário digite uma senha. garanta que ela tenha mais de 8 caracteres, menos de 16,possua pelo menos uma 
# maiuscula, pelo menos um numero, pelo menos um caracterer especial
senha = str(input('Digite uma senha: ')).strip()
if len(senha)==8 and len(senha)<16:
    print('ok')
elif len(senha) in len(senha.isupper):
    print('ok')
elif len(senha) in '@#$!%¨&*_-+=§ªº?°><:;/\|)':
    print('ok')
elif len(senha) in len(senha.isnumeric):
    print('ok')
else:
    print('sua senha esta falando uma especificação')
print('sua senha foi criada')