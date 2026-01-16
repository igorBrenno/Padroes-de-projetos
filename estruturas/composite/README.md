# Padrão de Projeto: Composite

## 📌 Objetivo
O **Composite** é um padrão de projeto estrutural que permite agrupar objetos em estruturas de árvore e trabalhar com essas estruturas como se fossem objetos individuais.



---

## 🧩 Como funciona?
O padrão sugere que você trabalhe com **Folhas** (objetos simples) e **Compostos** (objetos complexos que contêm folhas ou outros compostos) através de uma interface comum.

1. **Componente**: Declara a interface comum para todos os objetos da árvore.
2. **Folha (Leaf)**: Um elemento básico que não possui filhos. Ele define o comportamento final.
3. **Composto (Composite)**: Um elemento que possui filhos (folhas ou outros compostos). Ele delega o trabalho para seus filhos e resume os resultados.

## ✅ Vantagens
* **Polimorfismo**: Você pode usar o mesmo código para manipular toda a estrutura da árvore.
* **Facilidade de expansão**: É fácil adicionar novos tipos de elementos sem quebrar o código existente.

## ❌ Desvantagens
* **Design Genérico**: Pode ser difícil restringir quais componentes podem ser adicionados a determinadas pastas, já que a interface é comum para todos.