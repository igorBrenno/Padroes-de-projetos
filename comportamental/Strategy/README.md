# Padrão de Projeto: Strategy (Estratégia)

## 📌 Objetivo
O **Strategy** é um padrão de projeto comportamental que transforma um conjunto de comportamentos ou algoritmos em objetos separados, tornando-os intercambiáveis dentro de um objeto de contexto original.



---

## 🧩 Como funciona?
Imagine que você está criando um **GPS**. Ele pode calcular rotas para:
1. Ir de **Carro**.
2. Ir a **Pé**.
3. Ir de **Bicicleta**.

Cada uma dessas opções é uma **Estratégia**. O aplicativo de mapas (Contexto) não precisa saber os detalhes de como calcular cada uma; ele apenas chama o método "calcular rota" da estratégia que você selecionou.

### Componentes:
* **Estratégia (Interface)**: Uma interface comum para todos os algoritmos suportados.
* **Estratégias Concretas**: Implementam o algoritmo específico.
* **Contexto**: Mantém uma referência para um objeto Estratégia e o utiliza para executar o algoritmo.

## ✅ Vantagens
* **Troca em tempo de execução**: Você pode alterar o comportamento de um objeto enquanto o programa roda.
* **Isolamento**: Você separa a lógica de negócio do algoritmo (Princípio de Responsabilidade Única).
* **Extensibilidade**: Facilita a adição de novos algoritmos sem alterar o Contexto (Princípio Aberto/Fechado).

## ❌ Desvantagens
* **Complexidade Inicial**: Se você tiver apenas dois algoritmos que raramente mudam, o padrão pode ser um exagero.
* **Conhecimento do Cliente**: O cliente precisa saber a diferença entre as estratégias para escolher a correta.