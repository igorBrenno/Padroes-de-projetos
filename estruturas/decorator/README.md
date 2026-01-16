# Padrão de Projeto: Decorator

## 📌 Objetivo
O **Decorator** é um padrão de projeto estrutural que permite adicionar responsabilidades adicionais a um objeto dinamicamente. Ele fornece uma alternativa flexível ao uso de subclasses para extensão de funcionalidades.

---

## 🧩 Como funciona?
Imagine uma boneca **Matrioshka** (boneca russa). Você tem uma boneca base e pode colocar várias camadas (decoradores) ao redor dela. Cada camada adiciona algo novo, mas para quem olha de fora, o objeto continua sendo uma "boneca".

1. **Componente**: A interface comum para o objeto original e para os decoradores.
2. **Componente Concreto**: O objeto básico que receberá as decorações.
3. **Decorador Base**: Mantém uma referência ao objeto componente e implementa a mesma interface.
4. **Decoradores Concretos**: Adicionam estados ou comportamentos extras antes ou depois de delegar o trabalho ao objeto envolvido.

## ✅ Vantagens
* **Flexibilidade**: É possível combinar vários decoradores para criar comportamentos complexos.
* **Dinâmico**: Você pode adicionar ou remover responsabilidades durante a execução do programa.

## ❌ Desvantagens
* **Dificuldade de depuração**: Pode ser difícil rastrear erros em um objeto que está envolto em muitas camadas de decoradores.
* **Código inicial**: A configuração inicial de muitos decoradores pode tornar o código do cliente um pouco extenso.