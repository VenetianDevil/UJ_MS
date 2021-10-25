# Zestaw 1
## Generator liczb losowych
**Problem A1** (Obowiązkowe)
* Implementacja generatoru liczb losowych z rozkładu normalnego  metodą polarną
* Narysowanie histogramu i porównanie ze wzorem analitycznym
* Obliczyć eksperymentalne wartości średniej oraz wariancji

**Problem A2** (Obowiązkowe)
* Implementacja generatoru liczb losowych z rozkładu Cauchy’ego , metodą odwróconej dystrybuanty:
<a href="https://www.codecogs.com/eqnedit.php?latex=f(y)=\frac{1}{\pi&space;\gamma&space;\left&space;[&space;1&plus;\left&space;(&space;\frac{y-y_{0}}{\gamma&space;}&space;\right&space;)^{2}\right&space;]},&space;y\in&space;\left&space;(-&space;\infty,&space;\infty&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(y)=\frac{1}{\pi&space;\gamma&space;\left&space;[&space;1&plus;\left&space;(&space;\frac{y-y_{0}}{\gamma&space;}&space;\right&space;)^{2}\right&space;]},&space;y\in&space;\left&space;(-&space;\infty,&space;\infty&space;\right&space;)" title="f(y)=\frac{1}{\pi \gamma \left [ 1+\left ( \frac{y-y_{0}}{\gamma } \right )^{2}\right ]}, y\in \left (- \infty, \infty \right )" /></a>
* Narysowanie histogramu i porównianie ze wzorem analitycznym dla różnych wartości <img src="https://latex.codecogs.com/gif.latex?y_{0}" title="y_{0}" /> i <img src="https://latex.codecogs.com/gif.latex?\gamma" title="\gamma" /> 
* Obliczyć eksperymentalne wartości średniej oraz wariancji

## Ruina gracza
Ruina gracza dla 2 graczy: gracz **A** z kapitalem początkowym **a** i gracz **B** z kapitalem początkowym **b**. Po każdej rozgrywce wygrywający gracz otrzymuje jedną jednostkę kapitału od przegranego. Nie ma remisów.  - prawdopodobieństwo wygranej gracza A w jednej rozgrywce (dla dwoch graczy <img src="https://latex.codecogs.com/gif.latex?\mathbf{p_{B}=1-p_{A}}" title="\mathbf{p_{B}=1-p_{A}}" />).

Dla każdego z problemów wyniki są pobierane z zaimplementowanej symulacji gry(gier) ruiny gracza.
**N** - parametr który wyznaćza iłość symulowanych gier, dla róźnych zadań ten parametr może być róźnym (generalnie im więcej tym lepiej, może być wybrany tak, żeby symulacją nie trwała za długo).

**Problem B** (Obowiązkowe)  
**a** = 50, **b** = 50  
Symulacja **N** gier z róźnymi wartościami <img src="https://latex.codecogs.com/gif.latex?\mathbf{p_{A}}" title="\mathbf{p_{A}}" />. Dla każdej wartości obliczyć prawdopodobieństwo ruiny gracza **A**.
1. Wykres <img src="https://latex.codecogs.com/gif.latex?\mathbf{P_{ruiny}\left&space;(&space;p_{a}&space;\right&space;)}" title="\mathbf{P_{ruiny}\left ( p_{a} \right )}" /> - zależności prawdopodobieństwa ruiny gracza A od prawdopodobieństwa wygranej w jednej rozgrywce <img src="https://latex.codecogs.com/gif.latex?\mathbf{p_{A}}" title="\mathbf{p_{A}}" />.
2. Porównanie z wynikiem teoretycznym
3. Spróbować dla róźnych wartościej **a** i **b**

