Для создания заказа нужно в первую очередь ввести своё имя:
>>>>>>=======================================================================
>>>>>>Please input your orders here!
>>>>>>=======================================================================
>>>>>>Please input your name:
После нас попросят ввести название рецепта:
>>>>>>Create your receipt!
>>>>>>Type ? to watch help and current storage state
>>>>>>Type -go to abort receipt and continue
>>>>>>=======================================================================
>>>>>>Input name of your receipt:
Далее необходимо ввести ингредиенты пиццы. Ингредиенты вводятся через пробел одной строкой.
Вводить следует артикулы ингредиентов, один артикул один ингредиент. Артикулы в строке могут посторятся,
Попытка ввести что то другое или недостаток продуктов на складе приведёт к ошибке и нас попросят
ввести ингредиты заново. Список доступных артикулов прилагается к запросу:
>>>>>>=======================================================================
>>>>>>3 - olives
>>>>>>8 - chicken
>>>>>>2 - cucumbers
>>>>>>9 - bacon
>>>>>>6 - cheese
>>>>>>7 - sauce
>>>>>>1 - tomatoes
>>>>>>4 - anchovies
>>>>>>10 - fish
>>>>>>5 - mushrooms
>>>>>>Input ingredients articles from list you want thought space
После создания рецепта, нам незамедлительно будет предложено создать следующий.
Что бы перейти к "выполнению" заказа введите -go (Команду можно ввести в любом поле
создания рецепта)
Для просмотра справки и текущего состояния склада введите ?:
Пример справки:
>>>>>>Available products and indexes:
>>>>>>3 - olives : 19
>>>>>>8 - chicken : 20
>>>>>>2 - cucumbers : 19
>>>>>>5 - mushrooms : 20
>>>>>>6 - cheese : 20
>>>>>>7 - sauce : 20
>>>>>>1 - tomatoes : 18
>>>>>>4 - anchovies : 20
>>>>>>10 - fish : 20
>>>>>>9 - bacon : 20
>>>>>>Enter -go for complete your order
>>>>>>=======================================================================
После создания заказа будет предложено создать новый, введите yes если желаете продолжить
Ниже приведён листинг программы где пользователь создаёт 2 рецепта. Символом -> отмечен
пользовательский ввод

#############################################################################

=======================================================================
Please input your orders here!
=======================================================================
Please input your name:
->Anton
=======================================================================
Create your receipt!
Type ? to watch help and current storage state
Type -go to abort receipt and continue
=======================================================================
Input name of your receipt:
->Margaritta
=======================================================================
1 - tomatoes
3 - olives
9 - bacon
6 - cheese
2 - cucumbers
5 - mushrooms
10 - fish
7 - sauce
8 - chicken
4 - anchovies
Input ingredients articles from list you want thought space
->7 6 6 5 1
=======================================================================
Create your receipt!
Type ? to watch help and current storage state
Type -go to abort receipt and continue
=======================================================================
Input name of your receipt:
->Boston
=======================================================================
1 - tomatoes
3 - olives
9 - bacon
6 - cheese
2 - cucumbers
5 - mushrooms
10 - fish
7 - sauce
8 - chicken
4 - anchovies
Input ingredients articles from list you want thought space
->4 10 7 1
=======================================================================
Create your receipt!
Type ? to watch help and current storage state
Type -go to abort receipt and continue
=======================================================================
Input name of your receipt:
->-go
Ordered by: Anton
Order time: 2016-10-12 on 22:5:28
Receipt: Margaritta
tomatoes - 1
cheese - 2
mushrooms - 1
sauce - 1
=======================================================================
Receipt: Boston
tomatoes - 1
sauce - 1
anchovies - 1
fish - 1
=======================================================================
=======================================================================
Type yes if you want to create another order
