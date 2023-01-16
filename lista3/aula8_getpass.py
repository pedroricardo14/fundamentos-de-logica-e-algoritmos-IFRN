import getpass #ativa o comando ler senha.
usu = input("Usuário? ")
sen = getpass.getpass ("Senha? ")

if (usu=="ana" and sen=="999") or (usu=="caio" and sen=="777") :
  print("Acesso permitido.")
else :
  print("Acesso negado.")

# O "getpass" é usado em casos que o sistema que estamos criando requer mais segurança e privacidade. Isso para não mostrar a senha na tela. 
  
#lembrando que o python diferencia letra maiúscula de minúscula. No caso do usuário ser só com letra minuscula, o python só aceitará se o usuário ou senha for digitado só com letra minúscula.
