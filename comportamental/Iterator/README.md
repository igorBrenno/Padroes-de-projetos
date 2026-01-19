# Padrão de Projeto: Iterator (Iterador)

## 📌 Objetivo
O **Iterator** é um padrão de projeto comportamental que permite percorrer elementos de um objeto agregado sem expor sua representação subjacente (seja ela uma lista, pilha, árvore, etc.).



---

## 🧩 Como funciona?
A ideia principal é retirar a responsabilidade de acesso e percurso da lista e colocá-la em um objeto **Iterator**. Isso mantém a coleção limpa e focada apenas em armazenar dados.

### Componentes:
* **Iterator (Interface)**: Define as operações para acessar os elementos (como `next()`, `has_next()`).
* **Concrete Iterator**: Implementa o algoritmo de percurso (ex: ordem direta, ordem reversa, busca em profundidade).
* **Aggregate (Interface)**: Define um método para criar o iterador.
* **Concrete Aggregate**: A coleção real que retorna uma instância do iterador correspondente.

## ✅ Vantagens
* **Princípio de Responsabilidade Única**: Você limpa o código do cliente e das coleções ao mover algoritmos de percurso pesados para classes separadas.
* **Princípio Aberto/Fechado**: Você pode implementar novos tipos de coleções ou iteradores e passá-los para o código existente sem quebrar nada.
* **Iteração Paralela**: Dois iteradores podem percorrer a mesma coleção ao mesmo tempo, pois cada um mantém seu próprio estado de posição.

## ❌ Desvantagens
* **Overkill**: Pode ser desnecessário se a sua aplicação só trabalha com listas simples.
* **Performance**: Usar um iterador pode ser ligeiramente menos eficiente do que percorrer os elementos de uma coleção específica diretamente, devido à abstração adicional.