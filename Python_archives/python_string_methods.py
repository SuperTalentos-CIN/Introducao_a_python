# capitalize() Converte o primeiro caractere para maiúsculo
print("hello world".capitalize()) # -> Hello world

# casefold() Converte a string para letras minúsculas (mais agressivo que o lower())
print("Hello World".casefold()) # -> hello world

# center() Retorna uma string centralizada
print("banana".center(20)) # ->        banana        

# count() Retorna o número de vezes que um valor específico aparece na string
print("I love apples, apple are my favorite fruit".count("apple")) # -> 2

# encode() Retorna uma versão codificada da string
print("My name is Ståle".encode()) # -> b'My name is St\xc3\xa5le'

# endswith() Retorna verdadeiro se a string termina com o valor especificado
print("Hello, welcome to my world.".endswith(".")) # -> True

# expandtabs() Define o tamanho da tabulação (espaço do Tab) da string
print("H\te\tl\tl\to".expandtabs(2)) # -> H e l l o

# find() Procura um valor específico na string e retorna a posição onde foi encontrado
print("Hello, welcome to my world.".find("welcome")) # -> 7

# format() Formata valores especificados dentro de uma string
print("For only {price:.2f} dollars!".format(price = 49)) # -> For only 49.00 dollars!

# format_map() Formata valores especificados em uma string usando um dicionário
print("My name is {name}".format_map({'name': 'John'})) # -> My name is John

# index() Procura um valor específico na string e retorna a posição onde foi encontrado
print("Hello, welcome to my world.".index("welcome")) # -> 7

# isalnum() Retorna Verdadeiro se todos os caracteres da string forem alfanuméricos
print("Company12".isalnum()) # -> True

# isalpha() Retorna Verdadeiro se todos os caracteres da string estiverem no alfabeto
print("CompanyX".isalpha()) # -> True

# isascii() Retorna Verdadeiro se todos os caracteres da string forem caracteres ASCII
print("Company123".isascii()) # -> True

# isdecimal() Retorna Verdadeiro se todos os caracteres da string forem decimais
print("1234".isdecimal()) # -> True

# isdigit() Retorna Verdadeiro se todos os caracteres da string forem dígitos
print("50800".isdigit()) # -> True

# isidentifier() Retorna Verdadeiro se a string for um identificador (nome de variável válido)
print("Demo".isidentifier()) # -> True

# islower() Retorna Verdadeiro se todos os caracteres da string forem minúsculos
print("hello world!".islower()) # -> True

# isnumeric() Retorna Verdadeiro se todos os caracteres da string forem numéricos
print("565543".isnumeric()) # -> True

# isprintable() Retorna Verdadeiro se todos os caracteres da string forem imprimíveis
print("Hello! #1".isprintable()) # -> True

# isspace() Retorna Verdadeiro se todos os caracteres da string forem espaços em branco
print("   ".isspace()) # -> True

# istitle() Retorna Verdadeiro se a string seguir as regras de um título
print("Hello, And Welcome To My World!".istitle()) # -> True

# isupper() Retorna Verdadeiro se todos os caracteres da string forem maiúsculos
print("THIS IS NOW!".isupper()) # -> True

# join() Une os elementos de um iterável (como uma lista) ao final da string
print("#".join(["John", "Peter", "Vicky"])) # -> John#Peter#Vicky

# ljust() Retorna uma versão da string justificada à esquerda
print("banana".ljust(20)) # -> banana              

# lower() Converte uma string para letras minúsculas
print("Hello my FRIENDS".lower()) # -> hello my friends

# lstrip() Retorna uma versão da string sem os espaços à esquerda (trim)
print("     banana     ".lstrip()) # -> banana     

# maketrans() Retorna uma tabela de tradução para ser usada em substituições
print(str.maketrans("a", "b")) # -> {97: 98}

# partition() Retorna uma tupla onde a string é dividida em três partes
print("I could eat bananas all day".partition("bananas")) # -> ('I could eat ', 'bananas', ' all day')

# replace() Retorna uma string onde um valor específico é substituído por outro
print("I like bananas".replace("bananas", "apples")) # -> I like apples

# rfind() Procura um valor específico e retorna a última posição onde ele foi encontrado
print("Mi casa, su casa.".rfind("casa")) # -> 12

# rindex() Procura um valor específico e retorna a última posição onde ele foi encontrado
print("Mi casa, su casa.".rindex("casa")) # -> 12

# rjust() Retorna uma versão da string justificada à direita
print("banana".rjust(20)) # ->               banana

# rpartition() Retorna uma tupla onde a string é dividida em três partes (da direita para esquerda)
print("I could eat bananas all day".rpartition("bananas")) # -> ('I could eat ', 'bananas', ' all day')

# rsplit() Divide a string no separador especificado e retorna uma lista (da direita para esquerda)
print("apple, banana, cherry".rsplit(", ")) # -> ['apple', 'banana', 'cherry']

# rstrip() Retorna uma versão da string sem os espaços à direita(right strip)
print("     banana     ".rstrip()) # ->      banana

# split() Divide a string no separador especificado e retorna uma lista
print("welcome to the jungle".split()) # -> ['welcome', 'to', 'the', 'jungle']

# splitlines() Divide a string nas quebras de linha e retorna uma lista
print("Thank you for the music\nWelcome to the jungle".splitlines()) # -> ['Thank you for the music', 'Welcome to the jungle']

# startswith() Retorna verdadeiro se a string começa com o valor especificado
print("Hello, welcome to my world.".startswith("Hello")) # -> True

# strip() Retorna uma versão da string sem espaços nas extremidades (início e fim)
print("     banana     ".strip()) # -> banana

# swapcase() Inverte as caixas: minúsculas tornam-se maiúsculas e vice-versa
print("Hello My Name Is PETER".swapcase()) # -> hELLO mY nAME iS peter

# title() Converte o primeiro caractere de cada palavra para maiúsculo
print("Welcome to my world".title()) # -> Welcome To My World

# translate() Retorna uma string traduzida usando uma tabela de mapeamento
print("Hello Sam!".translate(str.maketrans("S", "P"))) # -> Hello Pam!

# upper() Converte uma string para letras maiúsculas
print("Hello my friends".upper()) # -> HELLO MY FRIENDS

# zfill() Preenche a string com um número especificado de zeros no início
print("50".zfill(10)) # -> 0000000050