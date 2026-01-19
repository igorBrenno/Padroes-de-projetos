# Padrão de Projeto: Visitor (Visitante)

## 📌 Objetivo
O **Visitor** é um padrão de projeto comportamental que permite que você defina uma nova operação sem mudar as classes dos elementos sobre os quais ela opera.



---

## 🧩 Como funciona?
Imagine que você tem uma estrutura de objetos complexa (como uma árvore de componentes de hardware). Você quer gerar um relatório XML, um relatório JSON e calcular o preço total. Em vez de adicionar três métodos em cada classe de hardware, você cria "Visitantes" que percorrem a estrutura e realizam a lógica específica.

### Componentes:
* **Visitor (Interface)**: Declara um conjunto de métodos de visita, um para cada classe de elemento concreto.
* **Concrete Visitor**: Implementa as operações que devem ser realizadas nos elementos.
* **Element (Interface)**: Declara o método `aceitar(visitor)`.
* **Concrete Element**: Implementa o método `aceitar`, que geralmente apenas chama o método correspondente no visitante (técnica conhecida como *Double Dispatch*).

## ✅ Vantagens
* **Princípio de Responsabilidade Única**: Você pode reunir várias versões de um algoritmo na mesma classe.
* **Princípio Aberto/Fechado**: Você pode introduzir novas operações que trabalham com objetos de diferentes classes sem mudar essas classes.
* **Acúmulo de Estado**: O visitante pode acumular informações úteis enquanto visita os elementos (ex: somar o valor total de uma lista).

## ❌ Desvantagens
* **Dificuldade de Manutenção**: Se uma nova classe de elemento for adicionada, você precisará atualizar todos os visitantes existentes.
* **Encapsulamento**: O visitante pode precisar de acesso a atributos internos dos elementos que deveriam ser privados para realizar seu trabalho.