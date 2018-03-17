mapa = [[2,2,2,2,2,2,2,2,2,2,2],
        [2,1,1,0,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,3,3,1,1,1,1,2],
        [2,1,1,1,3,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,1,2],
        [2,1,1,1,1,1,1,1,1,1,2],
        [2,2,2,2,2,2,2,2,2,2,2]]

fila=1
columna=3
  

while True:
    
    print "    ",mapa [0][0],mapa[0][1],mapa[0][2],mapa[0][3],mapa[0][4],mapa[0][5],mapa[0][6],mapa[0][7],mapa[0][8],mapa[0][9],mapa[0][10]
    print "    ",mapa [1][0],mapa[1][1],mapa[1][2],mapa[1][3],mapa[1][4],mapa[1][5],mapa[1][6],mapa[1][7],mapa[1][8],mapa[1][9],mapa[1][10]
    print "    ",mapa [2][0],mapa[2][1],mapa[2][2],mapa[2][3],mapa[2][4],mapa[2][5],mapa[2][6],mapa[2][7],mapa[2][8],mapa[2][9],mapa[2][10]
    print "    ",mapa [3][0],mapa[3][1],mapa[3][2],mapa[3][3],mapa[3][4],mapa[3][5],mapa[3][6],mapa[3][7],mapa[3][8],mapa[3][9],mapa[3][10]
    print "    ",mapa [4][0],mapa[4][1],mapa[4][2],mapa[4][3],mapa[4][4],mapa[4][5],mapa[4][6],mapa[4][7],mapa[4][8],mapa[4][9],mapa[4][10]
    print "    ",mapa [5][0],mapa[5][1],mapa[5][2],mapa[5][3],mapa[5][4],mapa[5][5],mapa[5][6],mapa[5][7],mapa[5][8],mapa[5][9],mapa[5][10]
    print "    ",mapa [6][0],mapa[6][1],mapa[6][2],mapa[6][3],mapa[6][4],mapa[6][5],mapa[6][6],mapa[6][7],mapa[6][8],mapa[6][9],mapa[6][10]
    print "    ",mapa [7][0],mapa[7][1],mapa[7][2],mapa[7][3],mapa[7][4],mapa[7][5],mapa[7][6],mapa[7][7],mapa[7][8],mapa[7][9],mapa[7][10]


    movimiento = raw_input(" a - izquierda\n d - derecha\n w - arriba\n s - abajo\n f - super fuerza\n q - salir")
    movimiento=str(raw_input("ingrese una opcion:"))
    if movimiento == "d":
        if mapa [fila][columna + 1]==1:
            columna = columna + 1
            mapa [fila][columna]=0 
            mapa [fila][columna - 1]=1 

    if movimiento == "a":
        if mapa [fila][columna - 1]==1:
            columna = columna - 1
            mapa [fila][columna]=0 
            mapa [fila][columna + 1]=1 

    if movimiento == "w":
        if mapa [fila - 1][columna]==1:
            fila= fila - 1
            mapa [fila][columna]=0
            mapa [fila + 1][columna]=1

    if movimiento == "s":
        if mapa [fila + 1][columna]==1:
            fila= fila + 1
            mapa [fila][columna]=0
            mapa [fila - 1][columna]=1

    if movimiento == "d":
         if mapa [fila][columna + 1]==3 and mapa [fila][columna + 2]==1:
                mapa [fila][columna + 1]=0
                mapa [fila][columna + 2]=3
                mapa [fila][columna]=1
                columna=columna+1

    if movimiento == "a":
         if mapa [fila][columna - 1]==3 and mapa [fila][columna - 2]==1:
                mapa [fila][columna - 1]=0
                mapa [fila][columna - 2]=3
                mapa [fila][columna]=1
                columna=columna-1

    if movimiento == "s":
         if mapa [fila + 1][columna]==3 and mapa [fila + 2][columna]==1:
                mapa [fila + 1][columna]=0
                mapa [fila + 2][columna]=3
                mapa [fila][columna]=1
                fila=fila + 1

    if movimiento == "w":
         if mapa [fila - 1][columna]==3 and mapa [fila - 2][columna]==1:
                mapa [fila - 1][columna]=0
                mapa [fila - 2][columna]=3
                mapa [fila][columna]=1
                fila=fila - 1

    if movimiento == "f":
            if mapa[fila][columna + 1]==3 and mapa [fila][columna + 2]==3:
                      if  mapa [fila][columna + 3]==1:
                                 mapa [fila][columna]=1
                                 mapa [fila][columna + 1]=0
                                 mapa [fila][columna + 2]=3
                                 mapa [fila][columna + 3]= 3
                                 columna=columna+1
    if movimiento == "f":
            if mapa[fila][columna - 1]==3 and mapa [fila][columna - 2]==3:
                      if  mapa [fila][columna - 3]==1:
                                 mapa [fila][columna]=1
                                 mapa [fila][columna - 1]=0
                                 mapa [fila][columna - 2]=3
                                 mapa [fila][columna - 3]= 3
                                 columna=columna-1

    if movimiento == "f":
            if mapa[fila - 1][columna]==3 and mapa [fila - 2][columna]==3:
                       if  mapa [fila - 3][columna]==1:
                                 mapa [fila][columna]=1
                                 mapa [fila - 1][columna]=0
                                 mapa [fila - 2][columna]=3
                                 mapa [fila - 3][columna]= 3
                                 fila=fila - 1

    if movimiento == "f":
            if mapa[fila + 1][columna]==3 and mapa [fila + 2][columna]==3:
                       if  mapa [fila + 3][columna]==1:
                                 mapa [fila][columna]=1
                                 mapa [fila + 1][columna]=0
                                 mapa [fila + 2][columna]=3
                                 mapa [fila + 3][columna]= 3
                                 fila=fila + 1



    elif movimiento == 'q':
        break