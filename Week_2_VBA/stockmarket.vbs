Create a script that will loop through each year of stock data and grab the total amount of volume each stock had over the year.
You will also need to display the ticker symbol to coincide with the total volume.
Your result should look as follows (note: all solution images are for 2015 data).

Sub Stockmarket()

' Declare a type of variable to start counting total volume
Dim TotalVolume As Double

'Create a variable to count the length of the data
Dim lastrow As Double
lastrow = Cells(Rows.Count, 1).End(xlUp).Row
'MsgBox (lastrow)

TotalVolume = 0
'MsgBox(TotalVolume)

'Add names in cells I1 and J1
    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Total Volume"


For i = 2 To lastrow


    ' If ticker changes then print results
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

    'Sum up "volume" column
        TotalVolume = TotalVolume + Cells(i, 7).Value
    'MsgBox (TotalVolume)

    'write ticker name in cell (2 + j, 9)
        Cells(2 + j, 9).Value = Cells(i, 1).Value
 
    'write TotalVolume value in cell (2 + j, 10)
        Cells(2 + j, 10).Value = TotalVolume
 
    'Reset value of TotalVolume
        TotalVolume = 0
 
    'Increase value of variable j to move to next row
        j = j + 1

    'else add value to TotalVolume
        Else: TotalVolume = TotalVolume + Cells(i, 7).Value
 
         End If
 
    Next i
 
End Sub
