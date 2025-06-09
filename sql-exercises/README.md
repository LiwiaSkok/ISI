# EXCERCISE-01

> Write a SQL query to select the sex and body mass columns from the little_penguins in that order, sorted such that the largest body mass appears first.

``` 
SELECT sex,body_mass_g FROM little_penguins ORDER BY body_mass_g DESC
```

![exercise-01](./screenshots/exercise-01.png)

# EXCERCISE-02

> Write a SQL query to select the islands and species from rows 50 to 60 inclusive of the penguins table. Your result should have 11 rows.

``` 
SELECT  species, island FROM penguins
limit 11
OFFSET 49
```

![exercise-02](./screenshots/exercise-02.png)

# EXCERCISE-03

> Modify your query to select distinct combinations of island and species from the same rows and compare the result to what you got in part 1.

``` 
SELECT DISTINCT species, island FROM (
SELECT species, island FROM penguins
limit 11
OFFSET 49
)

```

![exercise-03](./screenshots/exercise-03.png)

# EXCERCISE-04

> Write a query to select the body masses from penguins that are less than 3000.0 grams.

``` 
SELECT body_mass_g FROM penguins WHERE body_mass_g < 3000


```

![exercise-04](./screenshots/exercise-04.png)

# EXCERCISE-05

> Write another query to select the species and sex of penguins that weight less than 3000.0 grams. This shows that the columns displayed and those used in filtering are independent of each other.

``` 
SELECT species, sex FROM penguins WHERE body_mass_g < 3000

```

![exercise-05](./screenshots/exercise-05.png)


# EXCERCISE-06
> Use the not operator to select penguins that are not Gentoos.

```
SELECT * FROM penguins WHERE species != "Gentoo"
```

![exercise-06](./screenshots/exercise-06.png)

# EXCERCISE-07
> SQL's or is an inclusive or: it succeeds if either or both conditions are true. SQL does not provide a specific operator for exclusive or, which is true if either but not both conditions are true, but the same effect can be achieved using and, or, and not. Write a query to select penguins that are female or on Torgersen Island but not both.

```
SELECT * FROM penguins 
WHERE (island="Torgersen" AND sex !="FEMALE") OR (island!="Torgersen" AND sex="FEMALE")
```

![exercise-07](./screenshots/exercise-07.png)

# EXCERCISE-08
> Write a single query that calculates and returns:
> A column called what_where that has the species and island of each penguin separated by a single space.
> A column called bill_ratio that has the ratio of bill length to bill depth.

```
SELECT  
 species || ' ' || island
,bill_length_mm / bill_depth_mm as bill_ratio
FROM penguins
```

![exercise-08](./screenshots/exercise-08.png)


# EXCERCISE-09
> Use SQLite's .nullvalue command to change the printed representation of null to the string null and then re-run the previous query. When will displaying null as null be easier to understand? When might it be misleading?

```
.nullvalue null
SELECT species || ' ' || island ,bill_length_mm / bill_depth_mm as bill_ratio FROM penguins;
```

![exercise-09](./screenshots/exercise-09.png)

# EXCERCISE-10
> Write a query to find penguins whose body mass is known but whose sex is not.

```
SELECT * FROM penguins
WHERE body_mass_g is NOT NULL AND sex is NULL
```

![exercise-10](./screenshots/exercise-10.png)


hh