torre1 = [5, 4, 3, 2, 1]
torre2 = []
torre3 = []
vitoria = False

def ret1bot2():
   torre2.append(torre1[-1])
   torre1.pop(-1)

def ret1bot3():
   torre3.append(torre1[-1])
   torre1.pop(-1)

def ret2bot1():
   torre1.append(torre2[-1])
   torre2.pop(-1)

def ret2bot3():
   torre3.append(torre2[-1])
   torre2.pop(-1)

def ret3bot1():
   torre1.append(torre3[-1])
   torre3.pop(-1)

def ret3bot2():
   torre2.append(torre3[-1])
   torre3.pop(-1)

while vitoria == False:
   print(torre1)
   print(torre2)
   print(torre3)
   print("  ")

   qualTorreret = int(input(("Qual torre você quer retirar?")))
   qualTorrebot = int(input("Qual torre você quer colocar?"))
 
   if qualTorreret == 1 and qualTorrebot == 2:
       if torre2 != [] and torre1 != []:
           if torre1[-1] > torre2[-1]:
                print("você não pode fazer isso nao ein")
                continue
           else:
               ret1bot2()
       elif torre1 != []:  
               ret1bot2()
 
   if qualTorreret == 1 and qualTorrebot == 3:
       if torre3 != [] and torre1 != []:
           if torre1[-1] > torre3[-1]:
                print("você não pode fazer isso nao ein")
                continue
           else:
               ret1bot3()
       elif torre1 != []:
           ret1bot3()

   if qualTorreret == 2 and qualTorrebot == 1:
       if torre1 != [] and torre2 != []:
           if torre2[-1] > torre1[-1]:
               print("você não pode fazer isso nao ein")
               continue
           else:
               ret2bot1()
       elif torre2 != []:
           ret2bot1()

   if qualTorreret == 2 and qualTorrebot == 3:
       if torre3 != [] and torre2 != []:
           if torre2[-1] > torre3[-1]:
               print("você não pode fazer isso nao ein")
               continue
           else:
               ret2bot3()
               
       elif torre2 != []:
               ret2bot3()
 
   if qualTorreret == 3 and qualTorrebot == 1:
       if torre1 != [] and torre3 != []:
           if torre3[-1] > torre1[-1]:
                print("você não pode fazer isso nao ein")
                continue
           else:
               ret3bot1()
       elif torre3 != []:
           ret3bot1()
 
   if qualTorreret == 3 and qualTorrebot == 2:
       if torre2 != [] and torre3 != []:
           if torre3[-1] > torre2[-1]:
                print("você não pode fazer isso nao ein")
                continue
           else:
               ret3bot2()
       elif torre3 != []:
           ret3bot2()


   if torre3 == [5, 4, 3, 2, 1]:
       verificaçãoVitoria=str(input("Beleza, cê ganhou. Quer jogar de novo?"))
       if verificaçãoVitoria == "nao":
           break
       elif verificaçãoVitoria == "sim":
           torre1 = [5, 4, 3, 2, 1]
           torre2 = []
           torre3 = []
           continue