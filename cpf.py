import res
import sys

cpf_usuario = input('CPF: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    cpf_usuario
)
entrada_e_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)
if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()
nove_dig = cpf_usuario[:9]
cont = 10
resultado = 0
for i in nove_dig:
    resultado += int(i) * cont
    cont -= 1
i = (resultado * 10) % 11
i = i if i <= 9 else 0

dec_dig = cpf_usuario[:10]
resultado_2 = 0
cont2 = 11
for i2 in dec_dig:
    resultado_2 += int(i2) * cont2
    cont2 -= 1
i2 = (resultado_2 * 10) % 11
i2 = i2 if i2 <= 9 else 0

cpf_verif = f'{nove_dig}{i}{i2}'

if cpf_usuario == cpf_verif:
    print(f'CPF: {cpf_usuario}, válido')
elif len(cpf_usuario) > 10 or len(cpf_usuario) < 10:
    print('CPF inválido')
else:
    print(f'CPF: {cpf_usuario} inválido')