**Problem C** (Obowiązkowe)  
**a** + **b** = 100;  
<img src="https://latex.codecogs.com/gif.latex?\mathbf{p_{A}=&space;\frac{1}{2}}" title="\mathbf{p_{A}= \frac{1}{2}}" />  
Symulacja **N** gier z róźnymi wartościami **a**. Dla każdej wartości obliczyć prawdopodobieństwo ruiny gracza **A**.
1. Wykres <img src="https://latex.codecogs.com/gif.latex?\mathbf{P_{ruiny}\left&space;(&space;a&space;\right&space;)}" title="\mathbf{P_{ruiny}\left ( a \right )}" /> - zależności prawdopodobieństwa ruiny gracza A od początkowego kapitalu a
2. Porównanie z wynikiem teoretycznym
3. Spróbować dla róźnych wartościej <img src="https://latex.codecogs.com/gif.latex?\mathbf{p_{A}}" title="\mathbf{p_{A}}" />

**Problem D** (Obowiązkowe)  
**L** - liczba rozgrywek do ukończenia gry  
<img src="https://latex.codecogs.com/gif.latex?\mathbf{P_{}=\frac{1}{2},\frac{1}{5},\frac{4}{5}};" title="\mathbf{P_{}=\frac{1}{2},\frac{1}{5},\frac{4}{5}};" />  
**a** = **b** = 50  
Proponowana całkowita liczba gier **N** = 20000  
Symulacja N gier, dla każdej gry obliczyć iłość rozgrywek.
1. Histogram prawdopodobieństwa P(L) - liczby rozgrywek do ukończenia gry
2. Wyliczyć średnią długość rozgrywki

**Problem E** (Obowiązkowe)  
**N** - wybrana wartość symulowanych gier  
Symulacja **N** gier z róźnymi wartościami <img src="https://latex.codecogs.com/gif.latex?\mathbf{p_{A}}" title="\mathbf{p_{A}}" />. Dla każdej wartości <img src="https://latex.codecogs.com/gif.latex?\mathbf{p_{A}}" title="\mathbf{p_{A}}" /> obliczyć maksymalną iłość rozgrywek.
1. Wykres <img src="https://latex.codecogs.com/gif.latex?\mathbf{L_{max}(p_{A}))}" title="\mathbf{L_{max}(p_{A}))}" /> - maksymalna długość rozgrywek <img src="https://latex.codecogs.com/gif.latex?\mathbf{L_{max}}" title="\mathbf{L_{max}}" /> przy **N** rozgrywkach jako zależność od wartości <img src="https://latex.codecogs.com/gif.latex?\mathbf{p_{A}}" title="\mathbf{p_{A}}" />

**Problem F** (Nie obowiązkowe)  
**n** = 2,10,20,…,100  
**a** = **b** = 50  
<img src="https://latex.codecogs.com/gif.latex?\mathbf{P_{}=\frac{1}{2},\frac{1}{5},\frac{4}{5}};" title="\mathbf{P_{}=\frac{1}{2},\frac{1}{5},\frac{4}{5}};" /> 
Symylacja **n** rozgrywek **N** razy.
1. Histogram prawdopodobieństwa **P(M)** - że gracz **A** ma kapitał **M** po **n** rozgrywkach

**Problem G** (Obowiązkowe)  
Symulacja kilku gier (do 10)  
spróbować dla różnych wartości <img src="https://latex.codecogs.com/gif.latex?\mathbf{p_{A}}" title="\mathbf{p_{A}}" />
1. Wykres trajektorii liczby wygranych jednego z graczy jako zależność od numera rozgrywki
2. Wykres trajektorii kapitału jednego z graczy jako zależność od numera rozgrywki

**Problem H** (Obowiązkowe częściowo)  
Problemy B, C, D, H dla kilku, np. pięciu, graczy.
Różne kombinacje wartościej <img src="https://latex.codecogs.com/gif.latex?\mathbf{p_{i}}" title="\mathbf{p_{i}}" /> - prawdopodobieństw wygranej dla gracza numer **i**.  
<img src="https://latex.codecogs.com/gif.latex?\mathbf{a_{i}}" title="\mathbf{a_{i}}" /> = 20 - kapitały początkowe graczej (lub spróbować inne wartości).  
(studenci dostają 1 punkt za każdy problem)