#O programa receberá informações de 10 candidatos à doação de sangue. O programa deverá ler a idade e informar a seguinte condição: 
#- Se menor de 16 ou acima de 69 anos, não poderá doar;
#- Se tiver entre 16 e 17 anos, somente poderá doar se estiver acompanhado dos pais ou responsáveis (neste caso criar uma condição: "Está acompanhado de pais ou responsável: 1-sim ou 2-não);
#- Se  tiver entre 18 e 69 anos, poderá doar.

#Ao final o programa deverá mostrar quantos candidatos poderão doar sangue.

idade=0
doadorMenorIdoso=0
doadorAdolescente=0
doadorAdulto=0
simNao=0
podeDoar=0
naoPodeDoar=0
adolescente=0

for i in range(0, 10):
 idade = int(input('Informe a idade do candidato à doação: '))

 if idade <16 or idade > 69:
  doadorMenorIdoso+=1
 elif 16<=idade<=17:
  simNao = int(input('Está acompanhado de pais ou responsável? Digite [1 - SIM] ou [2 - NÃO]'))
  if simNao == 1:
   doadorAdolescente+=1
  else :
   adolescente+=1
 else :
   doadorAdulto+=1

naoPodeDoar = doadorMenorIdoso + adolescente
podeDoar = doadorAdolescente + doadorAdulto

print(naoPodeDoar, ' candidatos não atenderam aos critérios para doação de sangue.')
print(podeDoar, ' candidatos atenderam aos critérios para doação de sangue e poderão doar.')