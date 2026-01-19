# Padrão de Projeto: Memento (Lembrança)

## 📌 Objetivo
O **Memento** é um padrão de projeto comportamental que permite capturar e externalizar um estado interno de um objeto, de maneira que o objeto possa ser restaurado para esse estado mais tarde, sem violar o encapsulamento.



---

## 🧩 Como funciona?
Imagine que você está jogando um videogame e chega em um "Checkpost". O jogo salva seu progresso (HP, itens, posição). Se você perder, o jogo te retorna exatamente para aquele ponto.

### Componentes:
* **Originator (Criador)**: É o objeto que possui um estado interno. Ele sabe como criar um `Memento` de si mesmo e como usar um para restaurar seu estado.
* **Memento**: Um objeto de valor que armazena o estado do Originator. Ele é imutável e não expõe os dados para ninguém além do Originator.
* **Caretaker (Zelador)**: É responsável por guardar os mementos. Ele nunca opera sobre o conteúdo de um memento, apenas o armazena e o devolve ao Originator quando necessário.

## ✅ Vantagens
* **Encapsulamento**: Você não precisa expor os detalhes internos de uma classe para salvar seu estado.
* **Simplificação do Originator**: A responsabilidade de manter o histórico de versões fica com o Caretaker, e não dentro da classe de negócio.

## ❌ Desvantagens
* **Consumo de Memória**: Se os snapshots forem grandes ou muito frequentes, a memória RAM pode acabar rapidamente.
* **Ciclo de Vida**: O Caretaker precisa monitorar o ciclo de vida do Originador para destruir mementos obsoletos e liberar memória.