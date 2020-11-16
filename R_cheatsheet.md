### Tipuri de date
```R
a <- 'a' # caracter
a <- 1.3 # numar real (IEEE 754)
a <- 1L  # integer
a <- TRUE # boolean
a <- 1+1i # numar complex 

vec <- c(1, 2, 3, 4) # vector
vec <- c(1, 'a', 3L, TRUE) # se pastreaza cel mai general (caracter)

l <- list(1, 'a', 3L, TRUE) # lista

a <- matrix(c('a','b','c','d','e','f'),nrow=2,ncol=3) # matrice
```

### Opeartorul [] si [[]]
[] -> returneaza un subset cu aceeasi clasa ca obiectul initial <br>
[[]] -> valoarea de return va avea calsa elementului

### Secvente de control
#### For/While
```R
a <- 1:6
for(elem in a) {
	if(elem<3) next
	print(elem)
}

a <- 2
b <- 4
while(a<b) {
	a <- a+2
	b <- b+1
}
print(a)
```

#### Repeat
```R
a <- 2
b <- 4
repeat {
	a <- a+2
	b <- b+1
	if(a>=b) {
	break
	}
}
print(a)
```

#### Functii
```R
my_sum_2 <- function(a,b=2) {
	a <- a+1
	b <- b/2
	a+b
}
my_sum_2(4)

```

#### Functii predefinite
```R
a <- 1:10
max(a) # 10
min(a) # 1
sum(a) # 55
median(a) # 5.5
mean(a) # 5.5
```

#### Functii iterative
 - lapply(lista, functie) – aplica functia asupra fiecărui element al listei (returnează listă mereu)
 ```R
 iter <- function(a) {a+1}
 lapply(a, iter)
 ```
 - sapply(lista, functie) – analog lapply, dar poate returna vector, matrice sau listă
 ```R
 sapply(a, iter)
 ```
 - apply(vector/matrice, randuri/coloana, functie) – c(1,3) păstrează dimensiunea 1 si 3 a unei matrice cel putin tridimensionala
 ```R
 a <- matrix(c(1:6),nrow=2,ncol=3)
 apply(a,1, iter)
 ```
 - mapply(functie, vector, vector) – aplică o functie avand ca argumente un element din x si un element din y
 ```R
 a <- 1:6
 b <- 3:8
 mapply(sum,a, b)
 ```
 - tapply(vector, factori, functie) – aplică functia grupand elementele vectorului în functie de factori
 ```R
 a <- 1:6
 tapply(a,a<3, iter)

 ```
 - split(vector/data.frame/list,matrice, factori) – imparte vectorul in elemente de lista in functie de factori (list(factori,factori))
 ```R
 a <- 1:6
 split(a,a<3)
 ```
