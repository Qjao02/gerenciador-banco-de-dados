# coding: utf-8# # Gerador de scripts para popular o banco de dados# 
import django.db.backends.my
from faker import Faker
from math import pi
faker = Faker()
#lista que armazena os nomes dos clientes
names = []
cpf = []
cnpj = []
faker.address()
faker.company()
script = open('popula.sql', 'w')
# ## Criando o script que popula o banco
# gerando as partes fixa do template# In[7]:
script.write('USE `DBBANCO`;\r\nSET SQL_SAFE_UPDATES = 0;\r\nSET foreign_key_checks = 0;\r\n')
# Inserindo nomes aleatorios para preencher as tuplas da relação agencia:
script.write("DELETE FROM AGENCIA;\r\n")
for i in range (0,100):
	script.write('INSERT INTO AGENCIA(endereco, nome)\r\n\tVALUES("' +faker.address() +'", "'+faker.company() + '");\r\n')
# gerando as tuplas de clientes# In[9]:
script.write('DELETE FROM CLIENTE;\r\n')
for i in range(0,100):
		fakename = faker.name()
		names.append(fakename)
		script.write('INSERT INTO CLIENTE(cadastroDatetime, endereco, nome)\r\n\tVALUES(CURDATE(), "'+ faker.address() + '","'+fakename+'");\r\n')
	
# Gera as tuplas para a tabela FISICO
script.write("DELETE FROM FISICO;\r\n");
for i in range(0, 50):
	tmpcpf = faker.ipv4();
	cpf.append(tmpcpf);
	script.write('INSERT INTO FISICO(cpf, cliente)\r\n\tVALUES("'+ cpf[i] +'", (SELECT id FROM cliente WHERE nome="'+ names[i] + '"));\r\n')
# Tuplas JURIDICO
script.write("DELETE FROM JURIDICO;\r\n");
j = 0;
for i in range(24, 75):
	tmpcnpj = faker.ipv4();
	cnpj.append(tmpcnpj);
	script.write("INSERT INTO JURIDICO(cnpj, cliente)\r\n\tVALUES(\"" + cnpj[j] +"\", (SELECT id FROM cliente WHERE nome=\""+ names[i] + "\"));\r\n");
	j = j + 1;
# Tuplas OPERACAO
script.write("DELETE FROM OPERACAO;\r\n");
for i in range(0, 50):
	script.write("INSERT INTO OPERACAO(operacao, fisico, fisicoCPF)\r\n\tVALUES(13, " + "(SELECT id FROM FISICO WHERE cpf=\"" + cpf[i] + "\", (SELECT cpf FROM FISICO WHERE cpf=\"" + cpf[i] + "\"));\r\n");
j = 0;
for i in range(24, 75):
	script.write("INSERT INTO OPERACAO(operacao, juridico, juridicoCNPJ)\r\n\tVALUES(2, " + "(SELECT id FROM JURIDICO WHERE cnpj=\"" + cnpj[j] + "\", (SELECT cnpj FROM JURIDICO WHERE cnpj=\"" + cnpj[j] + "\"));\r\n");
	j = j + 1;
# Tuplas CONTA
for i in range(0, 50):
	script.write("INSERT INTO CONTA(conta, cadastroDatetime, senha, saldo, operacao)\r\n\tVALUES(\"" + i + "\", NOW(), \"password" + i + "\", " + i * math.format(pi) + ", (SELECT id FROM operacao WHERE fisicoCPF=\"" + cpf[i] + "));\r\n");
j = 0;
for i in range(24, 75):
	script.write("INSERT INTO CONTA(conta, cadastroDatetime, senha, saldo, operacao)\r\n\tVALUES(\"" + i + "\", NOW(), \"password" + i + "\", " + 2 * i * math.format(pi) + ", (SELECT id FROM operacao WHERE juridicoCNPJ=\"" + cnpj[j] + "));\r\n");
	j = j + 1;
script.close();