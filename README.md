# 538_riddler_11_15_2019
FiveThirtyEight's Riddler Challenge for 15 November 2019: "How Long Can You Roll." Link here: https://fivethirtyeight.com/features/how-low-can-you-roll/

This short program is divided into three functions: main(), makeRandomNum(), and concat().

In short, a random number is selected using package random() and added to a list.
After the first digit is added, each subsequent digit is evaluated if it is greater than
or less than the number before it. If it is less than or equal to the previous digit,
it is added to the list. If it is not, the number ends there and is added to a list.
In the final steps, and because of the way I organized the program, the list of lists
becomes a list of numbers, which are then divided by a factor of 10 to get them between
0 and 1.

One million iterations were performed (~20 seconds) and the resultant average of all
one million decimals was ~0.4155.
