import os


def ori_editor(file,amount):
    file = open(file,'r')
    data = file.readlines()
    start = 0
    end = 1
    for num,line in enumerate(data):
        line = line.replace('\n','')
        if 'geometry' in line:

            start += num
            end += num+amount
    #print(data[start:end])
    last_Hline = ''
    #print(start)
    line_num = 0
    for num,i in enumerate(data[start:end]):
        if 'H' in i:
            last_Hline = i
            line_num = start+num
#    print(line_num)
#    print(last_Hline)

    return last_Hline,line_num,end



def incre(amount,edit):
    edit = edit.replace('0.0',str(amount))
    return edit
            

def input_creator(oldfile,newline,last_num,basis,charge,spin,exc):
    filename = open(oldfile,'r')
    data = filename.readlines()
    file = open('new.com','w')
    Hydro_list = []

    for num,line in enumerate(data):
        if 'H' in line:
            Hydro_list.append(num)
    data[Hydro_list[-1]] = newline
    for num,i in enumerate(data):
        if num >= last_num:
            i
        else:
            file.write(i)
    file.write(newline)
    file.write('}\n')
    file.write(' oc= 1.20456374\n')
    file.write(' co= 1.33807754\n')
    file.write(' oco=125.71940157\n')
    file.write(' ho= 0.96539172\n')
    file.write(' hoc=105.87929761\n')
    file.write('\n')
    file.write(' basis=' + str(basis) + '\n')
    file.write(' hf,orbprint=75,maxit=100;wf,charge=' + str(charge) + ',spin=' + str(spin)+';accu,20\n')
    file.write(' orbital,ignore_error;\n')
    file.write(' {ccsd\n')
    file.write(' eom,'+ str(exc) + ',trans=1}\n')
  #  print(data[line_num])
    return

def pbs_creater(path):
    return



def main():
   
    amountofatoms = 6
    file = '../ori/test.com'
    basis = 'apVTZ'
    charge = 0
    spin = 0
    state = '2.1,3.1,4.1,1.2,2.2,3.2,1.3,2.3,1.3,2.3,1.4,2.4' 





    for num in range(0,181,3):
        increment=float(num)
        form = "{:03d}".format(int(increment))
        
        last_Hline,line_num,end = ori_editor(file,amountofatoms)
        newline = incre(increment,last_Hline)
        print(newline)
        if os.path.exists('../'+form+'/'):
            os.chdir('../'+form)
            input_creator(file,newline,line_num,basis,
            charge,spin,state)
        #    os.chdir('../src')
        else:
            print(form)
            print(last_Hline)

            os.mkdir('../'+str(form))
            os.chdir('../'+str(form))
            print(increment)
            input_creator(file,newline,line_num,basis,
            charge,spin,state)
        #    os.chdir('../src')

        


       # form = "{:03d}".format(int(increment))
        #increment += 3.0
       # print((increment,form))
        





    return
main()