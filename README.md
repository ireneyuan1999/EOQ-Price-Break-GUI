# EOQ-Price-Break-GUI
This Python project utilizes sympy and the math python libraries to create a graphical user interface based EOQ price break solver from a Qt Designer. 

![alt text](https://github.com/ireneyuan1999/EOQ-Price-Break-GUI/blob/main/eoq.JPG?raw=true)

A price break EOQ model takes the classical EOQ model further byy including a discount price after a certain amount of bulk order. The inputs for this eoq model are demand per time unit, holding costs, setup costs, led time, cost before bulk, cost after bulk (discounted price), and unit number price break point. 

ym or y minimum is calculated with the classical EOQ equation. It then compares ym to the price break point to determine whether to continue calculating. Total cost per time unit (TCU) of ym is then determins with a modified equation from the classical EOQ model. It is then used to find Q where TCU(ym)=TCU(Q). The price break point is then compared to ym and Q to see which zone it may fall in to determine EOQ. Reorder point follows the classical EOQ model. 
