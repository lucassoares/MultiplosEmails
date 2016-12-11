import smtplib
import getpass

print("\n \n #################### Desenvolvido por LUCAS SOARES ####################### \n")
usuarioEmail = raw_input("E-mail: ")
usuarioSenha = getpass.getpass("Senha: ")

try:
	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.starttls()

	smtp.login(usuarioEmail,usuarioSenha)

	contatoEmail = raw_input("E-mail do destinatario: ")
	mensagem = raw_input("Digite a mensagem que queira enviar: \n")
	numeroMensagens = int(raw_input("Digite o numero de vezes que desseja enviar esta mensagem: \n"))
	mensagensEnviadas = 0

	while mensagensEnviadas < numeroMensagens:
		mensagensEnviadas+=1
		smtp.sendmail(usuarioEmail,contatoEmail,mensagem)
		print("Enviando mensagens... Aperte CTRL + C -> para parar")
	smtp.quit()

except Exception as e:
	print("Ocorreu um erro no seu script", e)
