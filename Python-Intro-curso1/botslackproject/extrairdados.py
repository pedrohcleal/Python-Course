from openpyxl import load_workbook #importa o leitor de excel

arq = load_workbook('Inicidentes-relatório.xlsx') #Abre a planilhe

planilha = arq['Página1'] #abre a pasta da planihlha

#recebe os valores da planilha

#incidentes
novos = planilha['D13'].value
andamento = planilha['E13'].value
espera = planilha['F13'].value

criticos = planilha['J4'].value
moderados = planilha['J7'].value
baixos = planilha['J10'].value

#requisiçõpes
novas_reqs = planilha[]

