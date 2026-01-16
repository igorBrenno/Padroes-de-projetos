# Padrão de Projeto: Flyweight (Peso-Mosca)

## 📌 Objetivo
O **Flyweight** é um padrão de projeto estrutural que permite ajustar mais objetos na quantidade disponível de memória RAM, compartilhando partes comuns do estado entre múltiplos objetos, em vez de manter todos os dados em cada objeto.

---

## 🧩 Como funciona?
O padrão divide o estado de um objeto em dois tipos:
1. **Estado Intrínseco**: Dados que são constantes e podem ser compartilhados por muitos objetos (ex: a imagem de um ícone, o tipo de uma fonte, a cor de uma unidade em um jogo).
2. **Estado Extrínseco**: Dados que mudam conforme o contexto e são únicos para cada instância (ex: as coordenadas X e Y onde o ícone será desenhado).

### Componentes:
* **Flyweight Factory**: Uma fábrica que decide se cria um novo objeto ou se retorna um já existente que possua o mesmo estado intrínseco.
* **Flyweight (Compartilhado)**: O objeto que contém os dados repetitivos.
* **Contexto (Não Compartilhado)**: O objeto "leve" que contém apenas o que é único e uma referência ao Flyweight.

## ✅ Vantagens
* **Economia de Memória**: Pode reduzir drasticamente o consumo de RAM em sistemas com milhões de instâncias.
* **Performance**: Reduz a pressão sobre o Garbage Collector, já que existem menos objetos para gerenciar.

## ❌ Desvantagens
* **Complexidade**: O código fica mais complexo devido à separação dos estados e ao uso da Factory.
* **CPU vs RAM**: Você pode economizar memória, mas gastar um pouco mais de processamento para calcular estados extrínsecos ou buscar objetos na Factory.