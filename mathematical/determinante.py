
matrixA = [[3,2,3],
           [4,5,6],
           [7,12,9]]

matrixB = [[5, 2,20,30],
          [10, 0,0, 15],
          [4,21,11, 1],
          [114,4,41,7]]

matrixC = [[2,2,3,6],
           [0,5,6,9],
           [0,0,9,12],
           [0,0,0,3]]

matrixD = [[0.3,0.2],
           [0.1,0.1]]


def determinant(matrix):
    x = len(matrix)
    if(x == 2):
        a11 = matrix[0][0]
        a21 = matrix[0][1]
        a12 = matrix[1][0]
        a22 = matrix[1][1]
        
        detA = (a11 * a22) - (a21 * a12) 
    
    elif (x== 3):
        # Der laplacesche Entwicklungssatz wird hier angewendet mit (-1)^i+j, wobei i die Zeilen- und j die Spaltenanzahl sind
        matrixa11 = matrix[0][0]
        # Hier wird mit -1 multipliziert, da hier (-1)^1+2 negativ ist.
        matrixa12 = matrix[0][1] * -1
        matrixa13 = matrix[0][2]
      
        teil_matrix0 = [
            [matrix[1][1], matrix[1][2]],
            [matrix[2][1], matrix[2][2]] 
            ]
        teil_matrix1 = [
            [matrix[1][0], matrix[1][2]],
            [matrix[2][0], matrix[2][2]] 
            ]
        teil_matrix2 = [
            [matrix[1][0], matrix[1][1]],
            [matrix[2][0], matrix[2][1]] 
            ]
        
        teil_matrizen = [teil_matrix0, teil_matrix1, teil_matrix2]
        
        teil_deten = []
        
        # (1) Für jeden Teilmatrix wird die Determinante bestimmt und am Ende einer Liste hinzugefügt. Mithilfe dieser Determinanten wird die Determinante von der 3x3 Matrix bestimmt. 
        for teil_matrix in teil_matrizen:
            a11 = teil_matrix[0][0]
            a21 = teil_matrix[0][1]
            a12 = teil_matrix[1][0]
            a22 = teil_matrix[1][1]
        
            teil_detA = (a11 * a22) - (a21 * a12)
            teil_deten.append(teil_detA)
        
        detA = (matrixa11 * teil_deten[0])+(matrixa12 * teil_deten[1])+(matrixa13 * teil_deten[2])
        
    elif (x == 4):
        ober_matrixa11 = matrix[0][0]
        ober_matrixa12 = matrix[0][1] * -1
        ober_matrixa13 = matrix[0][2]
        ober_matrixa14 = matrix[0][3] * -1
        
        ober_matrix0 = [
            [matrix[1][1], matrix[1][2], matrix[1][3]],
            [matrix[2][1], matrix[2][2], matrix[2][3]],
            [matrix[3][1], matrix[3][2], matrix[3][3]]
            ]
        ober_matrix1 = [
            [matrix[1][0], matrix[1][2], matrix[1][3]],
            [matrix[2][0], matrix[2][2], matrix[2][3]],
            [matrix[3][0], matrix[3][2], matrix[3][3]]
            ]
        ober_matrix2 = [
            [matrix[1][0], matrix[1][1], matrix[1][3]],
            [matrix[2][0], matrix[2][1], matrix[2][3]],
            [matrix[3][0], matrix[3][1], matrix[3][3]]
            ]
        ober_matrix3 = [
            [matrix[1][0], matrix[1][1], matrix[1][2]],
            [matrix[2][0], matrix[2][1], matrix[2][2]],
            [matrix[3][0], matrix[3][1], matrix[3][2]]
            ]
    
        ober_matrizen = [ober_matrix0, ober_matrix1, ober_matrix2, ober_matrix3 ]    
        
        ober_deten = []
        
        
        #Jeder 3x3 Matrix wird hier in 2x2 Matrizen geteilt.
        for ober_matrix in ober_matrizen:
            teil_matrixa11 = ober_matrix[0][0]
            teil_matrixa12 = ober_matrix[0][1] * -1
            teil_matrixa13 = ober_matrix[0][2]
            
            teil_matrix0 = [
                [ober_matrix[1][1], ober_matrix[1][2]],
                [ober_matrix[2][1], ober_matrix[2][2]] 
                ]
            teil_matrix1 = [
                [ober_matrix[1][0], ober_matrix[1][2]],
                [ober_matrix[2][0], ober_matrix[2][2]] 
                ]
            teil_matrix2 = [
                [ober_matrix[1][0], ober_matrix[1][1]],
                [ober_matrix[2][0], ober_matrix[2][1]] 
                ]
            
            teil_matrizen = [teil_matrix0, teil_matrix1, teil_matrix2]
            
            teil_deten = []
            
            # Der Schritt aus (1) wird dann wiederholt.
            for teil_matrix in teil_matrizen:
                
                a11 = teil_matrix[0][0]
                a21 = teil_matrix[0][1]
                a12 = teil_matrix[1][0]
                a22 = teil_matrix[1][1]
            
                teil_det = (a11 * a22) - (a21 * a12)
                teil_deten.append(teil_det)
                  
            ober_det = (teil_matrixa11 * teil_deten[0])+(teil_matrixa12 * teil_deten[1])+(teil_matrixa13 * teil_deten[2])     
            
            ober_deten.append(ober_det)        
       
        detA =  (ober_matrixa11 * ober_deten[0])+(ober_matrixa12 * ober_deten[1])+(ober_matrixa13 * ober_deten[2])+(ober_matrixa14 * ober_deten[3])
        
    return detA

