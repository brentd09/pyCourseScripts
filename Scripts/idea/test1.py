while True:
  degc = input ('Enter the Temp in DegC ')
  if degc == 'q':
    break
  elif degc == '':
    continue
  floatdegc = float(degc)
  f = ((9 * floatdegc) /5) + 32
  strf = str(f)
  print (degc + ' in Deg C is ' + strf + ' degrees in F')
print('Finished')