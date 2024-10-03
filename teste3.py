fat_sp = 67.836
fat_rj = 36.678
fat_mg= 29.229
fat_es = 27.165
fat_outros = 19.849

fat_total = fat_sp+fat_rj+fat_mg+fat_es+fat_outros

percentualsp = (fat_sp/fat_total) *100
percentualrj = (fat_rj/fat_total) *100
percentualmg = (fat_mg/fat_total) *100
percentuales = (fat_es/fat_total) *100
percentualoutr = (fat_outros/fat_total) *100

print("""Porcentagem de faturamento de cada estado:
      SP: {}
      RJ: {}
      MG: {}
      ES: {}
      OUTROS: {}
      """.format(percentualsp,percentualrj,percentualmg,percentuales,percentualoutr))
    